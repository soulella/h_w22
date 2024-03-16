# Task_1


class User:
    user_name = 0

    def __init__(self, users):
        self.users = users
        User.user_name += 1


u1 = User("johnsmith10")
print(u1.user_name)
u2 = User("marysue1989")
print(u1.user_name)
u3 = User("milan_rodrick")
print(u3.user_name)
print(u1.users)
print(u2.users)
print(u3.users)


# Task_2

class Book:
    def __init__(self):
        self.title = "Harry Potter"
        self.author = "J.K Rowling"

    def get_title(self):
        print(f"Title: {self.title}")

    def get_author(self):
        print(f"Author: {self.author}")


HP = Book()
print(HP.title)
print(HP.author)
HP.get_title()
HP.get_author()


# Task_3

class Composer:
    count = 0

    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob
        self.country = country
        Composer.count += 1


c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
print(Composer.count)
c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
c3 = Composer("Johannes Brahms", 1833, "Germany")
print(Composer.count)


# Task_4

class Person:

    def __init__(self, name, love, hate):
        self.name = name
        self.love = love
        self.hate = hate

    def taste(self, food):
        if food in self.love:
            return f"{self.name}eats the {food} and loves it!"
        elif food == "cheese":
            return f"{self.name} eats the {food}!"
        elif food in self.hate:
            return f"{self.name} eats the {food} and hates it!"
        else:
            return f"u asked unknown food"


p1 = Person("Sam", ["ice cream"], ["carrots"])


while True:
    food = input("Enter the name of food:  ")
    print(p1.taste(food))
    break


# Task_5

class Country:

    def __init__(self, country, population, area):
        self.is_big = ""
        self.country = country
        self.population = population
        self.area = area

        if self.population > 250000 and self.area > 3000:
            self.is_big = True
        else:
            self.is_big = False

    def compare_pd(self, other):
        if self.population < other.population:
            return f"{self.country} has a larger population density than {other.country}"


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

print(australia.is_big)
print(andorra.is_big)
print(andorra.compare_pd(australia))


# Task_6

class Programmer:
    def __init__(self, salary, work_hours):
        self.salary = salary
        self.work_hours = work_hours

    def __del__(self):
        print(f"oof, {self.salary}, {self.work_hours}")


prog = Programmer(25000, 5)
print(prog.salary)
print(prog.work_hours)
del prog


# Task_7

class IceCream:
    def __init__(self, flavor, num_sprinkles):
        self.flavor = flavor
        self.num_sprinkles = num_sprinkles
        if self.flavor == "Chocolate":
            a = num_sprinkles + 10
            print(f"Value of {a}")
        elif self.flavor == "Vanilla":
            b = num_sprinkles + 5
            print(f"Value of {b}")
        elif self.flavor == "Strawberry":
            d = num_sprinkles + 10
            print(f"Value of {d}")
        elif self.flavor == "Plain":
            print(f"Value of {self.num_sprinkles}")
        elif self.flavor == "ChocolateChip":
            e = num_sprinkles + 5
            print(f"Value of {e}")
        else:
            print("Sorry, u asked unknown ice cream")


ice1 = IceCream("Chocolate", 13)
ice2 = IceCream("Vanilla", 0)
ice3 = IceCream("Strawberry", 7)
ice4 = IceCream("Plain", 18)
ice5 = IceCream("ChocolateChip", 3)