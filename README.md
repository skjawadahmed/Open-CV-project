# Open-CV-project
# Identical Image Cleaner for Desktops and Laptops

This tool is perfect for anyone looking to organize their image collections by removing duplicate images and freeing up storage space.

The **Identical Image Cleaner** is a specialized desktop application designed to help users identify and remove duplicate images from their local folders with ease. Whether you're a photographer, designer, or someone with a large collection of images, this tool can help streamline your image management by efficiently detecting and removing duplicates.

## Purpose

Over time, image libraries can accumulate many duplicate files, which take up valuable storage space and make it harder to organize your collections. This application addresses that problem by using a **difference hashing (dHash)** algorithm, which compares the structural differences between images to detect even slight variations, ensuring that duplicates are accurately identified. Once detected, the app provides you with visual feedback to easily compare duplicates and decide which files to delete.

## How It Works

1. **Image Processing**: The app scans a folder specified by the user and processes each image to compute its unique hash using the dHash algorithm. This hash represents the structure of the image and is used to compare it against others in the folder.
  
2. **Duplicate Detection**: By comparing image hashes, the app quickly identifies duplicates within the folder. Even if images have slight modifications, such as different resolutions or minor edits, the algorithm is robust enough to flag them as duplicates.

3. **Visual Comparison**: Detected duplicates are displayed side-by-side in a montage format, allowing users to easily view and compare them. The intuitive interface provides a clear visual presentation to help users make informed decisions about which images to keep.

4. **One-Click Deletion**: After viewing the duplicates, users can choose to delete unnecessary files with a single click. The app safely removes the selected duplicates, helping you free up storage space without having to manually sort through the files.

## Installation
1. Clone this Repository
```bash
  https://github.com/skjawadahmed/Open-CV-project.git
  cd Open-CV-project
```

2. Install required dependencies: Install all the libraries present in (requirements.txt) file.
```bash
  pip install -r requirements.txt
```
3. Click on app.py file

4. Run this command in terminal
```bash
  streamlit run app.py
```
5. Copy paste the path to the folder containing images 

## Key Features

- **Efficient Scanning**: Utilizes the fast and accurate dHash algorithm to identify duplicates in large image collections.
- **Intuitive Interface**: Optimized for desktops and laptops, the app offers a clean and user-friendly interface designed for easy navigation and interaction.
- **Visual Feedback**: Duplicate images are displayed side-by-side in a montage format, making it easy to compare them visually.
- **Simple Deletion Process**: After comparison, duplicates can be deleted directly from the app with just one click, simplifying the cleanup process.
- **Desktop-Optimized**: The application is designed specifically for desktop environments, providing a seamless experience on larger screens.

## Use Cases

This tool is ideal for anyone who deals with large numbers of images, such as:

- **Photographers**: Manage extensive photo libraries by easily identifying and removing redundant photos.
- **Designers**: Clean up your workspace by eliminating duplicate images that clutter your project folders.
- **Everyday Users**: Organize your personal photo collections by finding and deleting duplicate images, saving disk space in the process.

## Screenshots
![Screenshot 2024-09-11 225428](https://github.com/user-attachments/assets/f6d1d3af-49db-4bb2-b155-2b840188ecd4)
![Screenshot 2024-09-11 225457](https://github.com/user-attachments/assets/4c191550-d3af-4038-9850-4b6ba7353808)
![Screenshot 2024-09-11 225520](https://github.com/user-attachments/assets/9309dd5a-f437-4bd4-9cd2-69a1c0e5e146)

## Conclusion

The **Identical Image Cleaner** offers a fast, efficient, and user-friendly solution for managing image collections. By using advanced hashing techniques, it ensures accurate detection of duplicates while providing a simple interface for visual comparison and deletion. This tool helps you maintain a clutter-free, organized image library while saving valuable storage space.



