import pyautogui
import pyperclip
import time


time.sleep(3)
with open("Sims_Skills.txt", 'r') as skill_cheat:
    skills = skill_cheat.readlines()
    for skill in skills:
        pyperclip.copy(skill)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.1)
        pyautogui.press("enter")
        time.sleep(0.1  )