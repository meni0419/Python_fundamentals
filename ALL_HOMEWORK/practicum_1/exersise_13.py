def sec_in_hour(sec):
    day = 0
    SD = 86400
    SH = 3600
    SM = 60
    if sec < 0:
        sec = abs(sec)
    if sec > SD:
        day = sec // SD
        sec = sec % SD
    hours = sec // SH
    minutes = (sec % SH) // SM
    seconds = sec % SM
    if day:
        print(f"{day}d:{hours}h:{minutes}m:{seconds}s")
    else:
        print(f"{hours}h:{minutes}m:{seconds}s")


s = int(input("Enter seconds: "))
sec_in_hour(s)
