import streamlit as st
import pandas as pd
import plotly.express as px

# REMOVE 2013 DATA??

st.set_page_config(
    page_title="Financial Data",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

def load_data():
    dataset_path = 'https://github.com/JuanAlvin03/Datasets/raw/main/Financial_Sample.xlsx'
    dataset = pd.read_excel(dataset_path, sheet_name="Sheet1")  # 'Sales' column has space somehow at beginning, so please use ' Sales' to refer to it
    dataset.rename(columns={' Sales': 'Sales'}, inplace=True)
    # Remove 2013 data??
    return dataset

def plot_pie_chart(df):
    df['Discount Band'] = df['Discount Band'].fillna('None')
    discount_band_counts = df['Discount Band'].value_counts()

    fig = px.pie(discount_band_counts, names=discount_band_counts.index, values=discount_band_counts.values, title="Sales per Discount Band")

    st.plotly_chart(fig)

def calculate_measurements(df, product, measurement):
    if product:
        df = df[df['Product'].str.contains(product, na=False)]

    return df[measurement].sum()

def main():
    dataset = load_data()
    st.title("2014 Financial/Sales Data")

    col = st.columns((1, 1, 1, 1), gap='medium')

    with col[0]:
        product_unique_list = dataset['Product'].unique().tolist()
        selected_product = st.selectbox('Select Product', options=product_unique_list, index=0, placeholder="Select Product...")

    with col[1]:
        #country_unique_list = dataset['Country'].unique().tolist()
        #selected_country = st.selectbox('Select Country', options=country_unique_list, index=0, placeholder="Select Country...")

        #segment_unique_list = dataset['Segment'].unique().tolist()
        #selected_segment = st.selectbox('Select Segment', options=segment_unique_list, index=0, placeholder="Select Segment...")
        st.metric(label="Units Sold", value=calculate_measurements(dataset, selected_product, "Units Sold"))

    with col[2]:
        #plot_pie_chart(dataset)
        st.metric(label="Sales", value=calculate_measurements(dataset, selected_product, "Sales"))

    with col[3]:
        st.metric(label="Profit", value=calculate_measurements(dataset, selected_product, "Profit"))

    col2 = st.columns((1, 1.5, 1.5), gap='medium')
    with col2[0]:
        measurement = ['Units Sold', 'Gross Sales', 'Discounts', 'Sales', 'COGS', 'Profit']
        selected_measurement = st.selectbox('Select Measurement', options=measurement, index=0, placeholder="Select Measurement...")

    with col2[1]:
        st.markdown("# Country/Segment")

    with col2[2]:
        st.markdown("# Time")

if __name__ == "__main__":
    main()
