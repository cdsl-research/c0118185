from machine import Pin, RTC
import network, urequests, utime
import ujson

def get_time():
    rtc = RTC()
    url_jst = "http://worldtimeapi.org/api/timezone/Asia/Tokyo" # see http://worldtimeapi.org/timezones
    retry_delay = 5000 # interval time of retry after a failed Web query
    response = urequests.get(url_jst)
    # parse JSON
    parsed = response.json()
    #parsed=ujson.loads(res) # in case string
    datetime_str = str(parsed["datetime"])
    year = int(datetime_str[0:4])
    month = int(datetime_str[5:7])
    day = int(datetime_str[8:10])
    hour = int(datetime_str[11:13])
    minute = int(datetime_str[14:16])
    second = int(datetime_str[17:19])
    subsecond = int(round(int(datetime_str[20:26]) / 1000)) # milliseconds 三桁まで
    # update internal RTC
    rtc.datetime((year, month, day, 0, hour, minute, second, subsecond))
    # setup day of the week
    daysOfTheWeek = "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"
    # get timestamp since 2000.1.1 from now
    am = utime.mktime(utime.localtime())
    tm = utime.localtime(utime.mktime(utime.localtime()))
    # generate formated date/time strings from internal RTC
    date_str = "{0:4d}/{1:02d}/{2:02d}".format(*rtc.datetime())
    time_str = "{4:02d}:{5:02d}:{6:02d}.{7:02d}".format(*rtc.datetime())
    date_ok = date_str + " " + time_str
    # due to the timestamp of micropython is not from 1970.1.1 which different from normal timestamp,
    # I have made a some change by number caculation to fill the 30-year vacancy.
    # 由于micropyhon的时间戳不同于正常的时间戳，是从2000/1/1开始计算（而非1970/1/1）。
    # 我在此处进行了一些数值的调整来填补30年的空白(9开头的数字是从1970年到2000年的秒数，后面是我自己测定的误差)
    # micropythonのタイムスタンプは従来のタイムスタンプと異なり, 1970/1/1ではなく2000/1/1からの数値ので,
    # それを従来のタイムスタンプに一致させるためにここで数値修正をしました。 
    am = (am+950745600-4093200)*1000 + subsecond
    return am