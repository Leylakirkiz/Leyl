import random


def custom_hash(key):
    return (key * 123456789) % 1000 + 100  

price_list = {f'Item {i+1}': custom_hash(i) for i in range(100)}

for item, price in price_list.items():
    print(f'{item}: ${price/100:.2f}')