# To-Do List App (Python Terminal Version)

## Overview

This is a basic console-based To-Do List application written in Python.
The app runs in a continuous loop, allowing users to manage personal to-do items through text commands.
Unlike the C version, it **does not support user accounts or file storage** (yet).
This is more of a prototype — made for quick tests and beginner-level practice with Python control flows, input handling, and string operations.

> ⚠️ Note: Tasks are only stored in memory. Once you exit, your list vanishes like your motivation on Monday morning.

---

## Features

* **Add Task**: Input a task, and it gets added to the list.
* **Remove Task**: Choose and remove a task by index.
* **Complete Task**: Mark a task as completed (adds a ✔️).
* **View Tasks**: Shows all current tasks in the list.
* **Clear List**: Removes all tasks from the list.
* **Exit App**: Ends the session with a farewell message.

---

## How It Works

1. **Startup**

   * The program greets the user and enters an infinite loop.
2. **Main Menu**

   * A list of available actions is displayed:

     ```
     Actions        |     Type
     ________________________________
     Adding a To-Do     |     Add
     Removing a To-Do   |     Remove
     Clear the App      |     Clear
     Complete a To-Do   |     Complete
     Showing the List   |     View
     Exiting the App    |     End
     ```
3. **User Input**

   * Based on the command typed (`add`, `remove`, `complete`, etc.), the corresponding block of logic runs.
   * Inputs are case-insensitive.
4. **Data Handling**

   * Tasks are stored in a simple Python list (`todos`).
   * Each task is a string. Completed tasks are suffixed with a ✔️.
5. **Exit**

   * Choosing `end` or `exit` cleanly breaks the loop and prints a goodbye message.

---

## Example Usage

```
Welcome to To-Do List App

Actions        |     Type
________________________________
Adding a To-Do     |     Add
Removing a To-Do   |     Remove
Clear the App      |     Clear
Complete a To-Do   |     Complete
Showing the List   |     View
Exiting the App    |     End

Type: add
Enter a To-Do: Buy groceries
Okay! we have added 'Buy groceries' to your list.

Type: view
Your To-do list contains 1 things.
1. Buy groceries

Type: complete
Choose which one to complete from the list (enter the index): 1
Marked 'Buy groceries ✔️' as completed.
```

---

## Requirements

* Python 3.x
* A keyboard (yes, that’s all)

---

## Limitations

* ❌ No persistent storage — nothing is saved to file.
* ❌ No user accounts — one session = one list.
* ❌ No input validation beyond `try/except` for integers.

But hey, it works. That’s the first step.

---

## Setup

To run the app:

```bash
python3 todo.py
```

Or just double-click the file (if your system has Python installed correctly).

---

## Future Plans (Maybe?)

    🗂️ File-Based Storage
    Save tasks to a JSON file and load them automatically on startup to maintain persistence across sessions.

    👥 Multi-User Support
    Let users log in with a username. Each user will have a separate task file (e.g., john_tasks.json), allowing personalized task management.

    📌 Task Priority
    Add a priority field (High/Medium/Low) to tasks. Tasks can later be filtered or sorted by priority.

    🕓 Deadlines for Tasks
    Include optional due dates for tasks. Tasks will display whether they are pending, due soon, or overdue based on the current date.

    ✏️ Task Editing
    Add functionality to edit an existing task’s description, priority, or deadline.

    🔍 Filtering and Sorting
    Enable users to filter tasks by status (pending/completed), priority, or due date — and optionally sort the list.


---

## Contribution

Feel free to fork this and improve it.
Want to add user authentication? Or maybe make it save tasks? Go ahead and send a pull request.

---

## Credits

Built for fun and practice by [Sourov Saha](https://github.com/theborinprogrammer).
Inspired by the good ol' C version of mine— this time with Python’s flex.
