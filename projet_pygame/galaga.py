import pgzrun
import random

WIDTH = 800
HEIGHT = 900

ship = Actor('ship')
ship.pos = (200 , 460)

#Define bullets
bullets = []

def on_key_down(key):
  if ship.dead == False:
    if key == keys.SPACE:
      bullets.append(Actor('bullet'))
      bullets[-1].x = ship.x
      bullets[-1].y = ship.y-80

#Define enemies
enemies = []

for x in range(3):
  for y in range(3):
    enemies.append(Actor('bug'))
    enemies[-1].x = 100 + 90*x
    enemies[-1].y = 10 + 10*y

direction = 1


#Movements
def update():
  global score
  global direction
  if ship.dead == False:
    if keyboard.left:
      ship.x-=3
    elif keyboard.right:
      ship.x+=3

  for bullet in bullets:
    if bullet.y < -20:
      bullets.remove(bullet)
    else:
     bullet.y -=10
  
  moveDown = False
  if len(enemies)>0 and (enemies[-1].x > WIDTH-80 or enemies[0].x < 80):
    moveDown = True
    direction = direction*-1
  for enemy in enemies:
    enemy.x += 4*direction
    if moveDown == True:
      enemy.y += 85
    for bullet in bullets:
      if enemy.colliderect(bullet):
        score += 150
        bullets.remove(bullet)
        enemies.remove(enemy)
    if enemy.colliderect(ship):
      dead = True
      ship 
ship.dead = False
#Score 
score = 0


def drawScore():
  screen.draw.text(str(score),(50, 30))

    

def draw():
  screen.clear()

  for bullet in bullets:
    bullet.draw()
  for enemy in enemies:
    enemy.draw()
  if ship.dead == False:
    ship.draw()
    drawScore()



pgzrun.go()
