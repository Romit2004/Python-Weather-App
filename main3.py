import requests
import pandas as pd
import json
import streamlit as st
import datetime as dt
import api
import dataProcessor
import chart
lat =""
lon=""
placeholder = st.empty()
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

st.title("Check the current weather")
st.image("https://i.postimg.cc/44S1ywbQ/tanjiro-kamado-monochrome-kimetsu-no-yaiba-thumb.jpg")
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
city = st.text_input("**Enter City Name :**")
if st.button("Get Weather") or city != '':
  response = api.get_weather(city)
  dataProcessor.printWeather(response)

if city != '':
  selected_chart_type = st.selectbox('Select Chart Type', ( 'Line Chart', 'Bar Chart', 'Pie Chart', 'Scatter Plot'),
                                      index=0)
  duration = st.selectbox('Select days',('-7','-6','-5','-4','-3','-2', '-1','1', '2','3','4','5','6','7'),
                          index=3)
  chart.plot_chart(selected_chart_type,duration)