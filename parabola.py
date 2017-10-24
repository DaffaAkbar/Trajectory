import math as mt
import matplotlib.pyplot as pl

def main():
    gravity=9.807
    #input initial velocity
    v=int(input("initial velocity?"))
    angle=mt.radians(int(input("angle?")))
    vx=v* mt.cos(angle)
    vy=v*mt.sin(angle)
    #record time of flight in miliseconds
    time_of_flight=(((2*v)*(mt.sin(angle)/gravity)*1000))
    #project the vector
    x=[vx*(x/1000)for x in range(0,int(time_of_flight))]
    y=[(vy*(x/1000))-((gravity*((x/1000)**2))/2)for x in range(0,int(time_of_flight))]
    #print the line
    pl.plot(x,y)

    pl.title("parabola")
    pl.xlabel("distance")
    pl.ylabel("height")
    #ask for another graph
    j=input("do you want another graph?")
    if j =="y":
        main()
    else:
        pl.show()
main()

