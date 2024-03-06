import os
def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):  
            os.remove(file_path)
            print(f"File '{file_path}' has been deleted.")
        else:
            print(f"You do not have write access to '{file_path}'. Cannot delete.")
    else:
        print(f"File '{file_path}' does not exist.")

file_to_delete = "path/to/your/file.txt"
delete_file(file_to_delete)