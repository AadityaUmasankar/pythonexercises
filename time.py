a = '05:00:56PM'


if a[-2:] == "AM" and a[:2] == "12":
    print("00" + a[2:-2])
elif a[-2:] == "AM":
    print(a[:-2])
elif a[-2:] == "PM" and a[:2] == "12":
    print(a[:-2])
else:
    print(str(int(a[:2]) + 12) + a[2:8])

