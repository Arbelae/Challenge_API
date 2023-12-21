#!/usr/bin/env python
# coding: utf-8

# # VacationPy
# ---
# 
# ## Starter Code to Import Libraries and Load the Weather and Coordinates Data

# In[1]:


# Dependencies and Setup
import hvplot.pandas
import pandas as pd
import requests
from pathlib import Path

# Import API key
from api_keys import geoapify_key


# In[2]:


# Load the CSV file created in Part 1 into a Pandas DataFrame
csv_file = Path("output_data/cities.csv")
city_data_df = pd.read_csv(csv_file)

# Display sample data
city_data_df.head()


# ---
# 
# ### Step 1: Create a map that displays a point for every city in the `city_data_df` DataFrame. The size of the point should be the humidity in each city.

# In[3]:


get_ipython().run_cell_magic('capture', '--no-display', '\n# Configure t.hvplot.pointshe map plot\nMap = city_data_df.hvplot.points ("Lng","Lat",\n                                   frame_width = 700,\n                                   frame_heidht = 500,\n                                   title = "OSM",\n                                   size = "Humidity",\n                                   geo = True,\n                                   color = "city")\n\n# Display the map\nMap\n')

