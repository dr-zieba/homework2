if __name__ == "__main__":
    while True:
        sql_fetch_all_data("Customer")
        user_input = int(
            input(
                """What's your action?: 
        1: Add
        2: Subtract
        3: Exit
        """
            )
        )
        customer_id_input = int(input("Insert customer ID: "))
        amount_input = int(input("Insert amount to be added: "))
        if user_input == 1:
            add(customer_id_input, amount_input, table_name)
        elif user_input == 2:
            subtract(customer_id_input, amount_input, table_name)
        elif user_input == 3:
            exit()