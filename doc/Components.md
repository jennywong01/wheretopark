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

## Find lowest occupancy parking
