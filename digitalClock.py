import time

def digital_clock():
    while True:
        # Get current time
        current_time = time.strftime("%H:%M:%S", time.localtime())

        # Clear the screen (for better visual)
        print("\033[H\033[J")

        # Display the current time
        print("Digital Clock")
        print(current_time)

        # Wait for one second before updating the time
        time.sleep(1)

# Run the digital clock
digital_clock()
