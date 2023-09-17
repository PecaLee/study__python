# List
day_of_week = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

print(day_of_week[0])

#Methods
print(day_of_week[0].capitalize())
print(day_of_week[1].upper())

day_of_week.append("weeks!")
print(day_of_week)

day_of_week.remove("weeks!")
print(day_of_week)

# Tuples
days = ("mon", "tue", "wed")
# Tuples can't change
print(days[0])
print(days[-1])

# Dictionary
player = {
    "name" : "peca",
    "age" : 12,
    "alive" : True,
    "fav_food" : ["kimchi", "buger", "pizza"] 
}

print(player["fav_food"][0])

player.pop("name")
player["xp"] = 1400
player["fav_food"].append("bossam")

print(player["fav_food"])