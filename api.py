import requests
import pandas as pd
import json
import streamlit as st
import datetime as dt
import main3
def get_weather(city):
  main3.placeholder.text('Loading Data......')
  API_key = "ca988591e83474e52a2e43afb8aaf70d"
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
  response = requests.get(url)
  return response


def getForecast(duration, pastdays):
  hr_forcast_api = f"https://api.open-meteo.com/v1/forecast?latitude={main3.lat}&longitude={main3.lon}&hourly=temperature_2m&&timeformat=unixtime&forecast_days={duration}&past_days={pastdays}"
  print(hr_forcast_api)
  return requests.get(hr_forcast_api)