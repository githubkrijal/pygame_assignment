import pygame  #“>” and “<”

#initializing pygame
pygame.init()

#creating a window
win = pygame.display.set_mode((1000,500))

#name of the game
pygame.display.set_caption("Made by Krijal")
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
#bulletround = pygame.image.load("bullet1.png")

clock = pygame.time.Clock()

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



def redrawGameWindow():
    # filling the screen with a image
    win.blit(bg, (0,0))
    #calling robot from class
    robot.draw(win)

    for bullet in bullets:
        bullet.draw(win)


    # refresh the display
    pygame.display.update()


#creating a main loop
robot = player(300, 370, 80, 80)
bullets = []
run = True
while run:
    clock.tick(24)
    #checking for event users command
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 1000 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
        #delete bullet
            bullets.pop(bullets.index(bullet))

    #continue to move charater when you press and hold key
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        #moving bullet in left direction
        if robot.left:
            facing = -1
        #moving bullet in right direction
        else:
            facing = 1

        if len(bullets) < 10:
            #making this so bullet cames from wherever player is facing
            bullets.append(projectile(round(robot.x + robot.width//2), round(robot.y + robot.height//2), 6, (255,0,0),facing ))

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