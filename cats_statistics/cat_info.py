def get_cats_info(path: str) -> list[dict]:
    try:
        with open(path, "r", encoding="utf-8") as file:

            cats_info = [
                dict(zip(["id", "name", "age"], line.strip().split(",")))
                for line in file
            ]

        return cats_info

    except FileNotFoundError:
        print(f"File {path} not found")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
