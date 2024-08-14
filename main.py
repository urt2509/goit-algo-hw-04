# Task_1

from calculate_salaries.calculate_salary import total_salary


def main():
    path = "./salaries.txt"
    total, average = total_salary(path)
    print(
        f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
    )


if __name__ == "__main__":
    main()

# Task_2
