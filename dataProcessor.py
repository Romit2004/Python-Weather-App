import requests
import pandas as pd
import json
import streamlit as st
import datetime as dt
import utils
import globals
from streamlit_lottie import st_lottie



  

def printWeather(response):
  try:
    data = json.loads(response.text)
    

    if data['cod'] == 200:
      #Extract relevant weather information
      print(data)
      # print(data['coord']['lat'])
      globals.lat = data['coord']['lat']
      globals.lon = data['coord']['lon']
      weather_description = data['weather'][0]['main']
      temperature = data['main']['temp']
      humidity = data['main']['humidity']
      pressure = data['main']['pressure']
      icon = data['weather'][0]['icon']
      feels_like = data['main']['feels_like']
      visibility = data['visibility']
      speed = data['wind']['speed']
      temp_min = data['main']['temp']
      temp_max = data['main']['temp']
      
     
      df = pd.DataFrame(
      [[data['coord']['lat'],data['coord']['lon']]],    
      columns=['lat', 'lon']
      )

     
      
      # Convert temperature from kelvin to celsius
      temperature = round(temperature - 273.15, 2)

      #print the weather forecast
      # st.write(data)
      col1, col2, col3 = st.columns(3)
      with col1:
        st.success(f"Weather in {globals.city} : {weather_description}")
        st.info(f"Pressure : {pressure}mbar" )
        st.success(f"Visibility:{visibility}km")
      with col2:
        st.info(f"Temperature : {temperature}C")
        st.success(f"Feels_like:{feels_like}C")
        st.info(f"Min Temperature: {temp_min}C")
      with col3:
        st.success(f"Humidity : {humidity}%")
        st.info(f"wind_speed:{speed}km/h")
        st.success(f"Max Temperature:{temp_max}C")
     
        
        


      
      
    
      web_str = "https://openweathermap.org/img/wn/"+icon+"@2x.png"
      left_co, cent_co, right_co = st.columns(3)
      with left_co:
        st.subheader(f"{weather_description} :")
      with cent_co:
        st.image(web_str)
      st.map(df)
  
      
    else:
      utils.handleError(data,'httpError')
  except:
    utils.handleError(response, 'parseError')
  globals.placeholder.empty()