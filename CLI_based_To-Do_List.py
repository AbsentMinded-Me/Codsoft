import sqlite3
#connect to SQLite database
conn = sqlite3.connect('ToDoList.db')
cursor = conn.cursor()

#to create a table for tasks with specified name
def create_table(table_name):
    # Create a table for tasks with the specified name and a due_date column
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        due_date TEXT,  -- Store due date as text (ISO format recommended)
        status TEXT NOT NULL DEFAULT 'Pending'
    )
    ''')
    conn.commit()
    print(f"Table '{table_name}' created successfully!")

#to add the entries in the table
def add_task(table_name, title, description, due_date):
    cursor.execute(f"INSERT INTO {table_name} (TITLE, DESCRIPTION, DUE_DATE) VALUES (?,?,?)", (title, description, due_date))
    conn.commit()
    print("Task added successfully!")

#to view the table 
def view_tasks(table_name):
    cursor.execute(f'SELECT * FROM {table_name}')
    tasks = cursor.fetchall()
    for task in tasks:
        print(f"ID: {task[0]}, Title: {task[1]}, Description: {task[2]}, Due Date: {task[3]}, Status: {task[4]}")

#to update the task
def update_task(table_name, task_id, status):
    cursor.execute(f'UPDATE {table_name} SET status = ? WHERE id = ?', (status, task_id))
    conn.commit()
    print("Task updated successfully!")

#to delete the task
def delete_task(table_name, task_id):
    cursor.execute(f'DELETE FROM {table_name} WHERE id = ?', (task_id,))
    conn.commit()
    print("Task deleted successfully!")

#Giving options on the console
def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Create Table")
        print("2. Add Task")
        print("3. View Tasks")
        print("4. Update Task Status")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            table_name = input("Enter table name: ")
            create_table(table_name)
        elif choice == '2':
            table_name = input("Enter existed table name to add task: ")
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")  # Prompt for due date
            add_task(table_name, title, description, due_date)
        elif choice == '3':
            table_name = input("Enter existed table name to view tasks: ")
            view_tasks(table_name)
        elif choice == '4':
            table_name = input("Enter existed table name to update task: ")
            task_id = int(input("Enter task ID to update: "))
            status = input("Enter new status (Pending/Completed): ")
            update_task(table_name, task_id, status)
        elif choice == '5':
            table_name = input("Enter existed table name to delete task: ")
            task_id = int(input("Enter task ID to delete: "))
            delete_task(table_name, task_id)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
# Close the database connection
conn.close()
