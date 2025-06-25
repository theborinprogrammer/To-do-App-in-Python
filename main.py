def main() :
    print("Welcome to To-Do List App\n")
    prompt3 = "What would you like to do?\nType:  "
    prompt2 = "What would you like to add?\nEnter a To-Do:  "
    todos = []

    while True:
        prompt = print("""
    Actions        |     Type
________________________________
Adding a To-Do     |     Add
Removing a To-Do   |     Remove
Clear the App      |     Clear
Complete a To-Do   |     Complete
Showing the List   |     View
Exiting the App    |     End
        """)
        
        todo1 = input(prompt3).strip().casefold()
        if todo1 == "add":
            whatdo = input(prompt2).capitalize()
            print(f"Okay! we have added '{whatdo}' to your list.")
            todos.append(whatdo)
            input("Press Enter to continue...")
            
        elif todo1 == "clear":
            clear(todos)
            input("Press Enter to continue...")
        
        elif todo1 == "complete":
            complete(todos)
            input("Press Enter to continue...")
                
        elif todo1 == "remove":
                view(todos)
                while True:    
                    try:
                        remove = int(input("Choose which one to remove from the list:  Please type to index of the To-Do:  "))
                        break
                    except ValueError:
                        print("Please enter a valid number.")
                        continue
                while True:
                    if 1 <= remove <= len(todos):
                        inputConfirmation = input(f"Are you sure you want to remove '{todos[remove - 1]}' from your list? (yes/no):  ").strip().casefold()
                        if inputConfirmation == "yes" or inputConfirmation == "y":
                            print(f"Okay! we have removed '{todos[remove - 1]}' from your list.")
                            todos.pop(remove - 1)
                            break
                        elif inputConfirmation == "no" or inputConfirmation == "n":
                            print("Okay! we have not removed anything from your list.")
                            break
                        else :
                            print("Please enter a valid answer.")
                            continue
                input("Press Enter to continue...")
            
        elif todo1 == "view":
            view(todos)
            input("Press Enter to continue...")
            
        elif todo1 in ("end", "exit"):
            print("Thanks for using our app. See you soon!")
            print("Exiting the app...")
            break 
    
        else :
            print("Please choose any of the given choices")
            continue
        
     
        
        
def view(todos):
    if not todos:
            print("Your To-Do List is empty.")
    else :
        print(f"Your To-do list containts {len(todos)} things.\nYour To-do List:", end="\n")
        for i in range(len(todos)): 
            print(f"{i+1}.{(todos[i])}")
            
            
            
def complete(todos):
    if not todos:
        print("Your To-Do List is empty.")
        return
    view(todos)
    while True:
        try:
            idx = int(input("Choose which one to complete from the list (enter the index): "))
            if 1 <= idx <= len(todos):
                confirm = input(f"Are you sure you want to mark '{todos[idx-1]}' as completed? (yes/no): ").strip().casefold()
                if confirm in ("yes", "y"):
                   
                    if not todos[idx-1].endswith(" ✔️"):
                        todos[idx-1] += " ✔️"
                        print(f"Marked '{todos[idx-1]}' as completed.")
                        view(todos)  
                    else:
                        print("This to-do is already marked as completed.")
                    break
                elif confirm in ("no", "n"):
                    print("Okay! No changes made.")
                    break
                else:
                    print("Please enter a valid answer.")
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")


def clear(todos):
    if not todos: 
        print("Your list is Empty.")
    else :
        print("Okay! Clearing the list...")
        todos.clear()
        print("Your list has been cleared.")
        

              
        
main()
