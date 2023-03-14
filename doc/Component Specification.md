# Component Specification

## Software components.
In this project, the data manager component plays a key role in determining the recommended parking space for a given destination. To achieve this, it first stores all the parking locations available in Seattle. Next, when it receives the destination coordinates as input, it calculates the distances from the destination to all the available parking locations. Finally, it sorts the parking locations by distance and returns the top 10 closest parking locations as a dataframe.

As the visualization manager, our team utilizes the bokeh.plot and bokeh.gmap libraries to create interactive visualizations of data frames on Google Maps. The input for this component consists of the data frame with geocoded parking locations, as well as options for customizing the plot type, hover effects, and more. The output of this process is a map with Google Maps serving as the base layer, and all the parking locations plotted on top of it. Additionally, hovering over any parking space reveals detailed information about that location.

In addition to other components, our project includes a Google Maps API component, which plays a critical role in geocoding users' inputs. This component allows us to convert a user's destination name or address into a geocoded location by utilizing the API's geocoding services. It takes the user's input as an address or destination name and then outputs the corresponding geometry coordinates.


## Interactions to accomplish use cases. 
The user inputs their destination into the system. The Google Maps API component then verifies the input, and if it is valid, it passes the location coordinates to the data manager component. Using these coordinates, the data manager component calculates the distances to all available parking locations and outputs the top 10 closest parking locations to the destination in a dataframe. This dataframe is then passed to the visualization manager component, which utilizes the dataframe to display the recommended parking locations on Google Maps. 



## Preliminary plan. 
A list of tasks in priority order.

### Data Preparation
* Parse all parking data
* Join datasets

### Create Distance Sorting Feature
* Display required information on map (parking location, color code, hover)
* Research for input options with bokeh( address/ business name)
* Write a function to take input address and output a list of parking location sort by distance

### Create Occupancy Sorting Feature
* Allow zoom in function when user choose area
* Write a function to take area that user choose and output a list of parking location sort by occupancy

### Implement UI using Flask
