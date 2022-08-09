import turtle
import pandas

screen = turtle.Screen()
screen.title("European countries quiz")
image = "map_of_europe.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("european_countries - Sheet1.csv")
country_list = data.country.to_list()
guessed_countries = []

while len(guessed_countries) < 42:
    answer = screen.textinput(title=f"{len(guessed_countries)}/42", prompt="Guess a country:").title()
    if answer == "Exit":
        countries_to_learn = []
        for country in country_list:
            if country not in guessed_countries:
                countries_to_learn.append(country)
        new_data = pandas.DataFrame(countries_to_learn)
        new_data.to_csv("countries_to_learn.csv")
        break

    if answer in country_list:
        guessed_countries.append(answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        country_data = data[data.country == answer]
        t.goto(int(country_data.x), int(country_data.y))
        t.write(answer)

turtle.mainloop()