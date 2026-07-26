from __future__ import annotations
from typing import TYPE_CHECKING
import argparse

if TYPE_CHECKING:
    from database import Db

command_name = "delete"

def main(args: argparse.Namespace, db:Db) -> None:
    entry_id = str(args.id)
    del db[entry_id]
    db.save()

def apply_subparser(subparsers: argparse._SubParsersAction):
    delete_subparser = subparsers.add_parser(
            "delete",
            help="Delete an entry by its id"
            )

    delete_subparser.add_argument("id", type=int, help="id of the entry to delete")
    

