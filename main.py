class Student:
    def __init__(self, name, age, money, energy, grade):
        self.name = name
        self.age = age
        self.money = money
        self.energy = energy
        self.grade = grade

    def work(self):
        self.money += 100
        self.energy -= 20
        print(self.name, "worked and earned money. Money:", self.money)

    def study(self):
        self.grade += 1
        self.energy -= 15
        print(self.name, "studied. Grade:", self.grade)

    def chill(self):
        self.energy += 20
        self.money -= 30
        print(self.name, "is resting. Energy:", self.energy)

    def live_day(self):
        print("- Day -")

        if self.money < 50:
            print("Not enough money - going to work")
            self.work()

        elif self.grade < 5:
            print("Problems with study- studying")
            self.study()

        elif self.energy < 30:
            print("Too tired - resting")
            self.chill()

        else:
            print("Normal day - resting")
            self.chill()

    def live_year(self):
        for day in range(1, 11): 
            print("Day", day)
            self.live_day()


student1 = Student("Karina", 18, 100, 100, 4)
student1.live_year()
