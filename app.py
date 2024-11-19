# frontend to filter application using streamlit
#
import streamlit as st
from PIL import Image
import backend
# Set up the Streamlit app
st.title("Image Editing Application")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    column1, column2 = st.columns(2)
    column1.write("## Uploaded Image")
    column1.image(image, use_container_width=True, width=400)
    # Select filter type
    filter_type = st.sidebar.selectbox(
        'Select a filter type',
        ('BLUR','EMBOSS', 'FIND_EDGES', 'DETAIL', 'EDGE_ENHANCE')
    )
    enhancement_type = st.sidebar.selectbox('Select an enhancement type', ('COLOR', 'CONTRAST', 'BRIGHTNESS', 'SHARPNESS'))
    enhancement_value = st.sidebar.slider('Select enhancement value', 0.0, 2.0, 1.0)

    # Apply filters using backend functions
    filtered_image = backend.apply_filter(image,filter_type)
    filtered_image = backend.apply_enhancement(filtered_image, enhancement_type, enhancement_value)
    
    # Display filtered image
    column2.write("## Filtered Image")
    column2.image(filtered_image, use_container_width=True, width=400)