# ApexPlanet Internship — Task 2
## Exploratory Data Analysis, SQL Analysis, and Dashboard

## 1. Project Overview

Task 2 focuses on exploring a retail sales dataset using Python, performing business analysis using SQL, and presenting key results through visualizations and a consolidated dashboard.

The objective is to identify sales trends, compare product and category performance, analyze geographic sales distribution, and investigate relationships between numerical variables.

## 2. Tools and Technologies

- **Python:** Data analysis and exploratory data analysis (EDA)
- **Pandas:** Data manipulation and aggregation
- **Matplotlib:** Data visualization
- **Jupyter Notebook:** Interactive analysis and experimentation
- **MySQL:** SQL-based business analysis and validation
- **GitHub:** Project version control and documentation

## 3. Dataset Overview

The cleaned dataset contains 1,000 records and 13 columns.

Important fields include:

- Transaction ID and Order ID
- Order Date
- Customer ID and Customer Name
- Age, Gender, and City
- Product and Category
- Quantity and Unit Price
- Total Sales

The dataset was used to analyze transaction-level sales performance, product demand, category contributions, city-level performance, and correlations.

## 4. Key Findings

### 4.1 Overall Sales Performance

- Total sales amounted to 139,399,439.65 in the dataset's numerical units.
- The dataset contains 1,000 unique transactions.
- Six products and five categories are represented.
- Eight distinct non-null cities are represented.

### 4.2 Category Performance

Electronics recorded the highest total sales at 50,778,581.70, contributing approximately 36.43% of total sales.

This indicates that Electronics was the strongest category by recorded sales in the analyzed dataset.

### 4.3 Product Performance

Laptop recorded the highest total sales among the six products, at 25,443,008.51.

Product-level comparisons help identify which products contribute most to overall sales.

### 4.4 Monthly Sales Trend

March 2025 recorded the highest monthly sales, at 13,059,899.94.

January 2026 recorded substantially lower sales. However, this month contains only five transactions, so the result may reflect an incomplete reporting period rather than a genuine decline in demand.

### 4.5 City-Level Performance

Patna recorded the highest city-level sales, at 19,323,101.85.

Further investigation would be required to determine the factors behind this performance before making expansion or marketing decisions.

### 4.6 Correlation Analysis

The calculated Pearson correlation coefficients were:

- Quantity versus Total Sales: approximately 0.6466
- Unit Price versus Total Sales: approximately 0.6863

Both variables showed positive relationships with total sales. Correlation does not establish causation, and the results should be interpreted in the context of the dataset.

## 5. Data Quality Findings

### 5.1 Missing Values

The original dataset contained:

- 19 missing Age values
- 11 missing City values

These missing values were retained in the final analysis rather than silently assigning invented demographic or geographic information.

### 5.2 Duplicate Records

The cleaned dataset contained zero duplicate rows during the earlier validation.

The transaction ID validation also returned 1,000 unique transaction IDs for 1,000 records.

### 5.3 Customer Name Inconsistencies

The analysis identified 52 customer IDs associated with multiple customer names.

This issue may affect customer-level aggregation and ranking. Customer-level conclusions should therefore be treated cautiously until the underlying records are reviewed.

### 5.4 Sales Calculation Validation

The validation found zero discrepancies in the calculation:

`Total_Sales = Quantity × Unit_Price`

This check passed for the analyzed dataset.

### 5.5 Potential Outliers

The Interquartile Range (IQR) method flagged 19 transactions as potential high outliers in Total Sales.

These records were flagged for investigation, not automatically removed. High transaction values may represent legitimate purchases.

## 6. Problems Faced and Solutions

### Problem 1: Incomplete MySQL Import

**Issue:** The initial MySQL import contained 981 records instead of the expected 1,000.

**Solution:** A temporary-value workaround was used to import the complete dataset, followed by restoration of the original missing values.

**Verification:** The final SQL validation was reported as successful.

### Problem 2: Blank Exported Chart Images

**Issue:** Charts appeared in the Jupyter Notebook, but some exported PNG images appeared blank.

**Solution:** The chart-saving workflow was corrected, and the five exported PNG files were checked for file validity, dimensions, and visible pixel variation.

### Problem 3: Dashboard Layout and Image Scaling

**Issue:** Initial dashboard versions had blank panels, excessive whitespace, and incorrectly scaled chart images.

**Solution:** The layout was adjusted, the existing PNG images were reused, and the final dashboard was checked for successful generation and basic image validity.

### Problem 4: Inconsistent Customer Names

**Issue:** Some customer IDs were associated with multiple names.

**Solution:** The inconsistency was documented instead of silently choosing one name. Further data investigation is required before relying on customer-level rankings.

## 7. Validation and Testing

The following checks were completed:

- The Jupyter Notebook ran successfully after a kernel restart.
- All five chart PNG files passed the initial technical image checks.
- The generated dashboard passed basic file, dimension, and non-blank image checks.
- SQL validation against the `sales_reimport` table was reported as completed and verified successfully.

These checks establish basic execution and file validity. They do not independently guarantee that every chart or business interpretation is correct.

## 8. Limitations

- January 2026 may represent a partial month, limiting comparisons with complete months.
- Missing age and city values limit some demographic and geographic analyses.
- Customer ID and name inconsistencies affect customer-level analysis.
- Correlation results identify associations rather than causal relationships.
- Potential outliers require contextual investigation before any action is taken.
- The dataset's currency and business context should be confirmed before interpreting the sales values as a specific currency or making external financial comparisons.

## 9. Conclusion

Task 2 combined Python-based exploratory data analysis, SQL business analysis, data quality checks, and dashboard development.

The analysis identified the leading sales category, top-selling product, peak sales month, highest-performing city, and positive correlations between numerical variables. It also identified missing values, customer identity inconsistencies, and potential high-value outliers.

The resulting dashboard consolidates the major analytical views, while the documented limitations provide context for interpreting the findings responsibly.

## 10. Future Improvements

- Investigate and resolve customer identity inconsistencies.
- Compare only complete reporting periods when assessing monthly trends.
- Investigate potential outliers using transaction-level context.
- Expand the analysis with profit, customer retention, or product-level trend metrics if the required data becomes available.
- Improve dashboard interactivity and presentation as a separate enhancement, without delaying completion of the current task.