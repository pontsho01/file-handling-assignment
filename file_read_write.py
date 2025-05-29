# File Read & Write Challenge 🖋️

try:
    # Read from original file
    with open("original.txt", "r") as original_file:
        content = original_file.read()

    # Modify the content (e.g., make it uppercase)
    modified_content = content.upper()

    # Write to new file
    with open("modified.txt", "w") as modified_file:
        modified_file.write(modified_content)

    print("File has been read and modified successfully.")

except FileNotFoundError:
    print("The file 'original.txt' does not exist. Please create it first.")
