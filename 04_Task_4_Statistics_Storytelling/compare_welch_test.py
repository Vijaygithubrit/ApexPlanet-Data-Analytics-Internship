
# Compare Welch's t-test results with and without the flagged Order_ID rows.
# The original dataset is never modified or overwritten.

from pathlib import Path

import pandas as pd
from scipy import stats

# Resolve the project root from this script's location.
project_root = Path(__file__).resolve().parents[1]

# Load the cleaned dataset used for Task 4.
dataset_path = (
    project_root
    / "03_Task_3_Deep_Dive_Dashboard"
    / "data"
    / "ApexPlanet_Cleaned_Sales_Dataset.xlsx"
)
df = pd.read_excel(dataset_path)

# Identify the flagged rows for a sensitivity check only.
flagged_rows = df["Order_ID"].astype(str).eq("ORD100050")


def prepare_customer_averages(data):
    """Return one mean recorded sales value per consistent-gender customer."""

    # Keep only fields needed for the hypothesis test.
    data = data[["Customer_ID", "Gender", "Total_Sales"]].copy()

    # Clean sales values and remove missing required values.
    data["Total_Sales"] = pd.to_numeric(
        data["Total_Sales"], errors="coerce"
    )
    data = data.dropna(
        subset=["Customer_ID", "Gender", "Total_Sales"]
    )

    # Exclude customers whose gender differs across their records.
    gender_counts = data.groupby("Customer_ID")["Gender"].nunique()
    consistent_ids = gender_counts[gender_counts == 1].index
    data = data[data["Customer_ID"].isin(consistent_ids)]

    # Compute one average transaction-sales value per customer.
    return data.groupby(["Customer_ID", "Gender"])["Total_Sales"].mean()


def run_welch_test(data, scenario_name):
    """Run a two-sided Welch test and calculate its 95% confidence interval."""

    # Calculate customer-level averages for the chosen scenario.
    customer_means = prepare_customer_averages(data)

    # Separate the independent customer-level observations by gender.
    male = customer_means.xs("Male", level="Gender").to_numpy()
    female = customer_means.xs("Female", level="Gender").to_numpy()

    # Run Welch's t-test, which does not assume equal group variances.
    test = stats.ttest_ind(male, female, equal_var=False)

    # Calculate the standard error and Welch-Satterthwaite degrees of freedom.
    male_var = male.var(ddof=1)
    female_var = female.var(ddof=1)
    male_n = len(male)
    female_n = len(female)

    standard_error = (
        male_var / male_n + female_var / female_n
    ) ** 0.5

    numerator = (male_var / male_n + female_var / female_n) ** 2
    denominator = (
        (male_var / male_n) ** 2 / (male_n - 1)
        + (female_var / female_n) ** 2 / (female_n - 1)
    )
    degrees_freedom = numerator / denominator

    # Calculate the 95% confidence interval for male mean minus female mean.
    mean_difference = male.mean() - female.mean()
    critical_value = stats.t.ppf(0.975, degrees_freedom)
    margin = critical_value * standard_error

    print(f"\n=== {scenario_name} ===")
    print(f"Male customers: {male_n}")
    print(f"Female customers: {female_n}")
    print(f"Male mean: {male.mean():.2f}")
    print(f"Female mean: {female.mean():.2f}")
    print(f"Mean difference (male - female): {mean_difference:.2f}")
    print(f"Welch t-statistic: {test.statistic:.4f}")
    print(f"Degrees of freedom: {degrees_freedom:.2f}")
    print(f"Two-sided p-value: {test.pvalue:.6f}")
    print(
        "95% confidence interval: "
        f"[{mean_difference - margin:.2f}, "
        f"{mean_difference + margin:.2f}]"
    )

    # Apply the preselected 5% significance level.
    if test.pvalue < 0.05:
        print("Decision: Reject the null hypothesis.")
    else:
        print("Decision: Fail to reject the null hypothesis.")


# Scenario 1: Retain every row in the source dataset.
run_welch_test(df, "All rows retained")

# Scenario 2: Exclude flagged rows temporarily for sensitivity analysis.
run_welch_test(
    df.loc[~flagged_rows],
    "Flagged Order_ID rows excluded temporarily"
)
