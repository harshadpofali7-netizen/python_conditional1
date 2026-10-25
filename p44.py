# Program to check traffic signal actions using match-case

signal = input("Enter traffic signal color (Red/Yellow/Green): ").lower()

match signal:
    case "red":
        print("🔴 Stop! Vehicles must not move.")
    case "yellow":
        print("🟡 Get Ready! Vehicles should slow down and prepare to stop.")
    case "green":
        print("🟢 Go! Vehicles can move ahead.")
    case _:
        print("❌ Invalid input! Please enter Red, Yellow, or Green.")