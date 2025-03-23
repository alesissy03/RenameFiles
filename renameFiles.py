import os

def rename_files(directory):
    for filename in os.listdir(directory):
        new_name = f"Desired Name{filename}" # change Desired Name with the name you want to append to your file
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
        print(f'Renamed: {filename} -> {new_name}')

# The new names of the files will be: Desired Name + old name

# Change 'your_directory' to the actual directory path /mnt/d/ for linux or wsl
rename_files('your_directory')
