# Month arrays mNLY (monthsNonLeapYear) mLY (monthsLeapYear)
mNLY = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mLY = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Leap years array
leapYears = [2024, 2028, 2032, 2036, 2040]

# Input
def userInput():
    M = int(input("What month is it (type in number form): "))
    D = int(input("What day is it (type in number form): "))
    Y = int(input("What year is it (type in number form ex (2023): "))
    return M, D, Y
M, D, Y = userInput()

# Calculations
def calculations(M, D, Y, mNLY, mLY, leapYears):
    monthsArray = mLY if Y in leapYears else mNLY

    # Uses a loop to calculate the total days till Christmas
    totalDays = 0
    for monthDays in monthsArray[M - 1:]:
        totalDays += monthDays
    #final calculation
    final = totalDays - D - 6
    return final

final = calculations(M, D, Y, mNLY, mLY, leapYears)

# Output
def output(final):
    print("There are", final, "days till Christmas")

output(final)
