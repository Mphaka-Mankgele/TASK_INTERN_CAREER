


import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Define the SAWS weather page URL
weather_url = "https://weather.com/en-ZA/weather/hourbyhour/l/2f2a561189c1f6cef568e565d2819a370cd44d5b499ad1961d88f41b97e1f51d"

# Fetch the content from the URL
response = requests.get(weather_url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract relevant data (you may need to adjust the CSS selectors)
forecast = soup.find("div", class_="HourlyForecast--DisclosureList--MQWP6")
dates = forecast.find_all("h2", class_="HourlyForecast--longDate--J_Pdh")


#print(forecast.prettify())
for date in dates:
    print(date.text)
# # Initialize empty lists to store data
# location_names = []
# temperature = []
# humidity = []
# wind_speed = []
# rainfall = []

# # Extract data for each location
# for loc, data in zip(locations, weather_data):
#     location_names.append(loc.find("h1").text)
#     rows = data.find_all("tr")
#     for row in rows:
#         cols = row.find_all("td")
#         if len(cols) == 5:
#             temperature.append(float(cols[1].text.strip("°C")))
#             humidity.append(int(cols[2].text.strip("%")))
#             wind_speed.append(float(cols[3].text.strip(" km/h")))
#             rainfall.append(float(cols[4].text.strip(" mm")))

# # Create a DataFrame
# weather_df = pd.DataFrame({
#     "Location": location_names,
#     "Temperature (°C)": temperature,
#     "Humidity (%)": humidity,
#     "Wind Speed (km/h)": wind_speed,
#     "Rainfall (mm)": rainfall
# })

# print(weather_df)

# # Plot graphs
# plt.figure(figsize=(12, 8))

# # Temperature vs. Location
# plt.subplot(2, 2, 1)
# plt.bar(weather_df["Location"], weather_df["Temperature (°C)"])
# plt.xlabel("Location")
# plt.ylabel("Temperature (°C)")
# plt.title("Temperature Variation")

# # Humidity vs. Location
# plt.subplot(2, 2, 2)
# plt.bar(weather_df["Location"], weather_df["Humidity (%)"])
# plt.xlabel("Location")
# plt.ylabel("Humidity (%)")
# plt.title("Humidity Variation")

# # Wind Speed vs. Location
# plt.subplot(2, 2, 3)
# plt.bar(weather_df["Location"], weather_df["Wind Speed (km/h)"])
# plt.xlabel("Location")
# plt.ylabel("Wind Speed (km/h)")
# plt.title("Wind Speed Variation")

# # Rainfall vs. Location
# plt.subplot(2, 2, 4)
# plt.bar(weather_df["Location"], weather_df["Rainfall (mm)"])
# plt.xlabel("Location")
# plt.ylabel("Rainfall (mm)")
# plt.title("Rainfall Variation")

# plt.tight_layout()
# plt.show()
