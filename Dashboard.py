from assets import *


hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stToolbar {visibility: hidden;}
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
