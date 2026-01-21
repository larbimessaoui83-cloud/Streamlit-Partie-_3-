import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

# ============================
# Données utilisateurs
# ============================
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'administrateur'
        }
    }
}

# ============================
# Authenticator
# ============================
authenticator = Authenticate(
    lesDonneesDesComptes,
    "cookie_name",
    "cookie_key",
    30
)

authenticator.login()

# ============================
# Si authentifié
# ============================
if st.session_state["authentication_status"]:

    # Sidebar
    with st.sidebar:
        st.write(f"Bienvenue {st.session_state['name']}")
        authenticator.logout("Déconnexion")

        menu = option_menu(
            menu_title=None,
            options=[" Accueil", " Les photos de mon chat"],
            icons=["house", "camera"],
            default_index=0
        )

    # ============================
    # Page Accueil
    # ============================
    if menu == " Accueil":
        st.title("Bienvenue sur la page d'accueil !")
       

    # ============================
    # Page Album Photo
    # ============================
    elif menu == " Les photos de mon chat":
        st.title("Bienvenue dans l'album de mon chat ")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("https://www.woopets.fr/assets/ckeditor/2021/jul/all/11687/xl/tucked-in-kitties-subreddit-60f9404e96a22__700.jpg")

        with col2:
            st.image("https://www.woopets.fr/assets/ckeditor/2021/jul/all/11687/xl/tucked-in-kitties-subreddit-60f95b813716d__700.jpg")

        with col3:
            st.image("https://www.woopets.fr/assets/img/011/687/1200x675/20-photos-attendrissantes-de-chats-bien-installes-sous-la-couverture.jpg")

# ============================
# Erreurs de connexion
# ============================
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est incorrect")

elif st.session_state["authentication_status"] is None:
    st.warning("Les champs username et mot de passe doivent être remplis")
