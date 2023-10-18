import pandas as pd
import streamlit as st

COFFEE_PALETTE = ["#38220f", "#634832", "#634832", "#dbc1ac", "#ece0d1"]


@st.cache
def load_data(csv_path):
    data_df = pd.read_csv(csv_path)
    return data_df


@st.cache_data
def select_top_totals(df, country_column, total_column, top_rows):
    top_df = (
        df[[country_column, total_column]]
        .sort_values(
            by=[total_column],
            ascending=True
        )
        .head(top_rows)
    )
    return top_df


@st.cache_data
def select_top_years(df, total_column, top_rows):
    top_df = (
        df
        .sort_values(by=[total_column], ascending=False)
        .head(2)
        .drop([total_column], axis=1)
        .reset_index(drop=True)
        .T
    )
    top_df = top_df.rename(columns=top_df.iloc[0]).rename_axis("Year")
    return top_df
