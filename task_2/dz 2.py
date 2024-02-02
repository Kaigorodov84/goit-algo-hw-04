def get_cats_info(path):
    cats_list = [] #створюємо список 

    try:
        with open(path, 'r') as file: # відкриваємо та читаєм файл
            lines = file.readlines()

            for line in lines:
                cat_info = line.strip().split(',') # розділяємо за комою
                cat_dict = {
                    'id': cat_info[0],
                    'name': cat_info[1],
                    'age': int(cat_info[2])
                }                                 # утворюємо словник з ключами 
                cats_list.append(cat_dict)        #

    except FileNotFoundError:                     # обробка винятків
        print(f"File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return cats_list

# Приклад використання функції:
cats_info = get_cats_info('Task_2/cats_file.txt')
print(cats_info)

   