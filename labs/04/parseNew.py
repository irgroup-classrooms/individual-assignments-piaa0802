import re 


def main():
    
    # Read the CSV file with the product orders
    with open('C:/Uni/DIS08/individual-assignments-piaa0802/assignments/04/csv/orders.csv') as f_in:
        text = f_in.read()

    # Define the regular expressions
    regex = r'\d+'
    order_number_regex = r'Order #(\d+)' #Task 1
    product_names_regex = r'Product: (\w+)' #Task 2
    price_regex = r'Price: (\$\d+\.\d{2}))' #Task 3
    order_dates_regex = r'Date: (\d{4}-\d{2}-\d{2})' #Task 4

    # Match the regex with the text
    orders = re.findall(regex, text)
    order_numbers = re.findall(order_number_regex, text) #Task 1
    product_names = re.findall(product_names_regex, text) #Task 2
    prices = re.findall(price_regex, text) #Task 3
    order_dates = re.findall(order_dates_regex, text) #Task 4

    # Print the results
    print(orders)
    print(order_numbers) #Task 1
    print(product_names) #Task 2
    print(prices) #Task 3
    print(order_dates) #Task 4
    

if __name__ == '__main__':
    main()

