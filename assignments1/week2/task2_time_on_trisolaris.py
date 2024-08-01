"""
This program can convert a given seconds into hours, minutes and seconds.
It then shows the result according to custom-defined scales.
"""


def time_convert(input_second, trisolaris_function):
    """
    converts a given seconds into hours, minutes, seconds and return it
    could choose custom-defined time scales
    """
    sec = input_second

    if trisolaris_function is True:
        minute_scale = int(input("Input the number of seconds in a minute on Trisolaris:\n"))
        hour_scale = int(input("Input the number of minutes in an hour on Trisolaris:\n"))
    else:
        minute_scale = 60
        hour_scale = 60

    sec_remain = sec % minute_scale
    min_all = sec // minute_scale

    min_remain = min_all % hour_scale
    hour_remain = min_all // hour_scale

    return hour_remain, min_remain, sec_remain


print("TIME ON EARTH")
seconds = int(input("Input a time in seconds:\n"))
time = time_convert(seconds, 0)
print(f"\nThe time on Earth is {time[0]} hours {time[1]} minutes and {time[2]} seconds.")

print("TIME ON TRISOLARIS")
trisolaris_time = time_convert(seconds, 1)
print(f"\nThe time on Trisolaris is {trisolaris_time[0]} hours {trisolaris_time[1]} minutes \
and {trisolaris_time[2]} seconds.")
