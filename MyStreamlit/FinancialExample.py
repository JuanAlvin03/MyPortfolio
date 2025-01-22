# ==============================
# Imports
import streamlit as st
import pandas as pd
import plotly.express as px

# ==============================
# Page Config
st.set_page_config(
    page_title="Financial Data",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

# ==============================
# Get Data From Excel
def load_data():
    dataset_path = 'https://github.com/JuanAlvin03/Datasets/raw/main/Financial_Sample.xlsx'
    dataset = pd.read_excel(dataset_path, sheet_name="Sheet1")  # 'Sales' column has space somehow at beginning, so please use ' Sales' to refer to it
    dataset.rename(columns={' Sales': 'Sales'}, inplace=True)
    dataset = dataset[dataset['Year'] != 2013]
    return dataset

# ==============================
# Plot Pie Chart
def plot_pie_chart(df, measurement, product):
    if product:
        df_filtered = df[df['Product'].isin(product)]
    else:
        df_filtered = df

    df_grouped = df_filtered.groupby('Country')[measurement].sum().reset_index()
    fig = px.pie(df_grouped, names='Country', values=measurement, title=f'Selected product(s) {measurement} for each Country')
    st.plotly_chart(fig)

# ==============================
# Plot Line Chart
def plot_line_chart(df, measurement, product):
    if product:
        df_filtered = df[df['Product'].isin(product)]
    else:
        df_filtered = df

    #df_filtered = df[df['Product'] == product]
    df_filtered['Month'] = pd.to_datetime(df_filtered['Date']).dt.to_period('M')
    df_filtered['Month'] = df_filtered['Month'].dt.to_timestamp()
    df_grouped = df_filtered.groupby('Month')[measurement].sum().reset_index()
    fig = px.line(df_grouped, x='Month', y=measurement, title=f'Monthly {measurement} for selected product(s)')
    st.plotly_chart(fig)

# ==============================
# Calculate Measurements (Units sold, Sales, Profit)
def calculate_measurements(df, product, measurement):
    if product:
        df_filtered = df[df['Product'].isin(product)]
    else:
        df_filtered = df

    return df_filtered[measurement].sum()

# ==============================
# Format Number
def format_number(number):
    number = int(number)
    formatted_number = f"{number:,}"
    return formatted_number

# ==============================
# Main (might just remove main and the bottom 2 lines)
def main():
    dataset = load_data()

    # ==============================
    # Sidebar
    with st.sidebar:
        st.title("2014 Financial/Sales Data")

        product_unique_list = dataset['Product'].unique().tolist()
        selected_product = st.multiselect('Select Product(s): ', options=product_unique_list,
                                          placeholder="Select Product...")

        measurement = ['Units Sold', 'Gross Sales', 'Discounts', 'Sales', 'COGS', 'Profit']
        selected_measurement = st.selectbox('Select Measurement', options=measurement, index=0,
                                            placeholder="Select Measurement...")

        products_manufacturing_price = dataset.groupby('Product')['Manufacturing Price'].unique().reset_index()

        with st.expander("Products' Manufacturing Price"):
            st.dataframe(products_manufacturing_price, hide_index=True)

    # ==============================
    # Columns
    col = st.columns((1, 1, 1), gap='medium')
    with col[0]:
        st.metric(label="Units Sold", value=format_number(calculate_measurements(dataset, selected_product, "Units Sold")))

    with col[1]:
        st.metric(label="Sales", value=format_number(calculate_measurements(dataset, selected_product, "Sales")))

    with col[2]:
        st.metric(label="Profit", value=format_number(calculate_measurements(dataset, selected_product, "Profit")))

    col2 = st.columns((1.5, 1.5), gap='medium')
    with col2[0]:
        plot_pie_chart(dataset, selected_measurement, selected_product)

    with col2[1]:
        plot_line_chart(dataset, selected_measurement, selected_product)

if __name__ == "__main__":
    main()
