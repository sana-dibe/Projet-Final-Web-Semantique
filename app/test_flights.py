import rdflib
from rdflib import Graph, URIRef, Literal

g = rdflib.Graph()
g.parse("/Users/Sana/Documents/GitHub/Projet-Final-Web-Semantique/app/flights_with_city_country.ttl", format="ttl")

# query for all triples that have rdf:type <http://www.historical-trip.org/class#Flight>
query = """
    SELECT ?flight ?departureDate ?arrivalDate ?price ?arrAirport ?timeZone ?city ?airportName ?iata
    WHERE {
        ?flight a <http://www.historical-trip.org/class#Flight>;
               <http://www.historical-trip.org/porp#hasDepartureDate> ?departureDate;
               <http://www.historical-trip.org/porp#hasArrivalDate> ?arrivalDate;
               <http://www.historical-trip.org/porp#hasPrice> ?price;
                <http://www.historical-trip.org/porp#hasArrivalAirport> ?arrAirport.
        ?arrAirport a <http://www.historical-trip.org/class#Airport>;
                    <http://www.historical-trip.org/porp#hasTimezone> ?timeZone;
                    <http://www.historical-trip.org/porp#hasCity> ?city;
                    <http://www.historical-trip.org/porp#airportName> ?airportName;
                    <http://www.historical-trip.org/porp#hasIATA> ?iata.
    }
"""

# execute the query and iterate over the results
for row in g.query(query):
    flight, departureDate, arrivalDate, price, arrAirport, timeZone, city, airportName, iata = row
    #print("Flight: ", flight)
    print("Flight informations : ")
    print("Departure Date: ", departureDate)
    print("Arrival Date: ", arrivalDate)
    print("Price: ", price)
    #print("Arrival airport", arrAirport)
    print("Timezone: ", timeZone)
    print("City: ", city)
    print("Airport Name: ", airportName)
    print("Airport IATA: ", iata)
    print("\n")




