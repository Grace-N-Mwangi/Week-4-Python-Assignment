def modify_file_content(content):
    """
    Modify the content of the file. 
    For this example, we will convert all text to uppercase.
    
    Parameters:
    content (str): The original content of the file.

    Returns:
    str: The modified content.
    """
    return content.upper()

def read_and_write_files():
    """
    Reads a file and writes a modified version to a new file. 
    Handles errors if the file doesn't exist or can't be read.
    """
    try:
        # Ask the user for the filename
        input_filename = input("Enter the name of the file to read: ")
        
        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content
        modified_content = modify_file_content(content)

        # Write the modified content to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"The modified content has been written to '{output_filename}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read or written.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    read_and_write_files()
