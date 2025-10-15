# 🗽 U.S. Census 5-Year Estimates Dashboard (2019–2023)

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?logo=streamlit&logoColor=white)](https://app-census-5-year-estimate-ktbridge.streamlit.app/)

An interactive **Streamlit dashboard** built using **U.S. Census Bureau data (2019–2023)**.  
It visualizes key demographic and economic indicators across all U.S. states, including:

-  **Population**
-  **Median Household Income**
-  **Per Capita Income**
-  **Poverty Rate**
-  **Median Age**

---

## 📖 Project Overview

This dashboard allows users to explore changes in population, income, and poverty rates across all 50 U.S. states, Washington, D.C., and Puerto Rico between **2019 and 2023**.  
It uses **Plotly** for dynamic data visualization and **Streamlit** for an interactive web interface.

**Live Demo:**  
👉 [Streamlit App](https://app-census-5-year-estimate-ktbridge.streamlit.app/)

---

## 🧩 Features

- Interactive **state filter** (select one or multiple states)
- Year selection (view data for any combination of years 2019–2023)
- Color-coded bar charts for income data
- Bubble charts showing **poverty vs. income relationships**
- Scatter plots for **median age** distribution
- Responsive layout with a sidebar and custom color themes

---

## 🗂️ Data Source

All data was obtained from the **U.S. Census Bureau** using official 5-Year American Community Survey (ACS) estimates:

- [American Community Survey 5-Year Estimates](https://data.census.gov/)

Each dataset (2019–2023) contains:
- `State`
- `Population`
- `Median Age`
- `Household Income`
- `Per Capita Income`
- `Poverty Rate`
- `Poverty Count`

---

##  Installation

To run the app locally:


# Clone the repository
git clone https://github.com/ktbridge/Streamlit-Census-5-Year-Estimate.git
cd Streamlit-Census-5-Year-Estimate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run census_estimates.py
Then open the local URL shown in your terminal (typically http://localhost:8501).

🎨 Preview


🚀 Deployment
This app is deployed via Streamlit Community Cloud:

Push all files (census_estimates.py, datasets, and requirements.txt) to your GitHub repo.

Go to streamlit.io/cloud.

Select your repo and deploy.

Any new commit to main will automatically update the app.

🧠 Technologies Used
Python 3.9+

Streamlit

Plotly Express

Pandas

📜 License
© 2025 Christina Trowbridge.
All rights reserved.
This project is intended for educational and public data visualization purposes only.
