def modify_content(content):
    # Example modification: Convert to uppercase
    return content.upper()

def main():
    input_file = input("Enter the name of the file to read: ")
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            modified_content = modify_content(content)
            output_file = input("Enter the name of the file to write to: ")
            with open(output_file, 'w') as file:
                file.write(modified_content)
                print(f"Content written to {output_file}")
    except FileNotFoundError:
            print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()

