import os
import datetime

def get_paths(script_dirpath):

    tasks_dirpath = os.path.split(script_dirpath)[0]

    parameters_filepath     = os.path.join(tasks_dirpath, 'cache.yaml')
    current_tasks_filepath  = os.path.join(tasks_dirpath, 'today.md')
    planned_tasks_filepath  = os.path.join(tasks_dirpath, 'plans.md')    
    
    return {
        'parameters_filepath':      parameters_filepath,
        'tasks_dirpath':            tasks_dirpath,
        'current_tasks_filepath':   current_tasks_filepath,
        'planned_tasks_filepath':   planned_tasks_filepath,
    }

def get_current_date():

    current_date = datetime.datetime.today()

    return current_date.replace(hour = 0, minute = 0, second = 0, microsecond = 0)