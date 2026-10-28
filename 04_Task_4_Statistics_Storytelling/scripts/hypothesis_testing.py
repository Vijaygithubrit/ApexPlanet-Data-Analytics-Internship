"""
ApexPlanet Task 4: Statistical validation of average transaction value by gender.

Run this script from the repository root:
    python 04_Task_4_Statistics_Storytelling/scripts/hypothesis_testing.py

The script reads the existing Task 2 CSV, leaves the source file unchanged,
checks data quality, builds one observation per customer, performs Welch's
independent-samples t-test, and saves reproducible outputs.
"""

from pathlib import Path
import json
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

# Resolve paths from the repository root rather than the current terminal folder.
ROOT = Path(__file__).resolve().parents[2]
# Prefer the cleaned Task 3 dataset when it is available, since that is the
# dataset used for the completed dashboard. Fall back to the Task 2 CSV.
TASK3_XLSX = ROOT / "03_Task_3_Deep_Dive_Dashboard" / "data" / "ApexPlanet_Cleaned_Sales_Dataset.xlsx"
TASK2_CSV = ROOT / "02_Task_2_EDA_SQL" / "data" / "ApexPlanet_Sales_Import.csv"
INPUT_FILE = TASK3_XLSX if TASK3_XLSX.exists() else TASK2_CSV
OUTPUT_DIR = ROOT / "04_Task_4_Statistics_Storytelling" / "outputs"
FIGURE_DIR = ROOT / "04_Task_4_Statistics_Storytelling" / "figures"
ALPHA = 0.05
REQUIRED_COLUMNS = ["Order_ID", "Customer_ID", "Gender", "Total_Sales"]


def describe(values):
    """Return descriptive statistics for a numeric group of customer observations."""
    return {
        "n_customers": int(len(values)),
        "mean_average_transaction_value": float(np.mean(values)),
        "median_average_transaction_value": float(np.median(values)),
        "standard_deviation": float(np.std(values, ddof=1)),
    }


def main():
    # Stop early with a clear error if the expected existing dataset is unavailable.
    if not INPUT_FILE.exists():
        sys.exit(f"Neither Task 3 Excel nor Task 2 CSV source was found. Checked: {TASK3_XLSX} and {TASK2_CSV}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)

    # Load Task 2's existing CSV; do not create a second source dataset.
    # Load the Task 3 Excel workbook if present; otherwise use the Task 2 CSV.
    if INPUT_FILE.suffix.lower() == ".xlsx":
        df = pd.read_excel(INPUT_FILE)
        # The Task 3 cleaned workbook may contain an Excel index column. Drop it if present.
        df = df.loc[:, ~df.columns.astype(str).str.match(r"^Unnamed:|^index$")]
        if "Transaction_ID" not in df.columns:
            # This source stores one row per order, so create no fabricated transaction IDs.
            pass
    else:
        df = pd.read_csv(INPUT_FILE)
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing_columns:
        sys.exit(f"The dataset is missing required columns: {missing_columns}")

    # Normalize text and parse sales values so checks are not affected by whitespace.
    for column in ["Order_ID", "Customer_ID", "Gender"]:
        df[column] = df[column].astype("string").str.strip()
    df["Gender"] = df["Gender"].str.title()
    df["Total_Sales"] = pd.to_numeric(df["Total_Sales"], errors="coerce")

    # Capture quality diagnostics before any exclusion or aggregation.
    quality = {
        "source_file": str(INPUT_FILE.relative_to(ROOT)).replace("\\", "/"),
        "rows_loaded": int(len(df)),
        "columns_loaded": int(len(df.columns)),
        "missing_required_values": {
            column: int(df[column].isna().sum() + (df[column].astype("string").str.strip() == "").sum())
            for column in REQUIRED_COLUMNS
        },
        "duplicate_order_id_rows_beyond_first": int(df.duplicated(subset=["Order_ID"], keep="first").sum()),
        "invalid_or_missing_sales_values": int(df["Total_Sales"].isna().sum()),
        "gender_transaction_counts": {
            str(key): int(value) for key, value in df["Gender"].value_counts(dropna=False).items()
        },
        "unique_order_ids": int(df["Order_ID"].nunique(dropna=True)),
        "unique_customers": int(df["Customer_ID"].nunique(dropna=True)),
    }

    # Keep rows with usable identifiers, a supported gender group, and a numeric sales value.
    usable = df.dropna(subset=REQUIRED_COLUMNS).copy()
    usable = usable[
        usable["Order_ID"].ne("")
        & usable["Customer_ID"].ne("")
        & usable["Gender"].isin(["Male", "Female"])
        & usable["Total_Sales"].notna()
    ].copy()

    # A customer whose gender changes between records cannot belong to two groups.
    distinct_genders = usable.groupby("Customer_ID")["Gender"].nunique()
    inconsistent_ids = distinct_genders[distinct_genders > 1].index
    quality["customers_with_inconsistent_gender"] = int(len(inconsistent_ids))
    consistent = usable[~usable["Customer_ID"].isin(inconsistent_ids)].copy()

    # Each customer contributes only one independent observation: their mean transaction value.
    customer_summary = consistent.groupby(["Customer_ID", "Gender"], as_index=False).agg(
        transaction_count=("Order_ID", "size"),
        average_transaction_value=("Total_Sales", "mean"),
        total_sales=("Total_Sales", "sum"),
    )
    male = customer_summary.loc[
        customer_summary["Gender"].eq("Male"), "average_transaction_value"
    ].to_numpy(dtype=float)
    female = customer_summary.loc[
        customer_summary["Gender"].eq("Female"), "average_transaction_value"
    ].to_numpy(dtype=float)

    # Welch's two-sided t-test does not require equal population variances.
    if len(male) < 2 or len(female) < 2:
        sys.exit("At least two eligible customers per gender group are needed for this test.")
    test = stats.ttest_ind(male, female, equal_var=False, alternative="two-sided")

    # Compute Welch-Satterthwaite degrees of freedom and a 95% CI for mean difference.
    n_male, n_female = len(male), len(female)
    var_male, var_female = np.var(male, ddof=1), np.var(female, ddof=1)
    standard_error = np.sqrt(var_male / n_male + var_female / n_female)
    numerator = (var_male / n_male + var_female / n_female) ** 2
    denominator = (
        (var_male / n_male) ** 2 / (n_male - 1)
        + (var_female / n_female) ** 2 / (n_female - 1)
    )
    degrees_freedom = numerator / denominator
    critical_t = stats.t.ppf(1 - ALPHA / 2, degrees_freedom)
    mean_difference = float(np.mean(male) - np.mean(female))
    confidence_interval = [
        float(mean_difference - critical_t * standard_error),
        float(mean_difference + critical_t * standard_error),
    ]
    reject_null = bool(test.pvalue < ALPHA)

    # Build a machine-readable result. A non-significant result is not proof of equality.
    result = {
        "hypothesis": {
            "null": "Male and female customers have equal population means for customer-level average transaction value.",
            "alternative": "Male and female customers have different population means for customer-level average transaction value.",
            "test": "Two-sided Welch independent-samples t-test",
            "significance_level": ALPHA,
        },
        "data_quality": quality,
        "analysis": {
            "unit_of_analysis": "One customer; mean of that customer's recorded Total_Sales values.",
            "customers_excluded_for_inconsistent_gender": int(len(inconsistent_ids)),
            "male": describe(male),
            "female": describe(female),
            "mean_difference_male_minus_female": mean_difference,
            "relative_mean_difference_percent_vs_female": float(mean_difference / np.mean(female) * 100),
            "t_statistic": float(test.statistic),
            "degrees_of_freedom_welch": float(degrees_freedom),
            "p_value": float(test.pvalue),
            "confidence_level": 1 - ALPHA,
            "confidence_interval_difference": confidence_interval,
            "decision": "Reject the null hypothesis" if reject_null else "Fail to reject the null hypothesis",
            "business_interpretation": (
                "Evidence supports a difference in population means at the 5% level."
                if reject_null
                else "The observed sample difference is not statistically significant at 5%; this does not prove the population means are equal."
            ),
        },
    }

    # Save the auditable customer observations, group metrics, and full results.
    customer_summary.to_csv(OUTPUT_DIR / "customer_level_summary.csv", index=False)
    pd.DataFrame([
        {"gender": "Male", **describe(male)},
        {"gender": "Female", **describe(female)},
    ]).to_csv(OUTPUT_DIR / "group_summary.csv", index=False)
    (OUTPUT_DIR / "hypothesis_test_results.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8"
    )

    # Plot mean values with group-specific 95% t-based confidence intervals.
    means = [float(np.mean(male)), float(np.mean(female))]
    errors = [
        float(stats.t.ppf(0.975, n_male - 1) * stats.sem(male)),
        float(stats.t.ppf(0.975, n_female - 1) * stats.sem(female)),
    ]
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(["Male customers", "Female customers"], means, yerr=errors, capsize=6)
    ax.set_title("Customer-Level Average Transaction Value by Gender")
    ax.set_ylabel("Average transaction value (₹)")
    ax.set_xlabel("Customer gender")
    ax.grid(axis="y", alpha=0.25)
    ax.bar_label(bars, fmt="₹%.0f", padding=4)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "gender_average_transaction_value.png", dpi=180)
    plt.close(fig)

    # Print results in the VS Code terminal for quick validation.
    print(json.dumps(result, indent=2))
    print(f"\nOutputs saved in: {OUTPUT_DIR}")
    print(f"Chart saved to: {FIGURE_DIR / 'gender_average_transaction_value.png'}")


if __name__ == "__main__":
    main()
