#!/bin/python
'''
Reference:
https://yq.aliyun.com/articles/70529?utm_campaign=wenzhang&utm_medium=article&utm_source=QQ-qun&2017315&utm_content=m_13620
'''

class Coffee:
    def __init__(self, name):
        self.name = name
        self.price = len(name)
    def to_str(self):
        print("Coffee Name:%s Price:%s"%(self.name,self.price))

class CoffeFactory:
    '''
    using coffee factory is good for not creating too many object
    '''
    coffee_dict = {}
    def get_coffee(name):
        if coffee_dict.has_key(name) == False:
            self.coffee_dict[name] = Coffe(name)
        return self.coffee_dict[name]
    def getCoffeeCount(self):
        return len(self.coffee_dict)

class Customer:
    def __init__(self, name, coffee_factory):
        self.name = name
        self.coffee_factory = coffee_factory
    def order(self, coffee_name):
        print("%s ordered a cup of coffee:%s"%(self.name,coffee_name))
        return self.coffee_factory.get_coffee(coffee_name)
