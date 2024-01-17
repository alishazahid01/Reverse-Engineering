Basic Reverse Engineering Documentation
Introduction

The Basic Reverse Engineering script is a Python script that provides basic functionality for analyzing and reverse engineering binary files. It utilizes the r2pipe library to interact with the Radare2 reverse engineering framework. This documentation provides an overview of the code structure, usage, and functionality.
Getting Started

To use the Basic Reverse Engineering script, follow these steps:

    Install Radare2 and the r2pipe library:
        Radare2 Installation: https://github.com/radareorg/radare2
        r2pipe Installation: https://github.com/radareorg/radare2-r2pipe

    Clone or download this repository to your local machine.

    Open the Python script in a code editor or integrated development environment (IDE).

    Run the script using the command:

    python reverse_engineering.py

    Follow the prompts to provide the path to the binary file and choose the reverse engineering actions.

Code Structure

The Basic Reverse Engineering script consists of the following components:
1. ReverseEngineering Class


class ReverseEngineering:
    # Constructor 
    def __init__(self, path):
        self.path = path
        self.bin_file = None

This class is the core of the reverse engineering process. It takes the path to the binary file as an input parameter and initializes the r2pipe connection to the binary file.
2. Opening the Binary File


    # Open the binary file
    @print_message
    def open_file(self):
        try:
            self.bin_file = r2pipe.open(self.path)
        except Exception as e:
            print(f"Error occurred while opening the file: {str(e)}")

This method opens the specified binary file using r2pipe. It establishes a connection to the file for further analysis.
3. Printing the 'main' Function



    # Disassemble and print the 'main' function
    @print_message
    def print_main_func(self):
        try:
            disassembly = self.bin_file.cmd('pdf @main')
            print(disassembly)
        except Exception as e:
            print(f"Error occurred while printing the main function: {str(e)}")

This method disassembles and prints the 'main' function of the binary file. It uses the pdf @main command to disassemble and display the function's code.
4. Listing All Functions



    # List all functions in the binary
    @print_message
    def print_all_func(self):
        try:
            functions = self.bin_file.cmdj('aflj')
            for function in functions:
                print(function['name'])
        except Exception as e:
            print(f"Error occurred while printing all functions: {str(e)}")

This method lists all the functions present in the binary file. It uses the aflj command to retrieve a JSON list of functions and prints their names.
5. Extracting and Printing Strings



    # Extract and print strings from the binary
    @print_message
    def print_all_strings(self):
        try:
            strings = self.bin_file.cmdj('izzj')
            for string in strings:
                print(string['string'])
        except Exception as e:
            print(f"Error occurred while printing all strings: {str(e)}")

This method extracts and prints all the strings present in the binary file. It uses the izzj command to retrieve a JSON list of strings and prints their content.
6. Closing the Binary File


    # Close the binary file
    @print_message
    def close_file(self):
        try:
            self.bin_file.quit()
        except Exception as e:
            print(f"Error occurred while closing the file: {str(e)}")

This method closes the connection to the binary file using the quit command.
7. Decorator for Printing Messages


# Decorator 
def print_message(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        try:
            if "print_main_func" in func.__name__:
                print("Printing disassembly....") 
            elif "print_all_func" in func.__name__:
                print("Printing all the functions....") 
            elif "print_all_strings" in func.__name__:
                print("Printing all the strings....") 
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return None
        result = func(*args, **kwargs)
        print(f"{func.__name__} completed.")
        return result
    return wrapper

This decorator is used to print messages before and after each reverse engineering action. It adds a layer of information and error handling to the script.
Usage

    Run the Python script to initiate the Basic Reverse Engineering tool:


    python reverse_engineering.py

    Enter the path to the binary file when prompted.

    Choose one or more reverse engineering actions from the menu:
        Print the disassembly of the 'main' function.
        Print a list of all functions in the binary.
        Print all strings extracted from the binary.

    The script will perform the selected actions and provide feedback along the way.

Conclusion

This documentation provides an overview of the Basic Reverse Engineering script, which allows you to perform basic reverse engineering tasks on binary files. You can use this script to explore the disassembly of the 'main' function, list all functions in a binary, and extract and print strings from the binary for further analysis.
