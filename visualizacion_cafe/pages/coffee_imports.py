import plotly.express as px
import streamlit as st

from common import load_data, select_top_totals, select_top_years
from common import COFFEE_PALETTE


imports_df = load_data("coffee_files/Coffee_import.csv")

st.title("Top 5 Coffee Importer Countries")

top_imports = select_top_totals(imports_df, "Country", "Total_import", 5)
top_imports_fig = px.bar(
    top_imports,
    x="Total_import",
    y="Country",
    orientation="h",
    title="Top 5 Total of Kg of Coffee imported per Country (1990-2019)",
    labels={"Total_import": "Total imports (kg)"},
    color_discrete_sequence=COFFEE_PALETTE
)
top_imports_fig.update_layout(yaxis={'categoryorder':'total ascending'})
st.plotly_chart(top_imports_fig)

year_imports = select_top_years(imports_df, "Total_import", 5)
year_imports_figure = px.line(
    year_imports,
    title="Top 5 Coffee importers imports per year (1990-2019)",
    labels={"value": "Imports (Kg)", "variable": "Country"},
    color_discrete_sequence=COFFEE_PALETTE,
)
st.plotly_chart(year_imports_figure)
