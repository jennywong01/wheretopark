# Functional Specification

## Background
Parking in Seattle can be difficult, especially if one is unfamiliar with the neighborhood. Moreover, different areas have different specifications, such as *Paid Parking*, *Restricted Parking*, and *Carpool Parking*. Where to Park is a web-based application developed to assist users in locating all available parking spaces near their intended destination. With this application, users can easily input their desired location or scroll around the provided map, and see all available parking locations, labeled by parking specification. This tool will make it easier for users to plan ahead and find a suitable place to park their vehicle.



## User Profile
Where to Park has been created for users who own or rent vehicles and drive around Seattle. They are able to run basic commands in python (to set up the application), and are familiar with using a map application, such as Google Maps.



## Data Sources
We will use the following data sources:
- [Blockface Data](https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::blockface/about): This data set is structured as a GeoJSON file and contains geographic information for all parking spots (approximately 47,000 rows) in Seattle. It also includes columns for unit descriptions, and parking area types.
- [Paid Parking](https://data.seattle.gov/Transportation/Paid-Parking-Last-48-Hours-/hiyf-7edq): This data set is structured as a csv file with over 4.5 million rows and includes additional information for paid parking spots, such as occupancy in each parking location from the last 48 hours. However, the website states that occupancy data cannot accurately represent the availability of a parking space due to the possibility of unpaid vehicles. We have used this data set to display how many parking spots are contained in each paid parking area.
- Google Maps API: This data set is structured as an API. We have used the Google Maps API to overlay parking locations over a map, and allow users to search addresses and locations within Seattle. This is possible through the API's functionality for geocoding (converting addresses into geographic coordinates).



## Use Cases
- User 1 is driving to Seattle Uptown for dinner. She is unfamiliar with the area and would like to know where she should park for 2 hours during dinner time. User 1 knows the name of the restaurant to input in the tool and expects to see nearby parking spots. She searches the name of the restaurant in the search bar, selects the correct restaurant name in the table and sees a map with the nearest parking locations bolded. She scrolls through the map and uses the hover tool to explore the parking options and relevant details, and decides where she will park.

- User 2 is visiting an area she is familiar with, and knows that finding parking will be difficult. She would like to explore nearby parking areas and see which parking area will have the most parking spaces so she has a better chance of finding a spot. She scrolls through the map and sees all the parking spots surrounding the area. She uses the hover tool to see the details of each spot, and observes the number of spots in each paid parking area. She finds a nearby parking area with many spots and plans to park there.
