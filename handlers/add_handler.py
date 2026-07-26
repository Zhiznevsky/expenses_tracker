from __future__ import annotations
from typing import TYPE_CHECKING
import argparse

if TYPE_CHECKING:
    from database import Db


def main(args: argparse.Namespace, db:Db) -> None:
    pass


def apply_subparser(subparsers: argparse._SubParsersAction):
    add_subparser = subparsers.add_parser(
            "add",
            help="add expense to the database"
            )

    add_subparser.add_argument("category_name", type=str, help="category of the expense")
    add_subparser.add_argument("cost", type=float, help="how much money was spent")
    add_subparser.add_argument("description",
                               type=str,
                               nargs="?",
                               default="",
                               help="Optional. Description of expense"
                               )
    
