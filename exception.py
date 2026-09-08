# exception = an event that interrupts the flow of a rpogram
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.except, 3.finally

# 1 / 0
# 1 + "1"
# int("pizza")

try:
    number = int(input("enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("you can't divide by zero")
except ValueError:
    print("enter only number please!")
except Exception:
    print("something went wrong!")
finally:
    print("do some cleanup here")