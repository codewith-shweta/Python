def information(username , amount , due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount: .2f} is due: {due_date} ")

information("Shivam", 200.45, "01/01")