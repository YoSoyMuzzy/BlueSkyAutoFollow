import pyautogui
import subprocess
import time
from pynput import keyboard
import pygetwindow as gw

# Path to the button image (make sure to use a raw string or double backslashes for Windows paths)
BUTTON_IMAGE_PATH = r'C:\path\to\your\button_image.png'  # Example path
WINDOW_TITLE_KEYWORD = "Bluesky"  # Part of the window title to match Brave with Bluesky

# Variable to control the running state of the script
running = True

def get_window_bounds(window_title_keyword):
    """
    Get the bounds of the window matching the title keyword (Windows version).
    """
    try:
        # Get all windows with titles containing the keyword
        windows = gw.getWindowsWithTitle(window_title_keyword)
        if windows:
            win = windows[0]  # Get the first window that matches
            return win.left, win.top, win.right, win.bottom
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
