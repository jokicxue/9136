def time_fun(input_second):
    sec = input_second

    minute_scale = 60
    hour_scale = 60

    # Calculate the remain seconds after converting to minutes
    sec_remain = sec % minute_scale
    # Calculate the total minutes from the input seconds
    min_all = sec // minute_scale
    # Calculate the remain minutes after converting to hours
    min_remain = min_all % hour_scale
    # Calculate the remain number of hours
    hour_remain = min_all // hour_scale

    return (hour_remain, min_remain, sec_remain)


print("TIME ON EARTH")
seconds = int(input("Input a time in seconds:\n"))
time = time_fun(seconds)
print(f"\nThe time on Earth is {time[0]} hours {time[1]} minutes and {time[2]} seconds.")