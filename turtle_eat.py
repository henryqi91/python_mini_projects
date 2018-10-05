# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 15:08:03 2018

@author: Yan Qi
"""

import turtle as t
import random as r

class BallGame(object):
    
    def __init__(self):
        
        self.screen = t.Screen() #屏幕控制接受
        
        self.speed = 1 
        self.score = 0
        self.lb = self.score
        
        t.setup(700,800)
        t.hideturtle()
        
        self.t = t.Turtle() #玩家乌龟
        self.t.penup()
        self.t.goto(329,250)
        self.t.pendown()
        self.t.goto(329,-250)
        self.t.goto(-329,-250)
        self.t.goto(-329,250)
        self.t.goto(329,250)
        self.t.penup()
        self.t.goto(0,0)
        self.t.shape("turtle")
        
        self.b = t.Turtle() #被吃的球
        self.b.shape("circle")
        self.b.penup()
        self.b.goto(r.randint(-200,200),r.randint(-250,250))
        
        self.s = t.Turtle() #计分器
        self.s.penup()
        self.s.goto(-250,300)
        self.s.pendown()
        self.s.hideturtle()
        self.s.write(self.score,align="left", font=("Times",16,"bold"))

    def isCollided(self,tur,ball):
        colli_x = abs(tur.xcor() - ball.xcor()) < 15
        colli_y = abs(tur.ycor() - ball.ycor()) < 15
        res = colli_x and colli_y
        return res  #True: 碰上了 , False：没碰上
            
    def turnLeft(self):
        self.t.left(30)
        
    def turnRight(self):
        self.t.right(30)
        
    def accelerate(self):
        self.speed = self.speed+1
        self.t.speed(self.speed)
            
    def decelerate(self):
        self.speed = self.speed-1
        self.t.speed(self.speed)
        
    def run_game(self):
        self.screen.onkey(self.turnLeft,"Left")
        self.screen.onkey(self.turnRight,"Right")
        self.screen.listen()
        self.t.forward(self.speed)
        while True:
            self.t.forward(self.speed)
            xbound = 329
            if self.t.xcor()>=xbound:
               self.t.goto(xbound,self.t.ycor())
            if self.t.xcor()<=-xbound:
               self.t.goto(-xbound,self.t.ycor()) 
            ybound = 250
            if self.t.ycor()>=ybound :
               self.t.goto(self.t.xcor(),ybound)
            if self.t.ycor()<=-ybound:
               self.t.goto(self.t.xcor(),-ybound) 
            #如果乌龟碰上小球，加分
            res = self.isCollided(self.t,self.b)
            if res ==True:
                self.b.hideturtle()
                self.score = self.score+1
                self.lb =self.lb+1
                self.s.clear()
                self.s.write(self.score,align="left", font=("Times",16,"bold"))
                self.b.goto(r.randint(-200,200),r.randint(-250,250))
                self.b.showturtle()
            if self.lb==10:
                self.speed=self.speed+1
                self.lb =0
            
if __name__ == "__main__":
    game = BallGame()
    game.run_game()
        
        
