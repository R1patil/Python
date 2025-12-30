class shop:
    store_name="ABC Store"
    location="New York"

    def __init__(self, item,price):
        self.item=item
        self.price=price
    @classmethod
    def store_info(cls):
        return f"Welcome to {cls.store_name} located in {cls.location}"
    
    @classmethod
    def from_string(cls,item_string):
        item,price=item_string.split("-")
        return cls(item,int(price))
item1=shop("Laptop",1200)
item2=shop.from_string("Smartphone-800")
print(shop.store_info())
print(f"Item1: {item1.item}, Price: {item1.price}")