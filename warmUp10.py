#Claire Yegian
#10/5/17
#warmUp10.py - prints wallpaper

from ggame import *

petal = Color(0xFF66B2,1)
stem = Color(0x006600,1)

dot = CircleAsset(5,LineStyle(1,petal),petal)
dot2 = CircleAsset(2,LineStyle(1,stem),stem)
line = LineAsset(0,10,LineStyle(3,stem))

for j in range(10): #prints the row 10 times
    for i in range(20): #prints one row of dots
        Sprite(line,(7 + 50 * i, 13 + 50 * j))
        Sprite(dot,(3 + 50 * i,4 + 50 * j))
        Sprite(dot,(12 + 50 * i, 13 + 50 * j))
        Sprite(dot,(3 + 50 * i, 12 + 50 * j))
        Sprite(dot,(12 + 50 * i, 5 + 50 * j))
        Sprite(dot2,(7 + 50 * i, 7 + 50 * j))
App().run()