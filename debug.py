from customer import Customer
from coffee import Coffee


jan= Customer("jan")
harry = Customer("harry")
flo =  Customer("flo")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

jan.create_order(latte, 4.5)
jan.create_order(latte, 5.0)
harry.create_order(espresso, 3.5)
harry.create_order(latte, 5.5)
flo.create_order(espresso, 7.8)

print("Latte - Total Orders:", latte.num_orders())  
print("Latte - Average Price:", round(latte.average_price(), 2))  
print("Espresso - Total Orders:", espresso.num_orders())  
print("Espresso - Average Price:", espresso.average_price())  


print("jan's Coffees:", [c.name for c in jan.coffees()])  
print("harry's Coffees:", [c.name for c in harry.coffees()]) 