class Food:

    def __init__(self, name, price):  # Main Class

        self.price = price
        self.name = name
        print(f"{self.name} is created from Main Class")

    def eat(self):

        print("Eat Method From Base Class")


class Apple(Food):  # Derived Class

    def __init__(self, name, price, amount):
        self.amount = amount
        #self.name = name
        #Food.__init__(self, name)  # Create Instance From Base Class
        super().__init__(name, price)  # Super class which is the main class
        print(f"{self.name} is created from Derived Class And Price is {self.price} And Amount is {self.amount}")


    def get_from_tree(self):

        print("Get From Tree Derived Class")


#food_one = Food("pizza")
food_two = Apple("pizza", 150, 250)
food_two.eat()
food_two.get_from_tree()

