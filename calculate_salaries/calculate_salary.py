import re


def total_salary(path: str) -> tuple[int, float]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            total = 0
            length = 0

            for line in file:
                pattern = r"\n"
                replacement = ""
                modified_line = re.sub(pattern, replacement, line)
                salary = modified_line.split(",")
                total += int(salary[1])
                length += 1
            average = "{:.2f}".format(total / length)
        if total:
            return total, average
        else:
            print("No salaries are available")

    except FileNotFoundError:
        print(f"File {path} not found")
        return None
