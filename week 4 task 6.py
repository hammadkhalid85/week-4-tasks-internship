import os
import re
folder_path = input("Enter folder path: ")

pattern = re.compile(r"^report.*\.txt$", re.IGNORECASE)

print("Matching .txt files:")
for filename in os.listdir(folder_path):
    if filename.endswith(".txt") and pattern.match(filename):
        print(filename)
