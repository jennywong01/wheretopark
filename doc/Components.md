## Find closest parking

### Components:
Database with parking information \
User interface: to input address / restaurant name \
User interface: to verify the address \
User interface: display parking by distance to the input address \
Control logic


### Control Logic:
* Name
	* closest_parking
* What it does
	* Verify the input location and displays the sorted available parking by distance
* Inputs
	* Address, the street address or name of the destination
* Outputs
	* List, a list of parking location sorted by distance to the destination
* Assumption
	* User knows exactly where they want to go, and have the name or street address

### Pseudocode:
```
closest_parking(address):
	find parking location around address from database
	if parking locations found:
		save the location coordinates as a list
		calculate distance between parking locations and destination
		sort parking locations by distance in ascending order
		return sorted list
	else:
		print(“no parking location found”)
		return none
```
<img width="655" alt="closest_parking" src="https://user-images.githubusercontent.com/68675135/218924613-bd703d06-6ce0-4517-80e4-a2d7817af269.png">

## Find lowest occupancy parking
### Components:
Database with parking information \
User interface: display default map to Seattle \
User interface: filter to selected area on map \
User interface: display all parking facilities within map selection, sorted by occupancy rate
Control logic

### Control Logic:
* Name
	* occupancy_rate
* What it does
	* Calculate the average occupancy rate for parkings near selected location and displays the sorted available parking by occupancy rate
* Inputs
	* Address or none
* Outputs
	* List, a list of parking location sorted by occupancy rate
* Assumption
	* Selected map area has parking available

### Pseudocode:
```
occupancy_rate(location):
	Find all available parking within filtered location
	If parking location is found:
		Save parking location coordinates into a list
		ave_occupancy=Calculate the average occupancy for the past 48 hour
sort parking locations by distance in ascending order
			return sorted list
	If parking location is not found:
		Return none
```
<img width="728" alt="occupancy" src="https://user-images.githubusercontent.com/68675135/218924864-ec4aa040-e286-4993-9dcf-a231e56c6453.png">
