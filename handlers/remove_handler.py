from __future__ import annotations
from typing import TYPE_CHECKING
import argparse

if TYPE_CHECKING:
    from database import Db

command_name = "remove"

def main(args: argparse.Namespace, db:Db) -> None:
    inp = None
    while inp not in list("yn"):
        inp = input("All entries associated with this category will be removed. Procied? y/n: ")
    if inp == "y":
        entry_ids_to_delete = []
        for entry_id, entry_data in db.items():
            if entry_data["category_name"] == args.category_name:
                entry_ids_to_delete.append(entry_id)
        for entry_id in entry_ids_to_delete:
            del db[entry_id]
        db.category_names.remove(args.category_name)
        db.save()
    elif inp == "n":
        print(f"Category {args.category_name} is not deleted")


def apply_subparser(subparsers: argparse._SubParsersAction):
    create_subparser = subparsers.add_parser(
            "remove",
            help="Remove category" 
            )

    create_subparser.add_argument("category_name", type=str, help="category of the expenses")
    

