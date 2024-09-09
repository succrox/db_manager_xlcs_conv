import streamlit as st
import pandas as pd
from Vendors_functions import *

st.title("Vendors page")

vendors = get_all_the_vendors()

df_table = pd.DataFrame(vendors)

st.table(df_table)

st.title("Create vendor")


name = st.text_input('Name')
zone = st.text_input('Zone')
telf = st.text_input('Phone number')
mail = st.text_input('Mail')
goal = st.number_input(label="Sales goal", step = 1, min_value = 0)
sales = st.number_input(label="Completed sales", step = 1, min_value = 0)
comissions = st.number_input(label="Comissions", step = 1, min_value = 0)
clients = st.number_input(label="Clients", step = 1, min_value = 0)
state = st.text_input('State')
comments = st.text_input('Comments')

submit = st.button("Submit")

if submit:

    values = (
        name,zone,telf,mail,goal,sales,comissions,clients,state,comments
    )

    insert_single_vendor(values)

st.title("bulk upload vendors")

uploaded_file = st.file_uploader("Vendors list excel file", type=["xls", "xlsx"])

save = st.button("Save vendors")

if save:
    if uploaded_file is not None:
        df = extract_vendors_from_excel(uploaded_file)

        st.write(df)

        insert_vendors_in_bulk(df)

        st.write("Students have been created successfully")
    