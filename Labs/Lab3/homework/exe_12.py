def is_inside(x,y):
    if len(y) == 2:
        if x[0] <= y[0] and x[1] <= y[1]:
            print("ok")
        else:
            print("fail")

    elif len(y) == 4:
        if y[0] <= x[0] <= y[0] + y[2] and y[1] <= x[1] <= y[1] + y[3]:
            print("ok")
        else:
            print("fail")

is_inside([100, 120], [140, 60])

is_inside([200, 120], [140, 60, 100, 200])