import uping
import utime

target = '192.168.100.175'
a = input('Please enter the interval you want(seconds):')
try:
    num = int(a)
except ValueError:
    raise ValueError('An integer is required.')

while True:
    aaa = uping.ping(target,10,interval=1000)
    utime.sleep(num)
    if aaa[0] > aaa[1]:
        print("Packet lossing")
    elif aaa[0] == aaa[1]:
        print("Normal")
    else:
        raise ValueError('Unexpected Error occured.')