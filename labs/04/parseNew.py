import re 
from collections import Counter

def main():
    
    # Read the CSV file with the product orders
    with open('C:/Uni/DIS08/individual-assignments-piaa0802/assignments/04/csv/orders.csv') as f_in:
        text = f_in.read()

    # Define the regular expressions
    regex = r'\d+'
    order_number_regex = r'Order #(\d+)' #Task 1
    product_names_regex = r'Product: (\w+)' #Task 2
    price_regex = r'Price: (\$\d+\.\d{2})' #Task 3
    order_dates_regex = r'Date: (\d{4}-\d{2}-\d{2})' #Task 4

    # Match the regex with the text
    orders = re.findall(regex, text)
    order_numbers = re.findall(order_number_regex, text) #Task 1
    product_names = re.findall(product_names_regex, text) #Task 2
    prices = re.findall(price_regex, text) #Task 3
    order_dates = re.findall(order_dates_regex, text) #Task 4

    products_over_500 = [] #Task5
    for i in prices:
        price = float(i.replace('$', ''))
        if price > 500:
            expensive_product = price
            products_over_500.append(expensive_product)
    
    order_dates_format = [] #Task 6
    for i in order_dates:
         new_date = re.sub (r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', i)
         order_dates_format.append(new_date)

    products_over_6char = [] #Task 7
    for i in product_names:
        if len(i) > 6:
            products_over_6char.append(i)
    
    products_count = Counter(product_names) #Task 8

    prices_ending_99 = re.findall(r'Product: [A-Za-z]+, Price: \$\d+\.99',text) #Task 9
    
    cheapest_product = min(prices) #Task 10
    cheapest_product = float(cheapest_product.replace('$', ''))

    # Print the results
    print(orders)
    print("All order numbers: ", order_numbers) #Task 1
    print("All product names: ", product_names) #Task 2
    print("All prices: ", prices) #Task 3
    print("All order dates: ", order_dates) #Task 4
    print("All order products priced over $500: ", products_over_500) #Task 5
    print("All order numbers: ", order_dates_format) #Task 6
    print("All products that have more than 6 characters: ", products_over_6char) #Task 7
    print("The occurance of each product in the text: ", products_count) #Task 8
    print("All orders with prices ending in .99: ", prices_ending_99) #Task 9
    print("The cheapest product: ", cheapest_product) #Task10
    

if __name__ == '__main__':
    main()

