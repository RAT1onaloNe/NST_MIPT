import os
import streamlit as st
from PIL import Image
from main import test_image

style = {
    "Yellow": "yellow.pth",
    "Green": "green.pth",
    "Blue": "blue.pth"
}

style_images = {
    "Yellow": "./styles/yellow.jpg",
    "Green": "./styles/green.jpg",
    "Blue": "./styles/blue.jpg"
}

def main():
    st.title("Image Style Transfer")

    st.sidebar.title("Choose Style")
    style = st.sidebar.selectbox("Select the style", list(styles.keys()))

    st.sidebar.image(style_images[style], caption=style, use_column_width=True)

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        input_image = Image.open(uploaded_file)
        st.image(input_image, caption="Uploaded Image", use_column_width=True)

        if st.button("Stylize"):
            with st.spinner("Processing..."):
                # Save the uploaded image to a file
                input_image_path = f"./{uploaded_file.name}"
                input_image.save(input_image_path)

                # Process the image
                checkpoint_model = f"./checkpoints/{style[style]}"
                output_image_path = test_image(input_image_path, checkpoint_model, './')

                # Display the output image
                output_image = Image.open(output_image_path)
                st.image(output_image, caption="Stylized Image", use_column_width=True)

                # Remove the images
                os.remove(input_image_path)
                os.remove(output_image_path)

if __name__ == '__main__':
    main()
