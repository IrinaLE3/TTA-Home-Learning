bike_price = 2000

def calc_bike_price(bike_price):
    while bike_price > 1000:
        print(bike_price)
        bike_price = bike_price * 0.9
    return bike_price    

calc_bike_price(bike_price)
