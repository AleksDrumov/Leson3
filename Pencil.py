charge_workminutes_for_one_second = 2
charge_time = int(input('сколько минут заряжать?'))
charge_time_in_a_seconds = charge_time * 60
work_time_in_a_minutes = charge_time_in_a_seconds * charge_workminutes_for_one_second
work_time_in_a_hours = work_time_in_a_minutes / 60
work_time_in_a_hours = int(work_time_in_a_hours)
if work_time_in_a_hours > 20:
    work_time_in_a_hours = 20
print(work_time_in_a_hours,'hours будет работать')
#У меня максимумум часов 20 работы
#я бы мог сделать свою версию с модулями, но это просто понты и мне лень(и вам может тоже))))))


