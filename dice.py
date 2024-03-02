import streamlit as st
import numpy as np
from PIL import Image


st.set_page_config(page_title="Dice game", page_icon="😍", layout="wide")

st.title("Dice Game")
st.sidebar.image("Dice 2.gif")
st.sidebar.header("Roll for your chance to win big")
st.sidebar.subheader("18+ OGs only")


def dice_game():
    a, b = np.random.randint(1,7,2)
    st.write(f"Your numbers are {a} and {b}")
    if a==6 and b==6:
        st.balloons()
        return('Congratulations! You Win')
    else:
        return('Almost there! Keep Trying')

if st.button("Play now"):
    st.image("Dice 3.gif")
    st.write(dice_game())