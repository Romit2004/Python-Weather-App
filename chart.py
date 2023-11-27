import requests
import pandas as pd
import json
import streamlit as st
import datetime as dt
import utils
import api
import globals

def plot_chart(selected_chart_type,duration,lat,lon):
  print("latlon",lat,lon)
  days = int(duration)
  if days < 0:
    duration = 0
    pastdays = -(days)
  else:
    pastdays = 0
  print(pastdays, duration)
  try:
      response = api.getForecast(globals.lat,globals.lon,duration,pastdays)
      hr_forcast = json.loads(response.text)
      print(hr_forcast)
      #print(hr_forcast['hourly']['temperature_2m'])
      time = utils.time_format(hr_forcast['hourly']['time'],duration)
      chart_data = pd.DataFrame(
        {
            "Time": time,
            "Temperature": hr_forcast['hourly']['temperature_2m']
        }
      )

      
     # st.bar_chart(chart_data, x="Time", y="Temperature")
#       selected_chart_type = st.selectbox('Select Chart Type', ('Select Chart Type2', 'Line Chart', 'Bar Chart', 'Pie Chart', 'Scatter Plot'),
#        index=None,
#        placeholder= "Choose...."                                  
#        )
      print(selected_chart_type)

      if selected_chart_type == 'Line Chart':
        st.line_chart(chart_data, x="Time", y="Temperature")
          
      elif selected_chart_type == 'Bar Chart':
          
        st.bar_chart(chart_data, x="Time", y="Temperature")
        

    
      elif selected_chart_type == 'Scatter Plot':

        st.bar_chart(chart_data, x="Time", y="Temperature")
      else:
        st.line_chart(chart_data, x="Time", y="Temperature")

  
  except:
    print('chart plot error')