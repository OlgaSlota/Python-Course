# python2 required ! 

import sys, pygame,io, random
from pygame.locals import *
from urllib2 import urlopen

size = width, height = 64*15 , 48*15     # screen size
green = (5 ,205, 5)
red =(150, 5, 5)
color = green           # color of pplayer's battery level: green or red

me_charging = False     #boolen , says if player is connected to any socket
sockets = []            # list of wall sockets positions
in_socket = []          # additional spots and circle in square socket
my_battery = 50         # starting value of player's battery level

dx, dy = 0, 0           # player's speed

stop = False            #boolean value about escaping from game

player_url = "http://read.pudn.com/downloads74/sourcecode/game/269060/space%20invader%20packed/invader/alien2__.jpg"
player_str = urlopen(player_url).read()       # opening url
player_file = io.BytesIO(player_str)          # to create image jpg representing player
player = pygame.image.load(player_file)       # loading image
player_rect = player.get_rect()               # creating a Rect object of image
player_rect.move_ip(10,10)                    # moving created Rect to starting position

other_url = 'http://www.ufoencounters.co.uk/images/15817x50.jpg'
other_str = urlopen(other_url).read()
other_file = io.BytesIO(other_str)
other = pygame.image.load(other_file)           # creating image of other students
others = []                                     # list of other students
others_speed = []                               # of their speed
others_battery = []                             # their battery level a number from (0,100)
others_rect = []                                # list of Rect objects created for every student from "others" list
batteryImg = []                                 # ready to display battery level for every student from "others" list



end = 'GAME OVER!  PRESS ESC TO QUIT'
end_url= 'http://vignette1.wikia.nocookie.net/egamia/images/4/4e/Game_Over_Screen.jpg/revision/latest?cb=20140718104227'
end_str = urlopen(end_url).read()
end_file = io.BytesIO(end_str)              # info about game over
ending = pygame.image.load(end_file)
end_rect = ending.get_rect()
end_rect.move_ip(100,60)


# function called when losing a game

def end_of_game():
     stop = True
     screen.blit(ending, end_rect)
     screen.blit(endImg, (400, 300))            # displays game over info
     pygame.time.wait(500)                     # delays for 3 seconds waiting for player to escape


# for each student : adding their images , speed , battery level

for i in range(0,8):
    others.append(other)
    others_speed.append([random.randrange(1,3), random.randrange(1,3)])
    others_battery.append(random.randrange(1,100))

    # addiing Rect representation of every student and students' starting posisions

    others_rect.append(other.get_rect())
    others_rect[i].move_ip(random.randrange(40, width-40), random.randrange(40, height-40))


# for each socket

for i in range(0,10):

    x = random.randrange(30, width-30)             #random posisions of sockets
    y = random.randrange(30, height-30)

    sockets.append(pygame.Rect(x, y,18,18))

    #extra features of sockets
    in_socket.append([[x+6, y+8], [x+12, y+8], [x+9, y+9], [x+9, y+12]])

pygame.time.set_timer(USEREVENT+1, 500)         # creates new event on event queue every 0.5 second
pygame.init()

font = pygame.font.Font(None, 30)
text = "GO FIND SOCKET BEFORE YOU LOSE ENERGY! DON'T BUMP INTO OTHER STUDENTS!"  # main info displayed constantly on screen


# main loop of game

while True :

 # checking if we already lost the game
 if stop:
     sys.exit()

 # event handling (closing a window and pressing keys)
 for event in pygame.event.get():
   if event.type == pygame.QUIT: sys.exit()

   # handling keybord events to move player
   if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            dx -= 1
        if event.key == pygame.K_RIGHT:
            dx += 1
        if event.key == pygame.K_UP:
            dy-= 1
        if event.key == pygame.K_DOWN:
            dy += 1
        if event.key == pygame.K_SPACE:
            dx ,dy = 0,0
        if event.key == pygame.K_ESCAPE:
            sys.exit()

   # called every half of second to control battery level
   if event.type == USEREVENT+1:
         if me_charging:
             my_battery +=1
         else:
             my_battery -=1

             if my_battery<11:
                 color=red

                 if my_battery<1:
                      end_of_game()
             else:
                 color=green


 screen = pygame.display.set_mode(size,pygame.RESIZABLE)

 # displayed info about game rules
 textImg = font.render(text, 1, red, screen)
 screen.blit(textImg, (60,10))

 #displayed when game over
 endImg = font.render(end, 1, red, screen)

 # displayed player's battery level
 my_batteryImg = font.render(str(my_battery)+'%',1,color, screen)

 # displayed others students' battery levels
 for i in range (0,8):
     batteryImg.append(font.render(str(others_battery[i])+ '%', 1,red ,screen))



 # bumpping player from screen edges

 if screen.get_rect().contains(player_rect):
     player_rect = player_rect.move(dx,dy)
 else:
     dx,dy = -dx, -dy
     player_rect = player_rect.move(dx,dy)


 # drawingg player and his battery level

 screen.blit(player, player_rect)
 screen.blit(my_batteryImg, (player_rect.x,player_rect.y-10))


 #drawing all of sockets on screen

 for i in range(0,10):
  pygame.draw.rect(screen,(255,255,255),sockets[i],0)

  pygame.draw.circle(screen,(0,0,0), in_socket[i][0] , 2 ,2)
  pygame.draw.circle(screen,(0,0,0), in_socket[i][1] , 2 ,2)
  pygame.draw.circle(screen, (0,0,0), in_socket[i][3], 2 ,2)
  pygame.draw.circle(screen,(0,0,0), in_socket[i][2] , 9 ,2)


  # controlling if player is occupying socket or not

  if player_rect.colliderect(sockets[i]):
      dx, dy = 0, 0
      me_charging = True
  if player_rect.colliderect(sockets[i]):
      if my_battery>99:
          dx , dy = 1,1
          me_charging = False


 # drawing other students and bumping from screen edges

 for i in range(0,8):
  screen.blit(others[i] , others_rect[i])
  screen.blit(batteryImg[i], (others_rect[i].x, others_rect[i].y-20))


  if screen.get_rect().contains(others_rect[i]):
       others_rect[i] = others_rect[i].move(others_speed[i])
  else:
     others_speed[i][0],others_speed[i][1] = -others_speed[i][0],-others_speed[i][1]
     others_rect[i] = others_rect[i].move(others_speed[i])

  #game over if player collides any other student

  if player_rect.colliderect(others_rect[i]):
        end_of_game()

  # bumping students from each other

  for j in range (0,8):
      if others_rect[i].colliderect(others_rect[j]):
          others_speed[i][0]=-others_speed[i][0]
          others_speed[j][0]=-others_speed[j][0]

  # stoppping students for a while if they meet socket

  for j in range(0,10):
     if others_rect[i].colliderect(sockets[j]):
         others_speed[i] = [0,0]
         if others_battery[i]<100:
             others_battery[i]+=1
         else:
             others_speed[i]=[random.randrange(1,3), random.randrange(1,3)]

 pygame.display.flip()
