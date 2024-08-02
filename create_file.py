import os
import sys
import datetime
from typing import List, Optional


def create_directories(path_parts: List[str]) -> None:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Created directories: {path}")


def create_file(file_name: str, dir_path: Optional[List[str]] = None) -> None:
    if dir_path:
        full_path = os.path.join(*dir_path, file_name)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
    else:
        full_path = file_name

    file_exists = os.path.exists(full_path)

    with open(full_path, "a") as f:
        if not file_exists:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp}\n")

        line_count = 1
        while True:
            content_line = input(f"Enter content line {line_count}: ")
            if content_line.lower() == "stop":
                break
            f.write(f"{line_count} {content_line}\n")
            line_count += 1

    print(f"Created/updated file: {full_path}")


def main() -> None:
    args = sys.argv[1:]
    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            dir_path = args[d_index + 1:f_index]
            file_name = args[f_index + 1]
            create_file(file_name, dir_path)
        else:
            dir_path = args[d_index + 1:]
            create_directories(dir_path)
    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        create_file(file_name)
    else:
        print("Invalid arguments. Use -d for directories and -f for file.")


if __name__ == "__main__":
    main()
