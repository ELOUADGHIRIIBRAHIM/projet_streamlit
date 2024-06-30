import streamlit as st
import duckdb
import io
import pandas as pd

st.write('HEllo World!')


option = st.selectbox(
    "Sur quelle truc voulez-vous travailler?",
    ("Jointures","Groupby","Window functions"),
    index=None,
    placeholder="Sélectionner le truc"
)
st.write('Vous avez sélectionné', option)



tab1, tab2, tab3 = st.tabs(["Cat","Dog","Owl"])
df = pd.read_csv(io.StringIO("""a,b,c
    1,2,3
    7,9,7"""))
with tab1:
    query = st.text_area(label="entrez votre input")
    result = duckdb.sql(query).df()
    st.write(f"Query entée : {query}")
    st.dataframe(result)
with tab2:
    st.header("A dog")

with tab3:
    st.header('lkada')