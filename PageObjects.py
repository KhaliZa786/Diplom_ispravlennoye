from selenium.webdriver.common.by import By
from BaseApp import BasePage


class chrome_locators(BasePage):
    LOCATOR_WOMAN = (By.XPATH, '/html/body/header/div[1]/div/ul/li[1]/a')
    LOCATOR_SHOES = (By.XPATH, '/html/body/header/div[2]/div/div/ul/li[2]/a')
    LOCATOR_FILTER_COLOUR = (By.XPATH, '/html/body/div[2]/div/form/div/div[4]/div[1]')
    LOCATOR_BEGE_FILTER = (By.XPATH, '/html/body/div[2]/div/form/div/div[4]/div[1]/div/div[1]/label/span')

    LOCATOR_SHOPS = (By.XPATH, '/html/body/header/div[1]/div/div')

    LOCATOR_CLOTHES = (By.XPATH, '/html/body/header/div[2]/div/div/ul/li[1]/a')
    LOCATOR_ITEM_FAVOURITE = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/a[1]/div[1]/div[1]')
    LOCATOR_FAVOURITE = (By.XPATH, '/html/body/header/div[2]/div/div/div/a[2]')

    LOCATOR_USER = (By.XPATH, '/html/body/header/div[2]/div/div/div/a[1]/img')
    LOCATOR_REGISTRATION = (By.XPATH, '//*[@id="popup-reg"]/div[1]/ul/li[2]')
    LOCATOR_USERNAME = (By.XPATH, '//*[@id="user-name"]')
    LOCATOR_PHONE = (By.XPATH, '//*[@id="user-tel"]')
    LOCATOR_MAIL = (By.XPATH, '//*[@id="user-email"]')
    LOCATOR_PASSWORD = (By.XPATH, '//*[@id="user-password-reg"]')

    LOCATOR_USER = (By.XPATH, '/html/body/header/div[2]/div/div/div/a[1]/img')
    LOCATOR_LOGIN = (By.XPATH, '//*[@id="logins"]')
    LOCATOR_PASSWORD = (By.XPATH, '//*[@id="user-password"]')
    LOCATOR_ENTER = (By.XPATH, '//*[@id="popup-reg"]/div[2]/form/div[1]/div[3]/button')

    LOCATOR_FIND = (By.XPATH, '/html/body/header/div[2]/div/div/div/form/img')
    LOCATOR_BOOTS = (By.XPATH, '/html/body/header/div[2]/div/div/div/form/input')

    LOCATOR_NEGATIV = (By.XPATH, '/html/body/header/div[2]/div/div/div/form/input')

    LOCATOR_DZHEMPERY = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/a[2]/div[1]/div[3]/div/img')
    LOCATOR_HOW_TO_CHOOSE = (By.XPATH, '//*[@id="bx_117848907_658957_skudiv"]/div[1]/div[2]/div')

    LOCATOR_BRYUKI = (By.XPATH, '/html/body/header/div[2]/div/div/div/form/input')
    LOCATOR_BOSS = (By.XPATH, '/html/body/section/div/div[2]/div/div[1]/a[1]/div[1]/div[3]/div/div/img[2]')

    LOCATOR_SORTING = (By.XPATH, '/html/body/div[2]/div/form/div/div[4]/div[5]')
    LOCATOR_PRICE = (By.XPATH, '/html/body/div[2]/div/form/div/div[4]/div[5]/div/div[2]')
    LOCATOR_FILTER = (By.XPATH, '//*[@id="del_filter"]')

    def do_section_question(self):
        self.driverwait(chrome_locators.LOCATOR_WOMAN).click()
        self.driverwait(chrome_locators.LOCATOR_SHOES).click()
        self.driverwait(chrome_locators.LOCATOR_FILTER_COLOUR).click()
        self.driverwait(chrome_locators.LOCATOR_BEGE_FILTER).click()

    def do_favorite_question(self):
        self.driverwait(chrome_locators.LOCATOR_CLOTHES).click()
        self.driverwait(chrome_locators.LOCATOR_ITEM_FAVOURITE).click()
        self.driverwait(chrome_locators.LOCATOR_FAVOURITE).click()

    def do_registration_question(self, name, phone, mail, password):
        self.driverwait(chrome_locators.LOCATOR_USER).click()
        self.driverwait(chrome_locators.LOCATOR_REGISTRATION).click()
        self.driverwait(chrome_locators.LOCATOR_USERNAME).send_keys(name)
        self.driverwait(chrome_locators.LOCATOR_PHONE).send_keys(phone)
        self.driverwait(chrome_locators.LOCATOR_MAIL).send_keys(mail)
        self.driverwait(chrome_locators.LOCATOR_PASSWORD).send_keys(password)

    def do_shops_question(self):
        self.driverwait(chrome_locators.LOCATOR_SHOPS).click()

    def do_entrance_question(self, login, password):
        self.driverwait(chrome_locators.LOCATOR_USER).click()
        self.driverwait(chrome_locators.LOCATOR_LOGIN).send_keys(login)
        self.driverwait(chrome_locators.LOCATOR_PASSWORD).send_keys(password)
        self.driverwait(chrome_locators.LOCATOR_ENTER).click()

    def do_find_question(self, boots):
        self.driverwait(chrome_locators.LOCATOR_FIND).click()
        self.driverwait(chrome_locators.LOCATOR_BOOTS).send_keys(boots)

    def do_findnegativ_question(self, result):
        self.driverwait(chrome_locators.LOCATOR_FIND).click()
        self.driverwait(chrome_locators.LOCATOR_NEGATIV).send_keys(result)

    def do_kartopen_question(self):
        self.driverwait(chrome_locators.LOCATOR_CLOTHES).click()
        self.driverwait(chrome_locators.LOCATOR_DZHEMPERY).click()
        self.driverwait(chrome_locators.LOCATOR_HOW_TO_CHOOSE).click()

    def do_newwindow_question(self, result):
        self.driverwait(chrome_locators.LOCATOR_FIND).click()
        self.driverwait(chrome_locators.LOCATOR_BRYUKI).send_keys(result)
        self.driverwait(chrome_locators.LOCATOR_HOW_TO_CHOOSE).click()

    def do_filter_question(self):
        self.driverwait(chrome_locators.LOCATOR_CLOTHES).click()
        self.driverwait(chrome_locators.LOCATOR_SORTING).click()
        self.driverwait(chrome_locators.LOCATOR_PRICE).click()
        self.driverwait(chrome_locators.LOCATOR_FILTER).click()
