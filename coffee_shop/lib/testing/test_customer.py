from customer import Customer
from coffee import Coffee

def test_create_order_and_most_aficionado():
    c = Customer("Hibby")
    coffee = Coffee("iced coffee")
    c.create_order(coffee, 5.0)
    assert coffee.customers() == [c]
    assert Customer.most_aficionado(coffee) == c
