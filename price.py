def format_price(price):
    price=int(price)
    string=f'Цена: {price} руб.'
    return string
result=format_price(56.24)
print(result)
