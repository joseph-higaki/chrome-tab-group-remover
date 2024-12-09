import pyautogui
import time

def focus_chrome_window():
    print("Open the Chrome window in the left up most portion of your desktop")
    print("Waiting 3 seconds to allow manual focus...")
    time.sleep(3)

def click_on_tab_group():
    """
    Clicks on the tab group menu
    Adjust the coordinates as per your screen resolution.
    """
    # Coordinates where the tab group exists (change according to your screen layout)
    # Use pyautogui.position() to identify the coordinates of your tab group
    tab_group_coordinates = (50, 150)  # Example coordinates

    print(f"Clicking on tab group at {tab_group_coordinates}...")
    pyautogui.click(*tab_group_coordinates)
    time.sleep(0.5)  # Wait for the context menu to open


def delete_tab_group(i):
    """
    Select the 'Delete Group' option from the tab group context menu using keys
    """    
    print(f"Deleting the tab group ({i})...")
    time.sleep(0.5)    
    # Navigate the context menu (use arrow keys or find Delete Group coordinates)
    # Simulate key presses
    pyautogui.typewrite(['down'])
    pyautogui.typewrite(['down'])    
    pyautogui.typewrite(['apps'])
    time.sleep(0.2)
    pyautogui.typewrite(['down'])
    pyautogui.typewrite(['down'])
    pyautogui.typewrite(['down'])
    time.sleep(0.2)
    pyautogui.typewrite(['enter'])     

def main():        
    focus_chrome_window()
    i = 4
    while i > 0:
        click_on_tab_group()
        delete_tab_group(i)
        i -= 1

if __name__ == "__main__":
    main()
