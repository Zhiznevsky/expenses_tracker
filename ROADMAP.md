# Expenses_tracker roadmap
## Expense data Structure inside json db
* id type=int
    * category_name type=str
    * cost type=float
    * description type=str
    * CreatedAt type=formatted datetime
    * UpdatedAt type=formatted datetime

'1': {
    'category_name': 'Taxi',
    'cost': '12.25',
    'description': "",
    'CreatedAt': 'Mon Jul 20 19:03:36 2026'
    'UpdatedAt': 'Mon Jul 20 19:13:36 2026'
}

## To-implement

### Main function
* initialize parser() --> argparse.Argparser object
#### Structure:
For all the commands there is optional parameter --db db_path
create category_name
    Description:
    creates top_level json element named category_name
    Variables:
    * category_name type=str
remove category_name
    Description:
    deletes json element named category_name. Ask user to remove all
    expenses history related to that category or move it to the
    "other" category.
    Variables:
    * category_name type=str
add category_name cost [ description="" ]
    Description:
    Create entry in the database of an expense
    Variables:
    * category_name type=str
    * cost type=int
    * description
delete id
    Description:
    Deletes entry associated with the provided id
    Variables:
    * id type=int
update id [--cost amount] [--description description] [--category category_name]
    Description: 
    Change information about entry associated with the provided id.
    Information you can change:
    cost 
    description
    category
    Variables:
    * id type=int
    * cost type=int
    * description type=str
    * category type=str
list --category category_name [--month month_num]
    Description:
    Shows all entries matching provided parameters:
    * --category "name of the category"
    * --month [1-12]
    
    Whene no month was provided, default behavior is to list all entries 
    from this month.

* parser.parse_arguments() --> Namespace

* db_logic.load_db(Namespace.path_var) --> Db object
Db is a subclass of UserDict with 2 additional attributes:
    path
    last_index
        get it at the initialization with next(reversed(self.data)). 
        Dont forget to convert to int
    __getitem__(key):
        convert the key to str for compatability with json

As a database use json file. The default location is ./expenses_tracker_db.json



* extract command that needs to run:
    command = Namespace.command_var

* execute the command providing remaning arguments 
    use global dict of commands to call that speciefic one:
        commands[command](Namespace)
    

### Commands:
Define global dict *commands*:
    name: function: Callable

create decorator to automatically add the function to the *commands*:
    add_command(function: Callable)
        strips the first word until _
        adds entry to the *commands* global dict:
            stripped_name: function

#### Functions of commands:
Names must start with the name of the parameter that associates with the
function followed by the _:
    add_task
    delete_task
    list_tasks
    ...

#### Structure
./
    main.py
    To add a command I need to: 
        create a parser
        create a function corresponding to that parser
            What does the function access?
                db. Is a dict. so no need to import json. Also no need to 
                know about the main. Just manipulate the data or extract it
                and return new db dictionary.
                global dict of commands???
                    NO, I'll import the function to the main module
                    and there add to the global dictionary of all the commands
        here we import handlers, db_logic, 
        implement main function and helpers used inside it
    handlers/
        add_handler.py
        delete_handler.py
        etc....
    database.py
                
                
