def main():
    try:
        #File creation (write mode)
        with open("my_file.txt", "w") as file:
            file.write("This is the first line of text.\n")
            file.write("Here's a line with a number: 42\n")
            file.write("And a final line with a greeting!\n")
            print("Successfully created and wrote to 'my_file.txt'")

        #File Reading and Display
        with open("my_file.txt", "r") as file:
            contents = file.read()
            print("\nContents of 'my_file.txt':")
            print(contents)

        #File Appending
        with open("my_file.txt", "a") as file:
            file.write("Appending a new line.\n")
            file.write("Adding another line of text.\n")
            file.write("This is the final appended line.\n")
            print("\nSuccessfully appended text to 'my_file.txt'")

    except FileNotFoundError:
        print("Error: File 'my_file.txt' not found.")
    except PermissionError:
        print("Error: Permission denied while accessing the file.")
    finally:
        print("\nScript execution completed.")

if __name__ == "__main__":
    main()
