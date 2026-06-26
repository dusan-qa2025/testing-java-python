import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import getpass

BASE_URL = "https://www.it-akademija.com/"

def test_ita_platform():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Odlazak na sajt
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 20)

    dl_platform_link = wait.until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "DL platforma"))
    )
    dl_platform_link.click()

    # Login forma
    username_input = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='text']"))
    )
    username_text = input("Unesite korisnicko ime: ").strip()
    username_input.send_keys(username_text)

    password_input = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
    )
    password_text = getpass.getpass("Unesite sifru: ").strip()
    password_input.send_keys(password_text)

    login_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    login_button.click()

    # Otvoriti bocni meni 
    # Sacekati da skloni loading element
    wait.until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "loadingoverlay"))
    )

    # taster u side bar-u - klik na njega
    side_menu_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.sidebar-toggler"))
    )
    
    side_menu_button.click()

    # Servisi za korisnika klik
    user_services_link = wait.until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Servisi za korisnika"))
    )
    user_services_link.click()

    # Video arhiva klik
    video_archive_link = wait.until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Video arhiva"))
    )
    video_archive_link.click()

    # cekamo da nestane loader
    wait.until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "loadingoverlay"))
    )

    # provera da li smo u video arhivi
    video_archive_section = wait.until(
        EC.visibility_of_element_located((By.ID, "video-arhiva"))
    )

    assert "LIVE CLASS ARHIVA" in video_archive_section.text

    # Pretraga

    search_input = wait.until(
        EC.visibility_of_element_located((By.ID, "search"))
    )
    search_input.clear()
    search_input.send_keys("python")

    search_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "subPretrazi"))
    )
    search_btn.click()

    wait.until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "loadingoverlay"))
    )

    results_container = wait.until(
        EC.visibility_of_element_located((By.ID, "lcs_results"))
    )

    assert results_container.is_displayed()

    # da li postoji element koji pokrece video
    # ocekujemo da bude bar 1 (duzina liste > 0)
    video_results = results_container.find_elements(By.CLASS_NAME, "startvideo")
    assert len(video_results) > 0

    time.sleep(5)
    driver.quit()