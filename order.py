from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self,customer,coffee,price):
        if not isinstance(customer, Customer):
            raise TypeError ("the customer must be an object instance of Customer") 
        self._customer = customer
        if not isinstance(coffee, Coffee):
            raise TypeError ("the coffee name must be an object instance")
        self._coffee = coffee
        if not isinstance(price, float) or not  (1.0<= price <=10.0):
            raise ValueError("the price must be between 1.0 - 10.0")
        self._price = float(price)

        customer._orders.append(self)
        coffee._orders.append(self)


    @property
    def price(self):
        return self._price
    
    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

almasi = Customer("jobuu")
latte = Coffee ("latte")
price = 6.6
order1 = Order (almasi , latte, price)

print(order1.customer.name)
print(order1.coffee.name)
print (order1.price)
