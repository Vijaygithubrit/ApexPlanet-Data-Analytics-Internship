# Customer Segmentation and Sales Performance Analysis

## ApexPlanet Data Analytics Internship — Task 3

**Project:** Customer Segmentation Dashboard  
**Tool:** Microsoft Power BI  
**Dataset:** Sales Dataset  
**Analysis Period:** January 1, 2025 – January 1, 2026

---

## 1. Executive Summary

This project analyzes sales transactions and segments customers according to their total sales contribution. An interactive Power BI dashboard was developed to help understand sales performance, customer distribution, product-category contribution, and monthly sales trends.

The dashboard combines key performance indicators (KPIs), monthly sales analysis, customer segmentation, and category-level analysis. Year/Quarter, Category, and City slicers enable users to explore the data interactively.

The analysis identifies high-value customers who contribute substantially to overall sales and provides a foundation for developing targeted customer-retention and sales strategies.

## 2. Business Problem

Businesses need to understand which customers contribute most to revenue, how sales change over time, and which product categories generate the greatest sales.

Analyzing all transactions without grouping customers can make it difficult to identify valuable customer groups and prioritize business actions.

This project addresses the following questions:

- What are the overall sales, order, and customer metrics?
- How are customers distributed across value-based segments?
- Which customer segment contributes the most sales?
- Which product categories contribute most to total sales?
- Which months have the highest and lowest recorded sales?
- How do sales results change when different periods, categories, and cities are selected?

## 3. Dataset Overview

The dataset contains 1,000 transaction rows and 13 columns.

| Field | Description |
|---|---|
| Transaction_ID | Transaction identifier |
| Order_ID | Order identifier |
| Order_Date | Date of the order |
| Customer_ID | Customer identifier |
| Customer_Name | Customer name |
| Age | Customer age |
| Gender | Customer gender |
| City | Customer city |
| Product | Product name |
| Category | Product category |
| Quantity | Quantity purchased |
| Unit_Price | Price per unit |
| Total_Sales | Total sales amount for the transaction |

The recorded dates range from January 1, 2025, to January 1, 2026.

## 4. Tools and Technologies

- **Microsoft Power BI:** Interactive dashboard development and visualization.
- **Power Query / data preparation:** Preparing the cleaned dataset for analysis.
- **DAX:** Creating calculated tables, calculated columns, and measures.
- **Data visualization:** Column charts, bar charts, pie charts, and a donut chart.

## 5. Methodology

### 5.1 Data Preparation

The cleaned sales dataset was loaded into Power BI. The transaction data was used to calculate sales and order metrics, while a customer summary table was created to aggregate sales and purchasing activity at the customer level.

### 5.2 Customer Summary

A `Customer_Summary` calculated table was created using `Customer_ID` as the grouping field. It includes customer-level total sales, distinct order count, total quantity, first purchase date, and last purchase date.

Additional customer metrics include average order value, purchase frequency, sales rank, and order rank.

### 5.3 Customer Segmentation

Customers were assigned to three segments according to their total sales:

- **High-Value:** Customers at or above the 80th-percentile sales threshold.
- **Regular:** Customers between the 40th-percentile and 80th-percentile thresholds.
- **Occasional:** Customers below the 40th-percentile threshold.

Percentile-based thresholds help distinguish customers according to their relative sales contribution. Because customers may have equal sales values, the resulting segment percentages may differ slightly from the intended 20% / 40% / 40% distribution.

### 5.4 KPI Development

The dashboard includes five core KPIs:

| KPI | Formula | Purpose |
|---|---|---|
| Total Sales | Sum of `Total_Sales` | Measures recorded sales value |
| Total Customers | Distinct count of `Customer_ID` | Measures the number of unique customers |
| Total Orders | Distinct count of `Order_ID` | Measures unique orders |
| Average Order Value | Total Sales ÷ Total Orders | Measures average sales per order |
| Sales per Customer | Total Sales ÷ Total Customers | Measures average sales per customer |

The transaction-level measures are designed to respond to the dashboard's date, category, and city filters.

## 6. Dashboard Components

The interactive Power BI dashboard includes:

1. KPI cards for total sales, customers, orders, average order value, and sales per customer.
2. A monthly sales trend chart.
3. Highest monthly sales and lowest monthly sales insight cards.
4. A customer count by segment chart.
5. A sales contribution by customer segment chart.
6. A product-category sales donut chart.
7. Year/Quarter, Category, and City slicers.

The dashboard uses a dark purple and neon-accented design to maintain visual consistency while presenting key business metrics.

## 7. Key Findings

The following results were observed with the dashboard's filters cleared.

### 7.1 Overall Performance

| Metric | Observed result |
|---|---:|
| Total Sales | ₹139.40 million |
| Total Customers | 947 |
| Total Orders | Approximately 1,000 |
| Average Order Value | Approximately ₹139,400 |
| Sales per Customer | Approximately ₹147,200 |

These results summarize the recorded transactions. The distinct customer count is lower than the number of transaction rows because customers can appear in multiple transactions.

### 7.2 Customer Distribution

The customer segments contain the following observed counts:

| Segment | Customers | Approximate share |
|---|---:|---:|
| High-Value | 190 | 20.06% |
| Regular | 378 | 39.92% |
| Occasional | 379 | 40.02% |
| **Total** | **947** | **100%** |

The segmentation identifies a smaller high-value group alongside regular and occasional customers. The high-value segment is particularly important for understanding revenue concentration and developing customer-retention initiatives.

### 7.3 Sales Contribution by Segment

The dashboard shows approximately:

- **High-Value:** ₹66 million
- **Regular:** ₹58 million
- **Occasional:** ₹15 million

The high-value segment contributes the largest share of sales in the unfiltered dashboard. Regular customers also account for a substantial amount of recorded sales, making both groups important to business planning.

Values are rounded from the dashboard display.

### 7.4 Product-Category Performance

The category donut chart shows the following approximate sales distribution:

| Category | Sales | Share of sales |
|---|---:|---:|
| Electronics | ₹50.78 million | 36.43% |
| Education | ₹25.03 million | 17.96% |
| Grocery | ₹22.23 million | 15.95% |
| Furniture | ₹21.52 million | 15.44% |
| Fashion | ₹19.84 million | 14.23% |

Electronics is the largest category by recorded sales, contributing approximately 36.43% of total sales. The remaining categories provide additional sources of revenue.

### 7.5 Monthly Sales Trend

The monthly trend indicates that March 2025 recorded the highest monthly sales, at approximately ₹13.06 million. January 2026 recorded the lowest displayed sales, at approximately ₹809,390.

January 2026 should be interpreted cautiously because the dataset's recorded date range ends on January 1, 2026. It may represent an incomplete reporting period, so the low value should not automatically be interpreted as a genuine decline in business performance.

## 8. Business Recommendations

### 8.1 Retain High-Value Customers

Develop customer-retention initiatives for high-value customers, such as personalized offers, loyalty benefits, and relevant product recommendations. Monitor whether these initiatives improve repeat purchasing and sales contribution.

### 8.2 Encourage Repeat Purchases

Study regular and occasional customers to identify opportunities for increasing purchase frequency. Targeted promotions and relevant recommendations can be tested and evaluated using subsequent sales data.

### 8.3 Monitor Category Performance

Electronics contributes the largest share of recorded sales. Monitor its sales trend and category-level performance while continuing to evaluate opportunities in Education, Grocery, Furniture, and Fashion.

### 8.4 Use Interactive Filters for Investigation

Use the Year/Quarter, Category, and City slicers to investigate how performance differs across periods and locations. Compare results before making operational decisions, and validate that selected filters are applied consistently across relevant visuals.

### 8.5 Improve Time-Period Comparisons

Ensure that monthly comparisons use complete and comparable reporting periods. In particular, validate the coverage of January 2026 before using it to infer a decline in sales.

## 9. Limitations

- The dataset contains 1,000 transaction rows, so findings describe the supplied data rather than the entire market.
- January 2026 may be incomplete, limiting direct comparison with full months in 2025.
- Customer segments are based on total sales, not profitability, customer acquisition cost, or long-term customer value.
- Percentile-based segment sizes may vary because customers can have tied sales values.
- The dataset does not establish why customers purchase or whether a particular promotion caused a change in sales.
- Business recommendations should be tested and monitored before being treated as proven strategies.

## 10. Conclusion

This project demonstrates how Power BI can transform transaction data into an interactive sales and customer-segmentation dashboard. The analysis combines KPI monitoring, monthly sales trends, customer-level segmentation, and category-level sales contribution.

The findings show that high-value customers make the largest contribution among the three customer segments and that Electronics is the leading product category by recorded sales. These insights can support further investigation into customer retention, repeat purchasing, and category performance.

The dashboard provides a foundation for data-driven decision-making and demonstrates practical skills in data preparation, DAX calculations, interactive visualization, and business analysis.

---

**Project status:** Dashboard built and validated. Report content prepared for review before final submission.
