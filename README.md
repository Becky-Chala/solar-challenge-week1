# solar-challenge-week1

Week 1 challenge for solar data analysis.

## Environment Setup

To set up the development environment for this project:

  Clone the repository:
    
    git clone https://github.com/Becky-Chala/solar-challenge-week1.git
    cd solar-challenge-week1
    py -m venv .venv
    .venv\Scripts\activate  #this will activate the virtual enviroment
 
  
  # ☀️ Solar Dataset EDA: West African Countries

This project performs **end-to-end exploratory data analysis (EDA), profiling, and cleaning** on solar energy datasets from multiple West African countries. The objective is to prepare these datasets for meaningful **region-wise comparison** and **solar potential ranking** to support renewable energy planning and investment.

---

## 📂 Countries Covered

- 🇧🇯 **Benin**
- 🇸🇱 **Sierra Leone**
- 🇹🇬 **Togo**

Each country has its own EDA notebook and cleaned CSV file (not included in repo due to `.gitignore` rules).

---

## 🧩 Problem Statement

Solar energy potential is high in Sub-Saharan Africa, but poor-quality or uncleaned datasets make it difficult to compare regions and make strategic decisions. This project:
- Cleans, profiles, and explores solar datasets per country.
- Detects anomalies, missing values, and data quality issues.
- Provides statistical and visual insights into solar potential, temperature effects, and wind patterns.

---

## 🧪 EDA Workflow Summary

### ✅ Step-by-step for Each Country:
1. **Summary Statistics & Missing Values**
   - `df.describe()` and null percentage check.
2. **Outlier Detection**
   - Z-score method on key features like `GHI`, `DNI`, `DHI`, `ModA`, `WS`.
3. **Missing Value Handling**
   - Imputation with column medians.
4. **Time Series Analysis**
   - `GHI`, `DNI`, `Tamb` plotted over time.
5. **Sensor Cleaning Impact**
   - `ModA`, `ModB` before/after cleaning.
6. **Correlation Analysis**
   - Heatmaps and scatter plots of relevant variables.
7. **Wind Analysis**
   - Wind rose plots and wind distribution histograms.
8. **Temperature-Humidity Interaction**
   - Relative humidity effects on solar radiation.
9. **Bubble Charts**
   - `GHI` vs `Tamb`, with bubble size = RH or BP.

---
