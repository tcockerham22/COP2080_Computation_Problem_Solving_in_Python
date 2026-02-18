# ## tax.no_function.py
# done = False

# def get_inputs():
#     sentinel = str.upper(input(f'Enter Q for quit or any other key to compute tax '))
#     return sentinel

# def calculate_price_with_tax(price, tax):
#     calculated_price = price * (100 + tax) / 100
#     return calculated_price

# while not done:
#     sentinel = get_inputs()
#     if sentinel == 'Q':
#         done = True
#         print(sentinel,done)
#         continue
#     else:
#         print("Compute tax")
#     price = float(input('What is the price '))
#     tax = float(input('What is the tax rate? '))
#     calculated_price = calculate_price_with_tax(price, tax)
#     print(f'The calculated price is {calculated_price}')


# def add_mult(x, y):
#     return (x + y), (x * y)

# add, mult = add_mult(10,20)
# print(f"Addition: {add} \nMultiplication: {mult}")

add_mult = lambda x,y: ((x + y), (x * y))

add, mult = add_mult(10,20)
print(f"Addition: {add} \nMultiplication: {mult}")