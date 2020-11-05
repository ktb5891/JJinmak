def cal(lastTm,Travel_time):
    hour=int(lastTm[:2])
    min=int(lastTm[2:])
    minus_min=int(Travel_time)%60
    minus_hour=int(Travel_time)//60
    temp_min= min-minus_min
    if temp_min<0:
        hour-=1
        min=60+temp_min
    else:
        min=temp_min
    temp_hour = hour-minus_hour
    if temp_hour<0:
        hour=24+temp_hour
    else:
        hour = temp_hour
    if hour < 3:
        hour += 24
    if min == 0:
        min = "00"
    return str(hour)+str(min)

