task = input("Enter your task: ")
priority = input("Enter the priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")

match priority | time:
    case "high":
        if time == "yes":
            print(f"Reminder: Your high-priority task '{task}' is time-bound. Please address it immediately.")
        else:
            print(f"Reminder: Your high-priority task '{task}' needs your attention soon.")
    case "medium":
        if time == "yes":
            print(f"Reminder: Your medium-priority task '{task}' is time-bound. Please plan to complete it soon.")
        else:
            print(f"Reminder: Your medium-priority task '{task}' is pending. Please schedule it accordingly.")
    case "low":
        if time == "yes":
            print(f"Reminder: Your low-priority task '{task}' is time-bound. Please consider completing it when possible.")
        else:
            print(f"Reminder: Your low-priority task '{task}' can be addressed at your convenience.")
    case _:
        print("Invalid priority or time-bound input. Please enter valid values.")
        