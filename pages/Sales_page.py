import streamlit as st
import pandas as pd
from Sales_functions import *
from Vendors_functions import get_all_the_vendors

st.title("Sales page")

vendors = get_all_the_sales()

df_table = pd.DataFrame(vendors)

st.table(df_table)

st.title("Create sale")

vendors = get_all_the_vendors()

vendors_dict = {vendor['ID']: vendor['Nombre'] for vendor in vendors}
vendors_ids = list(vendors_dict.keys())

id_vendor = st.selectbox("Select a course", vendors_ids, format_func=lambda id: vendors_dict[id])
name = st.text_input('Name client')
product = st.text_input('Product name')
quantity = st.number_input(label="Quantity", step = 1, min_value = 0)
price = st.number_input(label="Price", step = 1, min_value = 0)
total = st.number_input(label="Total sale", step = 1, min_value = 0)
payment = st.text_input('Payment method')
status = st.text_input('Status')

submit = st.button("Submit")

if submit:

    values = (
        id_vendor,name,product,quantity,price,total,payment,status
    )

    insert_single_sale(values)

st.title("bulk upload vendors")

uploaded_file = st.file_uploader("Vendors list excel file", type=["xls", "xlsx"])

save = st.button("Save vendors")

if save:
    if uploaded_file is not None:
        df = extract_sale_from_excel(uploaded_file)

        st.write(df)

        insert_sale_in_bulk(df)

    