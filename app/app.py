import streamlit as st
import rdflib
from rdflib import Graph, Namespace, RDF, Literal
import json


def get_flights_by_price(price):
    g = rdflib.Graph()
    g.parse("/Users/Sana/Documents/GitHub/Projet-Final-Web-Semantique/app/flights_with_city_country.ttl", format="ttl")
    query = f"""
        SELECT ?flight ?departureDate ?arrivalDate ?price ?arrAirport ?timeZone ?city ?airportName ?iata
        WHERE {{
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
            FILTER (?price <= {price})
        }}
    """
    return g.query(query)


def extract_monument_data(city):
    g = Graph()
    g.parse("/Users/Sana/Documents/GitHub/Projet-Final-Web-Semantique/csv_lifting/monument_lifting/monument.ttl", format="ttl")
    historical_trip = Namespace("http://www.historical-trip.org/class#")
    schema = Namespace("http://schema.org/")
    monument_props = Namespace("http://www.historical-trip.org/porp#")
    wikidata = Namespace("https://www.wikidata.org/wiki/")


    city_uri = historical_trip[city]
    q = (
        "SELECT ?monument ?name ?opening_hours ?rating ?wikidata ?description "
        "WHERE { "
        "   ?monument a historical_trip:HistoricalSite; "
        f"      historical_trip:{city} \"{city}\"; "
        "      monument_props:hasName ?name; "
        "      monument_props:hasOpeningHours ?opening_hours; "
        "      monument_props:hasRating ?rating; "
        "      wikidata: ?wikidata ; "
        "      schema:description ?description . "
        "}"
    )
    results = g.query(q, initNs={
        "historical_trip": historical_trip,
        "schema": schema,
        "monument_props": monument_props,
        "wikidata": wikidata
    })
    monuments = []
    for row in results:
        monuments.append({
            "monument": row[0],
            "name": row[1],
            "opening_hours": row[2],
            "rating": row[3],
            "wikidata": row[4],
            "description": row[5]

        })
    return monuments

st.title("Flight Information")

price = st.number_input("Enter maximum price:")

results = get_flights_by_price(price)
counter = 1
selected_flight = None


st.write("Flights below maximum price:")
for row in results:
    flight, departureDate, arrivalDate, price, arrAirport, timeZone, city, airportName, iata = row
    checkbox_value = st.checkbox("Flight " + str(counter) + " : to " + city, value=False)
    #st.markdown("### Flight " + str(counter) + " informations")
    if checkbox_value:
        selected_flight = row
        st.image("/Users/Sana/Documents/GitHub/Projet-Final-Web-Semantique/app/flight.jpeg", width=None)
        st.write("Departure Date: ", departureDate)
        st.write("Arrival Date: ", arrivalDate)
        st.write("Price: ", price)
        st.write("Timezone: ", timeZone)
        st.write("City: ", city)
        st.write("Airport Name: ", airportName)
        st.write("Airport IATA: ", iata)
    counter += 1

if selected_flight:
    city = selected_flight[6]
    st.markdown("### Selected flight city: " + city)
    if st.button("Show information about monument in " + city):
        st.write("Information about the monument in", city)
        monuments = extract_monument_data(city)
        if monuments:
            for monument in monuments:
                st.markdown("## Monument Name: " +  monument["name"])
                st.write("Rating: ", monument["rating"])
                #st.write("WikiData: ", monument["wikidata"])
                st.write("Description: ", monument["description"])
                st.write("Opening Hours: ", monument["opening_hours"])

        else:
            st.write("Sorry, there is no information about the monument in ", city)

    







