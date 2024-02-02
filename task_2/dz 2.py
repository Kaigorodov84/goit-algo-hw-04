def get_cats_info(path):
    cats_list = []

    try:
        with open(path, 'r') as file:
            lines = file.readlines()

            for line in lines:
                cat_info = line.strip().split(',')
                cat_dict = {
                    'id': cat_info[0],
                    'name': cat_info[1],
                    'age': int(cat_info[2])
                }
                cats_list.append(cat_dict)

    except FileNotFoundError:
        print(f"File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return cats_list

# Приклад використання функції:
cats_info = get_cats_info('cats_file.txt')
print(cats_info)

   