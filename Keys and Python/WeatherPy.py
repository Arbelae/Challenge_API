#!/usr/bin/env python
# coding: utf-8

# # WeatherPy
# 
# ---
# 
# ## Starter Code to Generate Random Geographic Coordinates and a List of Cities

# In[ ]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
from datetime import datetime
from scipy.stats import linregress
import pprint

# Impor the OpenWeatherMap API key
from api_keys import weather_api_key

# Import citipy to determine the cities based on latitude and longitude
from citipy import citipy


# ### Generate the Cities List by Using the `citipy` Library

# In[ ]:


# Empty list for holding the latitude and longitude combinations
lat_lngs = []

# Empty list for holding the cities names
cities = []

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)

# Create a set of random lat and lng combinations
lats = np.random.uniform(lat_range[0], lat_range[1], size=1500)
lngs = np.random.uniform(lng_range[0], lng_range[1], size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
print(f"Number of cities in the list: {len(cities)}")


# In[ ]:


# Set the API base URL
url= "http://api.openweathermap.org/data/2.5/weather?"
query_url = url + "appid"+ weather_api_key+"&q="


# Define an empty list to fetch the weather data for each city
city_data = []

# Print to logger
print("Beginning Data Retrieval     ")
print("-----------------------------")

# Create counters
record_count = 1
set_count = 1

# Loop through all the cities in our list to fetch weather data
for i, city in enumerate(cities):
        
    # Group cities in sets of 50 for logging purposes
    if (i % 50 == 0 and i >= 50):
        set_count += 1
        record_count = 0

    # Create endpoint URL with each city
    target_url = query_url + city
    city_url = requests.get(target_url).json()
    
     # Log the url, record, and set numbers
    print("Processing Record %s of Set %s | %s" % (record_count, set_count, city))

      # Add 1 to the record count
    record_count += 1


# In[ ]:


print(query_url)


# ---

# ## Requirement 1: Create Plots to Showcase the Relationship Between Weather Variables and Latitude
# 
# ### Use the OpenWeatherMap API to retrieve weather data from the cities list generated in the started code

# In[ ]:


# Set the API base URL
url= "http://api.openweathermap.org/data/2.5/weather?"
query_url = url + "appid"+ weather_api_key+"&q="


# Define an empty list to fetch the weather data for each city
city_data = []

# Print to logger
print("Beginning Data Retrieval     ")
print("-----------------------------")

# Create counters
record_count = 1
set_count = 1

# Loop through all the cities in our list to fetch weather data
for i, city in enumerate(cities):
        
    # Group cities in sets of 50 for logging purposes
    if (i % 50 == 0 and i >= 50):
        set_count += 1
        record_count = 0

    # Create endpoint URL with each city
    target_url = query_url + city
    city_url = requests.get(target_url).json()
    
     # Log the url, record, and set numbers
    print("Processing Record %s of Set %s | %s" % (record_count, set_count, city))

      # Add 1 to the record count
    record_count += 1

    

    # Run an API request for each of the cities
    try:
        # Parse the JSON and retrieve data
        
        city_weather = requests.get(city_url).json()
        
  
        # Parse out latitude, longitude, max temp, humidity, cloudiness, wind speed, country, and date
        city_lat =  (city_weather['coord']['lat'])
        city_lng =  (city_weather['coord']['lng'])
        city_max_temp = (city_weather['main']['max_temp'])
        city_humidity = (city_weather['main']['humidity'])
        city_clouds =  (city_weather['all']['clouds'])
        city_wind =   (city_weather['speed']['wind'])
        city_country = (city_weather['sys']['country'])
        city_date =   (city_weather['dt'])
        
    
    

        # Append the City information into city_data list
        
        city_data.append({"City": city, 
                          "Lat": city_lat, 
                          "Lng": city_lng, 
                          "Max Temp": city_max_temp,
                          "Humidity": city_humidity,
                          "Cloudiness": city_clouds,
                          "Wind Speed": city_wind,
                          "Country": city_country,
                          "Date": city_date})
        
        city_data = pd.DataFrame(city_data)
        city_data.head()



    # If an error is experienced, skip the city
    except:
        print("City not found. Skipping...")
        pass
              
# Indicate that Data Loading is complete 
print("-----------------------------")
print("Data Retrieval Complete      ")
print("-----------------------------")       

 
        

              
# Indicate that Data Loading is complete 
#print("-----------------------------")
#print("Data Retrieval Complete      ")
#print("-----------------------------")


# In[ ]:


# Convert the cities weather data into a Pandas DataFrame
city_data_df = pd.DataFrame(city_data)

# Show Record Count
city_data_df.count()


# In[ ]:


# Display sample data
city_data_df.head(3)


# In[ ]:


# Export the City_Data into a csv
city_data_df.to_csv("output_data/cities.csv", index_label="City_ID")


# In[ ]:


# Read saved data
city_data_df = pd.read_csv("output_data/cities.csv", index_col="City_ID")

# Display sample data
city_data_df.head()


# ### Create the Scatter Plots Requested
# 
# #### Latitude Vs. Temperature

# In[ ]:


# Build scatter plot for latitude vs. temperature
value_x = city_data_df['Lat']
value_y = city_data_df['Max Temp']
plt.scatter(value_x,value_y)

# Incorporate the other graph properties


# Save the figure
plt.savefig("output_data/Fig1.png")

# Show plot
plt.show()


# #### Latitude Vs. Humidity

# In[ ]:


# Build the scatter plots for latitude vs. humidity
value_x = city_data_df['Lat']
value_y = city_data_df['Humidity']
plt.scatter(value_x,value_y)

# Incorporate the other graph properties 
plt.xlabel('Latitude')
plt.ylabel('Humidity')
plt.title("Latitude Vs Humidity")

# Save the figure
plt.savefig("output_data/Fig2.png")

# Show plot
plt.show()


# #### Latitude Vs. Cloudiness

# In[ ]:


# Build the scatter plots for latitude vs. cloudiness
value_x = city_data_df['Lat']
value_y = city_data_df['Cloudiness']
plt.scatter(value_x,value_y)

# Incorporate the other graph properties
plt.xlabel('Latitude')
plt.ylabel('Cloudiness')
plt.title("Latitude Vs Cloudiness")

# Save the figure
plt.savefig("output_data/Fig3.png")

# Show plot
plt.show()


# #### Latitude vs. Wind Speed Plot

# In[ ]:


# Build the scatter plots for latitude vs. wind speed
value_x = city_data_df['Lat']
value_y = city_data_df['Cloudiness']
plt.scatter(value_x,value_y)

# Incorporate the other graph properties
plt.xlabel('Latitude')
plt.ylabel('Cloudiness')
plt.title("Latitude Vs Cloudiness")

# Save the figure
plt.savefig("output_data/Fig4.png")

# Show plot
plt.show()


# ---
# 
# ## Requirement 2: Compute Linear Regression for Each Relationship
# 

# In[ ]:


# Define a function to create Linear Regression plots
def line_Regress(value_x,value_y,xlabel,ylabel):
    (slope, interacept, rvalue, pvalue,stderr) = linregress(value_x,value_y)
    regress_values = value_x * slope + intercept
    line_eq = "y = " + str(round(slope,2)) + " x + " + str (round (intercept,(2))
    plt.scatter(value_x,value_y)
    return plt.plot(value_x,regress_values,"r-")


# In[ ]:


# Create a DataFrame with the Northern Hemisphere data (Latitude >= 0)
northern_hemi_df = city_data_df.loc[city_data_df['Lat']>= 0]

# Display sample data
northern_hemi_df.head()


# In[ ]:


# Create a DataFrame with the Southern Hemisphere data (Latitude < 0)
southern_hemi_df = city_data_df.loc[city_data_df['Lat']>= 0]

# Display sample data
southern_hemi_df.head()


# ###  Temperature vs. Latitude Linear Regression Plot

# In[ ]:


# Linear regression on Northern Hemisphere
line_Regress_N = line_regress(northern_hemi_df['Lat'], northern_hemi_df['Max Temp'],"Latitude","Max Temp (C)")
plt.show()


# In[ ]:


# Linear regression on Southern Hemisphere
line_Regress_S = line_regress(southern_hemi_df['Lat'], southern_hemi_df['Max Temp'],"Latitude","Max Temp (C))
plt.show()


# ### Humidity vs. Latitude Linear Regression Plot

# In[ ]:


# Northern Hemisphere
line_Regress_N = line_regress(northern_hemi_df['Lat'], northern_hemi_df['Max Temp'],"Latitude","Humidity")
plt.show()


# In[ ]:


# Southern Hemisphere
line_Regress_S = line_regress(southern_hemi_df['Lat'], southern_hemi_df['Max Temp'],"Latitude","Humidity")
plt.show()


# ### Cloudiness vs. Latitude Linear Regression Plot

# In[ ]:


# Northern Hemisphere
line_Regress_N = line_regress(northern_hemi_df['Lat'], northern_hemi_df['Max Temp'],"Latitude","Cloudiness")
plt.show()


# In[ ]:


# Southern Hemisphere
line_Regress_S = line_regress(southern_hemi_df['Lat'], southern_hemi_df['Max Temp'],"Latitude","Cloudiness")
plt.show()


# ### Wind Speed vs. Latitude Linear Regression Plot

# In[ ]:


# Northern Hemisphere
line_Regress_N = line_regress(northern_hemi_df['Lat'], northern_hemi_df['Max Temp'],"Latitude","Wind Speed (m/s)")
plt.show()


# In[ ]:


# Southern Hemisphere
line_Regress_S = line_regress(southern_hemi_df['Lat'], southern_hemi_df['Max Temp'],"Latitude","Wind Speed (m/s)")
plt.show()

