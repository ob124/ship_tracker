import time
import streamlit as st
import google.cloud.firestore as firestore
import json
import google.oauth2.service_account as service_account
from model.ship import Ship
from util.create_ship_util import create_ship

st.set_page_config(
    page_title="Ship Damage Tracker",
    page_icon="⛵"
)

st.header('Ship Damage Tracker ⛵‽')

key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)

db = firestore.Client(credentials=creds, project="ship-tracker-eae6e")

# Create a reference to the test ship.
doc_ref = db.collection("Ship").document("CeNBhH6iD9hFtZwquP8g")

# creating a single-element container
placeholder = st.empty()

# get data
doc = doc_ref.get()
ship = Ship.from_dict(doc.to_dict())
ship.set_document_id(doc.id)

with st.form("my_form"):
    # inputs
    component = st.selectbox(label="Ship Component", options=["Helm", "Hull", "Sail"])
    value = st.slider(label="value", min_value=0, max_value=100)

    heal_button = st.form_submit_button("Heal")
    if heal_button:
        string = (component + "_health").lower()
        number = value
        doc_ref.update({string: ship.get_health_string(component.lower()) + number})

    damage_button = st.form_submit_button("Damage")
    if damage_button:
        string = (component + "_health").lower()
        number = value
        doc_ref.update({string: ship.get_health_string(component.lower())-number})

# main loop
while True:
    with placeholder.container():
        doc = doc_ref.get()
        ship = Ship.from_dict(doc.to_dict())
        ship.set_document_id(doc.id)

        st.write(f"{ship.ship_name}:", ship.to_dict_filtered())
        time.sleep(1)
