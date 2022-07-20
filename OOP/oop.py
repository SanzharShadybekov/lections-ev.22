import json
from register import User

class Product():
    FILE = 'jsondb/data.json'
    id = 0

    def __init__(self, title, description, price, quantitity, owner):
        self.title = title
        self.description = description
        self.price = price
        self.qty = quantitity
        self.owner = owner
        self.send_product_to_json()

    @classmethod
    def get_id(cls):
        cls.id += 1
        return cls.id

    @classmethod
    def get_data(cls):
        with open(cls.FILE) as file:
            return json.load(file)

    @staticmethod
    def get_one_product(data, id):
        product = list(filter(lambda x: x['id'] == id, data))
        if not product:
            return 'Нет такого продукта'
        return product[0]
    
    @classmethod
    def send_data_to_json(cls, data):
        with open(cls.FILE, 'w') as file:
            json.dump(data, file)

    def send_product_to_json(self):
        data = Product.get_data()
        product = {
            'id': Product.get_id(),
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'quantity': self.qty,
            'owner': self.owner
        }
        data.append(product)

        with open(Product.FILE, 'w') as file:
            json.dump(data, file)
        
        return {'status': '201', 'msg': product}

    @classmethod
    def retrieve_data(cls, id):
        data = cls.get_data()
        product = cls.get_one_product(data, id)
        return product

    @classmethod
    def update_data(cls, id, **kwargs):
        data = cls.get_data()
        product = cls.get_one_product(data, id)
        if type(product) != dict:
            return product
        index = data.index(product)
        data[index].update(**kwargs)
        cls.send_data_to_json(data)
        return {'status': '200', 'msg': 'Updated'}

    @classmethod
    def delete_data(cls, id):
        data = cls.get_data()
        product = cls.get_one_product(data, id)
        if type(product) != dict:
            return product

        index = data.index(product)
        data.pop(index)
        cls.send_data_to_json(data)
        return {'status': '204', 'msg': 'deleted'}

with open(Product.FILE, 'w') as file:
    json.dump([], file)

user = User().login('JohnSnow', 'john1234')
print(user)
username = user['user']['username']

obj1 = Product('Samsung Galaxy S22', 'Cool phone!', 1000, 10, username)
obj2 = Product('Iphone 14 Pro Max', 'Mega cool phone!', 1300, 3, username)
obj3 = Product('Redmi Note 10', 'Good phone !!', 200, 14, username)

print('Все продукты:\n', Product.get_data())
print('\n', Product.retrieve_data(3))
print(Product.update_data(15, title='Redmi Note 100'))
print(Product.retrieve_data(3))
print(Product.delete_data(3))
print('Все продукты:\n', Product.get_data())




