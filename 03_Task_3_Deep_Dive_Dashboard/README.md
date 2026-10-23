# Task 3: Deep-Dive Analysis & Interactive Dashboarding

## Customer Segmentation and Sales Performance Analysis

This project is part of the **60-Day Data Analytics Internship at ApexPlanet Software Pvt. Ltd.**

The objective of this task is to perform a deep-dive analysis of sales data, identify customer segments, define key performance indicators (KPIs), and develop an interactive Power BI dashboard to support data-driven business decisions.

## Project Overview

The project analyzes sales transactions to understand overall sales performance, customer distribution, monthly trends, and product-category contribution.

Customer segmentation is performed using customer-level total sales, grouping customers into three segments:

- **High-Value:** Customers at or above the 80th-percentile sales threshold.
- **Regular:** Customers between the 40th-percentile and 80th-percentile thresholds.
- **Occasional:** Customers below the 40th-percentile threshold.

## Tools and Technologies

- Microsoft Power BI
- DAX (Data Analysis Expressions)
- Power Query and data preparation
- Data visualization and business analysis

## Key Performance Indicators (KPIs)

The dashboard includes five core KPIs:

| KPI | Description |
|---|---|
| Total Sales | Total recorded sales value |
| Total Customers | Number of distinct customers |
| Total Orders | Number of distinct orders |
| Average Order Value | Total sales divided by distinct orders |
| Sales per Customer | Total sales divided by distinct customers |

## Dashboard Features

- Interactive monthly sales trend analysis
- Highest and lowest monthly sales insights
- Customer count by segment
- Sales contribution by customer segment
- Product-category sales distribution
- Year/Quarter, Category, and City slicers
- Interactive filtering for exploring sales performance

## Dataset Overview

The dataset contains **1,000 transaction rows and 13 columns**, including transaction and order identifiers, order date, customer information, city, product category, quantity, unit price, and total sales.

The recorded date range is January 1, 2025, to January 1, 2026.

## Key Findings

The following are approximate results from the dashboard with filters cleared:

- Total sales: ₹139.40 million
- Distinct customers: 947
- High-Value customers: 190
- Regular customers: 378
- Occasional customers: 379
- Highest recorded monthly sales: March 2025, approximately ₹13.06 million
- Lowest displayed monthly sales: January 2026, approximately ₹809,390
- Leading product category: Electronics, approximately ₹50.78 million in sales

**Data interpretation note:** January 2026 may represent an incomplete reporting period. Its low sales value should not be interpreted as a confirmed business decline without validating date coverage.

## Project Deliverables

- `Deep_Dive_Analysis_Report.md` — Detailed analysis, methodology, findings, limitations, and recommendations.
- Power BI dashboard (`.pbix`) — Interactive dashboard file.
- Dashboard screenshot — Visual evidence of the completed dashboard.

Add or update the relevant screenshot and Power BI file links after confirming their final filenames and locations.

## Business Recommendations

1. Develop retention strategies for high-value customers.
2. Encourage repeat purchases among regular and occasional customers.
3. Monitor category-level sales performance and opportunities for growth.
4. Use interactive filters to investigate trends across periods and cities.
5. Compare complete reporting periods when evaluating monthly performance.

## Limitations

- Findings are based on the supplied dataset and may not represent the entire business.
- January 2026 may be an incomplete reporting period.
- Customer segments are based on sales value, not profitability or customer lifetime value.
- Recommendations require further testing and monitoring before implementation.

## Conclusion

This project demonstrates the use of Power BI, DAX, customer segmentation, KPI development, and interactive data visualization to analyze sales performance.

The dashboard provides an accessible way to explore customer value, monthly sales trends, and product-category contribution, supporting further investigation and data-driven decision-making.

---

**Internship:** ApexPlanet Data Analytics Internship  
**Task:** Task 3 — Deep-Dive Analysis & Interactive Dashboarding  
**Project focus:** Customer Segmentation and Sales Performance Analysis
