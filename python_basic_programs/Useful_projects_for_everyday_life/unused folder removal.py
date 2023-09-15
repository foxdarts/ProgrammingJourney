import os
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import turtle

def is_unused_folder(folder, days_threshold, current_time):
    seconds_in_a_day = 24 * 60 * 60  # seconds in a day
    accessed_time = os.path.getatime(folder)
    return current_time - accessed_time > days_threshold * seconds_in_a_day

def list_unused_folders(base_directory, days_threshold):
    print(f'Finding folders not accessed in the last {days_threshold} days in {base_directory}:')
    
    unused_folders = []
    current_time = time.time()
    
    with ThreadPoolExecutor() as executor:
        for root, dirs, _ in os.walk(base_directory):
            if executor.submit(is_unused_folder, root, days_threshold, current_time).result():
                unused_folders.append(root)
    
    return unused_folders

def elapsed_timer():
    start_time = time.time()
    while not finished[0]:
        elapsed_time = time.time() - start_time
        timer_display.clear()
        timer_display.write(f"Elapsed time: {elapsed_time:.2f} seconds", align="center", font=("Arial", 16, "normal"))
        time.sleep(1)

if __name__ == "__main__":
    finished = [False]
    days_threshold = 30  # Adjust the threshold as needed
    
    # Set up the turtle screen
    screen = turtle.Screen()
    screen.title("Elapsed Timer")
    screen.bgcolor("white")
    screen.setup(width=500, height=100)
    screen.tracer(0)
    
    # Set up the timer display turtle
    timer_display = turtle.Turtle()
    timer_display.color("black")
    timer_display.penup()
    timer_display.hideturtle()
    timer_display.goto(0, 0)
    
    # Start the elapsed timer thread
    timer_thread = Thread(target=elapsed_timer)
    timer_thread.start()
    
    drives_to_scan = ['D:', 'E:', 'F:']  # Add more drives if needed
    
    for drive in drives_to_scan:
        if os.path.exists(drive):
            unused_folders = list_unused_folders(drive, days_threshold)
            
            # Display the results for the current drive
            if unused_folders:
                print(f"\nUnused folders in drive {drive}:")
                for folder in unused_folders:
                    print(folder)
            else:
                print(f"\nNo unused folders found in drive {drive}.")
        else:
            print(f"\nDrive {drive} does not exist.")
    
    # Set the flag to indicate that the main code has finished
    finished[0] = True
    
    # Join the timer thread to make sure it has finished before proceeding
    timer_thread.join()
    
    # Keep the Turtle window open until it's closed by the user
    turtle.done()

