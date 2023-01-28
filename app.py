"""
import streamlit as st
import datetime
st.title("Doctor's visit")


with st.form("Patient form"):
   title = st.text_input('First name', '')
   title = st.text_input('Last name', '')
   title = st.text_input('NSS', '')
   d= st.date_input("Patient birthday",) 
   txt = st.text_area('What the patient feel?', '''
    ''')
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("The form was submitted")

"""


import streamlit as st
import SPARQLWrapper
import pandas as pd

# Connect to the triplestore
sparql = SPARQLWrapper.SPARQLWrapper("http://example.com/sparql")

# Write the SPARQL query
query = """
PREFIX ex: <http://example.com/>
SELECT ?subject ?predicate ?object
WHERE {
  ?subject ?predicate ?object .
}
LIMIT 100
"""

# Run the SPARQL query
sparql.setQuery(query)
sparql.setReturnFormat(SPARQLWrapper.JSON)
results = sparql.query().convert()

# Convert the results to a Pandas dataframe
df = pd.io.json.json_normalize(results['results']['bindings'])

# Use Streamlit to display the results
st.write("Results of SPARQL query:")
st.write(df)