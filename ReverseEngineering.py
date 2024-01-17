# Basic Reverse engineering 
import r2pipe

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

# Class for Reverse Engineering
class ReverseEngineering:
    # Constructor 
    def __init__(self, path):
        self.path = path
        self.bin_file = None

    # Open the binary file
    @print_message
    def open_file(self):
        try:
            self.bin_file = r2pipe.open(self.path)
        except Exception as e:
            print(f"Error occurred while opening the file: {str(e)}")

    # Disassemble and print the 'main' function
    @print_message
    def print_main_func(self):
        try:
            disassembly = self.bin_file.cmd('pdf @main')
            print(disassembly)
        except Exception as e:
            print(f"Error occurred while printing the main function: {str(e)}")

    # List all functions in the binary
    @print_message
    def print_all_func(self):
        try:
            functions = self.bin_file.cmdj('aflj')
            for function in functions:
                print(function['name'])
        except Exception as e:
            print(f"Error occurred while printing all functions: {str(e)}")

    # Extract and print strings from the binary
    @print_message
    def print_all_strings(self):
        try:
            strings = self.bin_file.cmdj('izzj')
            for string in strings:
                print(string['string'])
        except Exception as e:
            print(f"Error occurred while printing all strings: {str(e)}")

    # Close the binary file
    @print_message
    def close_file(self):
        try:
            self.bin_file.quit()
        except Exception as e:
            print(f"Error occurred while closing the file: {str(e)}")

if __name__ == "__main__":

    # Prompt user to enter the path of the file
    path = input("Enter the path of the file: ")

    # Making class obj 
    cls_obj = ReverseEngineering(path)
    cls_obj.open_file()
    cls_obj.print_main_func()
    cls_obj.print_all_func()
    cls_obj.print_all_strings()
    cls_obj.close_file()
