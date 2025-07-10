from behave import given, when, then
import sys
import os

# Agregar el directorio padre al path para importar el módulo principal
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Variable global para simular la lista de tareas
to_do_list = []
error_message = ""

@given('the To-Do list is empty')
def step_given_empty_list(context):
    global to_do_list
    to_do_list = []

@given('the To-Do list contains tasks')
def step_given_list_with_tasks(context):
    global to_do_list
    to_do_list = ["Example task 1", "Example task 2"]

@given('the To-Do list contains the task "{task}"')
def step_given_list_contains_task(context, task):
    global to_do_list
    to_do_list = [task]

@when('the user adds a task "{task}"')
def step_when_add_task(context, task):
    global to_do_list
    to_do_list.append(task)

@when('the user requests to view all tasks')
def step_when_view_tasks(context):
    # En una implementación real, esto llamaría a la función de listar tareas
    context.displayed_tasks = to_do_list.copy()

@when('the user marks "{task}" as complete')
def step_when_mark_complete(context, task):
    global to_do_list
    if task in to_do_list:
        # En una implementación real, marcaríamos la tarea como completada
        # Por simplicidad, la movemos a una lista de completadas
        if not hasattr(context, 'completed_tasks'):
            context.completed_tasks = []
        context.completed_tasks.append(task)

@when('the user removes the task "{task}"')
def step_when_remove_task(context, task):
    global to_do_list
    if task in to_do_list:
        to_do_list.remove(task)

@when('the user attempts to mark "{task}" as complete')
def step_when_attempt_mark_complete(context, task):
    global to_do_list, error_message
    if task not in to_do_list:
        error_message = f"Task '{task}' not found in the to-do list"

@then('the to-do list should contain "{task}"')
def step_then_list_contains_task(context, task):
    assert task in to_do_list, f"Task '{task}' not found in the to-do list"

@then('all tasks should be displayed')
def step_then_all_tasks_displayed(context):
    assert hasattr(context, 'displayed_tasks'), "No tasks were displayed"
    assert len(context.displayed_tasks) > 0, "No tasks were found to display"

@then('"{task}" should be marked as complete')
def step_then_task_marked_complete(context, task):
    assert hasattr(context, 'completed_tasks'), "No completed tasks found"
    assert task in context.completed_tasks, f"Task '{task}' is not marked as complete"

@then('the To-Do list should not contain "{task}"')
def step_then_list_not_contains_task(context, task):
    assert task not in to_do_list, f"Task '{task}' should not be in the to-do list"

@then('the to-do list should contain both "{task1}" and "{task2}"')
def step_then_list_contains_both_tasks(context, task1, task2):
    assert task1 in to_do_list, f"Task '{task1}' not found in the to-do list"
    assert task2 in to_do_list, f"Task '{task2}' not found in the to-do list"

@then('an error message should be displayed')
def step_then_error_message_displayed(context):
    global error_message
    assert error_message != "", "No error message was displayed"

@then('the To-Do list should remain empty')
def step_then_list_remains_empty(context):
    assert len(to_do_list) == 0, "The to-do list should be empty"