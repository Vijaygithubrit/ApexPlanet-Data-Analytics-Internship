# Task 1 — Data Cleaning Report

## 1. Project Overview

This report documents the data quality assessment, cleaning decisions,
transformations, and validation performed on the ApexPlanet sales dataset.

The objective was to transform the raw dataset into an analysis-ready
dataset while preserving valid transaction records and maintaining
traceability to the original data.

---

## 2. Dataset Overview

- Source file: `ApexPlanet_DataAnalytics_Dataset.xlsx`
- Sheet: `Sales_Dataset`
- Original rows: 1,000
- Original columns: 12
- Cleaned rows: 1,000
- Cleaned columns: 13

A `Transaction_ID` column was added to provide a unique identifier for
each transaction record.

---

## 3. Data Quality Issues Identified

The following areas were investigated:

- Missing values
- Duplicate records
- Duplicate Order_ID values
- Data types
- Formatting consistency
- Categorical consistency
- Numerical validity
- Business-rule consistency
- Statistical outliers

---

## 4. Missing Values

### Age

Initially, 20 records contained missing Age values.

The investigation identified one reliably recoverable value:

- `CUST3730` → Age = 58

The remaining missing Age values could not be reliably recovered from
the available dataset and were therefore retained as missing.

Final missing Age values: **19**

### City

Initially, 13 records contained missing City values.

Two values could be reliably recovered:

- `CUST3730` → City = Gaya
- `CUST2870` → City = Patna

The remaining missing City values were retained as missing because
there was insufficient evidence to determine their correct values.

Final missing City values: **11**

---

## 5. Duplicate Analysis

No completely duplicated rows were identified.

However, repeated `Order_ID` values were identified.

`ORD100050` appeared multiple times with different transaction details,
including different customers, products, quantities, and sales values.

These records were therefore treated as different transactions rather
than exact duplicate rows.

The original `Order_ID` values were preserved.

A separate `Transaction_ID` was created to provide a unique identifier
for every transaction record.

---

## 6. Data Type Transformation

The `Order_Date` column was converted to a Pandas datetime data type.

This provides a consistent date representation for subsequent analysis.

---

## 7. Numerical Validation

Numerical columns were checked for invalid zero or negative values.

The following business rule was also validated:

`Total_Sales = Quantity × Unit_Price`

No Total_Sales mismatches were identified.

---

## 8. Outlier Analysis

Potential statistical outliers were identified using the Interquartile
Range (IQR) method.

These observations were not automatically removed because being a
statistical outlier does not necessarily indicate a data error.

The potentially unusual transactions were therefore retained.

---

## 9. Cleaning Principles

The following principles were followed:

1. Preserve valid transaction records.
2. Do not delete records without evidence that they are erroneous.
3. Do not invent missing values.
4. Recover missing values only when supported by reliable evidence.
5. Preserve original identifiers for traceability.
6. Validate business rules after cleaning.
7. Document unresolved data-quality limitations.

---

## 10. Final Dataset

The final cleaned dataset contains:

- 1,000 transaction records
- 13 columns
- Unique `Transaction_ID` for every record
- Standardized `Order_Date` data type
- Verified recoverable Age and City values
- Documented unresolved missing values
- Original `Order_ID` values preserved
- Statistical outliers retained

The cleaned dataset was successfully exported and reloaded for final
validation.