def total_salary(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()

        total_salary = 0
        developer_count = 0
        for line in lines:
            elements = line.split(',')  #розділ рядка за допомогою коми
            salary_index = 1
            try:
                total_salary += int(elements[salary_index])
                developer_count += 1
            except Exception:
                continue 

        average_salary = int(total_salary/developer_count if developer_count > 0 else 0)
        return total_salary, average_salary
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return None
   
total_salary, average_salary = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {average_salary}")
