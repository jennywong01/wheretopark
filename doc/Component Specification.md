# Component Specification

## Software components.
High level description of the software components such as: data manager, 
which provides a simplified interface to your data and provides application specific features (e.g., querying data subsets); and visualization manager, which displays data frames as a plot. Describe at least 3 components specifying: what it does, inputs it requires, and outputs it provides. If you have more significant components in your system, we highly suggest documenting those as well.

## Interactions to accomplish use cases. 
Describe how the above software components interact to accomplish your use cases. 
Include at least one interaction diagram.


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
