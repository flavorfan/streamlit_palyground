import streamlit as st
import pandas as pd
import numpy as np


st.title("Hello, world!")

# sider
with st.sidebar:
    st.header("Sidebar")
    st.write("this is my first app")
    
## text
# st.header
# https://docs.streamlit.io/develop/api-reference/text/st.header
st.header("This is a header with a divider", divider="rainbow")

## laygout & input
st.subheader("st.columns")
col1, col2 = st.columns(2)
with col1:
    x = st.slider("Select a value",1, 10)

with col2:
    st.write("The value of :blue[****x****] is", x)

## chart
st.subheader("st.area_chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)