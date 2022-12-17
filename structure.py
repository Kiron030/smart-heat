# Importing required libraries such as 'sensor', 'controller' or 'time'.
  # For loading in the data from a sensor or via an API (e.g. on the weather) the following libraries are required:
    # import sensor
    # import controller
    # import time
    # import numpy as np
    # import pandas as pd
    # import matplotlib
    # import seaborn as sns
    # import sklearn
    # import tensorflow as tf
    # import keras
    # import django  

# Getting the INPUT Data
  # 1. The data comes from a sensor (e.g. in the thermostat) and the data is controlled and send via
    #  a Raspberry Pi, via WLAN, LAN or 4G/5G 
  # 2. The data is scrapped from a webpage and is controlled and send via
    #  an API (openweathermap.org, weather.gov, etc.)
  # 3. The data is handcollected and combined in a database or an excel sheet

# Possible Datasets for the Input-Side of the I/O-flow 
  ## Average temperature outside in location (Germany or Berlin) as a sin function over the year --> maybe even with Fourier Transformation for daily swings
  ## Flate or room temperature 
  ## State of the valve (how open, closed is it) for the information of the speed of the heating water and the amount of heat brough into the room 

# Defining variables 
  # Temperature (outside temperature)
  # Adress (location)
  # DateTime (time and date)
  # Room Temperature (temperature in the room)

# Defining classes
  # class Thermostat or Valve (state of the valve) 
  # class Sensor
  # class Room
  
# Defining functions
  # Writing a get_weather() function that retrieves the weather forecast.
  # [Writing a get_energy_usage() function that retrieves the energy consumption and costs.]
  # Writing a get_temperature() function that reads the current room temperature via the sensor.
  # Writing a set_temperature() function that sets the desired room temperature.
  # Writing a get_valve_settings() function that retrieves the current valve settings.
  # Writing a set_valve_settings() function that changes the current state of the valve 
  

  

# Writing an update_temperature() function that reads the current room temperature via the sensor and adjusts the heating accordingly.

# Writing an adjust_for_weather() function that retrieves the weather forecast and adjusts the heating settings accordingly.

# Writing a function optimize_settings() that uses learning algorithms to optimize the heating settings over time.

# Writing a control_heating() function that periodically calls the update_temperature(), adjust_for_weather() and optimize_settings() functions to control the heating.

# Writing a monitor_energy_usage() function that logs and displays energy consumption and costs.
  ## Optimal would be to work with the django package or something similiar and matplotlib etc. to present a frontend user interface for the input or output of data
