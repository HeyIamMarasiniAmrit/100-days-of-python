# snake water gun
import random
def gamewin(comp,you):

    if comp == you:
        return None
    elif comp=="s":
        if you=="w":
            return False
    elif you== "g":
            return True

    elif comp=="W":
            if you =="g":
             return False
    elif you=="s":
              return True

    elif comp =="g":
        if you=="s":
            return False
        elif you=="W":
            return True

        print("comp turn:snake(s) water(w) or Gun(g)")
        randNo = random.randint(1,3)
        if randNo==1:
            comp="s"
        elif randNo == 2:
            comp="W"
        elif randNo == 3:
            comp = "g"
        you = input("you turn:snake(s) water(w) orGun(g)?\n")

        a = gamewin(comp, you)
        print(f"computer choose\t{comp}\n")
        print(f"you choose\t{you}\n")

        if a==None:
            print("the game is tie!")
        elif a:
            print("you Win!")

        else:
            print("you lose!")

