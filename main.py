import pandas as pd
import csv
from datetime import datetime
import data_entry as user_input

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"
    @classmethod
    def initialize_csv(cls):
        try:
            csv = pd.read_csv(cls.CSV_FILE)
            print(csv)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["date", "amount", "category", "description"])
            df.to_csv(cls.CSV_FILE, index=False)
            print("moved file to data frame")
    
    @classmethod
    def add_entry(cls, date, amount, category, description):

        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }

        with open(cls.CSV_FILE, "a", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
            print("new entry added")


    @classmethod
    def view_transactions(cls,start_date,end_date):

        CSV.FORMAT = "%d-%m-%Y"
        df = pd.read_csv(CSV.CSV_FILE)
        # print("BEFORE", df)
        # convert the date column to a datetime object
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        # print("AFTER", df)

        # set up a filter for the data frame and extract required rows
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transactions found")
        else:
            print(f"Transactions between {start_date} and {end_date} are:")
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))
        
        print("\nSummary")
        total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
        print(f"Total Income: ${total_income: .2f}:")

        total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
        print(f"Total Expense: ${total_expense: .2f}")

    @classmethod
    def get_user_choice(cls):
        choice = input("\nEnter your options (1-3):")

        if choice == "1":
            CSV.initialize_csv()
            valid_date = user_input.get_date("enter the date: ", fill_default=True)
            amount = user_input.get_amount("enter the amount: ")
            category = user_input.get_category("enter the transaction category (I/E) - income or expense: ")
            description = user_input.get_description("enter the description: ")
            CSV.add_entry(valid_date, amount,category,description)
        
        elif choice == "2":
            prompt = "enter the start date(dd-mm-yyyy):"
            start_date = user_input.get_date(prompt)
            prompt = "enter the end date(dd-mm-yyyy):"
            end_date = user_input.get_date(prompt)
            CSV.view_transactions(start_date,end_date)

        elif choice == "3":
            print("Exiting...")

        elif choice == "4":
            CSV.initialize_csv()
        else:
            print("Not a valid option..")
            return CSV.get_user_choice()

def main():
    print("\n1. Add transactions")
    print("2. View transactions")
    print("3. Exit")

    CSV.get_user_choice()

if __name__ == "__main__":
    main()
