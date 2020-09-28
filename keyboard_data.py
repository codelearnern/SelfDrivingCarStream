import keyboard

def keysOutput():
    output = [0, 0, 0, 0, 0, 0, 0, 0, 0] # w,a,s,d,wa,wd,sa,sd,nk

    if keyboard.is_pressed("w") and keyboard.is_pressed("a"):
        output[4] = 1
    elif keyboard.is_pressed("w") and keyboard.is_pressed("d"):
        output[5] = 1
    elif keyboard.is_pressed("s") and keyboard.is_pressed("a"):
        output[6] = 1
    elif keyboard.is_pressed("s") and keyboard.is_pressed("d"):
        output[7] = 1
    elif keyboard.is_pressed("w"):
        output[0] = 1
    elif keyboard.is_pressed("a"):
        output[1] = 1
    elif keyboard.is_pressed("s"):
        output[2] = 1
    elif keyboard.is_pressed("d"):
        output[3] = 1
    else:
        output[8] = 1

    return output

while True:
    print(keysOutput())