import pyautogui
import time

# Give time to switch to the browser
print("You have 5 seconds to switch to the browser window...")
time.sleep(5)

# Coordinates of the URL bar (Adjust if needed)
x, y = 14000, 750  # Adjust these based on your screen resolution and browser

# Move the mouse and click on the URL bar
pyautogui.moveTo(x, y, duration=0.5)  # Smooth movement
pyautogui.click()

# Type the URL
pyautogui.write("https://www.google.com", interval=0.5)  # Adjust typing speed if needed

# Press Enter
pyautogui.press("enter")

print("URL entered successfully!")
