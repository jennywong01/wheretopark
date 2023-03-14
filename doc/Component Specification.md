# Component Specification

## Software components.
data manager, which provides a simplified interface to your data and provides application specific features (e.g., querying data subsets)

As the visualization manager, our team utilizes the bokeh.plot and bokeh.gmap libraries to create interactive visualizations of data frames on Google Maps. The input for this component consists of the data frame with geocoded parking locations, as well as options for customizing the plot type, hover effects, and more. The output of this process is a map with Google Maps serving as the base layer, and all the parking locations plotted on top of it. Additionally, hovering over any parking space reveals detailed information about that location.

Describe at least 3 components specifying: what it does, inputs it requires, and outputs it provides. If you have more significant components in your system, we highly suggest documenting those as well.

## Interactions to accomplish use cases. 



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
