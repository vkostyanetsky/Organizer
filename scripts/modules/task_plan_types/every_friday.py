# каждая пятница
# каждая пт
# каждую пятницу
# каждую пт
#
# каждая пятница, начиная с 29.12.1983
# каждая пятница с 29.12.1983

import re
import modules.conditions as conditions

def is_task_current(task, date):
   
    def is_type_correct():

        pattern = '(каждая пятница|каждая пт|каждую пятницу|каждую пт).*'
        match   = re.match(pattern, task['recurrence'])

        return match != None

    def is_date_correct():

        is_friday = date.strftime('%a') == 'Fri'

        return is_friday and conditions.is_task_started(task, date)

    result = None
    
    if is_type_correct():
        result = is_date_correct()
    
    return result