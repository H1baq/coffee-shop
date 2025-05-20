# coffee-shop Domain Model (python OOP project)

Welcome to the **Coffee Shop** project! This application models real-world relationships using Python classes and object-oriented programming principles.

## 📖 Project Overview

This project simulates a coffee shop's order system using three classes:

- Customer: A person who orders coffee
- Coffee: A type of coffee sold
- Order: A record of a coffee purchase by a customer

### Relationships:

- A Customer can place many Orders.
- A Coffee can have many Orders.
- An Order belongs to one Customer and one Coffee.

Thus, Customer and Coffee share a **many-to-many** relationship through Order.

---

## 🛠️ Setup Instructions

### 1. Clone the Project

```bash
git clone 
cd coffee_shop


2. Set Up Virtual Environment

Use pipenv to manage packages:

-pipenv install
-pipenv shell

🔹Customer

✅ name (1–15 characters, string)

✅ create_order(coffee, price)

✅ orders() → list of Order instances

✅ coffees() → unique list of Coffee objects

✅ most_aficionado(coffee) → customer who spent most on that coffee

🔹Coffee
✅ name (at least 3 characters, string)

✅ orders() → list of Order instances

✅ customers() → unique list of Customer objects

✅ num_orders() → total orders

✅ average_price() → average price of orders


🔹Order
✅ Validates:

customer: Customer instance

coffee: Coffee instance

price: float between 1.0 and 10.0


10.0

🧪 Run Tests
Tests are written using pytest in the testing/ folder.

To run all tests:
 pytest.

