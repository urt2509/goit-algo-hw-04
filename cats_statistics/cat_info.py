import re


def get_cats_info(path: str) -> list[dict]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats_info = list()

            for line in file:
                pattern = r"\n"
                replacement = ""
                modified_line = re.sub(pattern, replacement, line)
                cat_list = modified_line.split(",")

                cat_dictionary = {
                    "id": cat_list[0],
                    "name": cat_list[1],
                    "age": cat_list[2],
                }
                cats_info.append(cat_dictionary)

            return cats_info
    except Exception as e:
        raise e
