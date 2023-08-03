## Tracking a flight

- [View the actual code for this project here](https://github.com/joshjetson/flight_tracker/blob/master/strmlt_fts.py)

*The inspiration for this project came from a buddy who works at Ratheon. They handle a large portion of incoming and outgoing flight data in the United States.*

---------------------


*If you wanted to build a program that tracked a flight where would you start ?*

> **Live Onboard Instrument Data From An API**

*Pros:*

- Live data would mean we can track and actual flight in real time.
- Could build the program and have a much greater chance of being able to sell it or have it be of use quicker.

*Cons:*

- Onboard instrument data from an api is gonna be expensive.

---------------------

> **Historical Data**

*Pros:*

- The data is free and readily available.

*Cons:*

- With historical data im not going to be able to track an actual flight im only going to be able to simulate the idea of tracking a flight.

---------------------------

> **Decision**

Since I don't have money for the former and I don't work for a company that can give me free access to an api ill just have to settle with using hitsorical data for the project.
What ill do though is work out all of the logic so that if I ever do get access to live onboard instrument data I can just plug and play or maybe someone else could take my code and plug and play.

-----------------------------------

> **Data Sources**

*"What I Need"*

CSV/JSON/EXCEL..

- All airports in the Unites States including their geographic data ie. Latitude and Longitude.
- All outbound flights from each airport in the Unites States for the last 10 years lets say.


**Concept Outline**


*Based on the idea that im working with historical data. I need to make a program that feels like its tracking a live flight even though its just going off of historical flight records.*

The user should be able to:

- Select a departure city
- Select an arrival city
- Recieve a prompt if the selected airport cities do not have flights to each other which notifies the user that the flight is not possible because there are no outbound flights from this specific airport to the other.
- Get an ETA right after the user selects both the departure city and the arrival city.
- Have a flight path from the selected airports be generated and viewable instantly on a map.
- Click a button to be able to simulate the flight
- Watch the simulated flight over a map 

*Considerations*

- If there are no historical records of flights from one city to another that means those two airports dont have direct flights.
- How im going to get the ETA from one airport to another ?
> - What I will do is just get all of the data for 10 years of flights from one city to another and ill just take the average flight time per city from all the flights and put that in another file to access quicker so I dont have to make the average calculation every time.
> - If I had live data this would be much easier actually cause I could use the speed the airplane was traveling at to calculate an ETA in intervals to create a live updated ETA.

*IDEAS:*

> Each outgoing flight is its own thing. What does an outgoing flight have?

- A departure city which has a name and is really just geographical points on a map.
- An arrival (Destination) city which also has a name and is also just some points on a map.
- A standard flight speed
- A finite distance between its point of origin and its destination
- Constantly evolving latitude and longitude data
- Cities, Zip codes or geographical points such as bodies of water, mountain ranges, national forrests, landmarks, etc...associated with its constantly evolving lat and long data

*OBJECT INFORMATION:*(Flight Object)

- Each object needs to have static and dynamic information.

> *STATIC OBJECT INFO:*
> - Origin City / Destination City Name or Airport call letters (AKA IATA location identifier)
> - Latitude / longitude data for origin city and destination city.

> *DYNAMIC OBJECT INFO:*
> - destination
> - Miles/KM From Origin
> - Miles/KM To Destination
> - Current Location::Lat/Long(updating..)

IDEA NOTES:

Im going to periodically need to make the program update itself with new data for each flight object. I have to increment the latitude and longitudinal data accordingly.

