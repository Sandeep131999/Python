from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import random
import time
import os

# ================= CONFIG =================
MAX_LIKES = 100
MIN_DELAY = 2
MAX_DELAY = 4
LIKE_RATIO = 0.85
# ==========================================

like_count = 0
pass_count = 0


def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")


# ---------- BROWSER SETUP ----------
def create_driver():
    from webdriver_manager.chrome import ChromeDriverManager

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )

    return driver


# ---------- HELPERS ----------
def wait_for_buttons(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "button"))
    )


def ensure_encounters(driver):
    if "encounters" not in driver.current_url:
        log("Navigating to Encounters...")
        driver.get("https://badoo.com/encounters/")
        WebDriverWait(driver, 10).until(
            EC.url_contains("encounters")
        )


def dismiss_popups(driver):
    try:
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for btn in buttons:
            text = (btn.text or "").lower()
            if text in ["allow", "not now", "skip", "no thanks", "accept"]:
                driver.execute_script("arguments[0].click();", btn)
                return True
    except:
        pass
    return False


def click_button(driver, keywords):
    buttons = driver.find_elements(By.TAG_NAME, "button")

    for btn in buttons:
        try:
            aria = (btn.get_attribute("aria-label") or "").lower()
            cls = (btn.get_attribute("class") or "").lower()

            if any(k in aria or k in cls for k in keywords):
                driver.execute_script("arguments[0].click();", btn)
                return True
        except:
            continue

    return False


def click_like(driver):
    return click_button(driver, ["like", "yes"])


def click_pass(driver):
    return click_button(driver, ["pass", "no", "skip"])


# ---------- MAIN SWIPE LOOP ----------
def swipe_loop(driver):
    global like_count, pass_count

    log("Bot started...")

    while like_count < MAX_LIKES:
        try:
            ensure_encounters(driver)

            wait_for_buttons(driver)

            dismiss_popups(driver)

            time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))

            if random.random() < LIKE_RATIO:
                if click_like(driver):
                    like_count += 1
                    log(f"👍 Like #{like_count}")
                else:
                    log("Like failed")
            else:
                if click_pass(driver):
                    pass_count += 1
                    log(f"👎 Pass #{pass_count}")
                else:
                    log("Pass failed")

        except TimeoutException:
            log("Timeout - retrying...")
        except Exception as e:
            log(f"Error: {e}")
            time.sleep(2)


# ---------- MAIN ----------
def main():
    driver = create_driver()

    driver.get("https://badoo.com/encounters/")

    print("\nLogin manually, then press ENTER...")
    input()

    swipe_loop(driver)

    log("Done!")
    driver.quit()


if __name__ == "__main__":
    main()