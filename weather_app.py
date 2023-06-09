import requests
from bs4 import BeautifulSoup
import streamlit as st

def get_metar(city):
    url = f'https://aviationweather.gov/metar/data?ids={city}&format=raw&date=&hours=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    metar_element = soup.find('code')
    if metar_element is not None:
        metar = metar_element.text
    else:
        metar = f"No METAR data found for {city}"
    
    return metar
col1, col2 = st.columns([1, 1])
col1.title('Weather')
city = col1.text_input('Enter city')
col2.image('weather.gif')
metar_data = get_metar(city)
st.write(metar_data)
