# Task 4 — Data Storytelling and Statistical Validation

## 1. Executive Summary

This analysis investigated whether male and female customers differ in their **customer-level average recorded transaction sales**. A two-sided Welch independent-samples t-test was conducted at a significance level of 0.05.

The male group had a mean of 140,930.68 and the female group had a mean of 135,163.78, a difference of 5,766.91. The difference was not statistically significant: Welch's *t* = 0.7728, degrees of freedom = 910.95, *p* = 0.439854. The 95% confidence interval for the male-minus-female mean difference was −8,878.91 to 20,412.73.

The conclusion remained unchanged in a sensitivity analysis that temporarily excluded nine rows associated with one repeated `Order_ID`. This does not prove that the population means are equal; it means the analysis did not find sufficient evidence of a difference at the selected significance level.

## 2. Business Question

**Question:** Do male and female customers differ in their population mean customer-level average recorded transaction sales?

Each observation represents one customer, calculated as the mean of that customer's recorded `Total_Sales` values. This is not the same as comparing total sales by gender or calculating conventional order-level average order value where order identifiers are known to represent unique orders.

## 3. Hypotheses and Method

- **Null hypothesis (H₀):** The population means are equal.
- **Alternative hypothesis (H₁):** The population means are different.
- **Test:** Two-sided Welch independent-samples t-test.
- **Significance level:** α = 0.05.
- **Unit of analysis:** One customer, represented by their mean recorded `Total_Sales`.

Welch's t-test does not require assuming equal population variances. This is observational analysis and does not establish causation.

## 4. Dataset and Data Quality

Source workbook: `03_Task_3_Deep_Dive_Dashboard/data/ApexPlanet_Cleaned_Sales_Dataset.xlsx`

| Check | Result |
|---|---:|
| Rows loaded | 1,000 |
| Columns loaded | 13 |
| Unique customers | 947 |
| Unique `Order_ID` values | 992 |
| Missing values in required fields | 0 |
| Invalid or missing sales values | 0 |
| Customers with inconsistent gender labels | 34 |
| Repeated `Order_ID` values | 1 |
| Rows associated with the repeated `Order_ID` | 9 |

The repeated identifier was `ORD100050`. It appeared in nine rows with nine different `Transaction_ID` values and nine different `Customer_ID` values. This is a potential identifier-reuse or data-generation anomaly. The available evidence does not establish whether the records are invalid, so the rows were retained in the primary analysis.

The 34 customers whose gender labels conflicted across records were excluded from the gender comparison. The resulting groups contained 468 male customers and 445 female customers.

**Data limitations:** The currency and the business rules defining `Order_ID` were not independently verified.

## 5. Primary Results

| Measure | Male | Female |
|---|---:|---:|
| Customers included | 468 | 445 |
| Mean customer-level average recorded transaction sales | 140,930.68 | 135,163.78 |
| Median customer-level average recorded transaction sales | 107,491.76 | 107,697.64 |
| Standard deviation | 115,149.73 | 110,336.69 |

| Test statistic | Result |
|---|---:|
| Mean difference (male − female) | 5,766.91 |
| Welch's t-statistic | 0.7728 |
| Degrees of freedom | 910.95 |
| Two-sided p-value | 0.439854 |
| 95% confidence interval for mean difference | [−8,878.91, 20,412.73] |
| Decision at α = 0.05 | Fail to reject H₀ |

### Interpretation

The observed male-group mean was higher in this sample. However, the p-value exceeded 0.05 and the confidence interval included zero. The analysis did not provide sufficient statistical evidence of a population mean difference between the groups.

This result does **not** prove that the population means are equal. The observed difference may reflect sampling variation or other factors not examined here.

## 6. Sensitivity Analysis: Repeated Order Identifier

To assess whether the flagged identifier affected the result, the nine rows associated with `ORD100050` were temporarily excluded and the customer-level summaries and test were recalculated. This was a sensitivity scenario only; it was not a permanent data-cleaning decision.

| Measure | All rows retained | Flagged rows excluded temporarily |
|---|---:|---:|
| Male customers | 468 | 463 |
| Female customers | 445 | 444 |
| Male mean | 140,930.68 | 140,239.39 |
| Female mean | 135,163.78 | 134,751.17 |
| Mean difference (male − female) | 5,766.91 | 5,488.23 |
| Welch's t-statistic | 0.7728 | 0.7339 |
| Degrees of freedom | 910.95 | 905.00 |
| Two-sided p-value | 0.439854 | 0.463171 |
| 95% confidence interval | [−8,878.91, 20,412.73] | [−9,187.41, 20,163.87] |
| Decision at α = 0.05 | Fail to reject H₀ | Fail to reject H₀ |

The test decision remained unchanged, and both confidence intervals included zero. This indicates robustness to this specific sensitivity check, not proof that the dataset is free of other quality issues.

## 7. Business Recommendations

1. Do not treat gender as a proven differentiator of customer-level average recorded transaction sales based on this analysis alone.
2. Explore product category, customer segment, purchase frequency, and other business-relevant variables that may explain sales variation.
3. Confirm the intended uniqueness and generation rules for `Order_ID` with the data owner before deduplicating or altering records.
4. Validate customer attributes that vary across a customer's records and document exclusions.
5. Report effect estimates, confidence intervals, sample sizes, and p-values together rather than relying on statistical significance alone.
6. Avoid causal claims or gender-based targeting decisions from this single observational test.

## 8. Limitations

- The analysis is observational and cannot establish causation.
- Thirty-four customers with inconsistent gender labels were excluded from the primary comparison.
- One `Order_ID` was associated with nine different customers; its business meaning remains unverified.
- The dataset's currency and the semantics of the order identifier were not independently verified.
- Results are limited to the supplied dataset, selected metric, and test assumptions.
- A non-significant result does not establish equality between population means.

## 9. Conclusion

At the 5% significance level, the analysis **failed to reject the null hypothesis** that male and female customers have equal population means for customer-level average recorded transaction sales. The result was not statistically significant, and the decision remained the same in the sensitivity analysis.

The next analytical step should explore product mix, customer segments, purchase frequency, and data-quality rules before making business decisions.

---
*Prepared for the ApexPlanet Data Analytics Internship — Task 4: Data Storytelling and Statistical Validation.*
