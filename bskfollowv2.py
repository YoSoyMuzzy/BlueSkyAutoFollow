import pyautogui
import subprocess
import time
from pynput import keyboard

# Path to the button image
BUTTON_IMAGE_PATH = 'C:\(location of screenshot of follow button)\image.png'
WINDOW_TITLE_KEYWORD = "Bluesky"  # Part of the window title to match Brave with Bluesky

# Variable to control the running state of the script
running = True

def get_window_bounds(window_title_keyword):
    """
    Get the bounds of the window matching the title keyword.
    """
    try:
        result = subprocess.check_output(["wmctrl", "-lG"]).decode("utf-8").splitlines()
        for line in result:
            if window_title_keyword.lower() in line.lower():
                parts = line.split()
                x, y, width, height = map(int, parts[2:6])
                return x, y, x + width, y + height
    except Exception as e:
        print(f"Error retrieving window bounds: {e}")
    return None

def scroll_page_down():
    """
    Scroll down by one page length using the 'Page Down' key.
    """
    pyautogui.press('pagedown')  # Press the 'Page Down' key to scroll by one screen length

def on_press(key):
    """
    Listener function for keyboard events. Stops the script if F10 is pressed.
    """
    global running
    if key == keyboard.Key.f10:
        print("F10 pressed, stopping the script.")
        running = False
        return False  # Stop the listener

def main():
    global running

    # Start the keyboard listener to detect F10 press
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    bounds = get_window_bounds(WINDOW_TITLE_KEYWORD)
    if not bounds:
        print(f"Window with title containing '{WINDOW_TITLE_KEYWORD}' not found!")
        return

    print(f"Target window found with bounds: {bounds}")
    while running:
        try:
            print("Searching for the button...")
            button_location = pyautogui.locateOnScreen(BUTTON_IMAGE_PATH, region=bounds, confidence=0.8)
            if button_location:
                button_x, button_y = pyautogui.center(button_location)
                print(f"Button found at {button_x}, {button_y}. Clicking...")
                pyautogui.click(button_x, button_y)
                time.sleep(0.1)
            else:
                raise pyautogui.ImageNotFoundException  # Trigger scroll if not found
        except pyautogui.ImageNotFoundException:
            print("Button not found. Scrolling down one page...")
            scroll_page_down()
            time.sleep(0.5)  # Delay to control the scroll interval

    listener.join()  # Wait for the listener to fully exit before closing the script

if __name__ == "__main__":
    main()
