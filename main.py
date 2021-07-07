import selenium
from selenium import webdriver
from time import sleep

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"\Users\KIIT\Desktop\PYTHON ENVIRONMENT\chrome driver\chromedriver")
driver.get("https://tinder.com/app/recs")
login = driver.find_element_by_xpath('//*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()

# google_login = driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div[1]/div/div[3]/span/div/div/button')
# google_login.click()
sleep(3)
buttons = driver.find_elements_by_class_name("button")
print(buttons)
btn_text = [button.text for button in buttons]
for button in buttons:
    print(button.text)
    if button.text == "LOG IN WITH FACEBOOK":

        button.click()
        print("done")
        break
    elif "LOG IN WITH FACEBOOK" not in btn_text:
            sleep(2)
            driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[3]/span/button").click()
            buttons = driver.find_elements_by_class_name("button")
            for button in buttons:
                if button.text == "LOG IN WITH FACEBOOK":
                    button.click()
                    print("done")
                    break

# google_login[0].click()
sleep(3)

fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)


input_list = driver.find_elements_by_class_name("inputtext")
print(input_list)
email = input_list[0].send_keys("#YOUR EMAIL#")
password = input_list[1].send_keys("#YOUR PASSWORD#")

log_in = driver.find_element_by_id("loginbutton")
print(log_in)
log_in.send_keys(Keys.ENTER)

sleep(10)
tinder_window = driver.window_handles[0]
driver.switch_to.window(tinder_window)
# confirm = driver.find_element_by_name("__CONFIRM__")
# confirm.send_keys(Keys.ENTER)

tinder_buttons = driver.find_elements_by_css_selector("button")
print(tinder_buttons)

for new_button in tinder_buttons:
    try:
        if new_button.text == "ALLOW":
            new_button.click()
            tinder_buttons = driver.find_elements_by_css_selector("button")
            for btn in tinder_buttons:
                if btn.text=="NOT INTERESTED":
                    btn.click()
    except StaleElementReferenceException:
        pass


# sleep(3)

final_buttons = driver.find_elements_by_css_selector("button")
print("fb")
print(final_buttons)

sleep(3)
swipes=0

while swipes<100:
        sleep(1)
        for btn in final_buttons:
            if btn.text == "NOPE":
                btn.click()
        swipes+=1
