import requests
import pandas as pd
import json
import streamlit as st
import datetime as dt
import api
import dataProcessor
import chart
import globals
from streamlit_lottie import st_lottie

back_img =f"""
   <style>
    body {{
    background-color: grey;
    background-size : cover;
    opacity: 0.9  ;
    base: "dark";
    }}
   </style>
   """
st.markdown(
   back_img,
   unsafe_allow_html=True)

#st.title("WeatherPy")
st.markdown("<h1 style='text-align: center; color: White;font-family: Arial;'>WeatherPy</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; background-color:blue;'>Check the current weather</h2>",unsafe_allow_html=True)


def get(path:str):
  with open(path,"r") as p:
    return json.load(p)
  
path=get("Animation - 1701104404073.json")
st_lottie(path)

st.markdown(
    """
    <style>
    text {
        font-size: 20px !important;
    }
    input {
        font-size: 20px !important;
    }

    </style>
    """,
    unsafe_allow_html=True,
)
globals.city = st.text_input("**Enter City Name :**")
if st.button("Get Weather") or globals.city != '':
  response = api.get_weather(globals.city, globals.placeholder)
  globals.get_city=""
  
  dataProcessor.printWeather(response)
  
if globals.city != '' and globals.get_city!="error":
  selected_chart_type = st.selectbox('Select Chart Type', ( 'Line Chart', 'Bar Chart', 'Scatter Plot'),
                                      index=0)
  duration = st.selectbox('Select days',('-7','-6','-5','-4','-3','-2', '-1','1', '2','3','4','5','6','7'),
                          index=7)
  chart.plot_chart(selected_chart_type,duration,globals.lat,globals.lon)