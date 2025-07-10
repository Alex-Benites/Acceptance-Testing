Feature: To-Do List Manager
  As a user
  I want to manage my tasks
  So that I can keep track of what I need to do

  Scenario: Adding a task
    Given the To-Do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: Listing tasks
    Given the To-Do list contains tasks
    When the user requests to view all tasks
    Then all tasks should be displayed

  Scenario: Marking a task as complete
    Given the To-Do list contains the task "Buy groceries"
    When the user marks "Buy groceries" as complete
    Then "Buy groceries" should be marked as complete

  Scenario: Removing a task
    Given the To-Do list contains the task "Buy groceries"
    When the user removes the task "Buy groceries"
    Then the To-Do list should not contain "Buy groceries"

  # Escenarios adicionales (2 más como se solicita)
  Scenario: Adding a task to non-empty list
    Given the To-Do list contains the task "Walk the dog"
    When the user adds a task "Buy groceries"
    Then the to-do list should contain both "Walk the dog" and "Buy groceries"

  Scenario: Attempting to mark non-existent task as complete
    Given the To-Do list is empty
    When the user attempts to mark "Buy groceries" as complete
    Then an error message should be displayed
    And the To-Do list should remain empty