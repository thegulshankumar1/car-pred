# S1.1: Design the "Visualise Data" page of the multipage app.
# Import necessary modules 
import streamlit as st, matplotlib.pyplot as plt, seaborn as sns
# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
    st.header('Visualise data')
    # Remove deprecation warning.
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Subheader for scatter plot.
    st.subheader("Scatter plot")
    # Choosing x-axis values for scatter plots.
    features_list = st.multiselect("Select the x-axis values:", 
                                            ('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))
    # Create scatter plots.
    for feature in features_list:
        st.subheader(f"Scatter plot between {feature} and price")
        plt.figure(figsize = (12, 6))
        sns.scatterplot(x = feature, y = 'price', data = car_df)
        st.pyplot()
    # Add a multiselect widget to allow the user to select multiple visualisation.
    # Add a subheader in the sidebar with label "Visualisation Selector"
    st.subheader("Visualisation Selector")

    # Add a multiselect in the sidebar with label 'Select the charts or plots:'
    # and pass the remaining 3 plot types as a tuple i.e. ('Histogram', 'Box Plot', 'Correlation Heatmap').
    # Store the current value of this widget in a variable 'plot_types'.
    plot_type = st.sidebar.multiselect("Select the chart/plots",('Histogram', 'Box Plot', 'Correlation Heatmap'))

    # Display Histogram for ('carwidth', 'enginesize', 'horsepower') using the 'matplotlib.pyplot' module and the 'st.pyplot()' function.
    if "Histogram" in plot_type:
      st.subheader("Histogram")
      columns = st.selectbox("Select the columns", ('carwidth', 'enginesize', 'horsepower'))
      plt.figure(figsize = (9,5))
      plt.title(f"Histogram for {columns} ")
      plt.hist(car_df[columns],  bins = 'sturges')
      st.pyplot()
        # Note: Histogram is generally created for continuous values not for discrete values.


    # Create box plot for ('carwidth', 'enginesize', 'horsepower') using the 'seaborn' module and the 'st.pyplot()' function.
    if 'Box Plot' in plot_type:
      st.subheader('Box Plot')
      columns = st.selectbox("Select the columns for boxplot", ('carwidth', 'enginesize', 'horsepower') )
      plt.figure(figsize = (16,4))
      plt.title(f'Boxplot for {columns}')
      sns.boxplot(car_df[columns])
      st.pyplot()
    # Display correlation heatmap using the 'seaborn' module and the 'st.pyplot()' function.
    if "Correlation Heatmap" in plot_type:
      st.subheader("Correlation Heatmap")
      plt.figure(figsize = (16,4))
      plt.title(f'Heatmap for {columns}')
      ax = sns.heatmap(car_df.corr(), annot = True)
      top, bottom = ax.get_ylim()
      ax.set_ylim(bottom + 0.5, top - 0.5)
      st.pyplot()
        # Creating an object of seaborn axis and storing it in 'ax' variable

        # Getting the top and bottom margin limits.

        # Increasing the bottom and decreasing the bottom margins respectively.
