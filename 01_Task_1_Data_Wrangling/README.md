# Task 1 — Data Immersion & Wrangling

## 📌 Overview

Task 1 of the ApexPlanet Data Analytics Internship focuses on
understanding, assessing, cleaning, and preparing the provided sales
dataset for further analysis.

The objective was to identify data-quality issues, investigate their
impact, apply justified cleaning transformations, validate the
resulting dataset, and produce an analysis-ready dataset.

---

## 🎯 Objectives

- Understand the structure and variables of the dataset.
- Create a data dictionary.
- Assess data quality.
- Identify missing values and duplicates.
- Check data types and formatting.
- Validate categorical and numerical values.
- Apply justified data-cleaning transformations.
- Validate the cleaned dataset.
- Document the cleaning process and decisions.

---

## 📊 Dataset

**Source:** `ApexPlanet_DataAnalytics_Dataset.xlsx`

**Sheet:** `Sales_Dataset`

### Original Dataset

- Rows: **1,000**
- Columns: **12**

### Cleaned Dataset

- Rows: **1,000**
- Columns: **13**

A `Transaction_ID` column was added to provide a unique identifier
for each transaction record.

---

## 🔍 Data Quality Assessment

The following areas were investigated:

- Missing values
- Complete duplicate records
- Duplicate `Order_ID` values
- Repeated `Customer_ID` values
- Data types
- Date formatting
- Text formatting
- Categorical consistency
- Product–Category consistency
- Numerical validity
- Business-rule validation
- Statistical outliers

---

## 🧹 Data Cleaning Performed

### 1. Order Date

The `Order_Date` column was converted to a proper Pandas datetime
data type.

---

### 2. Missing Age Values

Initially, **20** records contained missing `Age` values.

During investigation, one reliably recoverable value was identified:

- `CUST3730` → `Age = 58`

The remaining missing Age values could not be reliably determined
from the available dataset and were therefore retained as missing.

**Final missing Age values: 19**

---

### 3. Missing City Values

Initially, **13** records contained missing `City` values.

Two reliably recoverable values were identified:

- `CUST3730` → `Gaya`
- `CUST2870` → `Patna`

The remaining missing City values were retained because their correct
values could not be reliably determined.

**Final missing City values: 11**

---

### 4. Duplicate Order IDs

No completely duplicated rows were identified.

However, repeated `Order_ID` values were found.

For example, `ORD100050` appeared multiple times with different:

- Customers
- Products
- Quantities
- Unit prices
- Transaction dates
- Total sales

Therefore, these records were treated as different transactions and
were **not deleted**.

The original `Order_ID` values were preserved.

A new `Transaction_ID` was created to provide a unique identifier for
each transaction record.

---

### 5. Numerical Validation

Numerical columns were checked for invalid values such as negative
quantities, prices, and sales.

The following business rule was also validated:

```text
Total_Sales = Quantity × Unit_Price