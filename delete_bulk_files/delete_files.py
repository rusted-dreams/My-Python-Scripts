import os


directory_path = input("Enter the directory: ")
directory_path = r"{}".format(directory_path)  # Converts the normal string to raw string so that the back slashes are not used for escaping characters.

for root, dirs, files in os.walk(directory_path):
    for file in files:
        if file.endswith(".srt") and not file.endswith("English.srt"):
            os.remove(os.path.join(root, file))

# print(files)