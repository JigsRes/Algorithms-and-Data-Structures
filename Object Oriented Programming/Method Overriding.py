class Person(object):
    def __init__(self, name):
        self.name=name
    def reveal_identity(self):
        print("My name is  {}".format(self.name))


class SuperHero(Person):
    def __init__(self, name, superhero_name):
        super(SuperHero,self).__init__(name)
        self.superhero_name=superhero_name

    def reveal_identity(self):
        super(SuperHero,self).reveal_identity()
        print("My super hero name is {}".format(self.superhero_name))


superhero=SuperHero("Diana", "Wonder Woman")

superhero.reveal_identity()

