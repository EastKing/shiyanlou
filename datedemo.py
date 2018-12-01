#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from datetime import datetime,timedelta,timezone

def to_timestamp(dt_str,tz_str):

    #提取时区
    tz=re.match(r'UTC([+-]\d+):\d+',tz_str).group(1)
    print(tz)

    #str转datetime
    dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    print(dt)

    #本地时间转化为UTC时间
    replaced_tz=timezone(timedelta(hours=int(tz)))
    replaced_dt=dt.replace(tzinfo=replaced_tz)
    print(replaced_dt)

    #datetime转timestamp
    return replaced_dt.timestamp()





if __name__ == '__main__':
    t1=to_timestamp('2015-6-1 08:10:30','UTC+7:00')
    assert t1==1433121030.0,t1

    t2=to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
    assert t2==1433121030.0, t2

    print('ok')