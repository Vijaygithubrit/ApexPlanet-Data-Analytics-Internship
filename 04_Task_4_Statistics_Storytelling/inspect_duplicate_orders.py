
# Inspect duplicate order IDs from the Task 3 cleaned dataset.
from pathlib import Path
import pandas as pd

# Find the repository root from this script's location.
project_root = Path(__file__).resolve().parents[1]

# Build the correct path from the repository root.
dataset_path = (
    project_root
    / "03_Task_3_Deep_Dive_Dashboard"
    / "data"
    / "ApexPlanet_Cleaned_Sales_Dataset.xlsx"
)

# Check that the dataset exists before attempting to load it.
if not dataset_path.exists():
    raise FileNotFoundError(
        f"Dataset not found: {dataset_path}\n"
        "Verify the Excel filename in the Task 3 data folder."
    )

# Load the Excel dataset without changing the source file.
df = pd.read_excel(dataset_path)

# Find all rows associated with repeated order IDs.
duplicates = df[
    df.duplicated(subset="Order_ID", keep=False)
].sort_values("Order_ID")

# Show fields useful for investigating repeated order IDs.
columns = [
    col for col in [
        "Order_ID",
        "Transaction_ID",
        "Customer_ID",
        "Gender",
        "Product",
        "Quantity",
        "Total_Sales",
    ]
    if col in df.columns
]

# Print the inspection summary and matching records.
print(f"Dataset loaded: {dataset_path}")
print(f"Total dataset rows: {len(df)}")
print(f"Repeated order IDs: {duplicates['Order_ID'].nunique()}")
print(f"Rows belonging to repeated order IDs: {len(duplicates)}")

if duplicates.empty:
    print("No repeated order IDs found.")
else:
    print(duplicates[columns].to_string(index=False))

# Identify order IDs linked to multiple customers.
# This helps distinguish suspicious identifier reuse from simple duplicate rows.

customer_counts = (
    df.groupby("Order_ID")["Customer_ID"]
    .nunique()
    .sort_values(ascending=False)
)

# Keep only order IDs associated with more than one customer.
orders_with_multiple_customers = customer_counts[customer_counts > 1]

print("\nOrder IDs associated with multiple customers:")
print(orders_with_multiple_customers)

# Display the number of affected order IDs.
print(
    "\nNumber of order IDs linked to multiple customers:",
    len(orders_with_multiple_customers)
)
