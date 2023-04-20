days = int(input('Numbers of days: '))
hours_per_day = days*24
minutes_per_day = 60*hours_per_day
seconds_per_day = 60*minutes_per_day

print('There are ', hours_per_day, 'hours ',
      minutes_per_day, 'minutes', 'and ', seconds_per_day,
      'seconds in ', days, 'days.')