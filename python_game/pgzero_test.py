
import pgzrun

WIDTH = 600
HEIGHT = 800

car = Actor("car.png")
car.pos = (100 , 200)


def draw():
    screen.clear()
    car.draw()

def move_car(car):
  car.right += 1
  if car.left > WIDTH:
    car.right = 0

def update():
  move_car(car)

pgzrun.go() 

