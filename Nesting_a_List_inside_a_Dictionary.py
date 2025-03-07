# Nesting a List inside a Dictionary

Capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested list in dictionary

# travel_log = {
#     "France": ["paris", "lille", "dijon"],
#     "Germany": ["stuttgart", "berlin"]
# }
# See if you can figure out how to print out "Lille" from the nested List called travel_log.
# print(travel_log["France"][1])

# Nesting Lists inside other Lists

nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])


travel_log = {
    "France": {
        "cities visited": ["paris", "lille", "dijon"],
        "total visits": 12
    },
    "Germany": {
        "cities visited": ["berlin","hamburg", "stuttgart"],
        "total visits": 5
    }
}

print(travel_log["Germany"]["cities visited"][2])