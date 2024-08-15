import sys
from pathlib import Path
from colorama import Fore


def display_directory():
    try:
        if len(sys.argv) < 2:
            print("Enter directory name")
        else:
            source_dir = " ".join(sys.argv[1:])

            path = Path(source_dir)

            if not path.is_dir():
                print(f"{path} is not a directory")
            for item in path.iterdir():
                sub_dir = Path(item)

                if sub_dir.is_dir():
                    print(f"{Fore.GREEN} {item}")
                elif sub_dir.exists():
                    print(f"{Fore.BLUE} {item}")

    except IndexError:
        print("Enter directory name")


display_directory()
