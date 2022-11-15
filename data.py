import streamlit as st
import pandas as pd, numpy as np
# S6.3: Divide the web page into three columns to add more widgets.
def app(car_df):
    # Displaying orginal dataset
    st.header("View Data")
    # Add an expander and display the dataset as a static table within the expander.
    with st.expander("View Dataset"):
        st.table(car_df)

    # Display descriptive statistics.
    st.subheader("Columns Description:")
    if st.checkbox("Show summary"):
        st.table(car_df.describe())    
    
    # ADD NEW CODE FROM HERE
    beta_col1, beta_col2, beta_col3 = st.columns(3)

    # Add a checkbox in the first column. Display the column names of 'car_df' on the click of checkbox.
    with beta_col1:
        if st.checkbox("Show all column names"):
            st.table(list(car_df.columns))

    # Add a checkbox in the second column. Display the column data-types of 'car_df' on the click of checkbox.
    with beta_col2:
      if st.checkbox('View columns data-types'):
        st.table(car_df.dtypes)
    # Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
    with beta_col3:
      if st.checkbox("View columns data"):
        column = st.selectbox("select column", tuple(car_df.columns))
        st.write(car_df[column])