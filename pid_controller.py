from ROBOT_CLASS import *
import matplotlib.pyplot as plt

def pid_run(robot, pgain, igain, dgain,  n, speed):
    x_position=[]
    y_position=[]
    integral=0
    previous_error = 0
    cte=robot.y

    for i in range(n):

        x_position.append(robot.x)
        y_position.append(robot.y)
        error = cte - previous_error

        pval = cte * pgain
        ival = integral * igain
        dval = dgain * (previous_error/0.5)

        steer = -pval - ival - dval

        integral += cte*0.5
        previous_error = cte
        cte=robot.y

        robot.move(steer, speed)

    plt.plot(x_position,y_position)
    plt.show()