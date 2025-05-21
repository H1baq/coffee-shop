from coffee import Coffee

def test_coffee_name():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def test_invalid_name():
    try:
        Coffee("co")
    except ValueError as e:
        assert str(e) == "Coffee name must be at least 3 characters long."

def test_orders_and_customers():
    class MockOrder:
        def __init__(self, customer, price):
            self.customer = customer
            self.price = price
    
    coffee = Coffee("Latte")
    order1 = MockOrder("Hannah", 3.5)
    order2 = MockOrder("David", 4.0)
    order3 = MockOrder("Mary", 3.5)
    
    coffee._orders.extend([order1, order2, order3])
    
    assert coffee.num_orders() == 3
    assert set(coffee.customers()) == {"Hannah", "David", "Mary"}
    assert abs(coffee.average_price() - 3.6666) < 0.001
