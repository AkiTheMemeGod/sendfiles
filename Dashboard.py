from assets import *

center_title("center", 90, "Black", "Send-Files")
center_title("s", 70,"green","<br>")


c1, c2 = st.columns(2)
with c1:
    st.page_link("pages/Send Files.py", label=":green[Send Files]", icon="⬆️")
with c2:
    st.page_link("pages/Receive Files.py", label=":red[Receive Files]", icon="⬇️")

st.link_button("Share it with your friends", url="https://sendfiles.streamlit.app")