#Flexible Discount System

def product(base_price = 100, **discount):
    current_price = base_price
    for key,value in discount.items():
        discount_price = current_price * value
        current_price -= discount_price
        print(f"{key} applied - {discount_price}Rs -> price = {current_price}Rs")
    print(f"Final Price: {current_price}.Rs")
    return current_price
        


product(flat_discount=0.5,
        festival_season=0.10,
        rafay_season = 0.03)
