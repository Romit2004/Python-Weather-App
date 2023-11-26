import requests
import pandas as pd
import json
import streamlit as st
 
placeholder = st.empty()

# Do a API call to get wether data and return response
def get_weather(city):
  global placeholder
  placeholder.text('Loading Data......')
  API_key = "ca988591e83474e52a2e43afb8aaf70d"
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
     # map = fl.folium.Map(location=(data['coord']['lat'],data['coord']['lon']), zoom_start=13)
      df = pd.DataFrame(
      [[data['coord']['lat'],data['coord']['lon']]],    
      columns=['lat', 'lon']
      )


      # Convert temperature from kelvin to celsius
      temperature = round(temperature - 273.15, 2)

      #print the weather forecast
      # st.write(data)
      st.success(f"Weather in {city} : {weather_description}")
      st.info(f"Temperature : {temperature}C")
      web_str = "https://openweathermap.org/img/wn/"+icon+"@2x.png"
      left_co, cent_co, right_co = st.columns(3)
      with cent_co:
        st.image(web_str)
      st.map(df)
      
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

st.header("Check the current weather")
st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.wallpaperflare.com%2Fphoto-of-cloudy-sky-and-green-grass-field-land-tornadic-weather-wallpaper-tvzsz&psig=AOvVaw2-I60oCZPp9BBElXLjZzfT&ust=1700765984714000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCJDPrZWl2IIDFQAAAAAdAAAAABAE")
city = st.text_input("Enter City Name :")
if st.button("Get Weather"):
  response = get_weather(city)
  printWeather(response)
