'''
Bowen Niu
CS 5001 Fall 2023
Final Project
'''
import time
from turtle import pencolor, penup, setposition
from Marble import *
from board import *
import random

state = [0, 0]
Colors = ['red','blue','green','yellow','purple','black']
player_data = [0, '']

def get_rand_colors():
    randl = [0,1,2,3,4,5]
    random.shuffle(randl)
    return [Colors[randl[i]] for i in range(4)]

secrets = get_rand_colors()
print(secrets)

class DisplayMarbles:
    marbles = {}
    def __init__(self) -> None:
        pass

    def add(self, marble, row):
        if row in self.marbles:
            self.marbles[row].append(marble)
        else:
            self.marbles[row] = [marble]

class Clickables:
    marbles = []
    def __init__(self) -> None:
        pass

    def add(self, marble):
        self.marbles.append(marble)

class Indicators:
    indicators = {}
    def __init__(self) -> None:
        pass

    def add(self, marble, row):
        if row in self.indicators:
            self.indicators[row].append(marble)
        else:
            self.indicators[row] = [marble]
    
# global variables
displays = DisplayMarbles()
clickables = Clickables()
indicators = Indicators()

# action marbles
class YesMarble(Marble):
    def update(self):
        if state[0] <= 9 and state[1] == 4:
            state[1] = 0

            # update indicators according to logic
            marbles = displays.marbles[state[0]]
            colors = [i.color for i in marbles]
            player_data[0] += 1

            # win condition
            (black, _, result) = check_logic(colors, secrets)
            if black == 4:
                
                # repetitive
                for i in range(4):
                    marble = indicators.indicators[state[0]][i]
                    marble.color = 'black'
                    marble.draw()
                winscreen()
                print("win!")
                return
            
            # lose condition
            if state[0] == 9:
                print("lose")
                losescreen()
                return
            turtle.tracer(False)
            for i in range(len(result)):
                marble = indicators.indicators[state[0]][i]
                marble.color = result[i]
                marble.draw()
            turtle.tracer(True)
            reset_click()
            state[0] += 1

    def draw_empty(self):
        pass

class NoMarble(Marble):
    def update(self):
        state[1] = 0
        for i in displays.marbles[state[0]]:
            i.draw_empty()
        reset_click()

    def draw_empty(self):
        pass

class Quit(Marble):
    def clicked_in_region(self, x, y):
        x0 = self.position.x - 50
        x1 = self.position.x + 50
        y0 = self.position.y - 30
        y1 = self.position.y + 30
        if (x > x0 and x < x1) and y > y0 and y < y1:
            return True
        return False

    def update(self):
        turtle.register_shape("quitmsg.gif")
        t1 = turtle.Turtle()
        t1.shape("quitmsg.gif")
        t1.penup()
        t1.goto(0, 30)
        t1.pendown()
        time.sleep(2)
        quit()

# this function draws functions that 
def draw_marbles():
    (sw, sh) = (-300, 320)
    for i in range(10):
        for j in range(4):
            m = Marble(Point(sw + j * 50, sh), "yellow", 18)
            m.draw_empty()
            displays.add(m, i)
        sh -= 58

def draw_indicators():
    (sw, sh) = (-50, 343)
    for i in range(10):
        for j in range(2):
            m = Marble(Point(sw + j * 20, sh), "black", 5)
            m.draw_empty()
            indicators.add(m, i)
        for j in range(2):
            m = Marble(Point(sw + j * 20, sh - 20), "black", 5)
            m.draw_empty()
            indicators.add(m, i)
        sh -= 58

def draw_choice():
    w = -310
    for i in Colors:
        m = Marble(Point(w, -340), i, 18)
        m.draw()
        w+=55
        clickables.add(m)

def click(x, y):
    for k in clickables.marbles:
        if k.clicked_in_region(x, y):
            if k.update == None:
                return
            color = k.update()
            if color and state[1] != 4:
                k.draw_empty()
                fill_logic(color)

def reset_click():
    turtle.tracer(False)
    for i in range(len(Colors)):
        marble = clickables.marbles[i]
        marble.color = Colors[i]
        marble.draw()
    turtle.tracer(True)


def fill_logic(color):
    if state[1] == 4:
        return

    m = displays.marbles[state[0]][state[1]]

    state[1] += 1
    m.color = color
    m.draw()

# game logic section
def check_logic(choice, secret):
    
    # determine number of black indicator
    num_black = 0
    for i in range(len(secret)):
        if secret[i] == choice[i]:
            num_black += 1
    
    # determine number of red indicator
    num_red = 0
    secret_set = set()
    for i in secret:
        secret_set.add(i) 
    for i in choice:
        if i in secret_set:
            secret_set.remove(i)
            num_red += 1
    
    # need to subtract
    num_red = num_red - num_black 
    result = []
    for i in range(num_black):
        result.append('black')
    for i in range(num_red):
        result.append('red')
    return (num_black, num_red, result)

def winscreen():
    turtle.register_shape("winner.gif")
    t1 = turtle.Turtle()
    t1.shape("winner.gif")
    t1.penup()
    t1.goto(0, 30)
    t1.pendown()
    with open('Leaderboard.txt', 'a') as f:
        f.writelines("{} : {}\n".format(player_data[0], player_data[1]))
    end_game()
    time.sleep(2)
    quit()
    
def losescreen():
    turtle.register_shape("Lose.gif")
    t1 = turtle.Turtle()
    t1.shape("Lose.gif")
    t1.penup()
    t1.goto(0, 30)
    t1.pendown()
    end_game()
    time.sleep(2)
    turtle.textinput("Secret Code Was", secrets)
    quit()

def end_game():
    reset_click()
    for i in clickables.marbles:
        i.update = None
    turtle.tracer(True)

def main():
    
    # setting up
    turtle.tracer(False)
    screen = turtle.Screen()
    screen.setup(width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
    t = turtle.Turtle()
    t.pensize(LINEWIDTH)
    t.speed(0)
    
    # query name
    player_data[1] = turtle.textinput("CS5001 MasterMind", "Your name:")
    
    # draw gameboard
    draw_gameboard(t)
    
    # init clickable marbles
    draw_choice()
    draw_marbles()
    draw_indicators()
    turtle.tracer(True)
    yp = Point(50, -320)
    np = Point(120, -320)
    qp = Point(250, -320)
    yes_marble = YesMarble(yp, "black")
    no_marble = NoMarble(np, "black")
    quit_marble = Quit(qp, "black")
    clickables.add(yes_marble)
    clickables.add(no_marble)
    clickables.add(quit_marble)
    draw_yes(yp.x, yp.y)
    draw_no(np.x, np.y)
    draw_quit(qp.x, qp.y)

    # draw leaderboard
    try:
        with open('Leaderboard.txt', 'r') as f:
            data = f.readlines()
            data.sort(key = lambda x : int(x.split(" ")[0]))
            penup()
            setposition(145, 300 + 30)
            pencolor('blue')
            turtle.write("Leaderboard", move=False, font=("Arial", 26, ""))
            for i in range(len(data)):
                setposition(150, 250 - i * 50)
                turtle.write(data[i], move=False, font=("Arial", 20, ""))
    except:
        turtle.register_shape("file_error.gif")
        t1 = turtle.Turtle()
        t1.shape("file_error.gif")
        t1.penup()
        t1.goto(235, 300)
        t1.pendown()

    # game loop
    screen.onclick(click)
    screen.mainloop()
# draw board
# get user input for name
# start game logic    
if __name__ == "__main__":
    main()