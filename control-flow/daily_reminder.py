Task = input("input a task description: ")
Priority = input("Priority (high/medium/low): ").lower()
Time_Bound = input("Is it time-bound? (yes/no): ").lower()

match Priority:
    case "high":
        reminder = (f"{Task} is a high priority task")
    case "medium":
        reminder = (f"{Task} is a medium priority task")
    case "low":
        reminder = (f"{Task} is a low priority task")
    case _:
        reminder = (f"{Task} has an unknown priority")

if Time_Bound == "yes":
    reminder += (", that requres immediate attention today!")
else:
    reminder += (", consider completing it when you're free.")

print(f"Reminder: {reminder}")

