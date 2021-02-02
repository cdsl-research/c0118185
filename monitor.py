import uping
import utime

a = input('Please enter the interval you want(seconds):')
try:
    num = int(a)
except ValueError:
    raise ValueError('An integer is required.')

while True:
    uping.ping('192.168.100.181')
    utime.sleep(num)
    