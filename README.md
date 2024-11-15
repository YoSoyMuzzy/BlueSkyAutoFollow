# BlueSkyAutoFollow
On Bluesky, pull up someones follower or following page, start the script, and watch it go. Press F10 to kill it. 
You have to update the BUTTON_IMAGE_PATH variable in the script to the location of the image.png on your hard drive. The bot looks for that image to compare to the web page and know what to click. 

Dependinces needed for Linux
wmctrl pyautogui pynput

For Debian
pip install pyautogui pynput
sudo apt-get install wmctrl  # To install wmctrl for window management

Windows version should run OOTB but I haven't tested it.


Dependencies for Linux
pyautogui pynput wmctrl  # To install wmctrl for window management

Dependencies for Both Windows and Linux:
pyautogui: For GUI automation (screen interaction, mouse/keyboard control).
pynput: For listening to keyboard events (to stop the script using F10).
pygetwindow (Windows only): For interacting with window management (alternative to wmctrl on Windows).
wmctrl (Linux only): For interacting with window management (to get window bounds).

Windows:

pip install pyautogui pynput pygetwindow

Linux:

pip install pyautogui pynput

sudo apt-get install wmctrl  # For Ubuntu/Debian systems
