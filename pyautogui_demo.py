import pyautogui
import time
import openpyxl
import pyperclip

pyautogui.FAILSAFE = True  # Enable fail-safe feature
pyautogui.PAUSE = 1  # Set a pause duration between actions

pyautogui.alert("The script will start in 5 seconds. Please switch to the application you want to automate.")
time.sleep(5)  # Wait for 5 seconds before starting the automation 

# Example automation: Step1 open chrome
pyautogui.hotkey('win', 'r')  # Open the Run dialog
time.sleep(1)  # Wait for the Run dialog to open
pyautogui.typewrite('chrome\n')  # Type 'chrome' and press Enter
time.sleep(3)  # Wait for Chrome to open

# Example automation: Step2 open a weather website
pyautogui.typewrite('https://www.accuweather.com/en/in/bengaluru/204108/weather-forecast/2041081\n' )  # Type the URL

# Example automation: Step3 take todays weather information
pyautogui.hotkey('ctrl', 'l')  # Focus on the address bar
time.sleep(1)  # Wait for the address bar to be focused

# Example automation: Step4 copy the weather information
pyautogui.hotkey('ctrl', 'c')  # Copy the weather information

# Example automation: Step5 create a excel file with name daily_weather_todaysdate.xlsx
import datetime

today = datetime.date.today()
file_name = f'daily_weather_{today}.xlsx'

def create_excel_file(file_name):
    workbook = openpyxl.Workbook()
    workbook.save(file_name)

create_excel_file(file_name)

#Example automation: Step6 open excel
pyautogui.hotkey('win', 'r')  # Open the Run dialog
time.sleep(1)  # Wait for the Run dialog to open
pyautogui.typewrite('excel\n')  # Type 'excel' and press Enter
time.sleep(2)  # Wait for Excel to open 
workbook = openpyxl.load_workbook(file_name)
sheet = workbook.active
sheet['A1'] = str(today)  # Write today's date in the first cell
sheet['A2'] = pyperclip.paste()  # Paste the weather information
sheet['A3'] = 'Good Weather Information'  # Write "Weather Information" in the third cell
workbook.save(file_name)     # writes it to disk

print(f"Excel file '{file_name}' created successfully.")

# Example automation: Step10 close the workbook
pyautogui.hotkey('ctrl', 'w')  # Close the workbook

# Example automation: Step11 close the browser
pyautogui.hotkey('alt', 'f4')  # Close the browserhttps://www.accuweather.com/en/in/bengaluru/204108/weather-forecast/2041081
