def time_fun(input_second,minute_scale,hour_scale):
    #  converts a given seconds into hours, minutes, and seconds
    #  based on custom define time scales
    sec = input_second

    # Calculate the remaining seconds after converting to minutes
    sec_remain = sec%minute_scale
    # Calculate the total number of minutes from the input seconds
    min_all = sec//minute_scale
    # Calculate the remaining minutes after converting to hours
    min_remain = min_all%hour_scale
    # Calculate the remain number of hours
    hour_remain = min_all//hour_scale

    return(hour_remain,min_remain,sec_remain)

print("TIME ON EARTH")
seconds = int(input("Input a time in seconds:\n"))
time = time_fun(seconds,60,60)
print(f"\nThe time on Earth is {time[0]} hours {time[1]} minutes and {time[2]} seconds.")

print("TIME ON TRISOLARIS")
minute_scale = int(input("Input the number of seconds in a minute on Trisolaris:\n"))
hour_scale = int(input("Input the number of minutes in an hour on Trisolaris:\n"))
# input the time scales
tri_time = time_fun(seconds,minute_scale,hour_scale)
print(f"\nThe time on Trisolaris is {tri_time[0]} hours {tri_time[1]} minutes and {tri_time[2]} seconds.")

print("TIME AFTER WAITING ON TRISOLARIS")
duration = int(input("Input a duration in seconds:\n"))
wait_time = time_fun(seconds+duration,minute_scale,hour_scale)
# input the seconds and the duration
print(f"\nThe time on Trisolaris after waiting is {wait_time[0]} hours {wait_time[1]} minutes and {wait_time[2]} seconds.")