# File Read & Write Challenge 🖋️
# Error Handling Lab 🧪

def modify_content(content):
    """
    Simple modification function:
    - Converts text to uppercase
    (you can change this logic as needed)
    """
    return content.upper()


def main():
    # Ask the user for the input filename
    filename = input("Enter the filename to read: ")

    try:
        # Try opening and reading the file
        with open(filename, "r") as infile:
            content = infile.read()
        
        # Modify the content
        modified_content = modify_content(content)
        
        # Write modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)
        
        print(f"✅ File successfully modified and saved as '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


# Run the program
if __name__ == "__main__":
    main()
