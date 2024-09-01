import streamlit as st
import cv2
import numpy as np
import os
from imutils import paths

def dhash(image, hashsize=8):
    """Calculate the difference hash of an image."""
    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(imgGray, (hashsize + 1, hashsize))
    diff = resized[:, 1:] > resized[:, :-1]
    return sum([2**i for (i, v) in enumerate(diff.flatten()) if v])

def process_images(image_folder):
    """Process images in a folder and return a dictionary of hash values and image paths."""
    imagePaths = list(paths.list_images(image_folder))
    hashes = {}
    for imagePath in imagePaths:
        try:
            img = cv2.imread(imagePath)
            if img is None:
                st.write(f"Could not load image: {imagePath}")
                continue
            h = dhash(img)
            p = hashes.get(h, [])
            p.append(imagePath)
            hashes[h] = p
        except Exception as e:
            st.write(f"Error processing {imagePath}: {e}")
    return hashes

def delete_duplicates(hashes):
    """Display duplicates and provide options to delete them."""
    for idx, (h, hashedPaths) in enumerate(hashes.items()):
        if len(hashedPaths) > 1:
            st.subheader(f"Duplicates Found: {len(hashedPaths)}")

            # Create a montage of duplicates
            montage = None
            for p in hashedPaths:
                try:
                    image = cv2.imread(p)
                    image = cv2.resize(image, (150, 150))
                    if montage is None:
                        montage = image
                    else:
                        montage = np.hstack([montage, image])
                except Exception as e:
                    st.write(f"Error loading image {p}: {e}")

            # Display montage
            if montage is not None:
                st.image(montage, channels="BGR")

            # Add delete button with unique key
            delete_button_key = f"delete_button_{idx}"
            if st.button(f"Delete Duplicates ({len(hashedPaths)})", key=delete_button_key):
                for p in hashedPaths[1:]:
                    try:
                        if os.path.exists(p):
                            os.remove(p)
                            st.write(f"Successfully deleted {p}")
                        else:
                            st.write(f"File {p} does not exist")
                    except Exception as e:
                        st.write(f"Failed to delete {p}: {e}")
                st.experimental_rerun()

st.subheader('Enter file path & identify the repeated images and clean them')

folder_path = st.text_input("Enter the path to the folder containing images:")

if folder_path:
    if os.path.isdir(folder_path):
        hashes = process_images(folder_path)
        delete_duplicates(hashes)
    else:
        st.write("The provided path is not a valid directory.")

st.markdown("""
    <footer style='text-align: center; font-family: Arial; font-size: 14px; color: white;'>
        <hr style='border-color: white;'>
            Copyright &copy; Designed and Developed by S K Jawad Ahmed - All rights reserved.
    </footer>
    """, 
    unsafe_allow_html=True
)
