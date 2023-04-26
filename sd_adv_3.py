# define recommendations for each cuisine in each town
recommendations = {
    "downtown": {
        "mexican": ["Taco Stand", "Lolita's Mexican Food", "Cocina 35"],
        "american": ["Burger Lounge", "Werewolf", "The Smoking Gun"],
        "thai": ["Rama Thai Cuisine", "Lotus Thai Cuisine", "Thai Time"],
        "activities": ["Visit USS Midway Museum", "Take a Harbor Tour", "Explore Gaslamp Quarter"],
        "sight seeing": ["San Diego Zoo", "Balboa Park", "Old Town San Diego State Historic Park"]
    },
    "pb": {
        "mexican": ["Lolita's Mexican Food", "Oscar's Mexican Seafood", "Tony's Jacal"],
        "american": ["Kono's Cafe", "The Broken Yolk Cafe", "World Famous"],
        "thai": ["Thai Time", "PB Thai Food", "Thai Village"],
        "activities": ["Visit Belmont Park", "Take a Surfing Lesson", "Explore Crystal Pier"],
        "sight seeing": ["La Jolla Cove", "Torrey Pines State Natural Reserve", "Cabrillo National Monument"]
    },
    "encinitas": {
        "mexican": ["Juanita's Taco Shop", "Raul's Mexican Food", "La Especial Norte"],
        "american": ["Fish 101", "The Crack Shack", "ENCINITAS101"],
        "thai": ["Thai Society Restaurant", "Siamak's Carlsbad Thai", "Spice & Rice Thai Kitchen"],
        "activities": ["Visit Self Realization Fellowship Hermitage & Meditation Gardens", "Take a Surfing Lesson", "Explore San Diego Botanic Garden"],
        "sight seeing": ["Moonlight State Beach", "San Elijo State Beach", "Cardiff State Beach"]
    }
}

def get_recommendations(town, cuisine):
    if cuisine in recommendations[town]:
        print(f"I'd recommend the following places in {town}:")
        for item in recommendations[town][cuisine]:
            print(f"\u2022 {item}")
    else:
        print("Sorry, I don't have any recommendations for that cuisine in this town.")

# level 2 - decide which town you are going to go
while True:
    answer = input("Are you looking in Downtown, PB, or Encinitas? \n").lower()
    match answer:
        case "q":
            print('Thanks for trying my game, I hope it helped!\n')
            break
        case "downtown" | "pb" | "encinitas":
            town = answer
            print("Great, there is plenty to do there!\n"
                  "Do you want to get food, find an activity, or go sight seeing?")
            answer = input("Type 'food', 'activity', or 'sight seeing'\n").lower()
            match answer:
                case "food":
                    print("Ah, you're a hungry one. I can tell..."
                          "Luckily for you, there are a ton of great food options.\n"
                          "In order to point you in the right direction, what type of cuisine are you in the mood for?")
                    answer = input("Type 'mexican', 'american', or 'thai'\n").lower()
                    cuisine = answer
                    get_recommendations(town, cuisine)
                case "activity":
                    print("You want to have some fun, I like that! Here are some fun activities you can do in town:")
                    get_recommendations(town, "activities")
                case "sight seeing":
                    print("You want to explore the town, I like that! Here are some great sights to see:")
                    get_recommendations(town, "sight seeing")
                case _:
                    print("Sorry, I didn't understand your input. Please try again.")
        case _:
            print("Sorry, I didn't understand your input. Please try again.")