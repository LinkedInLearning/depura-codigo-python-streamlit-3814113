import plotly.express as px
import streamlit as st

from common import load_data, select_top_totals, select_top_years
from common import COFFEE_PALETTE


exports_df =load_data("coffee_files/Coffee_export.csv")


st.title("Top Coffee Exporter Countries")
top_value = st.slider("Top of Exporter Countries", 3, 10, 5)

top_exports = select_top_totals(exports_df, "Country", "Total_export", top_value)
top_exports_fig = px.bar(
    top_exports,
    x="Total_export",
    y="Country",
    orientation="h",
    title=f"Top {top_value} of Total of Kg of Coffee exported per Country (1990-2019)",
    labels={"Total_export": "Total exports (kg)"},
    color_discrete_sequence=COFFEE_PALETTE
)
top_exports_fig.update_layout(yaxis={'categoryorder':'total ascending'})
st.plotly_chart(top_exports_fig)

year_exports = select_top_years(exports_df, "Total_export", top_value)
year_exports_figure = px.line(
    year_exports,
    title=f"Top {top_value} Coffee exporters exports per year (1990-2019)",
    labels={"value": "Exports (Kg)", "variable": "Country"},
    color_discrete_sequence=COFFEE_PALETTE,
)
st.plotly_chart(year_exports_figure)
