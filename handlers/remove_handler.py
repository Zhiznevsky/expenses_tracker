from __future__ import annotations
from typing import TYPE_CHECKING
import argparse

if TYPE_CHECKING:
    from database import Db

command_name = "remove"

def main(args: argparse.Namespace, db:Db) -> None:
    db["category_names"].pop(args.category_name)
    db.save()

def apply_subparser(subparsers: argparse._SubParsersAction):
    create_subparser = subparsers.add_parser(
            "remove",
            help="Remove category" 
            )

    create_subparser.add_argument("category_name", type=str, help="category of the expenses")
    

