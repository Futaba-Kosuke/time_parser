working_time = 0

while True:
    start_time = input('開始時間 >> ')
    finish_time = input('終了時間 >> ')

    start_hour, start_minutes = [int(x) for x in start_time.split(':')]
    finish_hour, finish_minutes = [int(x) for x in finish_time.split(':')]

    working_time += (finish_hour + finish_minutes / 60) - (start_hour + start_minutes / 60)

    is_finish = input('まだ入力がありますか？ (y/n) ')
    if is_finish == 'n':
        break

print(f'勤務時間: {working_time}')
