import requests
import pandas as pd
import json
import streamlit as st
from streamlit_lottie import st_lottie
import os
 
placeholder = st.empty()
def get(path:str):
  with open(path,"r") as p:
    return json.load(p)
  
path=get("Animation - 1701105630153.json")
st_lottie(path)




st.success("WEATHER UPDATE")

def get(path:str):
  with open(path,"r") as p:
    return json.load(p)
  
path=get("Animation - 1701104404073.json")
st_lottie(path)


# Do a API call to get wether data and return response
def get_weather(city):
  global placeholder
  placeholder.text('Loading Data......')
  
   

  API_key = os.getenv("API")
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
  response = requests.get(url)
  return response

# Parse the response and print the result in case of any error call handleError fucntion
def printWeather(response):
  try:
    data = json.loads(response.text)
    if data['cod'] == 200:
      #Extract relevant weather information
      print(data)
      print(data['coord']['lat'])
      weather_description = data['weather'][0]['description']
      temperature = data['main']['temp']
      humidity = data['main']['humidity']
      pressure = data['main']['pressure']
      icon = data['weather'][0]['icon']
      feels_like = data['main']['feels_like']
      visibility = data['visibility']
      speed = data['wind']['speed']
      print(feels_like,visibility,speed)


     # map = fl.folium.Map(location=(data['coord']['lat'],data['coord']['lon']), zoom_start=13)

      # df = pd.DataFrame(
      # [[data['coord']['lat'],data['coord']['lon']]],    
      # columns=['lat', 'lon']
      # )


      # Convert temperature from kelvin to celsius
      temperature = round(temperature - 273.15, 2)

      #print the weather forecast
      # st.write(data)
     

      
      st.success(f"Weather in {city} : {weather_description}")
      st.info(f"Temperature : {temperature}C")
      st.warning(f"Humidity :{humidity}%")
      #st.snow(f"Pressure: {pressure}mbar")
      st.info(f"Feels_like:{feels_like}C")
      st.warning(f"Visibility:{visibility}km")
      st.info(f"wind_speed:{speed}km/h")



      web_str = f"https://openweathermap.org/img/wn/{icon}@2x.png"
      left_co, cent_co, right_co = st.columns(3)
      with cent_co:
        st.image(web_str)
      #st.map(df)
      
    else:
      handleError(data,'httpError')
  except:
    handleError(response, 'parseError')
  placeholder.empty()
  
# Handle the error response and print relavent message
def handleError(error, type):
  if(type == 'httpError'):
    st.write(error['message'])
  else:
    print(error)
    st.write(f'Something went wrong! Please try again. {error}')

st.warning("Check the current weather")





city = st.text_input("Enter City Name :")
if st.button("Get Weather"):
  response = get_weather(city)
  printWeather(response)

  
