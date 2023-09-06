import json
import os

def directories_folders(route):
    all_elements = os.listdir(route)

    # Filtrar solo los directorios
    directories = [element for element in all_elements if os.path.isdir(os.path.join(route, "/", element))]
    return directories

def directories_files(route):
    all_elements = os.listdir(route)

    # Filtrar solo los directorios
    files = [element for element in all_elements if os.path.isfile(os.path.join(route, "/", element))]
    return files

def search_loop(route):
    file_dictionary = dict()
    for i in directories_folders(route):
        folder_route = route + i
        for j in directories_files(folder_route):
                with open(file_name, "r") as file:
                    file_content = file.read()
                    file_dictionary[file_name] = file_content
   

    return file_dictionary


# function to dump all data into a json file 
def dump_json(file_name, file_dictionary):
    with open(file_name, "w") as json_file:
        json.dump(file_dictionary, json_file, indent=4)
    return None



