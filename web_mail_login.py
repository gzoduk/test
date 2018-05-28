from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Open webpage and write login\pass
driver = webdriver.Ie()
driver.get(url="https://mail.ru")

driver.maximize_window()
driver.implicitly_wait(5)
assert "Mail.Ru" in driver.title


login_elem = driver.find_element_by_xpath("//input[@name='login']")
pass_elem =  driver.find_element_by_xpath("//input[@name='password']")

login_elem.clear()
login_elem.send_keys ("user_name")
pass_elem.send_keys("user_pass")
pass_elem.send_keys(Keys.ENTER)
driver.implicitly_wait(5)

#take current url and update driver with new url
get_url = driver.current_url
driver.get(url=get_url)

write_button = driver.find_element_by_xpath("//a[@title='Написать письмо (N)' and @data-shortcut='n']")
write_button.click()

#write message with new url
get_url = driver.current_url
driver.get(url=get_url)

destination = driver.find_element_by_xpath("//textarea[@class='js-input compose__labels__input']")
subject = driver.find_element_by_xpath("//input[@class='b-input' and @name='Subject']")
send_button = driver.find_element_by_xpath("//span[@class='b-toolbar__btn__text']")

destination.send_keys ("user_name@mail.ru")
subject.send_keys("Test")
send_button.click()


assert "No results found" not in driver.page_source

driver.close()