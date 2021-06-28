import time

character_name = ''


answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]


sword = 0

required = ("\nUse only A, B, C, D\n")

character_name = input('please enter the name of your character: ')

print("\nWELCOME TO THE ADVENTURE GAME 🎮\n")
print(f"{character_name} wakes up in a dark and foggy forest. There is a certain peace in the forest.🌲\nYou want to get up but you feel pain in your left leg.")


def intro():

    print("You look around and notice that the path behind you is closed by a rocky mountain.⛰\nIn the far right there is a little light whose source is not known.\nThe path on the left is also impassable by a lot of felled trees.\nYou look ahead and find nothing but darkness.")
    time.sleep(1)
    print(
        "Which path will you choose???\n\nA: forward ⬆\nB: right ➡\nC: bakcwards ⬇\nD: left ⬅")
    choice = input(">>> ")
    if choice in answer_A:
        option_dark_path()
    elif choice in answer_B:
        option_light()
    elif choice in answer_C:
        print("How do you want to climb a mountain with this injured foot???🙄\n")
        intro()
    elif choice in answer_D:
        print("I do not think it is possible to pass through all these felled trees😩\n")
        intro()
    else:
        print(required)


def option_dark_path():
    print("\nYou gather all your strength and slowly walk towards the darkness.\nYou try not to feel the pain in your left leg and you feel that little by little your eyes got used to the darkness.👀\nSuddenly you hear a sound from behind the trees and your heart beat rises rapidly.😨")
    time.sleep(1)
    print("What would you do???\n\nA: Go back ⬇\nB: move deeper in the darkness")
    choice = input(">>> ")
    if choice in answer_A:
        intro()
    elif choice in answer_B:
        option_move_deeper()
    else:
        print(required)


def option_move_deeper():
    print("\nYou walk deeper into the forest and you hear a sound from behind the trees.👂🏻\nYou try not to pay attention to the sound and move forward.\nSuddenly you see a creature hovering in the air next to a tree staring at you with its red eyes.🧛🏻‍♀️")
    time.sleep(1)
    print("\nWhat would you do???\n\nA: Go Back ⬇\nB: Find a rock and throw at it 🧱\nC: Move towards it and try pass it ⬆\n")
    choice = input(">>> ")
    if choice in answer_A:
        intro()
    elif choice in answer_B:
        print("The creature is angry and come closer and bites your neck!!!😴")
        print("YOU ARE DEAD!!!\n❌❌❌!!!GAME OVER!!!❌❌❌")
    elif choice in answer_C:
        if sword == 0:
            print(
                "The creature block your path and wants to fight you.\nYou do not have a weapon and The creature bites your neck!!!😴")
            print("YOU ARE DEAD!!!\n❌❌❌!!!GAME OVER!!!❌❌❌")
        else:
            print(
                "You fight with all your being and use the ⚔sword⚔ to overcome the creature and move on untill you see the city light.")
            print("🎈🎉Congratulations you've done it 🎉🎈")
    else:
        print(required)


def option_light():
    print("\nAs you approach the light, you see that the dim light was the refletion of moonlight on a metal object.\nYou bend down and try to pick up the object and realize that the object is a samurai sword.\nYou look around and realize that there is no way forward and you have to go back to where you were before. 🗡🗡🗡")
    time.sleep(1)
    print("What would you do???\n\nA: Go Back ⬇\nB: Wait for no reason\n")
    global sword
    sword = 1
    choice = input(">>> ")
    if choice in answer_A:
        intro()
    elif choice in answer_B:
        print("Use your head and go back🧠")
        option_light()
    else:
        print(required)


intro()
