'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
import time

print("You should never have crossed them.")
time.sleep(1.33)
print("Reaching Salem is now your only hope of survival.")
time.sleep(1.66)
print("The cold Rocky Mountains are no friend to us human souls.")
time.sleep(2)
print("At last, you have no other option than to persevere.")
time.sleep(2.5)

class Perspective:
    def __init__(self):
        self.thirst = 0
        self.tainted = False
        self.exhaustion = 0
        self.drinks = 5
        self.journey = 0
        self.followers = -30
        self.dead = False
        self.done = False

    def status(self):
        print("Kilometers exerted:", self.journey)
        print("Thirst:", self.thirst)
        print("Exhaustion:", self.exhaustion)
        print("Drinks in flask:", self.drinks)
        print("Kilometers ahead:", self.journey - self.followers)
        if self.journey - self.followers <= 25:
            print("I recommend you exert yourself.")

    def temp(self):
        blizzard = random.randint(1, 46)
        if blizzard == 23:
            print("Some are just unable to handle the extremities of a blizzard.")
            self.done = True

    def poem(self):
        poems = ["Life is no friend to ambition.", "Never bite the hawk who feeds you worms.", "Ease is the most intriguing fallacy.", "Never rid yourself of your necessities in order to go forth.", "Don\'t sacrifice others in order to save oneself."]
        print(poems[random.randint(0, len(poems) - 1)])

    def encounter(self):
        scenario = random.randint(0, 15)
        if scenario == 0:
            print("You encounter an ole shack in your path. Inside is a barrel of a clear liquid.")
            action = input("A: Fill your flask\nB: Return to your path\nF: Forfeit\n")
            if action.upper() == "A":
                print("Never leave anything unused.")
                self.tainted = True
                self.drinks += 5
                time.sleep(1)
            elif action.upper() == "B":
                print("Don\'t get distracted, the focus of the mind is essential for survival.")
                time.sleep(1)
            elif action.upper() == "F":
                self.done = True
        elif scenario == 1:
            print("There is an extraordinary river in your path with a vigorous flow.")
            action = input("A: Push forth\nB: Wait for it to calm\nF: Forfeit\n")
            if action.upper() == "A":
                print("You\'ve gone all this way, why should you slow down now.")
                time.sleep(2.5)
                value = random.randint(0, 4)
                if value == 0:
                    print("Perhaps it would have been wiser to be patient.")
                    game.done = True
                if value == 1:
                    print("This river was your triumph, be proud of yourself. My only ask to not forget the flask you fed to the pebbles.")
                    game.journey += 2
                    self.tainted = True
                    time.sleep(1)
                if value > 1:
                    print("This river was your triumph, be proud of yourself. My only ask to not forget the flask you fed to the pebbles.")
                    game.journey += 2
                    time.sleep(1)
            elif action.upper() == "B":
                print("Patience is essential for survival.")
                game.journey -= 3
                time.sleep(1)
            elif action.upper() == "F":
                self.done = True
        elif scenario == 2:
            print("You encounter a camp along your escape.")
            action = input("A: Infiltrate the tent\nB: Return to your path\nF: Forfeit\n")
            if action.upper() == "A":
                print("A curious mind is not only the most dangerous but in addition the most rewarding.")
                time.sleep(2.5)
                value = random.randint(0, 3)
                if value == 0:
                    print("A figure leaps from the tent and restrains you. Fate is no longer in your hands.")
                    game.done = True
                if value == 1:
                    print("A stash of jars, a fine discovery for your situation.")
                    self.drinks += 6
                    time.sleep(1)
                if value > 1:
                    print("The tent is filled with nothing but a calm melancholic ambiance.")
                    time.sleep(1)
            elif action.upper() == "B":
                print("Don\'t get distracted, the focus of the mind is essential for survival.")
                time.sleep(1)
            elif action.upper() == "F":
                self.done = True
        elif scenario == 10:
            print("The fountain of youth lies in your gaze.")
            action = input("A: Collect its treasure\nB: Return to your path\nF: Forfeit\n")
            if action.upper() == "A":
                print("You and your stallion recharge yourself with the fountain\'s golden steam.")
                self.exhaustion = 0
                self.drinks += 25
                self.thirst = 0
                time.sleep(2.5)
            elif action.upper() == "B":
                print("Don\'t get distracted, the focus of the mind is essential for survival.")
                time.sleep(1)
            elif action.upper() == "F":
                self.done = True
        elif scenario == 11:
            self.temp()

game = Perspective()

while not game.done:
    if game.journey >= 600:
        print("Salem is in sight. Enjoy your days as a man bound to no one.")
        game.done = True
        break
    if 6 < game.thirst > 3:
        print("Water is essential for the living kind. It\'s unwise to neglect such essentials.")
    elif game.thirst > 5:
        print("Water is essential for the living kind. Remember that next in your next life.")
        game.done = True
        break
    else:
        pass
    if 8 < game.exhaustion > 4 and not game.dead:
        print("Slumber is essential for the living kind. It\'s unwise to neglect such essentials.")
    elif game.exhaustion > 7 and not game.dead:
        print("Slumber is essential for the living kind. Remember that next in your next life.")
        game.dead = True
        choice = input("A: Say your farewells\nF: Forfeit\n")
        if choice.upper() == "A":
            game.thirst = 0
            game.drinks -= 1
            print("Goodbye ole gunner.")
        elif choice.upper() == "F":
            game.done = True
            break
    else:
        pass
    if game.journey - game.followers <= 25 and game.journey - game.journey > 0:
        print("I recommend you exert yourself.")
    elif game.journey - game.followers <= 0:
        print("You deserved this, there is no shame in hiding that remorse now. Don\'t cross those who you depend on.")
        game.done = True
        break
    else:
        pass
    option = input("A: Drink from your flask\nB: Push with haste\nC: Push with leisure\nD: Set up camp\nE: Consult the map\nF: Forfeit\n")
    if option.upper() == "A":
        game.thirst = 0
        game.drinks -= 1
        print("Ah, refreshment.")
        time.sleep(1)
        if game.tainted:
            print("Perfection is unattainable, but it should always remain the standard.")
            game.done = True
            break
    elif option.upper() == "B":
        if game.dead:
            print("Sometimes it\'s best to halt rather than make pace.")
            game.followers += random.randint(12, 24)
            time.sleep(1)
            game.poem()
            time.sleep(4)
            game.temp()
            print("Kilometers exerted:", game.journey)
            time.sleep(1)
        else:
            print("Move forth we shall.")
            game.thirst += 1
            game.exhaustion += random.randint(1, 3)
            game.journey += random.randint(16, 32)
            game.followers += random.randint(12, 24)
            time.sleep(1)
            game.poem()
            time.sleep(4)
            game.temp()
            game.encounter()
            print("Kilometers exerted:", game.journey)
            time.sleep(1)
    elif option.upper() == "C":
        if game.dead:
            print("Sometimes it\'s best to halt rather than make pace.")
            game.followers += random.randint(12, 24)
            time.sleep(1)
            game.poem()
            time.sleep(4)
            game.temp()
            print("Kilometers exerted:", game.journey)
            time.sleep(1)
        else:
            print("Move forth we shall.")
            game.thirst += 1
            game.exhaustion += 1
            game.journey += random.randint(8, 19)
            game.followers += random.randint(12, 24)
            time.sleep(1)
            game.poem()
            time.sleep(4)
            game.temp()
            game.encounter()
            print("Kilometers exerted:", game.journey)
            time.sleep(1)
    elif option.upper() == "D":
        game.exhaustion = 0
        game.followers += random.randint(12, 24)
        print("Take your rest for granted, you never know when it may come again.")
        time.sleep(1)
        game.poem()
        time.sleep(4)
        print("Kilometers exerted:", game.journey)
        time.sleep(1)
    elif option.upper() == "E":
        game.status()
        time.sleep(5)
    elif option.upper() == "F":
        game.done = True
    else:
        print("No.")