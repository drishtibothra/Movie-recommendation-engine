import pickle
import pandas as pd
import streamlit as st
import requests
from streamlit_option_menu import option_menu

import sys
import os
import spidermanandthanos
import ironmanandhulk
import blackwidowandbatman

sys.path.append(os.path.abspath(r"C:\Users\drish\PycharmProjects\app"))
import app

with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu",
        options = ["Home", "Fun character guess rewards", "Movie recommendation"]
    )

if selected == "Home":
    st.title("Welcome to the Movie recommender system")
    st.text_input("Enter your name: ")
    st.text_input("Enter your age: ")

elif selected == "Fun character guess rewards":
    st.title(f"You have selected {selected}")

    choice = st.selectbox("Select the pair",
                            ("Spider Man and Thanos", "Iron Man and Hulk", "Black Widow and Batman"))
    if st.button("Select"):

        st.write(f"You have selected: {choice}")
        if choice == "Spider Man and Thanos":
            spidermanandthanos.classification()

        elif choice == "Iron Man and Hulk":
            ironmanandhulk.classification()

        elif choice == "Black Widow and Batman":
            blackwidowandbatman.classification()

elif selected == "Movie recommender system":
    st.title(f"You have selected {selected}")
    app.classification()


