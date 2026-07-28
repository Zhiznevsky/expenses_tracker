from __future__ import annotations
from typing import TYPE_CHECKING
import argparse
from datetime import datetime
from database import print_table_header, print_table_separator, print_entry

if TYPE_CHECKING:
    from database import Db

command_name = "list"

def is_from_month(entry, month):
    if entry["UpdatedAt"]:
        updated_dt_obj = datetime.strptime(entry["UpdatedAt"], "%a %b %d %H:%M:%S %Y")
        if updated_dt_obj.month == month:
            return True
        else:
            return False
    else:
        created_dt_obj = datetime.strptime(entry["CreatedAt"], "%a %b %d %H:%M:%S %Y")
        if created_dt_obj.month == month:
            return True
        else:
            return False

def is_from_category(entry, category_name):
    if entry["category_name"] == category_name:
        return True
    else:
        return False

def main(args: argparse.Namespace, db:Db) -> None:
    to_list = []
    no_args = False
    for entry_id, entry in db.items():
        if args.category_name:
            if is_from_category(entry, args.category_name):
                if args.month:
                    if is_from_month(entry, args.month):
                        to_list.append(entry_id)
                else:
                    if is_from_month(entry, datetime.now().month):
                        to_list.append(entry_id)
        elif args.month:
            if is_from_month(entry, args.month):
                to_list.append(entry_id)
        else:
            no_args = True
            break

    print_table_header()
    print_table_separator()
    if no_args:
        entries_by_categories = {category_name: [] for category_name in db.category_names}
        for entry_id, entry in db.items():
            entries_by_categories[entry["category_name"]].append(entry_id)
        
        for category_name, entry_ids in entries_by_categories.items():
            for entry_id in entry_ids:
                print_entry(db[entry_id])
                print_table_separator()
            
    else:
        for entry_id in to_list:
            print_entry(db[entry_id])
            print_table_separator()

def apply_subparser(subparsers: argparse._SubParsersAction):
    list_subparser = subparsers.add_parser(
            "list",
            help="List entries from database"
            )

    list_subparser.add_argument("--category_name",
                                type=str,
                                help="category of the expenses",
                                nargs="?",
                                default=None,
                                dest="category_name",
                                )
    list_subparser.add_argument("--month",
                                type=int,
                                help="month for which to show expenses",
                                choices=range(1,13),
                                default=None,
                                nargs="?",
                                dest="month",
                                )
