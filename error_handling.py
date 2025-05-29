# Error Handling Lab 🧪

filename = input("Enter the filename you want to open: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\n📄 File Content:\n", content)

except FileNotFoundError:
    print("🚫 Error: The file does not exist.")

except IOError:
    print("🚫 Error: The file could not be read.")
