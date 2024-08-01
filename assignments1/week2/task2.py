def time_fun(input_second,scale_fun):
    #  converts a given seconds into hours, minutes, and seconds
    #  scale_fun -- a flag indicating whether to use Trisolaris time scales (True) or Earth time scales (False)

    sec = input_second

    if scale_fun == True:
        minute_scale = int(input("Input the number of seconds in a minute on Trisolaris:\n"))
        hour_scale = int(input("Input the number of minutes in an hour on Trisolaris:\n"))
    else:
        minute_scale = 60
        hour_scale = 60

    # Calculate the remain seconds after converting to minutes
    sec_remain = sec%minute_scale
    # Calculate the total minutes from the input seconds
    min_all = sec//minute_scale
    # Calculate the remain minutes after converting to hours
    min_remain = min_all%hour_scale
    # Calculate the remain number of hours
    hour_remain = min_all//hour_scale

    return(hour_remain,min_remain,sec_remain)



print("TIME ON EARTH")
seconds = int(input("Input a time in seconds:\n"))
time = time_fun(seconds,0)
print(f"\nThe time on Earth is {time[0]} hours {time[1]} minutes and {time[2]} seconds.")

print("TIME ON TRISOLARIS")
tri_time = time_fun(seconds,1)
print(f"\nThe time on Trisolaris is {tri_time[0]} hours {tri_time[1]} minutes and {tri_time[2]} seconds.")