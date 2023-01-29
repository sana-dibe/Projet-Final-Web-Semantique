# flightlabs/findFlights

This SPARQL micro-service searches flights on [Goflightlabs](https://www.goflightlabs.com), that are going to the same destination.

**Query mode**: SPARQL

**Input**:
- Arrival airport iata code

## Run Docker with SPARQL micro-service

To start running SPARQL micro-services, place in api_lifting folder where you will run docker-compose, and set file access rights as demonstrated below so that the Docker container can read/write the necessary files and folders.

```bash
chmod -R 755 services
chmod -R 755 config
chmod -R 777 logs
```

Then, run:

```
docker-compose up -d
```

Wait a few seconds for Corese to initialize properly. 
Then, you can test the services using the commands below in a bash.

```bash
# URL-encoded query: construct where {?s ?p ?o}
CONSTRUCT=construct%20WHERE%20%7B%20%3Fs%20%3Fp%20%3Fo%20%7D%20

curl --header "Accept: text/turtle" \
  "http://localhost/service/amadeus4dev/cheapestFlights?query=${CONSTRUCT}&departure_iata=MAD&max_Price=1000" 

# URL-encoded query: select * where {?s ?p ?o}
SELECT='select%20*%20where%20%7B%3Fs%20%3Fp%20%3Fo%7D'

curl --header "Accept: application/sparql-results+json" \
  "http://localhost/service/amadeus4dev/cheapestFlights?query=${CONSTRUCT}&departure_iata=MAD&max_Price=1000" 
```

