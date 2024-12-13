# Bloomberg Billionaires Dashboard

[![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-red?logo=streamlit)](https://streamlit.io/)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg?logo=python)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

An interactive dashboard built with **Streamlit** and **Plotly** to explore the Bloomberg Billionaires Index. Visualize net worth, growth trends, and distributions across countries and industries in a user-friendly environment.

<img src="path_to_your_screenshot.png" alt="Dashboard Screenshot" width="80%">

## Features

- **Global Data Preview:**  
  Explore a filtered list of billionaires, including key attributes like Rank, Name, Country, Net Worth, and Industry.

- **Dynamic Filters:**  
  Use the sidebar to filter by Country and Industry, updating the charts and tables in real-time.

- **Visual Insights:**  
  - **Top 10 Countries by Average Net Worth:** Quick snapshot of where the wealth is concentrated.
  - **YTD Change vs. Total Net Worth Scatter:** Understand how fortunes fluctuate over time.

- **Key Metrics:**  
  Display the total count of billionaires and identify the richest individual at a glance.

## Getting Started

### Prerequisites

- **Python 3.9+** (though it may work with earlier versions)
- **pip** or **conda** for installing dependencies

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/buzagloidan/billionaires-dashboard.git
   cd billionaires-dashboard
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   On Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add the dataset:**
   Place your `billionaires.csv` file in the project directory. Make sure it matches the expected format (see code comments in `dashboard.py`).

### Running the Dashboard

```bash
streamlit run dashboard.py
```

After running the command, open the provided URL (usually `http://localhost:8501`) in your web browser.

## Directory Structure

```
billionaires-dashboard/
├─ dashboard.py
├─ requirements.txt
├─ billionaires.csv
└─ README.md
```

## Example Screenshots

*Home View (All Countries):*  
*(Insert a screenshot or GIF here)*

## Customization

- **Columns & Renaming:** Adjust column names or mapping in `dashboard.py` if your dataset differs.
- **Filters:** Add more filters (e.g., by net worth range) using `st.slider` or `st.multiselect`.
- **Charts:** Experiment with other Plotly chart types like pie charts, histograms, or box plots for richer insights.

## Contributing

1. Fork the repository
2. Create a feature branch:  
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch:  
   ```bash
   git push origin feature/new-feature
   ```
5. Open a Pull Request and describe your changes

## License

This project is licensed under the [MIT License](LICENSE).
