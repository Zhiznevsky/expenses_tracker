from collections import UserDict
from pathlib import Path
import json
import sys
from typing import TypedDict

category_name_col_width = 15
cost_col_width = 10
descripton_col_width = 50
created_at_col_width = 27
updated_at_col_width = 27


class Entry(TypedDict):
    category_name: str
    cost: float
    description: str
    CreatedAt: str
    UpdatedAt: str


class Db(UserDict):
    data: dict[str, Entry] 


    def __init__(self, *args, path: Path, last_id: int = 0, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = path

        self.category_names = self.data.pop("category_names", [])
        if self.data:
            try:
                self.last_id = int(next(reversed(self.data.keys())))
            except ValueError as err:
                self.corruption_handler(err)
        else:
            self.last_id = last_id

    def save(self) -> None:
        try:
            with self.path.open("w") as file:
                self.data["category_names"] = self.category_names
                json.dump(self.data, file, indent=2)
        except FileNotFoundError:
            print(f"Database file which was open for this process was not\
                    found. Exiting...")
            sys.exit()

    def delete(self) -> None:
        self.path.unlink(missing_ok=True)

    def corruption_handler(self, error):
        i = input(f"Corrupted database file. Manually fix the issue\
        or delete database file.\n{error}\n\n\
                Do you want to delete database file? y/n:")
        if i == "y":
            self.delete()
            print("Database file deleted. Try running the programm again.")
        elif i == "n":
            print("Exiting without deleting the file...")
            sys.exit()



def load_db(path: Path) -> Db:
    try:
        with path.open() as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    db = Db(data, path=path)
    return db

def print_table_header() -> None:
    print(f"{'Category':^{category_name_col_width}}|{'Cost':^{cost_col_width}}|{'Description':^{descripton_col_width}}|{'Created':^{created_at_col_width}}|{'Updated':^{updated_at_col_width}}")

def print_table_separator() -> None:
    print(f"{'-' * category_name_col_width}|{'-' * cost_col_width}|{'-' * descripton_col_width}|{'-' * created_at_col_width}|{'-' * updated_at_col_width}")

def print_entry(entry: Entry) -> None:
    print(f"{entry['category_name']:^{category_name_col_width}}|{entry['cost']:^{cost_col_width}}|{entry['description']:^{descripton_col_width}}|{entry['CreatedAt']:^{created_at_col_width}}|{entry['UpdatedAt']:^{updated_at_col_width}}")

