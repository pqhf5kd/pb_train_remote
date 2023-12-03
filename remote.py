from pybricks.hubs import CityHub
from pybricks.pupdevices import Motor, Light, Remote
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = CityHub()
motor = Motor(Port.A)
light = Light(Port.B)
myremote = Remote(timeout=10000)

#user configuration
#minimum speed - the speed which the motor begins accelerating from
minspeed = 50
#minimum target speed - the speed of the first step
mintspeed = 225
#maximum target speed - the speed of the final step
maxtspeed = 750
#steps - the numbers of speed steps - must be greater than 1.
steps = 8
#acceleration - the higher the number, the quicker the acceleration
a = 5



#targetspeed
tspeed = 0
#currentspeed
cspeed = 0
#next step 
nstep = (maxtspeed-mintspeed)/(steps-1)
wpressed = ()

hub.light.on(Color.ORANGE)

def remote():
    global minspeed,mintspeed,a,tspeed,cspeed,wrpessed
    while True:
        if tspeed > 0:
            myremote.light.on(Color.ORANGE)
        elif tspeed < 0:
            myremote.light.on(Color.ORANGE)
        else:
            myremote.light.on(Color.RED)
        light.on(50)
        wpressed = myremote.buttons.pressed()
        if Button.LEFT_PLUS in wpressed:
            if tspeed is 0:
                tspeed = mintspeed
            elif tspeed is -mintspeed:
                tspeed = 0
            elif tspeed >= maxtspeed:
                tspeed = tspeed
            else:
                tspeed = tspeed+nstep
        if Button.LEFT_MINUS in wpressed:
            if tspeed is 0:
                tspeed = -mintspeed
            elif tspeed is mintspeed:
                tspeed = 0
            elif tspeed <= -maxtspeed:
                tspeed = tspeed
            else:
                tspeed = tspeed-nstep
        if Button.LEFT in wpressed:
            tspeed = 0
            cspeed = 0
        if Button.CENTER in wpressed:
            system.shutdown()
        print(tspeed)
        while wpressed:
            wpressed = myremote.buttons.pressed()
        if tspeed > cspeed and cspeed is 0:
            cspeed = minspeed
        elif tspeed > cspeed:
            cspeed = cspeed+a
        elif tspeed < cspeed and cspeed is 0:
            cspeed = -minspeed
        elif tspeed < cspeed:
            cspeed = cspeed-a
        print(cspeed)
        if cspeed is 0:
            motor.stop()
        else:
            motor.run(cspeed)

remote()