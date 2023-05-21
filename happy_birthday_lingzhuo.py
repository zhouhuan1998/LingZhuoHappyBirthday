import threading
import itertools
import time
import sys
import os
from multiprocessing import Process,Lock
from pyfiglet import Figlet



def printLine(line1, index):
    for i in range (0, index):
        print('\x1b[2K', end='\r')
        print('\n')
        #print(line1)
        print("{}".format(line1), end='\r')
        time.sleep(0.2)
    
def clear(index):
    for i in range(0, index):
        print('\033[F', end = '\r')
    print('\n')

def drawCake():
    line1 = "  ****************************"
    line2 = "    ||                    ||"
    line3 = "    ======================="
    line4 = "        ||           ||"
    line5 = "         ============="
    line6 = "            |  |  |"
    line7 = "            *  *  *"
    
    printLine(line1, 10)
    clear(20)
    printLine(line2, 8)
    clear(18)
    printLine(line2, 7)
    clear(16)
    printLine(line3, 6)
    clear(14)
    printLine(line4, 5)
    clear(12)
    printLine(line4, 4)
    clear(10)
    printLine(line5, 3)
    clear(8)
    printLine(line6, 2)
    clear(6)
    printLine(line7, 1)

def drawTextAndClear(text:str, s:int):
    f = Figlet(font='xhelvi')
    print(f.renderText(text))
    time.sleep(s)
    os.system("clear")

def drawHeart(text:str):
    print('\n'.join([''.join([(text[(x-y) %len(text)] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ') for x in range(-50, 50)]) for y in range(30, -30, -1)]))

if __name__ == '__main__':
    drawCake() 

    drawTextAndClear('HAPPY BIRTHDAY', 2)
    drawTextAndClear('LING ZHUO', 2)


    drawHeart('Ling Zhou Happy Birthday ')
    time.sleep(5)
    os.system("clear")

    drawTextAndClear('MADE BY ZHOUHUAN', 2)

    