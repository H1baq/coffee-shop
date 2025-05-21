from customer import Customer
from coffee import Coffee
from order import Order

hibby = Customer("Hibby")

iced_coffee =Coffee("Iced coffee")

order1 = Order(hibby, iced_coffee, 5.0)

print("Customer")
print(f"Name: {hibby.name}")

orders = hibby.orders()
print("orders:",orders if orders else "Not orders made")

coffees = hibby.coffees()
print("Coffees ordered:", [c.name for c in coffees] if coffees else "No coffees ordered")

print("\n Coffee ")
print("Name:", iced_coffee.name)

coffee_orders = iced_coffee.orders()
print("Orders:", coffee_orders if coffee_orders else "No orders yet")

customers = iced_coffee.customers()
print("Customers who ordered:", [c.name for c in customers] if customers else "No customers yet")

print("Number of Orders:", iced_coffee.num_orders())
print("Average Price:", iced_coffee.average_price())

print("\n Creating Another Order ")
hibby.create_order(iced_coffee, 5.0)

updated_orders = hibby.orders()
print("Updated Orders:", updated_orders if updated_orders else "No orders yet")

print("Updated Average Price:", iced_coffee.average_price())

print("\n Most Aficionado ")
aficionado = Customer.most_aficionado(iced_coffee)
if aficionado:
    print("Most Aficionado for", iced_coffee.name, "is", aficionado.name)
else:
    print("No aficionado found yet.")