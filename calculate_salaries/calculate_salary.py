import re

def total_salary(path: str) -> tuple[int, float]:
  
    with open(path, "r", encoding = "utf-8") as file:
       total = 0
       length = 0

       for line in file:
           pattern = r"\n"
           replacement = ""
           modified_line = re.sub(pattern, replacement, line)
           salary = modified_line.split(',')
           total += int(salary[1])
           length +=1
              
    average = "{:.2f}".format(total / length)
    return total, average
    
path = "./salaries.txt"
total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")