import rdflib
from rdflib import Graph, Namespace, RDF, Literal
import json

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

city = "Paris"
monuments = extract_monument_data(city)
for monument in monuments:
    ##print("Monument: ", monument["monument"])
    print("Name: ", monument["name"])
    print("Opening Hours: ", monument["opening_hours"])
    print("Rating: ", monument["rating"])
    print("Wikidata: ", monument["wikidata"])
    print("Description: ", monument["description"])
    print("\n")