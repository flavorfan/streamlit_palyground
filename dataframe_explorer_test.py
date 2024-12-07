import streamlit as st
from streamlit_extras.dataframe_explorer import dataframe_explorer, generate_fake_dataframe

def example_one():
    dataframe = generate_fake_dataframe(
        size=500, cols="dfc", col_names=("date", "income", "person"), seed=1
    )
    filtered_df = dataframe_explorer(dataframe, case=False)
    st.dataframe(filtered_df, use_container_width=True)

example_one()