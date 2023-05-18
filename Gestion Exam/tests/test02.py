def ActionForm(actions):
    while True:
        print("(", end="")
        for key in actions:
            print(f"{key}: {actions[key][0]}", end=", ")
        print("\b\b)")

        choice = input("Action: ")
        if choice in actions:
            actions[choice][1]()
            break
        else:
            print("Invalid choice. Please try again.")

def action1(argument):
    print("Executing action1 with argument:", argument)

def action2(argument):
    print("Executing action2 with argument:", argument)

def action3(argument):
    print("Executing action3 with argument:", argument)

# Call ActionForm with the desired actions
ActionForm({'l': ('Action 1', lambda: action1('something interesting')),
            'k': ('Action 2', lambda: action2('something else')),
            'lk': ('Action 1&2', lambda: action1('something interesting') or action2('something else')),
            'lkj': ('Action 1&2&3', lambda: action1('something interesting') or action2('something else') or action3('something more'))})
