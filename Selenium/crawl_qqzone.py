from selenium import webdriver
import time

driver = webdriver.PhantomJS()
driver.maximize_window()

# qq = input("input qq number:")
# pwd = input("input the password")

def get_info(qq):
    driver.get('http://user.qzone.qq.com/{}/311'.format(qq))
    driver.implicitly_wait(10)

    try:
        driver.find_element_by_id('login_div')
        a = True
    except:
        a = False

    if a == True:
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('u').clear()
        driver.find_element_by_id('u').send_keys('账号')
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys('密码')
        driver.find_element_by_id('login_button').click()
        time.sleep(3)
    driver.implicitly_wait(3)

    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
        b = True
    except:
        b= False
    if b == True:
        contents = driver.find_elements_by_xpath('//div[@class="f-item f-s-i"]/div[1]').text
        print(contents)


if __name__ == '__main__':
    get_info(381827702)