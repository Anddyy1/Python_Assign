def file_read_write():
    try:
        input_file = input("Enter the filename to read: ").strip()
        with open(input_file, "r") as f:
            content = f.read()

        modified_content = content.upper()
        output_file = "modified_" + input_file

        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"Successfully created '{output_file}' with modified content.")

    except FileNotFoundError:
        print(" Error: The file does not exist.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


file_read_write()
