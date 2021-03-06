import pygame
import math

#initializing pygame
pygame.init()

#creating a window
win = pygame.display.set_mode((1000,500))

#name of the game
pygame.display.set_caption("Robot vs Zombies")
walkright = [pygame.image.load("robotright/rightr1.png"),pygame.image.load("robotright/rightr2.png"),pygame.image.load("robotright/rightr3.png"),
             pygame.image.load("robotright/rightr4.png"),pygame.image.load("robotright/rightr5.png"),pygame.image.load("robotright/rightr6.png"),
             pygame.image.load("robotright/rightr7.png"),pygame.image.load("robotright/rightr8.png"),]
walkleft = [pygame.image.load("robotleft/leftr1.png"),pygame.image.load("robotleft/leftr2.png"),pygame.image.load("robotleft/leftr3.png"),
             pygame.image.load("robotleft/leftr4.png"),pygame.image.load("robotleft/leftr5.png"),pygame.image.load("robotleft/leftr6.png"),
             pygame.image.load("robotleft/leftr7.png"),pygame.image.load("robotleft/leftr8.png"),]
bg = pygame.image.load("BG3.jpg")
idle_right = pygame.image.load("idelr.png")
idle_left = pygame.image.load("idlel.png")
character = pygame.image.load("robot.png")


clock = pygame.time.Clock()
#initialization of score
score = 0

#sounds
#maingamemusic = pygame.mixer.music.load("mainsound.wav")
#pygame.mixer.music.play(-1)

#keeping character attribute inside a class
class player(object):
    #player's characteristics
    def __init__(self, x , y , width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.jumpcount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 37, self.y+10, 55, 110)

    #players fuctions
    def draw(self,win):
        # we have 8 sprint image and our fps is 3 p/sec so after all 8 sprint we go to count 0
        if self.walkCount + 1 >= 24:
            self.walkCount = 0

        if not(self.standing):
            #draw character to left
            if self.left:
                win.blit(walkleft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            # draws character to right
            elif self.right:
                win.blit(walkright[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

        # if we are not going left or right then we must be standing still and [] is index of image
        else:
            if self.right:
                win.blit(idle_right,(self.x, self.y))  #walkright[6]
            else:
                win.blit(idle_left,(self.x, self.y))    #walkleft[6]

        self.hitbox = (self.x + 37, self.y+10, 55, 110)
        #hitbox to check collision area
        #pygame.draw.rect(win,(255, 0, 0), self.hitbox,2)

    def hit(self):
        self.x = robot.x
        self.y = robot.y
        self.walkCount = 0
        '''font1 = pygame.font.SysFont("comicsans", 100)
        text = font1.render("-5",1,(255,0,0))
        win.blit(text, (500 - (text.get_width()/2), 250))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time. delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()'''

#
class projectile(object):
    #
    def  __init__(self,x ,y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 30 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)



class enemy(object):
    walkright = [pygame.image.load("planeright1.png"), pygame.image.load("planeright2.png")]
    walkleft = [pygame.image.load("planeleft1.png"), pygame.image.load("planeleft2.png")]

    def __init__(self,x, y, width , height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 10, self.y, 180, 125)
        self.health = 10
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 6:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkright[self.walkCount//3], (self.x, self.y))
                self.walkCount +=1
            else:
                win.blit(self.walkleft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            #health bar
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1]- 20, 120, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1]- 20, 120 - ((120/10) * (10 - self.health)), 10))

            self.hitbox = (self.x + 10, self.y, 180, 125)
            #hitbox to check collision area
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


    #plane movement
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False
        print("hit")



class groundenemy(object):
    # image of zombie
    zombiewalkright = [pygame.image.load("zombieright/zombieright1.png"),
                       pygame.image.load("zombieright/zombieright2.png"),
                       pygame.image.load("zombieright/zombieright3.png"),
                       pygame.image.load("zombieright/zombieright4.png"),
                       pygame.image.load("zombieright/zombieright5.png"),
                       pygame.image.load("zombieright/zombieright6.png"),
                       pygame.image.load("zombieright/zombieright7.png"),
                       pygame.image.load("zombieright/zombieright8.png"),
                       pygame.image.load("zombieright/zombieright9.png"),
                       pygame.image.load("zombieright/zombieright10.png")]

    zombiewalkleft = [pygame.image.load("zombieleft/zombieleft1.png"), pygame.image.load("zombieleft/zombieleft2.png"),
                      pygame.image.load("zombieleft/zombieleft3.png"), pygame.image.load("zombieleft/zombieleft4.png"),
                      pygame.image.load("zombieleft/zombieleft5.png"), pygame.image.load("zombieleft/zombieleft6.png"),
                      pygame.image.load("zombieleft/zombieleft7.png"), pygame.image.load("zombieleft/zombieleft8.png"),
                      pygame.image.load("zombieleft/zombieleft9.png"), pygame.image.load("zombieleft/zombieleft10.png")]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 10
        self.hitbox = (self.x + 10, self.y, 180, 125)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 6:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.zombiewalkright[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.zombiewalkleft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            # health bar
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 70, 10))
            pygame.draw.rect(win, (0, 128, 0),
                            (self.hitbox[0], self.hitbox[1] - 20, 80 - ((70 / 10) * (10 - self.health)), 10))

            #creating hitbox for collision
            self.hitbox = (self.x + 20, self.y+20, 70, 125)
            #display hitbox to check collision area
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


#zombie movement
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False
        print("hit")

def redrawGameWindow():
    # filling the screen with a image
    win.blit(bg, (0,0))

    #score board
    text = font.render("Score: "+ str(score), 1, (255,0,0))
    win.blit(text, (390, 10))

    #high score
    scorehigh = font.render("High Score : " + str(score), 1, (200, 150, 55))
    win.blit(scorehigh, (700, 10))


    #calling robot from class
    robot.draw(win)

    plane.draw(win)

    zombie.draw(win)

    #enemies.draw(win)

    for bullet in bullets:
        bullet.draw(win)

    for zombie1 in zombies:
        zombie1.draw(win)



    # refresh the display
    pygame.display.update()


#main loop
font = pygame.font.SysFont("comicsans", 35, True)
robot = player(800, 370, 80, 40)
plane = enemy(20,100, 100,100, 900)
zombie = groundenemy(30,360, 80, 40, 900)
enemies = []
maxenemies = 10
bullets = []
shootloop = 0
zombies = []
zombie1 = groundenemy(zombie.x, zombie.y, zombie.width, zombie.height, zombie.end)
run = True
while run:
    clock.tick(24)

    if zombie.visible == True:
        if robot.hitbox[1] < zombie.hitbox[1] + zombie.hitbox[3] and robot.hitbox[1] + robot.hitbox[3] > zombie.hitbox[1]:
            if robot.hitbox[0] + robot.hitbox[2]  > zombie.hitbox[0] and robot.hitbox[0] < zombie.hitbox[0] + zombie.hitbox[2]:
                robot.hit()
                score -= 1


    if shootloop > 0:
        shootloop += 1
    if shootloop > 5:
        shootloop = 0

    #checking for event users command
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #spawning zombies
    if zombie.visible == False:
        for zombie1 in zombies:
            if robot.hitbox[1] < zombie1.hitbox[1] + zombie1.hitbox[3] and robot.hitbox[1] + robot.hitbox[3] > \
                    zombie1.hitbox[1]:
                if robot.hitbox[0] + robot.hitbox[2] > zombie1.hitbox[0] and robot.hitbox[0] < zombie1.hitbox[0] + \
                        zombie1.hitbox[2]:
                    robot.hit()
                    score -= 1


        if len(zombies) < 2:
            zombies.append(groundenemy(30,360, 80, 40, 900))


    #bullet on spawned zombies
        for bullet in bullets:
            if zombie1.visible == True:
                if bullet.y - bullet.radius < zombie1.hitbox[1] + zombie1.hitbox[3] and bullet.y + bullet.radius > zombie1.hitbox[1]:
                    if bullet.x + bullet.radius > zombie1.hitbox[0] and bullet.x - bullet.radius < zombie1.hitbox[0] +zombie1.hitbox[2]:
                        zombie1.hit()
                        score += 1
                        bullets.pop(bullets.index(bullet))

            if bullet.x < 1000 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
            #delete bullet
                bullets.pop(bullets.index(bullet))


#bullet hit on plane
    for bullet in bullets:
        if plane.visible:
            if bullet.y - bullet.radius < plane.hitbox[1] + plane.hitbox[3] and bullet.y + bullet.radius > plane.hitbox[1]:
                if bullet.x + bullet.radius > plane.hitbox[0] and bullet.x - bullet.radius < plane.hitbox[0] +plane.hitbox[2]:
                    plane.hit()
                    score += 2
                    bullets.pop(bullets.index(bullet))

        if bullet.x < 1000 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
        #delete bullet
            bullets.pop(bullets.index(bullet))

#bullet hit on zombie
    for bullet in bullets:
        if zombie.visible == True:
            if bullet.y - bullet.radius < zombie.hitbox[1] + zombie.hitbox[3] and bullet.y + bullet.radius > zombie.hitbox[1]:
                if bullet.x + bullet.radius > zombie.hitbox[0] and bullet.x - bullet.radius < zombie.hitbox[0] +zombie.hitbox[2]:
                    zombie.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))
                # ???>??? and ???<???
        if bullet.x < 1000 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
        #delete bullet
            bullets.pop(bullets.index(bullet))


    #continue to move charater when you press and hold key
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootloop == 0:
        #moving bullet in left direction
        if robot.left:
            facing = -1
        #moving bullet in right direction
        else:
            facing = 1

        if len(bullets) < 10:
            #making this so bullet cames from wherever player is facing
            bullets.append(projectile(round(robot.x + robot.width//2), round(robot.y + robot.height//2), 6, (255,0,0),facing ))

        shootloop = 1

    #keys function and setting boundry
    if keys[pygame.K_LEFT] and (robot.x + 50) > robot.vel:
        robot.x -= robot.vel
        robot.left = True
        robot.right = False
        robot.standing = False
    elif keys[pygame.K_RIGHT] and robot.x < 1000 - robot.width - robot.vel:
        robot.x += robot.vel
        robot.right = True
        robot.left = False
        robot.standing = False
    else:
        robot.standing = True
        robot.walkCount = 0

    #if character is in mid air we don't it to go up or down
    if not(robot.isJump):
        if keys[pygame.K_UP]:
            robot.isJump = True
            robot.right = False
            robot.left = False
            robot.walkCount = 0
    else:
        #jump
        if robot.jumpcount >= -10:
            neg = 1
            #come down
            if robot.jumpcount < 0:
                neg = -1
            #jump
            robot.y -= (robot.jumpcount ** 2) * 0.5 * neg
            robot.jumpcount -= 1
        else:
            #conclude player has jumped and can jump again
            robot.isJump = False
            robot.jumpcount = 10


    redrawGameWindow()