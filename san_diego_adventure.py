
# create lists for each area of San Diego
towns = ["downtown", "encinitas", "pb"]

# food lists
food_type = ["mexican", "thai", "american"]

dt_mex = ["La Puerta", "Cocina 35", "King & Queen Cantina"]
dt_thai = ["Thotsakan", "Sab Lai", "Aaharn"]
dt_american = ["Hidden Craft", "Werewolf", "Queenstown"]
en_mex = ["Los Tacos", "Case de Bandini", "La Especial Norte"]
en_thai = ["Similan", "Birdseye", "Thai Pan"]
en_american = ["Union", "Waverly", "Viewpoint"]
pb_mex = ["La Perla", "Pueblo", "Oscars"]
pb_thai =["Lanna Thai","55 Thai Kitchen", "The Orient"]
pb_american =["The Hideout","Luce", "Bayside Landing"]

# activity lists
dt_act = ["USS Midway","Harbor Cruise","Trolley Tour"]
en_act = ["Surfing", "Electric Scooter", "Wine Tasting"]
pb_act = ["La Jolla Tour", "Driving Day Tour", "Mission Beach Amusement Park"]

# sight seeing lists
dt_ss = ["USS Midway","SeaWorld", "Balboa Park"]
en_ss = ["Cardiff Dog Park", "Swami's Meditation Gardens", "Cardiff Kook"]
pb_ss = ["Kate Session's Park", "The Boardwalk", "PB Shore Club"]

# level 1 - intro and decide your first journey
print('\n\nWelcome to my San Diego Adventure journey\nI designed this application so you can'
      ' figure out where to eat, sight see, or do activities \nbased on where you are at in Sunny San Diego')
name = input("Type your name: ")
print("Welcome to San Diego", name, ". I am excited to give you some recommendations!\n"
      "At any point, press q to quit :)\n")

# level 2 - decide which town you are going to go
while True:
    answer = input("Are you looking in Downtown, PB, or Encinitas? \n").lower()
    if answer == "q":
        print('Thanks for trying my game, I hope it helped!\n')
        quit()
    if answer == "downtown":
        print("Great, there is plenty to do there!\n"
              "Do you want to get food, find an activity, or go sight seeing?")
        answer = input("Type 'food' 'activity' or 'sight seeing'\n").lower()
        if answer == "food":
            print("Ah, you're a hungry one. I can tell..."
                  "Luckily for you, downtown has a ton of great food options.\n"
                  "In order to point you in the right direction, what are you in the mood for?\n")
            answer = input("Mexican, American, or Thai: ").lower()
            if answer == "mexican":
                print("I'd recommend the following places:")
                for item in dt_mex:
                    print(f"\u2022 {item}")
            elif answer == "american":
                print("I'd reccomend the following places:")
                for item in dt_american:
                    print(f"\u2022 {item}")
            elif answer == "thai":
                print("I'd reccomend the following places:")
                for item in dt_thai:
                    print(f"\u2022 {item}")
            else:
                print("Let's try this again\n")
                continue
        elif answer == "activity":
            print("Awesome, activities are a great way to experience Downtown San Diego.\n"
                    "If you're not going to see a Padres game, here are some ideas:")
            for item in dt_act:
                print(f"\u2022 {item}")
        elif answer == "sight seeing":
            print("Sight seeing is a fantastic way to enjoy what's around you.\n"
                    "Here's what i'd reccomend seeing: ")
            for item in dt_ss:
                print(f"\u2022 {item}")
    elif answer == "pb":
        print("Great, there is plenty to do there!\n"
              "Do you want to get food, find an activity, or go sight seeing?")
        answer = input("Type 'food' 'activity' or 'sight seeing'\n").lower()
        if answer == "food":
            print("Ah, you're a hungry one. I can tell..."
                    "Luckily for you, Pacific Beach has a ton of great food options.\n"
                    "In order to point you in the right direction, what are you in the mood for?\n")
            answer = input("Mexican, American, or Thai: ").lower()
            if answer == "mexican":
                print("I'd recommend the following places:")
                for item in pb_mex:
                    print(f"\u2022 {item}")
            elif answer == "american":
                print("I'd reccomend the following places:")
                for item in pb_american:
                    print(f"\u2022 {item}")
            elif answer == "thai":
                print("I'd reccomend the following places:")
                for item in pb_thai:
                    print(f"\u2022 {item}")
            else:
                print("Let's try this again\n")
                continue
        elif answer == "activity":
            print("Awesome, there are a ton of activities in Pacific Beach. here are some ideas:")
            for item in pb_act:
                print(f"\u2022 {item}")
        elif answer == "sight seeing":
            print("Sight seeing is a fantastic way to enjoy what's around you.\n"
                  "Here's what i'd reccomend seeing: ")
            for item in pb_ss:
                print(f"\u2022 {item}")
    elif answer == "encinitas":
        print("Great, there is plenty to do there!\n"
                "Do you want to get food, find an activity, or go sight seeing?")
        answer = input("Type 'food' 'activity' or 'sight seeing'\n").lower()
        if answer == "food":
            print("Luckily for you, Encinitas has a ton of great food options.\n"
                    "In order to point you in the right direction, what are you in the mood for?\n")
            answer = input("Mexican, American, or Thai: ").lower()
            if answer == "mexican":
                print("I'd recommend the following places:")
                for item in en_mex:
                    print(f"\u2022 {item}")
            elif answer == "american":
                print("I'd reccomend the following places:")
                for item in en_american:
                    print(f"\u2022 {item}")
            elif answer == "thai":
                print("I'd reccomend the following places:")
                for item in en_thai:
                    print(f"\u2022 {item}")
            else:
                print("Let's try this again\n")
                continue
        elif answer == "activity":
            print("Awesome, there's great activities in Encinitas. Here are some ideas:")
            for item in en_act:
                print(f"\u2022 {item}")
        elif answer == "sight seeing":
            print("Sight seeing is a fantastic way to enjoy what's around you.\n"
                "Here's what i'd reccomend seeing: ")
            for item in en_ss:
                print(f"\u2022 {item}")
    else:
        print(f"Try again {name}! \n")
        continue
    