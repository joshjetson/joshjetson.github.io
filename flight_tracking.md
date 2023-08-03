## Tracking a flight

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



'''  The concept is that I have incoming and outgoing flight data. I want to track the location of each flight after it has left its
point of origin. Each flight and flight destinations are going to individually need to be stored in objects.
Im going to divide the tasks I need to accomplish into sections. I was thinking that by obtaining a csv file of all u.s cities inlcuding
their latitude and longitudinal information that I might be able to track a flight and pinpoint its location based on
its flight speed, time of departure, direction of departure, elapsed time since its departure relative from the point of departure
and the point of destination with the understanding that based on the speed that the craft is flying it would reach its destination
at a certain time traversing however many miles/km per hour in the process. Using a simple csv which contains all latitude and longitudinal
information for each city in the u.s along with each cities zip code I could then track the flight and get a rough estimate of where it is
assuming the most shortest distance flight path between the two points, origin and destination.'''
'''  SECTION ONE:::::::::::::::::::
         |__MAIN CONCEPTS:
                     How do I plan on storing the information of each outgoing flight?
                     #SIDENOTE
                         *I say outgoing because I want to start looking at the problem
                         *through the lens of the concept that all flights leaving from
                         * somewhere are outgoing.
                         *Ill consider incoming flight tracking after, since I imagine
                         *that will be easier to track after I have tackled the task
                         *of tracking the outgoing flights.
                         *At present im also not going to consider connecting flights
                         *but rather just fragment each flight and assume its destination
                         *its final destination.
                         *Once I tackle the problem from this perspective I will be
                         *able to factor in connecting flight data and layover
                         *time at a later point because conceptually it will be
                         *an almost identical thing simply now with something new added.

                     IDEAS:
                         Each outgoing flight is its own thing. What does an outgoing flight have?

                         -A point of origin
                         -A destination
                         -A standard flight speed
                         -A finite distance between its point of origin and its destination
                         -Constantly evolving latitude and longitude data
                         -Cities, Zip codes or geographical points such as bodies of water, 
                          mountain ranges, national forrests, landmarks, etc...
                          associated with its constantly evolving lat and long data
                     OBJECT INFORMATION:
                         -Each object needs to have static and dynamic information.
                         _STATIC OBJECT INFO:
                         __Origin City Name or Airport
                         __Lattitude / Longitude data for origin city

                         _DYNAMIC OBJECT INFO:
                         __destination
                         __Miles/KM From Origin
                         __Miles/KM To Destination
                         __Current Location::Lat/Long(updating..)

                     IDEA NOTES:
                         Im going periodically need to make the program update it self with new data
                         for each flight object. I have to increment the latitude and longitudinal
                         data accordingly.'''
