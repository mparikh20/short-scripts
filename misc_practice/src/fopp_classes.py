'''Some OOP practice from the Runestone FOPP online text book.'''
import random

class Point():

    # setting a class variable, this won't be bound to an instance
    expression = 'Lets do some math!'

    def __init__(self, x_val, y_val):

        # instance attributes - a point's x and y co-ordinates

        # to make this instance variables private i.e. other people cannot access them and change them directly:
            # self._x or self.__x is used
            # So if a person creates an instance p1 and then calls p1.__x it will throw an error instead of returning the value of x
        self.x = x_val
        self.y = y_val


    def get_x(self):

        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        '''Shows you can customize what gets printed when you print the instance of the object'''
        return self.__class__.__name__

    def halfway(self, second_point):
        '''Shows how a method can take in an object and return an object'''

        h_x = (self.x + second_point.x) / 2
        h_y = (self.y + second_point.y) / 2

        return Point(h_x,h_y)

    def __lt__(self, second_point):

        '''less than comparator method that assesses if the instance value less than other instance's value)'''
        return self.x < second_point.x

class Pet():

    hungry_threshold = 5
    bored_threshold = 10
    sounds = ['baa', 'moo']

    hungry_change = 1
    bored_change = 1

    hungry_reduce = 1
    bored_reduce = 1

    def __init__(self):

        self.hunger = random.randint(0, self.hungry_threshold+1)
        self.boredom = random.randint(0, self.bored_threshold+1)
        self.words = self.sounds.copy()

    def clock_tick(self):
        '''as time passes, increment the hunger and bored values.'''
        self.hunger += self.hungry_change
        self.boredom += self.bored_change

    def get_current_state(self):
        if self.hunger > self.hungry_threshold:

            if self.boredom > self.bored_threshold:

                inform = 'hungry and bored'

            else:
                inform = 'hungry'

        elif self.boredom > self.bored_threshold:

            inform = 'bored'

        else:
            inform = 'happy'

        return inform


    def __str__(self):

        status = self.get_current_state()

        return f"Pet's hunger is {self.hunger}/{self.hungry_threshold} and boredom is {self.boredom}/{self.bored_threshold}, making it {status}!"

    def teach(self, new_word):
        '''Teach a new word to the pet.'''
        self.words.append(new_word)
        self.reduce_boredom()

    def hi(self):
        '''Randomly say one of the words from the list.'''
        random_index = random.randint(0,len(self.words)+1)

        print(self.words[random_index])
        self.reduce_boredom()

    def reduce_boredom(self):
        '''Decrease boredom by varied level'''

        self.boredom = max(self.boredom - self.bored_reduce, 0)
        return self.boredom

    def reduce_hunger(self):
        '''Decrease hunger by varied level'''

        self.hunger = max(self.hunger - self.hungry_reduce, 0)

        return self.hunger

    def feed(self):
        '''Reduces hunger.'''
        self.reduce_hunger()

