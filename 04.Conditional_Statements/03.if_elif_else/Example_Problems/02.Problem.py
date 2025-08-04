# Enter time (24 hr format). If 5-11: Moring, 12-17:Aternoon, 18-21:Evening, else:Night

time=22

if time>=5 and time<=11:
    print("Moring")
elif time>=12 and time<=17:
    print("Afternoon")
elif time>=18 and time<=21:
    print("Evening")
else:
    print("Night")
