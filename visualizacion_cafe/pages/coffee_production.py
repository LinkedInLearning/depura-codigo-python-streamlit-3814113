import plotly.express as px
import streamlit as st

from common import load_data
from common import COFFEE_PALETTE


production_df =load_data("coffee_files/Coffee_production.csv")

st.title("Production of Coffee per Country")

countries = production_df["Country"].sort_values().unique()
country = st.selectbox(
    "Country",
    countries,
    index=6,
    placeholder="Select the country"
)


country_production_df = (
    production_df
    .loc[production_df["Country"] == country]
    .drop(["Country", "Total_production"], axis=1)
    .reset_index(drop=True)
    .T
)
country_production_df = (
    country_production_df
    .rename(columns=country_production_df.iloc[0])
    .rename_axis("Year")
    .drop(index=country_production_df.index[0])
)

year_production_figure = px.line(
    country_production_df,
    title=f"{country} yearly Production of Coffee (1990-2019)",
    color_discrete_sequence=COFFEE_PALETTE,
    labels={"value": "Production (Kg)", "variable": "Type of Coffe"}
)
st.plotly_chart(year_production_figure)
