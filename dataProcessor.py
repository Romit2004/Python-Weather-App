import requests
import pandas as pd
import json
import streamlit as st
import datetime as dt
import utils
import main3

def printWeather(response):
  try:
    data = json.loads(response.text)

    if data['cod'] == 200:
      #Extract relevant weather information
      print(data)
      # print(data['coord']['lat'])
      main3.lat = data['coord']['lat']
      main3.lon = data['coord']['lon']
      weather_description = data['weather'][0]['main']
      temperature = data['main']['temp']
      humidity = data['main']['humidity']
      pressure = data['main']['pressure']
      icon = data['weather'][0]['icon']
     # map = fl.folium.Map(location=(data['coord']['lat'],data['coord']['lon']), zoom_start=13)
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
        st.success(f"Weather in {main3.city} : {weather_description}")
        st.info(f"Pressure : {pressure}mbar" )
      with col2:
        st.info(f"Temperature : {temperature}C")
      with col3:
        st.success(f"Humidity : {humidity}%")
        


      
      
    
      web_str = "https://openweathermap.org/img/wn/"+icon+"@2x.png"
      left_co, cent_co, right_co = st.columns(3)
      with left_co:
        st.subheader(f"{weather_description} :")
      with cent_co:
        st.image(web_str)
      st.map(df)
     # plot_chart(lat,lon)
      #with st.container():
        # selected_chart_type = st.selectbox('Select Chart Type', ('Select Chart Type2', 'Line Chart', 'Bar Chart', 'Pie Chart', 'Scatter Plot'),
        # index=None,
        # placeholder= "Choose...."                                  
        # ) 
        # plot_chart(lat,lon,selected_chart_type)
      
    else:
      utils.handleError(data,'httpError')
  except:
    utils.handleError(response, 'parseError')
  main3.placeholder.empty()