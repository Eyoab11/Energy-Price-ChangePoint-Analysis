# dashboard.py

import streamlit as st
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Brent Oil Price Analysis",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- DATA LOADING ---
# Use Streamlit's caching to load data only once
@st.cache_data
def load_data():
    processed_path = os.path.join('data', '02_processed', 'brent_prices_processed.csv')
    df = pd.read_csv(processed_path, index_col='Date', parse_dates=True)
    
    events_data = {
        'EventDate': ['1990-08-02', '1997-07-02', '2001-09-11', '2003-03-20', '2008-09-15', '2011-01-25', '2014-11-27', '2016-11-30', '2020-03-11', '2022-02-24'],
        'EventName': ['Iraq Invades Kuwait', 'Asian Financial Crisis', '9/11 Attacks', 'Start of Iraq War', 'Lehman Collapse', 'Arab Spring', 'OPEC No-Cut', 'OPEC+ Cut', 'COVID-19 Pandemic', 'Russia Invades Ukraine']
    }
    events_df = pd.DataFrame(events_data)
    events_df['EventDate'] = pd.to_datetime(events_df['EventDate'])
    
    return df, events_df

df, events_df = load_data()

# --- SIDEBAR FILTERS ---
st.sidebar.header("Dashboard Filters")

# Date Range Slider
min_date = df.index.min().to_pydatetime()
max_date = df.index.max().to_pydatetime()

start_date, end_date = st.sidebar.slider(
    "Select Date Range:",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),
    format="DD/MM/YYYY"
)

# Filter data based on date range
filtered_df = df[(df.index >= start_date) & (df.index <= end_date)]

# Event Selector
all_events = events_df['EventName'].tolist()
selected_events = st.sidebar.multiselect(
    "Select Events to Highlight:",
    options=all_events,
    default=all_events
)

filtered_events_df = events_df[events_df['EventName'].isin(selected_events)]


# --- MAIN PAGE LAYOUT ---
st.title("🛢️ Brent Oil Price: Event Impact Dashboard")
st.markdown("An interactive dashboard to analyze the impact of major geopolitical and economic events on Brent oil prices.")


# --- KEY METRICS ---
col1, col2, col3 = st.columns(3)
avg_price = filtered_df['Price'].mean()
avg_volatility = filtered_df['log_return'].std() * 100 # In percent
max_price = filtered_df['Price'].max()

col1.metric("Average Price (USD)", f"${avg_price:.2f}")
col2.metric("Avg. Daily Volatility", f"{avg_volatility:.2f}%")
col3.metric("Max Price in Period", f"${max_price:.2f}")


# --- INTERACTIVE TIME SERIES CHART ---
st.header("Price and Volatility Analysis")

# Create figure with Plotly
fig = go.Figure()

# Add Price trace
fig.add_trace(go.Scatter(x=filtered_df.index, y=filtered_df['Price'], mode='lines', name='Price (USD)'))

# Add event markers
for _, event in filtered_events_df.iterrows():
    if start_date <= event['EventDate'] <= end_date:
        fig.add_vline(x=event['EventDate'], line_width=1, line_dash="dash", line_color="red")
        fig.add_annotation(x=event['EventDate'], y=filtered_df['Price'].max(), text=event['EventName'],
                           showarrow=False, yshift=10, textangle=-90, font=dict(color="red"))

# Update layout
fig.update_layout(
    title='Brent Oil Prices with Key Events',
    xaxis_title='Date',
    yaxis_title='Price per Barrel (USD)',
    hovermode='x unified'
)

st.plotly_chart(fig, use_container_width=True)


# --- DATA TABLE ---
st.header("Filtered Data")
st.dataframe(filtered_df.style.format({'Price': '${:.2f}', 'log_return': '{:.4f}'}))