task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task but not a high time bound so consider completing it.")
    
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task but has a time bound so consider completing it as soon as possible!")
        else:
            print(f"Reminder: '{task}' is a medium priority task but not a high time bound attach to it")
        
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task but has a time bound so consider doing it some time soon")
        else: 
            print(f"Note: '{task}' is a low priority task and not has no time bound attach to it. consider completing it when you're free")

