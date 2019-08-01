ball_x = 250
ball_y = 250

ball_dX = 0
ball_dY = 0

stuff = []
pits = []
score = 0

def setup():
    size(500, 500)

def draw():
    global ball_x, ball_y, ball_dX, ball_dY, stuff, pits, score
    background(0)
    fill(255)
    text(score, 10, 20)
    
    # draw stuff
    stuff_to_pop = []
    for i in range(len(stuff)):
        stuff_x, stuff_y, stuff_color = stuff[i]
        if ball_x + 10 >= stuff_x and ball_x <= stuff_x + 10 and ball_y + 10 >= stuff_y and ball_y <= stuff_y + 10:
            stuff_to_pop.append(i)
            score += 1
        else:
            fill(stuff_color)
            rect(stuff_x, stuff_y, 10, 10)
    for i in stuff_to_pop:
        stuff.pop(i)
        
    for pit_x, pit_y, pit_color in pits:
        draw_pit(pit_x, pit_y, pit_color)
        if ball_x + 10 >= pit_x and ball_x <= pit_x + 10 and ball_y + 10 >= pit_y and ball_y <= pit_y + 10:
            score = 0
            ball_x = 250
            ball_y = 250
            ball_dX = 0
            ball_dY = 0
        
    # draw ball
    fill(255)
    rect(ball_x, ball_y, 10, 10)
    
    # maybe add new stuff for the next frame
    if random(1) < 0.01:
        stuff.append((int(random(width)), int(random(height)), color(random(255),random(255),random(255))))
    if random(1) < 0.003:
        pits.append((int(random(width)), int(random(height)), color(random(255),random(255),random(255))))
    
    # update ball
    if ball_x + 10 < width:
        ball_x += ball_dX
        
    if ball_y + 10 < height:
        ball_y += ball_dY
    
def keyPressed():
    global ball_x, ball_y, ball_dX, ball_dY
    if key == CODED:
        if keyCode == UP:
            ball_dY = -1
        elif keyCode == DOWN:
            ball_dY = 1
        elif keyCode == LEFT:
            ball_dX = -1
        elif keyCode == RIGHT:
            ball_dX = 1
    
def keyReleased():
    global ball_x, ball_y, ball_dX, ball_dY
    if key == CODED:
        if keyCode == UP:
            ball_dY = 0
        elif keyCode == DOWN:
            ball_dY = 0
        elif keyCode == LEFT:
            ball_dX = 0
        elif keyCode == RIGHT:
            ball_dX = 0        
  
def draw_pit(x, y, c):
    fill(c)
    rect(x, y, 10, 10)
    stroke(0)
    line(x, y, x+10, y+10)
    line(x+10, y, x, y+10)
