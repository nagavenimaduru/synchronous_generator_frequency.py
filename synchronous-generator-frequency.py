print("==========================================")
print(" SYNCHRONOUS GENERATOR FREQUENCY CALCULATOR")
print("==========================================")

poles = int(input("Enter number of poles: "))
speed = float(input("Enter generator speed (RPM): "))

if poles <= 0 or speed <= 0:
    print("\nPlease enter valid positive values.")
elif poles % 2 != 0:
    print("\nNumber of poles should be an even number.")
else:
    frequency = (poles * speed) / 120

    print("\n------------- RESULTS -------------")
    print(f"Number of Poles    : {poles}")
    print(f"Generator Speed    : {speed:.2f} RPM")
    print(f"Generated Frequency: {frequency:.2f} Hz")
    print("-----------------------------------")
