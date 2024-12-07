import streamlit as st
import requests
from PIL import Image, ImageDraw
import numpy as np
from io import BytesIO

from streamlit_extras.image_selector import image_selector, convert_to_pil_image, show_selection


def example():
    response = requests.get(
        "https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
    )

    image = Image.open(BytesIO(response.content))

    selection_type = st.radio(
        "Selection type", ["lasso", "box"], index=0, horizontal=True
    )

    selection = image_selector(image=image, selection_type=selection_type)
    if selection:
        st.json(selection, expanded=False)
        show_selection(image, selection)


example()