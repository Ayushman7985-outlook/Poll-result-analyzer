# 📊 Poll Results Visualization Dashboard

An interactive data analytics project built with **Python, Streamlit, Pandas, and Plotly** to explore poll responses, compare voting preferences, and uncover audience insights through interactive visualizations.

## 🚀 Project Overview

The Poll Results Visualization Dashboard converts poll-response data into meaningful insights using an interactive web interface. Users can explore voting preferences, analyze demographic patterns, filter responses, and examine the underlying dataset.

## ✨ Key Features

- 📌 **Overview Dashboard** — View important metrics and response summaries.
- 📊 **Poll Results Analysis** — Compare answer options through interactive charts.
- 🥧 **Pie and Donut Charts** — Understand the distribution of responses.
- 👥 **Audience Insights** — Explore poll responses by region and age group.
- 📈 **Trend Analysis** — Examine response patterns over time when timestamp data is available.
- 🎛️ **Interactive Filters** — Filter by question, option, region, age group, and dates.
- 📂 **Raw Data Explorer** — Inspect records and download filtered results as CSV.
- 🔎 **Data Quality Checks** — Review the dataset for potential data issues.
- 🎨 **Professional Interface** — Organized sidebar navigation and a clean dashboard layout.

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 🎈 Streamlit | Interactive dashboard interface |
| 🐼 Pandas | Data manipulation and analysis |
| 📊 Plotly | Interactive charts and visualizations |
| 🧪 Pytest | Automated testing |

## 📁 Project Structure

```text
Poll Results Visualize/
├── app.py
├── data/
│   └── poll_responses.csv
├── src/
│   └── analysis.py
├── tests/
│   └── test_project.py
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: The exact files inside `src/` and `tests/` may differ depending on the current implementation.*

## 🗃️ Dataset

The project uses `data/poll_responses.csv`, containing poll-response information such as:

- Respondent ID
- Timestamp
- Question
- Option
- Region
- Age Group

The dashboard is designed around poll responses, not airline safety data.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd "Poll Results Visualize"
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository's actual URL.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Dashboard

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## 🧪 Running Tests

Run the project's automated tests:

```bash
python -m pytest -q
```

All tests should pass before submitting changes.

## 🖥️ How to Use

1. Launch the Streamlit application.
2. Select a section from the left sidebar.
3. Apply filters to explore specific responses.
4. Compare answer options using interactive charts.
5. Examine regional, age-group, and time-based patterns.
6. Inspect or download filtered data.

## 🔮 Future Enhancements

- Add more statistical analyses and comparison charts.
- Support compatible CSV uploads.
- Improve data validation and test coverage.
- Add additional demographic insights.
- Deploy the dashboard online.

## 👨‍💻 Author

Developed as a data science and data visualization project.

## 📄 License

For educational and portfolio use. Add a formal open-source license if you intend to permit redistribution under specific terms.
