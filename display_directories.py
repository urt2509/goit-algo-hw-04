import sys
from pathlib import Path
from colorama import Fore


def find_directory(path, prefix: str = " "):

    items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    print(items)
    total_items = len(items)
    print(total_items)

    # for item in path.iterdir():

    #     if item.is_file():

    #         print(f"{Fore.BLUE} {item} {Fore.RESET}")
    #     else:

    #         find_directory(item)
    #         print(f"{Fore.GREEN} {item} {Fore.RESET}")


def display_directory():

    try:
        if len(sys.argv) < 2:
            print("Enter directory name")
        else:
            source_dir = " ".join(sys.argv[1:])

            path = Path(source_dir)
            if not path.exists():
                print(f"{path} is not a directory")
            else:
                find_directory(path)

    except IndexError:
        print("Enter directory name")


display_directory()
