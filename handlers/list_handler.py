from __future__ import annotations
from typing import TYPE_CHECKING
import argparse

if TYPE_CHECKING:
    from database import Db

command_name = "list"

def main(args: argparse.Namespace, db:Db) -> None:
    pass

def apply_subparser(subparsers: argparse._SubParsersAction):
    list_subparser = subparsers.add_parser(
            "list",
            help="List entries from database"
            )

    list_subparser.add_argument("category_name", type=str, help="category of the expenses")
    
