joke_1 = "Knock, knock"
joke_2 = "lol"
joke_3 = "Ha-ha"
fav_number = int(input("What is your favourite number between 1 and 100?"))
if fav_number <= 30:
    print(joke_1)
elif fav_number >= 30 and fav_number <= 60:
    print(joke_2)
elif fav_number >= 60 and fav_number <= 100:
    print(joke_3)

