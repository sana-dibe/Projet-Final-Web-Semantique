import rdflib

class FlightService:

    def __init__(self, graph):
        self.graph = graph
        
    def add_city_flight(self,):
        # Loading airport turtle file
        g = rdflib.Graph()
        g.parse("/Users/Sana/Documents/GitHub/Projet-Final-Web-Semantique/csv_lifting/airport_lifting/airport.ttl", format="turtle")

        # Loading flight turtle file
        g1 = rdflib.Graph()
        g1.parse("/Users/Sana/Documents/GitHub/Projet-Final-Web-Semantique/api_lifting/cheapestFlights.ttl", format="turtle")

        # Defining namespaces
        class_ns = rdflib.Namespace("http://www.historical-trip.org/class#")
        prop = rdflib.Namespace("http://www.historical-trip.org/porp#")

        # Defining the SPARQL query
        query = """
            PREFIX class_ns: <http://www.historical-trip.org/class#>
            PREFIX prop: <http://www.historical-trip.org/porp#>
            SELECT ?flight ?depAirport ?arrAirport ?icao ?latitude ?longitude ?timeZone ?city ?airportName
            WHERE {
                ?flight a class_ns:Flight;
                    prop:hasDepartureAirport ?depAirport;
                    prop:hasArrivalAirport ?arrAirport.
                ?depAirport prop:hasIATA ?depIATA.
                ?arrAirport prop:hasIATA ?arrIATA.
                ?airport prop:hasIATA ?depIATA;
                    prop:hasICAO ?icao;
                    prop:hasLatitude ?latitude;
                    prop:hasLongitude ?longitude;
                    prop:hasTimezone ?timeZone;
                    prop:hasCity ?city;
                    prop:airportName ?airportName.
            }
        """
        # Executing the SPARQL query
        results = g1.query(query)
        # Adding the results to flight graph
        for row in results:
            g1.add((row.flight, prop.hasICAO, rdflib.Literal(row.icao)))
            g1.add((row.flight, prop.hasLatitude, rdflib.Literal(row.latitude)))
            g1.add((row.flight, prop.hasLongitude, rdflib.Literal(row.longitude)))
            g1.add((row.flight, prop.hasTimezone, rdflib.Literal(row.timeZone)))
            g1.add((row.flight, prop.hasCity, rdflib.Literal(row.city)))
            g1.add((row.flight, prop.airportName, rdflib.Literal(row.airportName)))
        # Saving the enriched flight graph
        g1.serialize("flights_with_city_country.ttl", format="turtle")


if __name__ == "__main__":
    graph = Graph()
    flight_service = FlightService(graph)
    flight_service.add_city_flight()
                