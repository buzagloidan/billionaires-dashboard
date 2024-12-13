import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("billionaires.csv")

# Clean columns
df.columns = df.columns.str.strip()  # Remove leading/trailing spaces
df.rename(columns={
    "Total net worth": "TotalNetWorth",
    "$ Last change": "LastChange",
    "$ YTD change": "YTDChange",
    "Country / Region": "CountryRegion"
}, inplace=True)

# Split CountryRegion
temp = df['CountryRegion'].str.split(pat='/', n=1, expand=True)
df['Country'] = temp[0].str.strip()
if temp.shape[1] > 1:
    df['Region'] = temp[1].str.strip()
else:
    df['Region'] = None
df.drop("CountryRegion", axis=1, inplace=True)

# Function to convert currency-like strings
def convert_currency(x):
    if not isinstance(x, str):
        return x
    x = x.replace('$', '').replace(',', '')
    multiplier = 1
    if x.endswith('B'):
        multiplier = 1_000_000_000
        x = x[:-1]
    elif x.endswith('M'):
        multiplier = 1_000_000
        x = x[:-1]
    elif x.endswith('k'):
        multiplier = 1_000
        x = x[:-1]
    if x.strip() == '':
        x = '0'
    return float(x) * multiplier

df['TotalNetWorth'] = df['TotalNetWorth'].apply(convert_currency)
df['LastChange'] = df['LastChange'].apply(lambda val: convert_currency(val.replace('+','').replace('-','')))
df['YTDChange'] = df['YTDChange'].apply(lambda val: convert_currency(val.replace('+','').replace('-','')))

# Ensure Name column exists
if 'Name' not in df.columns:
    st.write("Error: 'Name' column not found.")
    st.stop()

st.set_page_config(page_title="Bloomberg Billionaires Dashboard", layout="wide")

st.title("Bloomberg Billionaires Dashboard")

# Layout using columns
col1, col2, col3 = st.columns(3)

total_billionaires = len(df)
richest_person = df.loc[df['TotalNetWorth'].idxmax()]
col1.metric(label="Total Billionaires Listed", value=total_billionaires)
col2.metric(label="Richest Individual", value=richest_person['Name'])
col3.metric(label="Net Worth", value=f"{richest_person['TotalNetWorth'] / 1e9:.2f}B")

# Sidebar filters
country_list = ["All"] + sorted(df['Country'].dropna().unique().tolist())
selected_country = st.sidebar.selectbox("Filter by Country", country_list)

industry_list = ["All"] + sorted(df['Industry'].dropna().unique().tolist())
selected_industry = st.sidebar.selectbox("Filter by Industry", industry_list)

# Filter data based on selections
filtered_df = df.copy()
if selected_country != "All":
    filtered_df = filtered_df[filtered_df['Country'] == selected_country]
if selected_industry != "All":
    filtered_df = filtered_df[filtered_df['Industry'] == selected_industry]

st.write("### Data Preview")
st.write(f"Showing data for: {selected_country if selected_country != 'All' else 'All Countries'} and {selected_industry if selected_industry != 'All' else 'All Industries'}")

# Format numerical columns nicely
def format_billions(x):
    if pd.isnull(x):
        return ""
    if x >= 1e9:
        return f"${x/1e9:.2f}B"
    elif x >= 1e6:
        return f"${x/1e6:.2f}M"
    elif x >= 1e3:
        return f"${x/1e3:.2f}k"
    else:
        return f"${x:.2f}"

styled_df = filtered_df[['Rank', 'Name', 'Country', 'TotalNetWorth', 'YTDChange', 'Industry']].copy()
styled_df['TotalNetWorth'] = styled_df['TotalNetWorth'].apply(format_billions)
styled_df['YTDChange'] = styled_df['YTDChange'].apply(format_billions)

st.dataframe(styled_df)

# Plot: Top 10 Countries by Average Net Worth
avg_networth = (df.groupby('Country', as_index=False)['TotalNetWorth']
                  .mean()
                  .dropna()
                  .sort_values('TotalNetWorth', ascending=False)
                  .head(10))
fig_bar = px.bar(avg_networth, x='Country', y='TotalNetWorth', title='Top 10 Countries by Average Net Worth', labels={'TotalNetWorth': 'Net Worth'})
fig_bar.update_yaxes(tickprefix="$", ticksuffix="B", tickformat=".2f")
st.plotly_chart(fig_bar, use_container_width=True)

# Add another visualization (e.g., scatter plot of YTDChange vs TotalNetWorth)
fig_scatter = px.scatter(df, x='TotalNetWorth', y='YTDChange', hover_data=['Name', 'Country', 'Industry'],
                         title="YTD Change vs Total Net Worth",
                         labels={'TotalNetWorth': 'Total Net Worth (B)', 'YTDChange': 'YTD Change (B)'})
fig_scatter.update_xaxes(tickprefix="$", ticksuffix="B", tickformat=".2f")
fig_scatter.update_yaxes(tickprefix="$", ticksuffix="B", tickformat=".2f")
st.plotly_chart(fig_scatter, use_container_width=True)
