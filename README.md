````markdown
# 🌞 Cross-Country Solar Data Analysis – Week 0 Challenge

Welcome to the Week 0 challenge of 10 Academy's Artificial Intelligence Mastery program. This repository contains the complete solution to the solar farm analysis project, including data profiling, exploratory analysis, cross-country comparison, and an interactive dashboard.

---

## 🚀 Project Objective

MoonLight Energy Solutions is seeking data-driven insights to guide sustainable investments in solar farms across **Benin**, **Sierra Leone**, and **Togo**. This project analyzes key environmental metrics from each country to identify high-potential regions for solar deployment.

---

## 📁 Repository Structure

```bash
.
├── data/                      # Raw & cleaned data (ignored in git)
├── notebooks/                # EDA and comparison notebooks
│   ├── benin_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   ├── togo_eda.ipynb
│   └── compare_countries.ipynb
├── app/                      # Streamlit dashboard
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── dashboard_screenshots/    # Screenshot(s) of Streamlit app
├── .github/workflows/        # GitHub Actions CI pipeline
│   └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md                 # Project documentation
└── reports/                  # Final report (Markdown or PDF)
````

---

## 🧪 Methodology

This project followed a structured data science pipeline:

1. **Git & Environment Setup**

   * Repo initialized with `.gitignore`, `requirements.txt`, and GitHub Actions CI.
   * Environment reproducibility ensured via `venv` and proper commit hygiene.

2. **Data Profiling & Cleaning**

   * Handled missing values and outliers using statistical techniques.
   * Computed Z-scores for key metrics (GHI, DNI, DHI, ModA, ModB, WS).
   * Cleaned datasets exported to `/data` folder for analysis.

3. **Exploratory Data Analysis (EDA)**

   * Summary stats, correlation heatmaps, and time series visualizations.
   * Impact of cleaning events analyzed.
   * Wind and temperature distributions explored.

4. **Cross-Country Comparison**

   * Boxplots for irradiance metrics.
   * Summary table with mean, median, and standard deviation.
   * One-way ANOVA test on GHI to confirm statistically significant differences.

5. **Interactive Dashboard (Bonus)**

   * Developed using Streamlit for real-time exploration of solar metrics.
   * Users can select country and metric for dynamic plots and tables.

---

## 📊 Key Insights

* **Benin** showed the highest average and median GHI, indicating top solar potential.
* **Sierra Leone** had high variability, offering both opportunity and uncertainty.
* **Togo** exhibited stable, moderate solar radiation — suitable for balanced deployment.
* **Statistical Test:** One-way ANOVA on GHI yielded a p-value < 0.0001, confirming the differences across countries are significant.

---

## 💻 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Becky-Chala/solar-challenge-week0.git
cd solar-challenge-week0
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
venv\Scripts\activate           # Windows

pip install -r requirements.txt
```

### 3. Launch the Streamlit dashboard

---

## ✅ Tasks Completed

* [x] Task 1 – GitHub setup and CI/CD pipeline
* [x] Task 2 – Data cleaning, profiling, and exploratory analysis
* [x] Task 3 – Cross-country comparison and statistical testing
* [x] Bonus – Streamlit dashboard

---

## 📌 Notes

* All data files in the `/data` folder are excluded from version control.
* This project was developed as part of the 10 Academy Week 0 challenge.

---

## 🧠 Author

**Bereket**
Candidate, 10 Academy – Artificial Intelligence Mastery
\[Ethiopia, 2025]

---

## 📄 License

This project is for educational and evaluation purposes under the 10 Academy program. No commercial license is granted.

```
