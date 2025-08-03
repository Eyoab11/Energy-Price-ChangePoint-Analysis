# 📈 Brent Oil Price - Event Impact Analysis

**Project Status**: 🟢 *In Progress*  
**Task 1**: ✅ *Complete*

This repository contains the analysis for the **"Change Point Analysis and Statistical Modelling of Time Series Data"** project. The primary goal is to identify significant structural breaks in the historical Brent oil price series and associate them with major geopolitical and economic events.

The insights from this analysis aim to help **investors, analysts, and policymakers at Birhan Energies** understand market volatility and make better data-driven decisions.

---

## 🎯 Business Objective

The main objective is to study how important global events impact **Brent oil prices**. This includes identifying price changes linked to:
- Political decisions
- Conflicts in oil-producing regions
- Global economic sanctions
- Changes in OPEC policies

The aim is to provide clear, actionable insights to help stakeholders better understand and respond to price volatility.

---

## 🗂 Project Structure

The project follows a standard data science workflow:

```bash
Energy-Price-ChangePoint-Analysis/
├── data/
│ ├── 01_raw/ # Original, immutable data (BrentOilPrices.csv)
│ └── 02_processed/ # Cleaned and processed data for modeling
├── notebooks/ # Jupyter notebooks for exploration and analysis
├── reports/
│ └── task-1/ # Generated plots and figures from Task 1
├── src/ # (Future Use) Source code for modeling and utilities
└── venv/ # Project-specific Python virtual environment
```
## ⚙️ Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Energy-Price-ChangePoint-Analysis.git
   cd Energy-Price-ChangePoint-Analysis

2. **🛠️ Create and Activate a Virtual Environment**

### For Windows (PowerShell):
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. **For macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

4. **Install Dependencies**
```bash
pip install -r requirements.txt
```
Note: Make sure you've created requirements.txt using:
```bash
pip freeze > requirements.txt
```

## 🔄 Workflow

Each task in the analysis has its own dedicated Jupyter notebook.

---

### ✅ Task 1: Foundational Analysis & EDA  
**Notebook**: `notebooks/01_data_ingestion_and_eda.ipynb`

---

### ✔️ Steps Completed:

- Loaded raw Brent oil price data  
- Cleaned data, formatted dates, and set time series index  
- Tested for stationarity  
- Transformed series to log returns  
- Compiled a list of global events and visualized against price  
- Saved all visualizations and final dataset  

---

## 📌 Key Findings from Task 1

### 🧪 Stationarity Test on Raw Price Data
```yaml
ADF Statistic: -1.9939  
p-value: 0.2893  
Conclusion: NON-STATIONARY (p > 0.05)
```

## 🧪 Stationarity Test on Log Returns
```bash
ADF Statistic: -16.4271  
p-value: 0.0000  
Conclusion: STATIONARY (p <= 0.05)
```

## 📊 Event Overlay Analysis

Visual analysis of key geopolitical and economic events  
(e.g., **Gulf War**, **2008 Financial Crisis**, **COVID-19**)  
shows strong correlation with Brent oil price shifts.

---

## 💾 Processed Dataset Saved To

```bash
data/02_processed/brent_prices_processed.csv
```
## 🚀 Next Steps

### 🔹 Task 2: Change Point Modeling  
Apply a **Bayesian Change Point model** using **PyMC3** to statistically identify structural breaks in the log return series.

### 🔹 Task 3: Dashboard Development  
Build an **interactive dashboard** using **Flask + React** to visualize and present analytical findings to stakeholders.

---

## 🧰 Technology Stack

- **Language**: Python 3.13  
- **Core Libraries**: Pandas, NumPy, Matplotlib, Seaborn  
- **Statistical Analysis**: Statsmodels  
- **Bayesian Modeling**: PyMC  
- **Development Environment**: VS Code, Jupyter Notebooks

## Thank You
