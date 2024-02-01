from pathlib import Path

def get_cats_info(path):
    try:
        with open(path, 'r', encoding=None) as file:
            lines = file.readlines()
        for line in lines:
            elemments = line.split(',')
            #print(elemments)
            dict_cats = {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": 3,
                        "id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": 1,
                        "id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": 2,
                        "id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": 12,
                        "id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": 5,}
            return dict_cats
        dict_cats = cats_info
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return None

cats_info = get_cats_info("cats_file.txt")
print(cats_info)
