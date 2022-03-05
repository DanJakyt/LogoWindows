#Windows Logo

from turtle import *
speed(1)
bgcolor('#003153')
penup()
goto(-50,60)
pendown()
color('#007FFF')
begin_fill()
goto(100,100)
goto(100,-100)



#Draw windows
goto(-50,-60)
goto(-50, 60)
end_fill()
color('#003153')
goto(15,100)



#cut 2 equal parts
color('#003153')
width(10)
goto(15,-100)
penup()
goto(100,0)
pendown()
goto(-100,0)
done()