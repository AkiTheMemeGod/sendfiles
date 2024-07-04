import streamlit as st
import random as rd
import os


def center_title(pos, size, color, title, align="center"):
    if pos == "side":
        st.sidebar.markdown(f"""
                        <h1 style="font-family:monospace; color:{color}; font-size: {size}px;", align="{align}">{title}</h1>
                        """,
                            unsafe_allow_html=True)

    else:
        st.markdown(f"""
                <h1 style="font-family:monospace; color:{color}; font-size: {size}px;", align="{align}">{title}</h1>
""",
                    unsafe_allow_html=True)


def otp_gen():
    otp = ""
    for i in range(0, 6):
        z = str(rd.randint(0, 9))
        otp += z

    return otp


