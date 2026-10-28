# Task 4 — Data Storytelling and Statistical Validation

This folder contains the statistical analysis, business interpretation, stakeholder presentation, and supporting outputs for Task 4 of the ApexPlanet Data Analytics Internship.

## Objective

Evaluate whether male and female customers differ in their **customer-level average recorded transaction sales**, using a two-sided Welch independent-samples t-test at a 5% significance threshold.

## Project Structure

```text
04_Task_4_Statistics_Storytelling/
├── figures/
│   └── gender_average_transaction_value.png
├── outputs/
│   ├── customer_level_summary.csv
│   ├── group_summary.csv
│   └── hypothesis_test_results.json
├── ppt/
│   └── ApexPlanet_Task4_Statistical_Storytelling.pptx
├── report/
│   └── Deep_Dive_Analysis_Report.md
├── scripts/
│   └── hypothesis_testing.py
├── video/
│   └── ApexPlanet_Task4_Statistical_Storytelling.mp4
├── check_order_id_impact.py
├── compare_welch_test.py
├── inspect_duplicate_orders.py
├── README.md
└── requirements-task4.txt
```

## Data Source

The analysis uses the cleaned workbook from Task 3:

`../03_Task_3_Deep_Dive_Dashboard/data/ApexPlanet_Cleaned_Sales_Dataset.xlsx`

The analysis loaded 1,000 rows and 13 columns, with 947 unique customers and 992 unique `Order_ID` values.

## Methodology

1. Check required columns, missing values, invalid sales values, and repeated order identifiers.
2. Identify customers with inconsistent gender labels across records.
3. Exclude inconsistent-gender customers from the primary comparison.
4. Calculate each remaining customer's mean recorded `Total_Sales`.
5. Compare male and female customer-level averages using a two-sided Welch independent-samples t-test.
6. Report the p-value, 95% confidence interval, and decision at α = 0.05.
7. Run a sensitivity check with the nine rows associated with `ORD100050` temporarily excluded. The source data was not overwritten.

## Main Findings

| Measure | Result |
|---|---:|
| Male customers | 468 |
| Female customers | 445 |
| Male mean | 140,930.68 |
| Female mean | 135,163.78 |
| Mean difference (male − female) | 5,766.91 |
| Welch's t-statistic | 0.7728 |
| Degrees of freedom | 910.95 |
| p-value | 0.439854 |
| 95% confidence interval | [−8,878.91, 20,412.73] |
| Decision | Fail to reject the null hypothesis |

The observed difference was not statistically significant at the 5% level. This does not prove that the population means are equal.

## Sensitivity Analysis

One `Order_ID` (`ORD100050`) appeared in nine rows with nine different transaction IDs and nine different customers. The rows were retained in the primary analysis because the identifier anomaly alone did not establish that the records were invalid.

With those rows temporarily excluded, the mean difference was 5,488.23, the p-value was 0.463171, and the 95% confidence interval was [−9,187.41, 20,163.87]. The test decision remained unchanged.

## Requirements and Execution

The Task 4-specific dependencies are listed in `requirements-task4.txt`:

```text
pandas
numpy
scipy
matplotlib
openpyxl
```

Install them from the repository root if needed:

```powershell
python -m pip install -r .\04_Task_4_Statistics_Storytelling\requirements-task4.txt
```

Run analysis scripts from the repository root. For example:

```powershell
python .\04_Task_4_Statistics_Storytelling\inspect_duplicate_orders.py
python .\04_Task_4_Statistics_Storytelling\check_order_id_impact.py
python .\04_Task_4_Statistics_Storytelling\compare_welch_test.py
```

## Limitations

- This is observational analysis and does not establish causation.
- Thirty-four customers with inconsistent gender labels were excluded from the main comparison.
- The repeated `Order_ID` is an unresolved data-quality anomaly.
- The dataset's currency and the business definition of `Order_ID` were not independently verified.
- A non-significant result is not proof of equality.

## Conclusion

At α = 0.05, the analysis failed to reject the null hypothesis. The conclusion remained unchanged in the sensitivity check. Further analysis of product category, customer segment, purchase frequency, and data-quality rules is recommended.

---
*ApexPlanet Data Analytics Internship — Task 4*
