'''import shutil

class FileUtility:
    @staticmethod
    def read_text_file(filename):
        """Read and return the contents of a text file."""
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist.")
            return None
        except IOError as e:
            print(f"Error: Could not read the file '{filename}'.")
            print(f"Details: {e}")
            return None

    @staticmethod
    def write_text_file(filename, content):
        """Write content to a text file."""
        try:
            with open(filename, 'w') as file:
                file.write(content)
            print(f"File '{filename}' successfully written.")
        except IOError as e:
            print(f"Error: Could not write to the file '{filename}'.")
            print(f"Details: {e}")

    @staticmethod
    def copy_file(source_file, destination_file):
        """Copy a file from source to destination."""
        try:
            shutil.copyfile(source_file, destination_file)
            print(f"File '{source_file}' successfully copied to '{destination_file}'.")
        except FileNotFoundError:
            print(f"Error: The file '{source_file}' does not exist.")
        except shutil.SameFileError:
            print(f"Error: Source and destination files are the same.")
        except IOError as e:
            print(f"Error: Could not copy the file '{source_file}' to '{destination_file}'.")
            print(f"Details: {e}")'''
# method overriding#
'''class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()class Animal:
    def sound(self):
        print("Some generic sound")'''

method overloading#
'''class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


calc = Calculator()
print(calc.add(2, 3,9))
print(calc.add(2, 3, 4))'''


