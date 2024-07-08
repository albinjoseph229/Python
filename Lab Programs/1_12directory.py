import os

def create_directory(directory_name):
    try:
        os.makedirs(directory_name, exist_ok=True)
        print(f"Directory '{directory_name}' created successfully.")
    except Exception as e:
        print(f"Error creating directory '{directory_name}': {e}")

def list_directory_contents(directory_name):
    try:
        contents = os.listdir(directory_name)
        print(f"Contents of directory '{directory_name}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory_name}' does not exist.")
    except Exception as e:
        print(f"Error listing contents of directory '{directory_name}': {e}")

def search_py_files(directory_name):
    try:
        py_files = [f for f in os.listdir(directory_name) if f.endswith('.py')]
        print(f"'.py' files in directory '{directory_name}':")
        for file in py_files:
            print(file)
    except FileNotFoundError:
        print(f"The directory '{directory_name}' does not exist.")
    except Exception as e:
        print(f"Error searching for '.py' files in directory '{directory_name}': {e}")

def remove_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' removed successfully.")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error removing file '{file_path}': {e}")

directory_name = 'Euphoria Website'
file_name = 'a.txt'
file_path = os.path.join(directory_name, file_name)

create_directory(directory_name)
list_directory_contents(directory_name)

sample_py_file = os.path.join(directory_name, 'sample.py')
with open(sample_py_file, 'w') as f:
    f.write('# Sample Python file')

search_py_files(directory_name)
remove_file(sample_py_file)
list_directory_contents(directory_name)
