from time import *
import random

def mistakes(original,typed):
    error=0
    length=min(len(original),len(typed))
    for i in range(length): 
        if original[i] != typed[i]:
            error = error + 1
    error = error + abs(len(original) - len(typed))
        
    return error

def speed(typed,time3):
    words=len(typed.split())
    sped= words / time3*60
    print(f"The speed of ur typing is {sped:.2f}words/min")

para=[ "Dominic Toretto lives by one rule—family comes first. Whether it's behind the wheel or facing impossible odds, he never backs down from protecting those he loves",
        "Brian O' Conner started as an undercover cop but found a brother in Dom. His loyalty shifted from the law to the streets, proving that trust is earned where the pavement end",
        "Han was always the smoothest guy in the room, whether snacking on chips or drifting through Shibuya. His return shocked everyone, proving that in this world, nobody stays gone forever."]

choice=random.choice(para)
print("--------------------------Speed typing test------------------------------------")
print(choice)
time1=time()
data=input("Enter >>>")
time2=time()
time3=time2-time1
print(f"{time3:.2f}s")
mis=mistakes(choice,data)
print(f"The errors in your typed paragraph is {mis} errors")
speed(data,time3)
percentage_of_error = (mis / len(choice)) * 100
print(f"The percentage of error is {percentage_of_error:.2f}%")