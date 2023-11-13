from random import shuffle

def villager():
    global npcName
    global responses

    npcNameChoice = ["leon"]
    npcName = npcNameChoice[0]

    print(npcName, ":", "Hello, I am", npcName, ", would you like to talk to me?")

    shuffle(responses)

    answer_talk = input("Press y to talk to the villager")
    if answer_talk.lower() == "y":
        print(npcName, ":", responses[0])

        answer_hero = input("Are you the hero? (yes/no): ")
        if answer_hero.lower() == "yes":
            print(npcName, ": Thank god! We need your help.")
        else:
            print(npcName, ": Okay, maybe someone else will step up. Goodbye!")
    else:
        print(npcName, ": Goodbye")

responses = ["hi", "are you a hero?", "Are you from this village?"]

villager()
