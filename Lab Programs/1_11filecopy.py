# Define the function to copy file contents
def copy_file_contents(source_file, destination_file):
    try:
        # Open the source file in read mode
        with open(source_file, 'r') as src:
            # Open the destination file in write mode
            with open(destination_file, 'w') as dest:
                # Read and write each line from the source file to the destination file
                for line in src:
                    dest.write(line)
                    print(f"The file {source_file} does not exist.")
    except FileNotFoundError:
        
        print(f"Contents copied from {source_file} to {destination_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source = "a.txt"
destination = "b.txt"
copy_file_contents(source, destination)
