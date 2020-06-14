# -*- encoding=utf8 -*-
__author__ = "Yang"
import random
from airtest.core.api import *

from airtest.cli.parser import cli_setup
# if not cli_setup():
#     auto_setup(__file__, logdir=True, devices=[
#             "Android:///",
#     ])
auto_setup(__file__)
#剿灭
def jiaomie():
    touch(Template(r"tpl1592074683982.png", record_pos=(-0.079, 0.236), resolution=(1920, 1080)))#剿灭作战
    sleep(random.randint(1,3))

    touch(Template(r"tpl1592074825913.png", record_pos=(-0.327, -0.071), resolution=(1920, 1080))) #切尔偌伯格
    sleep(random.randint(1,3))


    for i in range(2):
        touch(Template(r"tpl1592074899870.png", record_pos=(0.396, 0.229), resolution=(1920, 1080)))
        sleep(random.randint(1,3))

        touch(Template(r"tpl1592074942925.png", record_pos=(0.362, 0.114), resolution=(1920, 1080)))
        sleep(350.0)

        touch((500,500))
        sleep(3.0)

        touch((500,500))
        sleep(3.0)

    for i in range(2):
        touch(Template(r"开始行动1.png", record_pos=(0.396, 0.229), resolution=(1920, 1080)))
        sleep(random.randint(1,3))

        touch(Template(r"开始行动2.png", record_pos=(0.362, 0.114), resolution=(1920, 1080)))
        sleep(350.0)

        touch((500,500))
        sleep(3.0)

        touch((500,500))
        sleep(3.0)

def material(loop, page):
    start1 = Template(r"tpl1592100806564.png", record_pos=(0.419, 0.231), resolution=(1920, 1080))
    start2 = Template(r"tpl1592101058502.png", record_pos=(0.359, 0.108), resolution=(1920, 1080))
    battle = Template(r"作战.png", record_pos=(0.26, -0.156), resolution=(1920, 1080))
    MENU = [398, 54]
    HOME = [143, 413]
    CHAPTER = Template(r"tpl1592100399932.png", record_pos=(0.011, 0.002), resolution=(1920, 1080))
    
    touch(battle)

    sleep(3)
        
    touch(CHAPTER)
    sleep(3)
    
    #最左边
        
    touch(page)
        
    for i in range(loop):    
        while not exists(start1):
            touch([500,500])
            sleep(20.0)
        touch(start1)
        sleep(5.0)
        touch(start2)
        sleep(115.0)
              
    while not exists(start1):
        touch([500,500])
        sleep(20.0)
    
    touch(MENU)
    sleep(3.0)
    
    touch(HOME)
page2_2 = Template(r"tpl1592101616234.png", record_pos=(0.254, -0.015), resolution=(1920, 1080))
material(3,page2_2)


# 打开程序
# # 


#     start_app("com.hypergryph.arknights")

#     sleep(random.randint(6, 8))

#     touch(Template(r"tpl1592072283758.png",
#                 record_pos=(-0.003, 0.249), resolution=(1920, 1080)))
#     sleep(random.randint(2, 3))

#     touch(Template(r"tpl1592072324171.png", record_pos=(
#         0.0, 0.119), resolution=(1920, 1080)))
#     sleep(random.randint(5, 7))

#     cailiao(2)

# 作战






