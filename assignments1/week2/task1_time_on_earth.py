"""
This program can convert a given seconds into hours, minutes, seconds and print it
"""


def time_fun(input_second):
    """
    converts a given seconds into hours, minutes, seconds and return it
    """

    sec = input_second

    minute_scale = 60
    hour_scale = 60

    sec_remain = sec % minute_scale
    min_all = sec // minute_scale

    min_remain = min_all % hour_scale
    hour_remain = min_all // hour_scale

    return hour_remain, min_remain, sec_remain


print("TIME ON EARTH")
seconds = int(input("Input a time in seconds:\n"))
time = time_fun(seconds)
print(f"\nThe time on Earth is {time[0]} hours {time[1]} minutes and {time[2]} seconds.")
