import requests
import pandas as pd
import json
import streamlit as st
import datetime as dt
import globals
def tohour(time):
  return dt.datetime.utcfromtimestamp(time).strftime('%H:%M')

def todatehour(time):
  return dt.datetime.utcfromtimestamp(time).strftime('%d-%m %H:%M')

def time_format(time, duration):
  result=[]
  if duration == "1":
    result = map(tohour,time)
  else:
    result = map(todatehour,time)
  print(result)
  return result
def handleError(error, type):
  if(type == 'httpError'):
    #print(error['message'])
    globals.get_city="error"
    st.warning(error['message'])
  else:
    st.warning(f'Something went wrong! Please try again. {error}')
 
  