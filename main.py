# IRP finder: find IRP appointment by clicking button automatically.

from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import winsound
import random

chrome_driver_path = "C:/webdrivers/chromedriver.exe"
chrome_port = "localhost:8989"
many_times = 300
waiting_time = [15, 20]

button_id_find_appointment = "btSrch4Apps"
no_appointment_text_xpath = "//tr[contains(.,'No appointment(s) are currently available')]"


def play_beep(duration=1000, count=2):
    beep_count = 0
    while beep_count < count:
        winsound.Beep(440, duration)
        beep_count += 1


# return True, when available appointments are found or need to reload page
def click_and_check_availability(driver):
    button = driver.find_element(By.ID, button_id_find_appointment)
    play_beep(300, 1)
    button.click()

    sleep(random.randint(waiting_time[0], waiting_time[1]))

    try:
        no_appointment_text = driver.find_element(By.XPATH, no_appointment_text_xpath)
        if no_appointment_text.is_displayed():
            return False
    except NoSuchElementException:
        return False
    return True


def start_find_appointment():
    play_beep()

    opt = Options()
    opt.add_experimental_option("debuggerAddress", chrome_port)
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=opt)
    sleep(3)

    click_count = 0
    appointment_available = False
    while (not appointment_available) and (click_count <= many_times):
        appointment_available = click_and_check_availability(driver)
        click_count += 1

    if appointment_available:
        print("********************found appointment! / or need to reload page!********************")
        play_beep(3000, 5)
        exit()

    print("-----------------------no appointment found yet!----------------------------------")
    play_beep(1000)
    exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_find_appointment()
