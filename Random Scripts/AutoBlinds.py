import datetime


def control_blinds():
    # gets current date time
    now = datetime.datetime.now()
    # formats date time
    current_time = now.strftime("%H:%M")

    open_time = "07.00"
    close_time = "20.00"

    if current_time >= open_time and current_time < close_time:
        print("Blinds open")
    else:
        print('Blinds closed')


control_blinds()
