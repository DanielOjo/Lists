#Daniel Ogunlana
#14/01/2015
#Programming Language Task 2

def calculate_total_price(products):
    for product in products:
        product[1] = product[1] + product[1] * VAT
    return products

def add_new_products(products):
    finished = False
    while not finished:
        product = input("please enter product name: ")
        if len(product) > 0:
            price = input("please enter product price: ")
            products.append([product,price])
        else:
            finished = True
    return products

def display_prices(products):
    print("{0:<15} {1:<15}".format("Name","Price (inc. VAT)"))
    for product in products:
        print("{0:<15} £{1:<15.2f}".format(product[0],product[1]))

#main program
VAT = 0.2
items = [["laptop",318],["mp3 player",52],["oled television",1144]]
items = add_new_products(items)
items = calculate_total_price(items)
display_prices(items)
