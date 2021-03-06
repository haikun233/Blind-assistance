#!/usr/bin/python
#-*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM) #使用BCM编码方式
#定义引脚
GPIO_OUT = 23
led = 21 
#设置引脚为输入和输出
GPIO.setwarnings(False) 
#设置23针脚为输入，接到红外避障传感器模块的out引脚
GPIO.setup(GPIO_OUT,GPIO.IN) 
GPIO.setup(led,GPIO.OUT)     

def warn():   #亮灯来作为有障碍物时发出的警告
    GPIO.output(led,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led,GPIO.LOW)
    time.sleep(1)
                            
while True:
    if GPIO.input(GPIO_OUT)==0: 
    #当有障碍物时，传感器输出低电平，所以检测低电平
        warn()
GPIO.cleanup()
