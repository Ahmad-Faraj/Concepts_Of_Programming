daily_steps = list(map(int, input("Enter the steps taken each day in a month\n").split()))

highest_steps = max(daily_steps)

lowest_steps = min(daily_steps)

average_steps = sum(daily_steps) / len(daily_steps)

daily_steps.sort()
daily_steps.reverse()

print("\nResults:")
print(f"Highest no. of daily steps: {highest_steps}")
print(f"Lowest no. of daily steps: {lowest_steps}")
print(f"Average no. of daily steps: {average_steps:.3f}")
print(f"Steps in Desc order: {daily_steps}")
