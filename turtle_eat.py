# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 15:08:03 2018

@author: Yan Qi
"""

import turtle as t
import random as r

class BallGame(object):
    
    def __init__(self):
        #TODO: 搭建游戏环境：属性、环境界面等等
        
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
    #TODO
    def isCollided(self,tur,ball):
        colli_x = abs(tur.xcor() - ball.xcor()) < 15
        colli_y = abs(tur.ycor() - ball.ycor()) < 15
        res = colli_x and colli_y
        return res  #True: 碰上了 , False：没碰上
            
    def turnLeft(self):
        self.t.left(30)
        
    def turnRight(self):
        self.t.right(30)
        
    def hahahaha(self):
        self.speed = self.speed+1
        self.t.speed(self.speed)
            
    def hehehehe(self):
        self.speed = self.speed-1
        self.t.speed(self.speed)
        
    def run_game(self):
        #TODO
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
        
#t.setup(700,800)
#t.penup()
#t.goto(329,250)
#t.pendown()
#t.goto(329,-250)
#t.goto(-329,250)
#t.goto(329,250)
#t.penup()
#t.shape("turtle")


# turtle for score（计分数的乌龟）
#s = t.Turtle()
#把分数乌龟移动到左上角
#s.goto(-250,300)
#s.hideturtle()
#s.clear()
#score = 0
#lb = 0
#s.write(score,align="left", font=("Times",16,"bold"))

#random appearance of the ball(小球随机出现)
#b = t.Turtle()
#b.shape("circle")
#b.penup()
#b.goto(r.randint(-200,200),r.randint(-250,250))
#判断是否碰到小球
#def isCollided(tur,ball):
#    colli_x = abs(tur.xcor() - ball.xcor()) < 15
#    colli_y = abs(tur.ycor() - ball.ycor()) < 15
#    res = colli_x and colli_y
#    return res  #True: 碰上了 , False：没碰上

#事件
#screen = t.Screen()

#键盘左方向键,左传30
#def turnLeft():
#    t.left(30)
#    
#def turnRight():
#    t.right(30)
#
#Speed=1
#def hahahaha():
#    global Speed
#    Speed = Speed+1
#    t.speed(Speed)
#    
#def hehehehe():
#    global Speed
#    Speed = Speed-1
#    t.speed(Speed)
#键盘右键，右转30度
#screen.onkey(turnLeft,"Left")
#screen.onkey(turnRight,"Right")
#screen.onkey(hahahaha,"Up")
#screen.onkey(hehehehe,"Down")
#screen.listen()

#while True:
#    t.forward(Speed)
#    xbound = 329
#    if t.xcor()>=xbound:
#       t.goto(xbound,t.ycor())
#    if t.xcor()<=-xbound:
#       t.goto(-xbound,t.ycor()) 
#    ybound = 250
#    if t.ycor()>=ybound :
#       t.goto(t.xcor(),ybound)
#    if t.ycor()<=-ybound:
#       t.goto(t.xcor(),-ybound) 
#    #如果乌龟碰上小球，加分
#    res = isCollided(t,b)
#    if res ==True:
#        b.hideturtle()
#        score = score+1
#        lb =lb+1
#        s.clear()
#        s.write(score,align="left", font=("Times",16,"bold"))
#        b.goto(r.randint(-200,200),r.randint(-250,250))
#        b.showturtle()
#    if lb==10:
#        Speed=Speed+1
#        lb =0
        