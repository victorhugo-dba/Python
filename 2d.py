
# fruits =     ["Apple", "Banana", "Orange", "coconut"]
# vegetables = ["Celery", "carrots", "Potatoes"]
# meats =      ["chicken", "fish", "turkey"]

# groceries = [["Apple", "Banana", "Orange", "coconut"], 
#              ["Celery", "carrots", "Potatoes"], 
#              ["chicken", "fish", "turkey"]]

# # print(groceries[2][2])

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9), 
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()