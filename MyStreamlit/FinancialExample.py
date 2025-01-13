import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
    dataset_path = 'https://github.com/JuanAlvin03/Datasets/raw/main/Financial_Sample.xlsx'
    dataset = pd.read_excel(dataset_path, sheet_name="Sheet1")  # 'Sales' column has space somehow at beginning, so please use ' Sales' to refer to it
    dataset.rename(columns={' Sales': 'Sales'}, inplace=True)
    return dataset

def plot_chart(df, selected_product, selected_metric):
    if selected_product:
        filtered_df = df[df['Product'].str.contains(selected_product, na=False)]
    else:
        filtered_df = df

    #sum_of_metric = filtered_df[selected_metric].sum()
    #sum_of_units_sold = filtered_df['Units Sold'].sum()

    fig = px.pie(filtered_df, values=selected_metric, names='Country', title=f"{selected_metric} by country")

    st.plotly_chart(fig)

def main():
    dataset = load_data()
    st.title("2014 Financial/Sales Data")

    metrics = ['Units Sold', 'Gross Sales', 'Discounts', 'Sales', 'COGS', 'Profit']
    selected_metric = st.selectbox('Select Metric', options=metrics, index=None, placeholder="Select Metric...")

    product_unique_list = dataset['Product'].unique().tolist()
    selected_product = st.selectbox('Select Product', options=product_unique_list, index=None, placeholder="Select Product...")

    plot_chart(dataset, selected_product, selected_metric)

if __name__ == "__main__":
    main()
