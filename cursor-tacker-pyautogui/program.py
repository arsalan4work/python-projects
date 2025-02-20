import pyautogui
import time
import pyperclip

# Step 1: Move to the WhatsApp icon and click to open the application
# (Specify the exact position where the WhatsApp icon is located)
pyautogui.moveTo(708,748, duration=0.5)
pyautogui.click()

# Allow time for WhatsApp to open
time.sleep(2)

# Step 2: Move to the chat where you want to send a message
# (Specify the exact position of the chat in WhatsApp UI)
pyautogui.moveTo(306,178, duration=0.5)
pyautogui.click()

# Allow some time for the chat to load
time.sleep(1)

# Step 3: Move to the message text box to type a message
# (Specify the exact position of the text input box)
pyautogui.moveTo(649,704, duration=0.5)
pyautogui.click()

# Step 4: Type the auto-reply message
message = "Hello World"
pyperclip.copy(message)  # Copy the message to clipboard
pyautogui.hotkey('ctrl', 'v')  # Paste the message into the text box

time.sleep(2)

# Step 5: Press Enter to send the message
pyautogui.press('enter')

time.sleep(2)

pyautogui.moveTo(1344,17, duration=1)
pyautogui.click()

print("Auto-reply message sent successfully!")
