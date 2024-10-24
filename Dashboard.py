from assets import *


hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;} /* Hides the hamburger menu */
    footer {visibility: hidden;} /* Hides the footer */
    header {visibility: hidden;} /* Hides the header */
    .stToolbar {visibility: hidden;} /* Hides the Streamlit toolbar */
    .viewerBadge_link__1S137 {display: none;} /* Hides the GitHub DP and fork ribbon */
    .stApp {margin-top: -40px;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

center_title("center", 90, "Black", "Send-Files")
center_title("s", 70,"green","<br>")


c1, c2 = st.columns(2)
with c1:
    st.page_link("pages/Send Files.py", label=":green[Send Files]", icon="⬆️")
with c2:
    st.page_link("pages/Receive Files.py", label=":red[Receive Files]", icon="⬇️")

st.link_button("Share it with your friends", url="https://sendfiles.streamlit.app")
