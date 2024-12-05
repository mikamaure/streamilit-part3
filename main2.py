import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

lesDonneesDesComptes = {'usernames': {'root': {
   'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
    )

authenticator.login()

if "authentication_status" in st.session_state:
    if st.session_state["authentication_status"]:
        with st.sidebar:
            selection = option_menu(menu_title=None, options = ["Accueil", "Photos"], icons=["house", "camera"])
            selection
            authenticator.logout("Déconnexion")

        if selection == "Accueil":
            st.write("Bienvenue sur ma page")
            st.image("Quête Streamlit Partie 3 accueil.png")
        elif selection == "Photos":
            st.write("Bienvenue dans l'album de mon chat")
            st.image("Quête Streamlit Partie 3 photos de mon chat.png")
      
    elif st.session_state["authentication_status"] is False:
        st.error("L'username ou le password est/sont incorrect")
    else: 
        st.warning("Les champs username et mot de passe doivent être remplie")
else: 
    st.error("État d'authentification non initialisé.")