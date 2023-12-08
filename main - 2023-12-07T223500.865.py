def check_health(steps_taken):
    # Define healthy step ranges
    min_healthy_steps = 5000
    max_healthy_steps = 10000

    # Check if steps taken are within the healthy range
    if min_healthy_steps <= steps_taken <= max_healthy_steps:
        return "Your steps are within a healthy range. Keep it up!"
    elif steps_taken < min_healthy_steps:
        return "You may want to take more steps for better health."
    else:
        return "You've taken a lot of steps! It's great, but ensure you're not overdoing it."

def main():
    try:
        # Get the number of steps taken from the user
        steps = int(input("Enter the number of steps you've taken today: "))

        # Check and print the health status
        result = check_health(steps)
        print(result)

    except ValueError:
        print("Please enter a valid number for steps.")

if __name__ == "__main__":
    main()
