#from turtle import Turtle,Screen
#
#timmy = Turtle()
#print(timmy)
#timmy.color("red")
#timmy.shape("turtle")
#timmy.forward(100)
#
#ground = Screen()
#print(ground.canvheight)
#ground.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()


table.add_column('pokemon',["pikachu","burba"])
table.add_column("type",["electric","grass"])
table.align = "l"
print(table)
