def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(f"{item}\n")
        print(f"List has been written to '{file_path}'.")

file_path = r"C:\Users\user\Desktop\pp2_2024\lab6\dir_and_files"
data_to_write = ["my", "name", "is", "Aya"]
write_list_to_file(file_path, data_to_write)