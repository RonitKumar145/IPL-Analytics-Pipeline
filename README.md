# 🏏 IPL Analytics Pipeline

An end-to-end Data Analytics project that automates IPL data ingestion, cleaning, transformation, SQL storage, and interactive visualization. The project demonstrates a production-style ETL (Extract, Transform, Load) pipeline using Python, SQLite, and Streamlit.

---

## 📌 Overview

The IPL Analytics Pipeline processes raw IPL match datasets into clean, analysis-ready data and provides interactive dashboards for exploring team, player, venue, and season statistics.

The project follows a real-world analytics workflow:

```
Raw CSV Files
      │
      ▼
Extract
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
SQLite Database
      │
      ▼
SQL Analytics
      │
      ▼
Interactive Dashboard
```

---

# 🎯 Objectives

- Build a modular ETL pipeline
- Clean and validate raw IPL datasets
- Engineer meaningful cricket analytics features
- Store processed data in SQLite
- Perform SQL-based analysis
- Visualize insights through an interactive Streamlit dashboard

---

# 🛠 Tech Stack

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- SQLAlchemy
- SQLite3
- Plotly
- Matplotlib
- Streamlit

### Tools

- VS Code
- Git
- GitHub
- Jupyter Notebook

---

# 📂 Project Structure

```text
IPL-Analytics-Pipeline/
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── processed/
│
├── notebooks/
│
├── pipeline/
│   ├── extract.py
│   ├── clean.py
│   ├── transform.py
│   ├── load.py
│   └── utils.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   └── app.py
│
├── reports/
│
├── images/
│
├── requirements.txt
├── README.md
└── main.py
```

---

# 📊 Dataset

The project uses publicly available Indian Premier League (IPL) datasets containing:

- Match Details
- Ball-by-Ball Data
- Player Information
- Team Information
- Venues
- Seasons

---

# ⚙️ ETL Pipeline

### 1️⃣ Extract

- Read raw CSV files
- Validate dataset structure

### 2️⃣ Transform

- Remove duplicate records
- Handle missing values
- Fix data types
- Standardize column names
- Engineer cricket-specific features

### 3️⃣ Load

- Store cleaned data in SQLite
- Execute SQL analytics queries

---

# 📈 Feature Engineering

The pipeline generates advanced cricket metrics including:

- Run Rate
- Strike Rate
- Economy Rate
- Boundary Percentage
- Dot Ball Percentage
- Winning Margin
- Powerplay Runs
- Death Overs Runs
- Venue Win Percentage
- Team Win Percentage

---

# 📊 Dashboard Features

### 🏏 Team Analytics

- Total Matches
- Win Percentage
- Home vs Away Wins
- Toss Impact
- Highest Team Scores

### 👤 Player Analytics

- Orange Cap Leaderboard
- Purple Cap Leaderboard
- Strike Rate Analysis
- Economy Rate
- Batting Average

### 🏟 Venue Analytics

- Highest Scores
- Best Chasing Grounds
- Average First Innings Score
- Venue Win Distribution

### 📅 Season Analytics

- Points Table
- Runs Distribution
- Wickets Distribution
- Team Performance Trends

### 📈 Match Analytics

- Winning Margin
- Highest Successful Chase
- Lowest Defended Total
- Super Over Matches

---

# 🗄 SQL Analytics

Example business questions answered:

- Top 10 Run Scorers
- Top Wicket Takers
- Best Strike Rate
- Best Economy
- Most Sixes
- Most Fours
- Highest Successful Chase
- Lowest Defended Total
- Toss Impact on Match Result
- Team Win Percentage
- Venue Performance Analysis

---

# 📸 Screenshots

### 🏠 Dashboard

*(Coming Soon)*

### 📊 Team Analytics

*(Coming Soon)*

### 👤 Player Analytics

*(Coming Soon)*

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/IPL-Analytics-Pipeline.git
```

Navigate into the project

```bash
cd IPL-Analytics-Pipeline
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📚 Skills Demonstrated

- Data Cleaning
- Data Validation
- ETL Pipeline Development
- Feature Engineering
- SQL Querying
- Data Visualization
- Dashboard Development
- Python Programming
- SQLite Database
- Git & GitHub

---

# 🚀 Future Improvements

- PostgreSQL Integration
- Docker Support
- Airflow Scheduling
- Automated Data Validation
- Power BI Dashboard
- Cloud Deployment
- CI/CD Pipeline

---

# 👨‍💻 Author

**Ronit Kumar**

Artificial Intelligence & Machine Learning Student

GitHub: https://github.com/RonitKumar145

LinkedIn: https://www.linkedin.com/in/ronit-kumar-64271b258

---

⭐ If you found this project useful, consider giving it a Star!