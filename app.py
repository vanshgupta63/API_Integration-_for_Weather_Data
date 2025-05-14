import streamlit as st
import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        weather = {
            'City': data['name'],
            'Temperature (°C)': data['main']['temp'],
            'Humidity (%)': data['main']['humidity'],
            'Weather': data['weather'][0]['description'].title()
        }
        return weather
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        st.error(f"Request error occurred: {req_err}")
    except KeyError:
        st.error("Unexpected response structure.")
    return None

def main():
    st.title("🌤️ Weather Dashboard")
    city = st.text_input("Enter city name:")
    api_key = "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"

    if st.button("Get Weather"):
        if city:
            weather_info = get_weather(city, api_key)
            if weather_info:
                st.subheader(f"Weather in {weather_info['City']}")
                st.write(f"Temperature:{weather_info['Temperature (°C)']} °C")
                st.write(f"**Humidity:** {weather_info['Humidity (%)']}%")
                st.write(f"**Condition:** {weather_info['Weather']}")
        else:
            st.warning("Please enter a city name.")

if __name__ == "__main__":
    main()
