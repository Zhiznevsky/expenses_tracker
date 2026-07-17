# Expenses_tracker roadmap

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

* load_db(Namespace.path_var) --> json object. Check if it is just a python dict
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
