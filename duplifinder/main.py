import os
import shutil
import csv

# specify the directory to search for duplicate files
dir_path = 'E:/Videos/'

# create a dictionary to store filenames and their full paths
files = {}

# iterate over all files in the directory and its subfolders
for root, dirs, filenames in os.walk(dir_path):
    for filename in filenames:
        # ignore desktop.ini file
        if filename == 'desktop.ini':
            continue
        # get the file name without extension
        file_name = os.path.splitext(filename)[0]
        # check if file name already exists in dictionary
        if file_name in files:
            # create the duplicates folder if it doesn't exist
            if not os.path.exists('duplicates'):
                os.mkdir('duplicates')
            # move the duplicate file to the duplicates folder
            file_path = os.path.join(root, filename)
            try:
                shutil.move(file_path, os.path.join('duplicates', filename))
            except shutil.Error as e:
                print(f"Unable to move {filename}: {e}")
        else:
            # add the file name and path to the dictionary
            files[file_name] = os.path.join(root, filename)

# write the dictionary to a CSV file
with open('duplicate_files.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    for filename, file_path in files.items():
        writer.writerow([filename, file_path])
