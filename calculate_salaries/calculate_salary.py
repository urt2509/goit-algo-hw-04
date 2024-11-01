def total_salary(path: str) -> tuple[int, float]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            total = 0
            length = 0
            for line in file:
                total += float(line.strip().split(",")[1])
                length += 1

            try:
                average = "{:.2f}".format(total / length)
            except ZeroDivisionError as e:
                print("Error: division by zero")
                return None
        if total:
            return "{:.2f}".format(total), average
        else:
            print("No salaries are available")
            return "{:.2f}".format(total), average

    except FileNotFoundError:
        print(f"File {path} not found")
        return None
