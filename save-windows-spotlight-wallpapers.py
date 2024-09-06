import os
import shutil

# Define paths
source_dir = r"%localappdata%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
source_dir = os.path.expandvars(source_dir)  # Expand environment variable
destination_dir = os.path.join(os.path.expanduser("~"), "Desktop", "WindowsImages")

# Create destination folder if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Copy files from source to destination
for file_name in os.listdir(source_dir):
    source_file = os.path.join(source_dir, file_name)
    if os.path.isfile(source_file):
        shutil.copy2(source_file, destination_dir)

# Rename the files in the destination folder by adding the .jpg extension
for file_name in os.listdir(destination_dir):
    file_path = os.path.join(destination_dir, file_name)
    if os.path.isfile(file_path) and not file_name.endswith('.jpg'):
        new_file_name = f"{file_name}.jpg"
        new_file_path = os.path.join(destination_dir, new_file_name)
        os.rename(file_path, new_file_path)

print("Wallpapers Successfully Saved to Desktop")
