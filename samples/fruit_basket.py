class FruitBasket:

    def __init__(self):
        # A collection of type list can contain many occurances of the same element
        self.basket = [
            'mango', 'apple', 'plum', 'peach', 'mango', 'mango', 'peach',
            'apple', 'peach', 'plum'
        ]

        # Mango weighs 100 fl oz, Apple weighs 30 fl oz, plum weighs 25 fl oz and peach weigh 15 fl oz.
        # A dictionary in python holds key value pairs
        self.fruitWeightMap = {
            'mango': 100,
            'apple': 30,
            'peach': 15,
            'plum': 25
        }
        print('########## Using a for loop #########')

    def countWeights(self):
        weightOfBasket = 0
        for fruitPicked in self.basket:
            print('Picked fruit ', fruitPicked, ' of weight ',
                  self.fruitWeightMap[fruitPicked])
            weightOfBasket = weightOfBasket + self.fruitWeightMap[fruitPicked]

        print('Total weight ', weightOfBasket)
        print()
        print('########## Using a while loop #########')
        indexOfFruit = 0
        weightOfBasket = 0
        while indexOfFruit < len(self.basket):
            fruitPicked = self.basket[indexOfFruit]
            print('Fruit at index', indexOfFruit, ' is ', fruitPicked,
                  ' with weight ', self.fruitWeightMap[fruitPicked])
            weightOfBasket = weightOfBasket + self.fruitWeightMap[fruitPicked]
            indexOfFruit += 1

        print('Total weight 2', weightOfBasket)
