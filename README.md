# wheretopark

[![Coverage Status](https://coveralls.io/repos/github/jennywong01/wheretopark/badge.svg?branch=main)](https://coveralls.io/github/jennywong01/wheretopark?branch=main)


## Project Type: Tool

## Project Goal: 
Output the information of the recommended parking location based on the search requests from the users

## Questions of Interest:
  1. Where to find nearest parking spaces near given destination?
  2. Which paid parking area has more space?
  
## Data sources:

Paid Parking Occupancy: https://data.seattle.gov/Transportation/Paid-Parking-Last-48-Hours-/hiyf-7edq

Seattle Parking Map: https://seattlecitygis.maps.arcgis.com/apps/webappviewer/index.html?id=5814e3f6c7054a40a9b4d175dcbf294b

Google map API: API key required

## Instructions:
* Pull on main to get the latest version of the application
* conda env create -f environment.yml
* conda activate wheretopark
* python app.py


