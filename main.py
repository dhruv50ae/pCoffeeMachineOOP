# from turtle import Turtle, Screen
# import AnotherMod
#
# print(AnotherMod.anotherVar)
#
# rammus = Turtle()
# print(rammus)
# rammus.shape("turtle")
# rammus.color("coral")
# rammus.forward(100)
# rammus.backward(200)
#
# myScreen = Screen()
#
# myScreen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)