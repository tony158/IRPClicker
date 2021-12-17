# IRP finder: find IRP appointment by clicking button automatically.

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import winsound
import random

wait_a_little = (12, 16)

chrome_driver_path = "C:/webdrivers/chromedriver.exe"
chrome_port = "localhost:8989"
many_times = 300

button_find_appointment = "btSrch4Apps"
xpath_no_appointment_text = "//tr[contains(.,'No appointment(s) are currently available')]"


def start_find_appointment():
    play_beep()
    opt = Options()
    opt.add_experimental_option("debuggerAddress", chrome_port)
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=opt)
    sleep(3)

    click_count = 0
    appointment_available = False
    while (not appointment_available) and (click_count <= many_times):
        handle_button_disabled(driver)
        appointment_available = click_and_check_available(driver)
        click_count += 1

    if appointment_available:
        print("********************found appointment! / or need to reload page!********************")
        play_beep(3000, 5)
    else:
        print("-----------------------no appointment found yet!----------------------------------")
        play_beep(1000)

    exit()


def handle_button_disabled(driver):
    button = driver.find_element(By.ID, button_find_appointment)
    if not button.is_enabled():
        print("***button is disabled***")
        to_enable = "document.getElementById('" + button_find_appointment + "').removeAttribute('disabled');"
        driver.execute_script(to_enable)
        sleep(3)
        print("***button is now:" + str(button.is_enabled()) + "***")


# return True: when appointments available or when you need to reload page
def click_and_check_available(driver):
    button = driver.find_element(By.ID, button_find_appointment)
    play_beep(300, 1)
    button.click()

    sleep(random.randint(wait_a_little[0], wait_a_little[1]))

    try:
        no_appointment_text = driver.find_element(By.XPATH, xpath_no_appointment_text)
        if no_appointment_text.is_displayed():
            return False
    except NoSuchElementException:
        return False
    return True


def play_beep(duration=1000, count=2):
    beep_count = 0
    while beep_count < count:
        winsound.Beep(440, duration)
        beep_count += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_find_appointment()
