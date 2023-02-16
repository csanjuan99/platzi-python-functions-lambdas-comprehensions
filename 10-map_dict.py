order_items = [
    {
        "id": 1,
        "name": "foo",
        "price": 100
    },
    {
        "id": 2,
        "name": "bar",
        "price": 200
    },
    {
        "id": 3,
        "name": "baz",
        "price": 300
    }
]

# list with only the prices

prices = list(map(lambda product: product["price"], order_items))
print(prices)

# list with each product but with new ket of shipping_cost

order_items_with_shipping_cost = list(
    map(lambda product: product | {"shipping_cost": product["price"] * 0.1}, order_items))  # product | ... = **product
print(order_items_with_shipping_cost)

# when u don't want to change the original list you should use .copy() method to create a new item and then change
