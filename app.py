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
        img = cv2.imread(imagePath)
        h = dhash(img)
        p = hashes.get(h, [])
        p.append(imagePath)
        hashes[h] = p
    return hashes

def delete_duplicates(hashes):
    """Display duplicates and provide options to delete them."""
    for idx, (h, hashedPaths) in enumerate(hashes.items()):
        if len(hashedPaths) > 1:
            st.subheader(f"Duplicates Found: {len(hashedPaths)}")

            # Create a montage of duplicates
            montage = None
            for p in hashedPaths:
                image = cv2.imread(p)
                image = cv2.resize(image, (150, 150))
                if montage is None:
                    montage = image
                else:
                    montage = np.hstack([montage, image])

            # Display montage
            if montage is not None:
                st.image(montage, channels="BGR")

            # Add delete button with unique key
            delete_button_key = f"delete_button_{idx}"
            if st.button(f"Delete Duplicates ({len(hashedPaths)})", key=delete_button_key):
                for p in hashedPaths[1:]:
                    if os.path.exists(p):
                        try:
                            os.remove(p)
                            st.write(f"Successfully deleted {p}")
                        except Exception as e:
                            st.write(f"Failed to delete {p}: {e}")
                    else:
                        st.write(f"File {p} does not exist")
                st.experimental_rerun()  # Refresh the app to update the display
# User Interface Instructions
# User Interface Instructions for Desktops and Laptops
st.markdown("""
# IDENTICAL IMAGE CLEANER for Desktops and Laptops

Welcome to the **IDENTICAL IMAGE CLEANER** app! This tool is designed to help you identify and manage duplicate images on your desktop or laptop.

## How to Use:
1. **Enter Folder Path**: Provide the path to the folder containing your images in the input box below.
2. **Process Images**: Click the "Press Enter to Apply" button to start scanning for duplicates.
3. **View Results**: Duplicate images will be displayed in a montage format. You can choose to delete the duplicates by clicking the "Delete Duplicates" button.

## Features:
- **Optimized for Desktops and Laptops**: This app is specifically designed for large screens and interaction via mouse and keyboard.
- **Efficient Scanning**: Quickly scans through large collections of images stored on your computer.
- **Clear Visual Feedback**: Duplicate images are presented side by side for easy comparison.
- **Simple Deletion Process**: Easily remove duplicate images with just one click.
- **Custom Background**: Experience a visually appealing design suited for desktop environments.

Feel free to enter the folder path and start finding duplicates now!
""")


# Streamlit app
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