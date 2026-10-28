
# Check whether the repeated Order_ID affects the gender comparison.
# This script compares customer-level averages with and without the nine flagged rows.

from pathlib import Path

import pandas as pd

# Locate the project root relative to this script.
project_root = Path(__file__).resolve().parents[1]

# Load the cleaned Excel dataset used for Task 4.
dataset_path = (
    project_root
    / "03_Task_3_Deep_Dive_Dashboard"
    / "data"
    / "ApexPlanet_Cleaned_Sales_Dataset.xlsx"
)

df = pd.read_excel(dataset_path)

# Identify every row associated with the repeated order identifier.
flagged_order_id = "ORD100050"
flagged_rows = df["Order_ID"].astype(str).eq(flagged_order_id)

print("Total rows:", len(df))
print("Rows with the flagged Order_ID:", int(flagged_rows.sum()))

# Define a function that computes one average sales value per customer.
def summarize_customer_averages(data):
    # Keep only the fields required for this comparison.
    data = data[["Customer_ID", "Gender", "Total_Sales"]].copy()

    # Convert sales to numeric values and discard invalid records.
    data["Total_Sales"] = pd.to_numeric(
        data["Total_Sales"], errors="coerce"
    )
    data = data.dropna(subset=["Customer_ID", "Gender", "Total_Sales"])

    # Exclude customers whose gender labels conflict across their records.
    gender_counts = data.groupby("Customer_ID")["Gender"].nunique()
    consistent_customers = gender_counts[gender_counts == 1].index
    data = data[data["Customer_ID"].isin(consistent_customers)]

    # Calculate the mean recorded transaction sales for each customer.
    customer_summary = (
        data.groupby(["Customer_ID", "Gender"], as_index=False)
        ["Total_Sales"]
        .mean()
    )

    # Summarize the customer-level averages separately by gender.
    return customer_summary.groupby("Gender")["Total_Sales"].agg(
        ["count", "mean", "median", "std"]
    )

# Calculate the baseline using all rows.
baseline = summarize_customer_averages(df)

# Calculate a comparison after excluding the flagged rows temporarily.
# This is a sensitivity check, not a recommendation to delete the rows.
without_flagged_rows = summarize_customer_averages(df.loc[~flagged_rows])

print("\n=== All rows retained ===")
print(baseline.round(2))

print("\n=== Flagged rows excluded for sensitivity check only ===")
print(without_flagged_rows.round(2))

print(
    "\nNote: This comparison checks the descriptive statistics only. "
    "It does not replace the formal hypothesis test."
)
