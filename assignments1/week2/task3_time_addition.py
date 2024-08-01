"""
This program can convert a given number of seconds into hours, minutes and seconds.
It then shows the time including the added duration according to custom-defined scales
"""


def time_convert(input_second, minute_scale, hour_scale):
    """
    converts a given seconds into hours, minutes, seconds and return it
    based on custom define time scales
    """
    sec = input_second

    sec_remain = sec % minute_scale
    min_all = sec // minute_scale

    min_remain = min_all % hour_scale
    hour_remain = min_all // hour_scale

    return hour_remain, min_remain, sec_remain


print("TIME ON EARTH")
seconds = int(input("Input a time in seconds:\n"))
time = time_convert(seconds, 60, 60)
print(f"\nThe time on Earth is {time[0]} hours {time[1]} minutes and {time[2]} seconds.")

print("TIME ON TRISOLARIS")
minute_scale_global = int(input("Input the number of seconds in a minute on Trisolaris:\n"))
hour_scale_global = int(input("Input the number of minutes in an hour on Trisolaris:\n"))
trisolaris_time = time_convert(seconds, minute_scale_global, hour_scale_global)
print(f"\nThe time on Trisolaris is {trisolaris_time[0]} hours {trisolaris_time[1]} minutes \
and {trisolaris_time[2]} seconds.")

print("TIME AFTER WAITING ON TRISOLARIS")
duration = int(input("Input a duration in seconds:\n"))
duration_time = time_convert(seconds+duration, minute_scale_global, hour_scale_global)
# input the seconds and the duration
print(f"\nThe time on Trisolaris after waiting is {duration_time[0]} hours {duration_time[1]} minutes \
and {duration_time[2]} seconds.")
