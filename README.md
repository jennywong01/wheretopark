# Where to Park

[![Coverage Status](https://coveralls.io/repos/github/jennywong01/wheretopark/badge.svg?branch=main)](https://coveralls.io/github/jennywong01/wheretopark?branch=main)

## Project Type: Tool

## Project Goal
Where to Park is a web-based application developed to assist drivers in Seattle with locating all available parking spaces in the city. With this application, users can input their desired location or scroll around the provided map and see all available parking locations, labeled with parking specifications. This tool will make it easier for users to plan ahead and find a suitable place to park their vehicle.

## Questions of Interest
1. What are the closest parking spaces to a given destination?
2. What parking locations and types of parking (category, number of spaces) are present around Seattle? 
  
## Data Sources
- [Blockface Data](https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::blockface/about): This data set contains geographic information for all parking spots in Seattle, and includes details such as Unit Descriptions and Categories.
- [Paid Parking](https://data.seattle.gov/Transportation/Paid-Parking-Last-48-Hours-/hiyf-7edq): We have used this data set to display how many parking spots are contained in each paid parking area.
- Google Maps API: We have used this API to overlay parking locations over a map, and allow users to search addresses and locations within Seattle.

## Set Up Instructions
1. Pull on main to get the latest version of the application
2. Run the command `conda env create -f environment.yml`
3. Run the command `conda activate wheretopark`
4. Run the command `python wheretopark/app.py`
5. Access the local URL provided
