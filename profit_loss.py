

selling_price=int(input("Enter selling price : "))


def profit_loss(price):
    cost_price=350
    if selling_price == cost_price:
        print("No profit no loss")
    elif selling_price > cost_price:
        profit=selling_price - cost_price
        print("You have earned profit" , profit)
    else:
        loss=selling_price - cost_price
        print('You have incurred loss', loss)


profit_loss(selling_price)
