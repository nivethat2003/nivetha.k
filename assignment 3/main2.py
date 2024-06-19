import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from items import items

def get_customer_details():
    """ Get customer details and products """
    try:
        print("-----------------------------------------------------------------\n")
        print("*..*..*..*..*  WELCOME TO SUPERMARKET  *..*..*..*..*\n")
        print("-----------------------------------------------------------\n")
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        email = input("Enter the email id: ")
        initial_balance = float(input("Enter the initial balance: "))
        products = input("Enter the products (comma separated): ").split(',')
        print("---------------------------------------------------")
        products = [product.strip() for product in products]
        return name, phone, email, initial_balance, products
    except Exception as e:
        print(f"Error getting customer details: {e}")
        return None, None, None, 0, []

def calculate_bill(products):
    """ Calculate the bill for each product """
    bill = {}
    total_amount = 0
    for product in products:
        if product in items:
            bill[product] = items[product]
            total_amount += items[product]
        else:
            print(f"Product {product} not found.")
    return bill, total_amount

def generate_bill_details(name, phone, email, initial_balance, bill, total_amount):
    """ Generate bill details as a string """
    try:
        remaining_balance = initial_balance - total_amount
        print("--------------------------------------------------------------------")
        bill_details = f"               ***NIVETHA SUPERMARKET***"
        print("---------------------------------------------------------------------")
        bill_details += f"Bill for {name}\n"
        bill_details += f"Phone: {phone}\n"
        bill_details += f"Email: {email}\n"
        bill_details += f"Date: {datetime.now()}\n"
        bill_details += "\nItems:\n"
        for product, price in bill.items():
            bill_details += f"{product}: ${price}\n"
        bill_details += f"\nTotal Amount: ${total_amount}\n"
        bill_details += f"Initial Balance: ${initial_balance}\n"
        bill_details += f"Remaining Balance: ${remaining_balance}\n"
        return bill_details, remaining_balance
    except Exception as e:
        print(f"Error generating bill details: {e}")
        return "", 0

def send_email(receiver_email, bill_details):
    """ Send the bill details via email """
    sender_email = "225027005@sastra.ac.in"
    sender_password = "nivethaakalya1406200331082004"
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Your Bill"
    message.attach(MIMEText(bill_details, "plain"))

    try:
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    name, phone, email, initial_balance, products = get_customer_details()
    if name and email:
        bill, total_amount = calculate_bill(products)
        bill_details, remaining_balance = generate_bill_details(name, phone, email, initial_balance, bill, total_amount)
        if bill_details:
            print(bill_details)
            send_email(email, bill_details)
            print(f"Remaining Balance: ${remaining_balance}")
            print("***********THANK YOU FOR VISTING NIVETHA SUPERMARKET************\n")
            print("-------------------------------------------------------------------------")
        else:
            print("Failed to generate bill details.")
    else:
        print("Invalid customer details.")
main()        
