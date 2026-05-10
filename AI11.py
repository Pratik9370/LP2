def evaluate_employee(attendance, task_completion, quality, punctuality):

    print("\n--- Employee Performance Evaluation ---")

    # RULE 1
    if attendance >= 90 and task_completion >= 90 and quality >= 90 and punctuality >= 90:
        print("Performance: EXCELLENT")
        print("Reason: High attendance, task completion, quality and punctuality.")

    # RULE 2
    elif attendance >= 75 and task_completion >= 75 and quality >= 75:
        print("Performance: GOOD")
        print("Reason: Satisfactory overall performance.")

    # RULE 3
    elif attendance >= 60 and task_completion >= 60:
        print("Performance: AVERAGE")
        print("Reason: Needs improvement in quality and punctuality.")

    # RULE 4
    else:
        print("Performance: POOR")
        print("Reason: Low performance in multiple factors.")


# --------- INPUT SECTION ----------
attendance = int(input("Enter attendance percentage: "))
task_completion = int(input("Enter task completion percentage: "))
quality = int(input("Enter work quality percentage: "))
punctuality = int(input("Enter punctuality percentage: "))

# --------- CALL EXPERT SYSTEM ----------
evaluate_employee(attendance, task_completion, quality, punctuality)