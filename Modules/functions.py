"""Functions"""

FILEPATH = "ToDos.txt"  #Contants shoudl be writen in capitals.

def get_todos(filepath=FILEPATH):
    """Function to read the file and return the content in a list"""
    with open(filepath, "r", encoding="utf-8") as archive:
        reading_content_list = archive.readlines()
    return reading_content_list

def write_todos(todos_arg, filepath=FILEPATH):
    """Function to write in the file the content of the provided list(todos_arg)"""
    with open(filepath, "w", encoding="utf-8") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":  #__name__ es una variable de python. Si se ejecuta este file -> __name__ es "__main__". Caso contrario, tomarà el valor del nombre del file .py
    print("Hello Puto :v")