# RenameFiles
21.03.2025
Alexia Mocanu

Rename Files script in Python

I put together this little script out of a necessity that I encountered: I needed to rename append a title to about 10 files (musical scores).
The original title was the name of the instrument, for example 'Piano' and the desired name would look something like 'Song_Title_Piano'.

I decided to use Python for this as it would be easy to implement.

I imported os to interact with the operations system.
Looping through all the files in my directory, I generated the new name.
os.rename requires fool paths to the files so I had the old_path with the old filename and new_path with the new filename.

I compiled this script using pyhon3 and on wsl.
Change 'your_directory' with the directory your files are, using absolute path of your directory.

command for running the code: python3 renameFiles.py
