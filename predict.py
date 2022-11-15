# S2.1: Import the necessary Python modules and create the 'prediction()' function as directed above.
# Importing the necessary Python modules.
import numpy as np, pandas as pd, streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_log_error, mean_squared_error

# Define the 'prediction()' function.
@st.cache
def prediction(car_df,car_width, engine_size, horse_power, drivewheel_fwd, car_company_buick):
  x = car_df.iloc[:, :-1]
  y = car_df['price']
  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 30, random_state = 42)
  model = LinearRegression()
  model.fit( x_train, y_train)
  moddel_score = model.score(x_train, y_train)
  price = model.predict([[car_width, engine_size, horse_power, drivewheel_fwd, car_company_buick]])
  y_test_pred = model.predict(x_test)
  r_squared_test = r2_score(y_test, y_test_pred)
  mae_test = mean_absolute_error(y_test, y_test_pred)
  msle_test = mean_squared_log_error(y_test, y_test_pred)
  rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
  return moddel_score, price, r_squared_test, mae_test, msle_test, rmse_test


# S2.2: Define the 'app()' function as directed above.
def app(car_df): 
    st.markdown("<p style='color:blue;font-size:25px'>This app uses <b>Linear regression</b> to predict the price of a car based on your inputs.", unsafe_allow_html = True) 
    st.subheader("Select Values:")
    car_wid = st.slider("Car Width", float(car_df["carwidth"].min()), float(car_df["carwidth"].max()))     
    eng_siz = st.slider("Engine Size", int(car_df["enginesize"].min()), int(car_df["enginesize"].max()))
    hor_pow = st.slider("Horse Power", int(car_df["horsepower"].min()), int(car_df["horsepower"].max()))    
    drw_fwd = st.radio("Is it a forward drive wheel car?", ("Yes", "No")) #'drivewheel_fwd'
    if drw_fwd == 'No':
        drw_fwd = 0
    else:
        drw_fwd = 1
    com_bui = st.radio("Is the car manufactured by Buick?", ("Yes", "No"))#, 'car_company_buick'
    if com_bui == 'No':
        com_bui = 0
    else:
        com_bui = 1
    
    # When 'Predict' button is clicked, the 'prediction()' function must be called 
    # and the value returned by it must be stored in a variable, say 'price'. 
    # Print the value of 'price' and 'score' variable using the 'st.success()' and 'st.info()' functions respectively.
    if st.button("Predict"):
        st.subheader("Prediction results:")
        price, score, car_r2, car_mae, car_msle, car_rmse = prediction(car_df, car_wid, eng_siz, hor_pow, drw_fwd, com_bui)
        st.success("The predicted price of the car: ${:,}".format(int(price)))
        st.info("Accuracy score of this model is: {:2.2%}".format(int(score)))
        st.info(f"R-squared score of this model is: {car_r2:.3f}")  
        st.info(f"Mean absolute error of this model is: {car_mae:.3f}")  
        st.info(f"Mean squared log error of this model is: {car_msle:.3f}")  
        st.info(f"Root mean squared error of this model is: {car_rmse:.3f}")