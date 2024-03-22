from datetime import datetime

def daysUntilChristmas():
    today = datetime.today()
    christmas = datetime(today.year, 12, 25)

    if today > christmas:
        christmas = datetime(today.year + 1, 12, 25)

    delta = christmas - today
    return delta.days

# Add 1 in the output to get in line with the correct days till
print(f"There are {daysUntilChristmas()+1} days until Christmas.")