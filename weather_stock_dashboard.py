import streamlit as st
import pandas as pd
import plost

# Configure the layout of the app
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

# Custom CSS for spacing and alignment adjustments
st.markdown("""
    <style>
    /* Reduce space above the sidebar header */
    [data-testid="stSidebar"] .block-container {
        padding-top: 1em;
    }

    /* Adjust main header spacing */
    .css-1d391kg { /* This targets the main header for the Streamlit app */
        margin-top: -2em; /* Adjust this value as needed */
    }

    /* Styling sidebar header */
    .css-1aumxhk h2 {
        margin-top: -1em; /* Adjust space above sidebar header */
        font-weight: bold;
    }

    /* Styling for metric containers */
    div[data-testid="metric-container"] {
        background-color: #FFFFFF;
        border: 1px solid #CCCCCC;
        padding: 5% 5% 5% 10%;
        border-radius: 5px;
        border-left: 0.5rem solid #9AD8E1 !important;
        box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.15) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar configuration
st.sidebar.header('Weather Stock Dashboard')

st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max'))

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))

st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

st.sidebar.markdown('''
---
Created with ❤ by Python
''')

# Row A: Display Metrics
st.markdown('## Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# Load datasets
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

# Row B: Heatmap and Donut Chart
c1, c2 = st.columns((7, 3))
with c1:
    st.markdown('### Heatmap')
    plost.time_hist(
        data=seattle_weather,
        date='date',
        x_unit='week',
        y_unit='day',
        color=time_hist_color,
        aggregate='median',
        legend=None,
        height=345,
        use_container_width=True
    )
with c2:
    st.markdown('### Donut chart')
    plost.donut_chart(
        data=stocks,
        theta=donut_theta,
        color='company',
        legend='bottom',
        use_container_width=True
    )

# Row C: Line chart
st.markdown('## Line chart')
st.line_chart(seattle_weather, x='date', y=plot_data, height=plot_height)
