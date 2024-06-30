import streamlit as st
import duckdb
import io
import pandas as pd


beverages = pd.read_csv(io.StringIO("""
beverage,price
Orange juice,2.5
Expresso,2
Tea,3"""))


food_items = pd.read_csv(io.StringIO("""
food_item,food_price
Cookie juice,2.5
Chocolatine,2
Muffin,3"""))


answer = """
SELECT * FROM beverages
CROSS JOIN food_items"""

solution = duckdb.sql(answer).df()


with st.sidebar:
    option = st.selectbox(
        "Sur quelle truc voulez-vous travailler?",
        ("Jointures","Groupby","Window functions"),
        index=None,
        placeholder="Sélectionner le truc"
    )
    st.write('Vous avez sélectionné', option)


st.header("enter your code:")
query = st.text_area(label="votre code SQL ici", key="user_input")
if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)


tab2, tab3 = st.tabs(['Tables','Solution'])

with tab2:
    st.write('table: beverages')
    st.dataframe(beverages)
    st.write('table: food_items')
    st.dataframe(food_items)
    st.write("expected:")
    st.dataframe(solution)
with tab3:
    st.write(answer)