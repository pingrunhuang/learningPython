from enum import Enum
import time

PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick')
PizzaSauce = Enum('PizzaSauce', 'tomato creme_fraiche')
PizzaTopping = Enum('PizzaTopping', 'mozzarella double_mozzarella bacon ham mushrooms, red_onion, oregano')
STEP_DELAY = 3


class Pizza:
    """
    final product, different builder will have different process of building this product
    """
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.source = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print('Preparing {} dough for your {}'.format(self.dough.name, self))
        time.sleep(STEP_DELAY)
        print('Done with the {} dough preparation'.format(self.dough.name))


class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        # change status
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print('adding the tomato sauce to your margarita...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the tomato sauce')

    def add_topping(self):
        print('adding the topping ({}) to margarita...'.format(','.join([x.name for x in PizzaTopping])))
        self.pizza.topping.append([i for i in PizzaTopping])
        time.sleep(STEP_DELAY)
        print('done with the topping {}'.format(','.join([x.name for x in PizzaTopping])))

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your margarita for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your margarita is ready')


class Waiter:
    """
    commander
    """

    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        [step() for step in (builder.prepare_dough, builder.add_sauce, builder.add_topping, builder.bake)]

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        pizza_style = input('What pizza would you like. [m]argarita or [c]reamy bacon?')
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError as e:
        print('Sorry, only margarita (key m) and creamy bacon (key c) are available')
        return False, None
    return valid_input, builder


if __name__ == "__main__":
    builders = dict(m=MargaritaBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print('Enjoy!')