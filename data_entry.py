from datetime import datetime

CATEGORIES = {"I": "Income", "E": "Expense"}
def get_date(prompt, fill_default=False):
    date_str = input(prompt)
    # if user did not enter the date
    if fill_default and not date_str:
        return datetime.today().strftime("%d-%m-%Y")
    else:
        try:
            user_date_obj = datetime.strptime(date_str,"%d-%m-%Y")
            return datetime.strftime(user_date_obj,"%d-%m-%Y")
        except ValueError:
            prompt = "Invalid date input, enter in dd-mm-YYYY format: "
            return get_date(prompt, fill_default)
        
def get_amount(prompt):
    try:
        amount = float(input(prompt))
        if amount <= 0:
            raise ValueError("amount must be +ve")
        return amount
    except ValueError as e:
        print("invalid amount")
        print(e)
        return get_amount(prompt)

def get_category(prompt):
    try:
        category = input(prompt)
        if category.upper() in CATEGORIES: 
            return CATEGORIES[category.upper()]
        else:
            prompt = "invalid category entered"
            return get_category(prompt)
    except:
        print("invalid invalid invalid")

def get_description(prompt):
    description = input(prompt)
    return description