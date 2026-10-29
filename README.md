# 📊 ApexPlanet Data Analytics Internship

A complete record of my **60-Day Data Analytics Internship at ApexPlanet Software Pvt. Ltd.**, documenting my journey from raw data preparation to exploratory analysis, SQL-based business analysis, interactive Power BI dashboards, statistical validation, business storytelling, and portfolio development.

---

## 🎯 Internship Overview

This repository contains the projects, datasets, notebooks, scripts, analysis reports, visualizations, dashboards, presentations, and supporting deliverables completed throughout the ApexPlanet Data Analytics Internship.

The project follows an end-to-end data analytics workflow:

**Data Wrangling → EDA & SQL → Customer Segmentation & Dashboarding → Statistical Analysis & Storytelling → Portfolio Development**

The objective is to demonstrate practical data analytics skills, analytical thinking, data quality validation, business intelligence, statistical interpretation, and professional communication.

---

## 📌 Internship Progress

| Task | Title | Status | Tools / Focus |
|---|---|---|---|
| **Task 1** | Data Immersion & Wrangling | 🟢 Completed | Python, Pandas, Excel |
| **Task 2** | Exploratory Data Analysis & SQL | 🟢 Completed | Python, Pandas, MySQL, Matplotlib, Seaborn |
| **Task 3** | Customer Segmentation & Interactive Dashboarding | 🟢 Completed | Power BI, DAX, Customer Analytics |
| **Task 4** | Statistical Analysis & Data Storytelling | 🟢 Completed | Python, SciPy, Statistics, PowerPoint |
| **Task 5** | Capstone Integration & Portfolio Development | 🟢 Completed | GitHub, GitHub Pages, HTML, CSS, JavaScript |

---

# 📂 Internship Tasks

## 1️⃣ Task 1 — Data Immersion & Wrangling

**Status:** 🟢 Completed

### Objective
Understand, assess, clean, transform, and validate the sales dataset to prepare reliable data for downstream analysis.

### Work Completed
- Dataset familiarization and structural profiling
- Data dictionary creation
- Missing-value and duplicate analysis
- Data-type and categorical consistency checks
- Numerical and business-rule validation
- Outlier investigation
- Data cleaning and transformation
- Final dataset validation and documentation

### Tools
Python, Pandas, Jupyter Notebook, Microsoft Excel, Git, and GitHub.

### Key Deliverables
- Data cleaning notebook
- Data dictionary and profiling results
- Raw and cleaned datasets
- Cleaning documentation
- Data quality validation evidence

👉 **[View Task 1 — Data Wrangling](./01_Task_1_Data_Wrangling/)**

---

## 2️⃣ Task 2 — Exploratory Data Analysis & SQL

**Status:** 🟢 Completed

### Objective
Explore the cleaned sales dataset to identify business patterns, sales trends, customer characteristics, and relationships using descriptive statistics, visualizations, and SQL.

### Work Completed
- Dataset structure and descriptive-statistics analysis
- Missing-value and data-quality investigation
- Category, product, city, and monthly sales analysis
- Customer and demographic analysis
- Correlation analysis
- SQL-based business queries and aggregations
- Sales visualizations and a static dashboard
- Documentation of findings, challenges, and limitations

### Tools
Python, Pandas, Jupyter Notebook, MySQL, SQL, Matplotlib, Seaborn, and GitHub.

### Key Deliverables
- Exploratory Data Analysis notebook
- SQL business-analysis queries
- Sales visualizations
- Retail sales dashboard image
- Findings and challenges report
- Supporting datasets and validation scripts

### Key Learnings
Developed practical skills in data exploration, data quality assessment, SQL querying, statistical interpretation, and communicating analytical findings through visualizations.

👉 **[View Task 2 — EDA & SQL](./02_Task_2_EDA_SQL/)**

---

## 3️⃣ Task 3 — Customer Segmentation & Interactive Dashboarding

**Status:** 🟢 Completed

### Objective
Analyze customer purchasing behavior, develop meaningful customer segments, define business KPIs, and communicate findings through an interactive Power BI dashboard.

### Work Completed
- Loaded and analyzed the cleaned sales dataset in Power BI
- Created a customer-level summary table
- Calculated customer sales, order counts, quantities, average order value metrics, and purchase frequency
- Developed customer sales and order ranking calculations
- Segmented customers using sales percentiles
- Created KPI measures and dashboard cards
- Built a customer count by segment visualization
- Developed monthly sales trend analysis
- Improved dashboard layout, colors, formatting, and interactivity
- Documented findings and prepared project deliverables

### Customer Segmentation Approach

| Segment | Definition |
|---|---|
| **High-Value** | Customer sales at or above the 80th percentile |
| **Regular** | Customer sales at or above the 40th percentile but below the 80th percentile |
| **Occasional** | Customer sales below the 40th percentile |

### Dashboard KPIs
- Total Sales
- Total Customers
- Total Orders
- Average Order Value
- Sales per Customer

### Tools
Microsoft Power BI, DAX, Excel, data modeling, data visualization, and GitHub.

### Key Deliverables
- Interactive Power BI dashboard
- Power BI `.pbix` project file
- Dashboard screenshot
- Deep-dive analysis report
- Supporting analysis and documentation

👉 **[View Task 3 — Customer Segmentation Dashboard](./03_Task_3_Deep_Dive_Dashboard/)**

---

## 4️⃣ Task 4 — Statistical Analysis & Data Storytelling

**Status:** 🟢 Completed

### Objective
Turn analytical findings into a clear business narrative and use statistical methods to investigate data quality concerns and evaluate whether observed differences between customer groups are statistically significant.

### Work Completed
- Investigated dataset quality and identifier consistency
- Examined repeated order identifiers and their potential impact
- Prepared customer-level summary data
- Compared customer-level average recorded transaction sales by gender
- Formulated null and alternative hypotheses
- Conducted Welch's independent two-sample t-test
- Calculated the p-value and 95% confidence interval
- Performed a sensitivity analysis excluding flagged records
- Documented the methodology, assumptions, findings, limitations, and recommendations
- Created a professional PowerPoint presentation and recorded presentation video

### Statistical Analysis

The primary analysis compared customer-level average recorded transaction sales between male and female customer groups.

**Hypotheses**

- **Null hypothesis (H₀):** The population means of customer-level average recorded transaction sales are equal for the two groups.
- **Alternative hypothesis (H₁):** The population means differ between the two groups.

**Significance level:** α = 0.05

**Primary test results**

| Metric | Result |
|---|---:|
| Male customers included | 468 |
| Female customers included | 445 |
| Difference in sample means (male − female) | 5,766.91 |
| Welch's t-statistic | 0.7728 |
| Degrees of freedom | 910.945 |
| p-value | 0.4399 |
| 95% confidence interval for the difference | −8,878.91 to 20,412.73 |
| Statistical decision | Fail to reject H₀ |

### Interpretation

The observed difference between the sample means was not statistically significant at the 5% significance level. The 95% confidence interval included zero, so the analysis did not provide sufficient evidence of a difference in population means.

This does **not** prove that the two groups are identical. It means the analysis did not establish a statistically significant difference using the selected test and data.

The analysis also identified a repeated `Order_ID` that appeared across multiple transaction and customer identifiers. This was treated as a potential data-quality issue rather than automatically deleting the affected records. A sensitivity analysis showed the same statistical decision after temporarily excluding flagged records.

**Important limitation:** The measure is described as *customer-level average recorded transaction sales*. The business meaning of the order identifier and the currency or unit of the sales values have not been independently verified. Therefore, the results should not be interpreted as a confirmed conventional average order value or as evidence of causation.

### Tools
Python, Pandas, NumPy, SciPy, Matplotlib, statistical hypothesis testing, PowerPoint, Markdown, and GitHub.

### Key Deliverables
- Statistical analysis scripts
- Customer-level summary CSV
- Group summary CSV
- Hypothesis test results in JSON
- Statistical comparison visualization
- Deep-dive analysis report
- PowerPoint presentation
- Presentation video
- Task-specific README and requirements file

👉 **[View Task 4 — Statistical Storytelling](./04_Task_4_Statistics_Storytelling/)**

---

## 5️⃣ Task 5 — Capstone Integration & Final Documentation

**Status:** 🟡 In Progress

### Objective

Consolidate the completed Tasks 1–4, review the internship deliverables, and finalize the master documentation and project evidence.

### Progress Completed

- Reviewed the README documentation for Tasks 1–4.
- Completed the separate HTML, CSS, and JavaScript portfolio website prototype.
- Created a dedicated GitHub repository for the prototype.
- Uploaded the website files and successfully deployed the prototype using GitHub Pages.
- Kept the prototype separate from the ApexPlanet internship repository and the future main personal portfolio website.

### Remaining Work

- Verify the final task deliverables and repository links.
- Keep the master README and task-specific documentation consistent.
- Complete any remaining Task 5 internship requirements.
- Update the internship progress tracker when the remaining work is finished.

### Tools

Git, GitHub, GitHub Pages, HTML, CSS, and JavaScript.

**Separate prototype repository:**  
https://github.com/Vijaygithubrit/Vijay-Data-Analyst-Portfolio

**Prototype website:**  
https://vijaygithubrit.github.io/Vijay-Data-Analyst-Portfolio/

---

# 🛠️ Technical Skills Demonstrated

### Programming & Data Analysis
- Python
- Pandas and NumPy
- Data cleaning and transformation
- Exploratory Data Analysis
- Descriptive statistics
- Statistical hypothesis testing
- Data quality validation

### Database & SQL
- MySQL
- SQL filtering and aggregation
- GROUP BY and analytical queries
- Business metric calculation
- Query result validation

### Visualization & Business Intelligence
- Microsoft Power BI
- DAX and calculated measures
- KPI development
- Customer segmentation
- Sales trend analysis
- Matplotlib and Seaborn
- Dashboard design and storytelling

### Statistical & Business Communication
- Hypothesis formulation
- Welch's t-test
- p-value and confidence interval interpretation
- Sensitivity analysis
- Analytical reporting
- Business recommendations
- PowerPoint presentation development

### Development & Portfolio
- Git and GitHub
- Technical documentation
- Project organization
- Markdown
- HTML, CSS, and JavaScript for portfolio development
- GitHub Pages deployment

---

# 📈 Internship Progress Tracker

```text
Task 1  ████████████████████  100%  ✅ Completed
Task 2  ████████████████████  100%  ✅ Completed
Task 3  ████████████████████  100%  ✅ Completed
Task 4  ████████████████████  100%  ✅ Completed
Task 5  ░░░░░░░░░░░░░░░░░░░░   In Progress
```

---

# 📂 Repository Structure

```text
ApexPlanet-Data-Analytics-Internship/
│
├── 01_Task_1_Data_Wrangling/
│   └── Data profiling, cleaning, notebooks, and datasets
│
├── 02_Task_2_EDA_SQL/
│   └── EDA, SQL analysis, visualizations, and reports
│
├── 03_Task_3_Deep_Dive_Dashboard/
│   └── Customer segmentation, Power BI dashboard, and analysis
│
├── 04_Task_4_Statistics_Storytelling/
│   ├── figures/
│   ├── outputs/
│   ├── ppt/
│   ├── report/
│   ├── scripts/
│   ├── video/
│   ├── README.md
│   └── requirements-task4.txt
│
│
└── README.md
```

*This structure summarizes the main task folders. Refer to each task's README for its actual contents and deliverables.*

---

## 📌 Repository Notes

- Each task has its own folder containing relevant code, documentation, and deliverables.
- Task-specific README files provide detailed information about the work completed.
- Analysis outputs and findings are documented to support reproducibility and review.
- Statistical conclusions are interpreted in the context of the available data and its limitations.
- The repository is updated as the internship progresses.

---

## 👨‍💻 About This Project

This repository represents my practical learning journey in data analytics, from preparing raw data to performing statistical analysis and communicating results through dashboards and presentations.

My focus is on developing the ability to **clean data, ask meaningful questions, validate analytical results, communicate insights, and support evidence-based business decisions**.

Thank you for visiting my ApexPlanet Data Analytics Internship repository! 🚀
