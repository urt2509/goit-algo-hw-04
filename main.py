from calculate_salaries.calculate_salary import total_salary
from cats_statistics.cat_info import get_cats_info
from display_directories import display_directory
from python_bot.bot import main as bot_command


# Function for Task_1
def calculate_salaries_statistics():
    path = "./salaries.txt"
    total, average = total_salary(path)
    print(
        f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
    )


# Function for Task_2
def create_cat_dictionary():
    path = "./cats.txt"
    cats_info = get_cats_info(path)
    print(cats_info)


# Function for Task_3

if __name__ == "__main__":
    # calculate_salaries_statistics()  # Run Task1

    # create_cat_dictionary()  # Run Task2

    # display_directory()

    bot_command()  # Run Task4
