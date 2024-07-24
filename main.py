"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd

st.title("hello quyet")
# df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})

# df
st.subheader("sub header")
st.header("header")
st.text("text")
# st.markdown("`print('abc')`")
# st.markdown("**hello markdown**")
# st.markdown("---")
# st.caption("abc")

code_str = """
print("test")
def hello():
    print("hello")
"""
st.code(code_str, language="python")

st.metric(label="wind speed", value="100ms/^-1", delta="-2.1ms/^-2")
