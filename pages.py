from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:
    # Locators
    # Setting the Address (To & From Fields)
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")
    # Selecting the Supportive Plan
    CALL_A_TAXI_LOCATOR = (By.XPATH, '//button[text()="Call a taxi"]')
    SUPPORTIVE_LOCATOR = (By.XPATH, '//div[text()="Supportive"]')
    # Filling in the Phone Number
    PHONE_NUMBER_LOCATOR = (By.XPATH, '//div[text()="Phone number"]')
    PHONE_INPUT_FIELD = (By.ID, "phone")
    NEXT_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Next"]')
    SMS_CODE_INPUT = (By.ID, "code")
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Confirm"]')
    # Adding a Credit Card
    PAYMENT_METHOD_LOCATOR = (By.XPATH, '//div[@class="pp-button filled"]')
    ADD_CARD_LOCATOR = (By.XPATH, '//div[@class="pp-title" and text()="Add card"]/parent::div')
    CARD_NUMBER_INPUT = (By.XPATH, '//input[@class="card-input" and @id="number"]')
    CARD_CODE_INPUT = (By.XPATH, '//input[@class="card-input" and @placeholder="12"]')
    ADDING_A_CARD_TITLE_LOCATOR = (By.XPATH, '//div[contains(@class, "head") and contains(text(), "Adding")]')
    LINK_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Link"]')
    CLOSE_CARD_POP_UP = (By.CSS_SELECTOR, 'button.close-button.section-close')
    PAYMENT_METHOD_RESULT = (By.XPATH, '//div[@class="pp-value-text"]')
    #Writing a Comment for the Driver
    COMMENT_INPUT_FIELD= (By.ID, "comment")
    #Ordering a Blanket and Handkerchiefs
    BLANKET_AND_HANDKERCHIEFS_TOGGLE = (By.XPATH, '//div[text()="Blanket and handkerchiefs"]/following::span[@class="slider round"][1]')
    BLANKET_AND_HANDKERCHIEFS_CHECKBOX = (By.XPATH, '//div[text()="Blanket and handkerchiefs"]/following::input[1]')
    #Ordering 2 Ice Creams (Supportive Taxi)
    ICE_CREAM_PLUS = (By.XPATH, '//div[text()="Ice cream"]/following::div[@class="counter-plus"][1]')
    ICE_CREAM_COUNT = (By.XPATH, '//div[text()="Ice cream"]/following::div[contains(@class, "counter-value")][1]')
    #Ordering a Taxi with the Supportive Tariff
    ORDER_BUTTON = (By.XPATH, '//span[@class="smart-button-main" and text()="Order"]/parent::button')
    CAR_SEARCH_MODAL = (By.XPATH, '//div[text()="Car search"]')

    def __init__(self, driver):
        self.driver = driver

    # Setting the Address (To & From Fields)
    def set_from(self, address):
        self.driver.find_element(*self.FROM_INPUT).send_keys(address)

    def get_from_value(self):
        return self.driver.find_element(*self.FROM_INPUT).get_attribute("value")

    def set_to(self, address):
        self.driver.find_element(*self.TO_INPUT).send_keys(address)

    def get_to_value(self):
        return self.driver.find_element(*self.TO_INPUT).get_attribute("value")

        # Combined method for convenience (used in most tests)

    def enter_locations(self, from_text, to_text):
        self.set_from(from_text)
        self.set_to(to_text)

    #Selecting the Supportive Plan
    def click_call_taxi(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CALL_A_TAXI_LOCATOR)).click()

    def click_supportive(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUPPORTIVE_LOCATOR)).click()

    def is_supportive_active(self):
        element = self.driver.find_element(By.XPATH, '//div[text()="Supportive"]/parent::div')
        return "active" in element.get_attribute("class")

    #Filling in the Phone Number
    def click_phone_field(self):
        self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).click()

    def enter_phone_number(self, number):
        self.driver.find_element(*self.PHONE_INPUT_FIELD).send_keys(number)
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()

    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()

    def enter_sms_code(self, code):
        self.driver.find_element(*self.SMS_CODE_INPUT).send_keys(code)
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()

    def click_confirm_button(self):
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()

    def get_phone_value(self):
        return self.driver.find_element(*self.PHONE_INPUT_FIELD).get_attribute("value")

    #Adding a Credit Card
    def click_payment_method(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PAYMENT_METHOD_LOCATOR)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PAYMENT_METHOD_LOCATOR)
        ).click()

    def click_add_card(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_CARD_LOCATOR)
        )
        element.click()

    def enter_card_number(self, number):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CARD_NUMBER_INPUT)
        )
        field.send_keys(number)

    def enter_card_code(self, code):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CARD_CODE_INPUT)
        )
        field.send_keys(code)

    def click_title(self):
        title = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADDING_A_CARD_TITLE_LOCATOR)
        )
        title.click()

    def is_link_button_enabled(self):
        return self.driver.find_element(*self.LINK_BUTTON_LOCATOR).is_enabled()

    def click_link_button(self):
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()

    def close_card_modal(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.ADDING_A_CARD_TITLE_LOCATOR)
        )

    def get_payment_method_text(self):
        return self.driver.find_element(*self.PAYMENT_METHOD_RESULT).text

    #Writing a Comment for the Driver
    def enter_comment(self, message):
        self.driver.find_element(*self.COMMENT_INPUT_FIELD).send_keys(message)

    def get_comment_value(self):
        return self.driver.find_element(*self.COMMENT_INPUT_FIELD).get_attribute("value")

    #Ordering a Blanket and Handkerchiefs
    def toggle_blanket(self):
        self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_TOGGLE).click()

    def is_blanket_selected(self):
        return self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_CHECKBOX).get_property("checked")

    #Ordering 2 Ice Creams (Supportive Taxi)
    def add_ice_cream(self):
        self.driver.find_element(*self.ICE_CREAM_PLUS).click()

    def get_ice_cream_count(self):
        return int(self.driver.find_element(*self.ICE_CREAM_COUNT).text)

    #Ordering a Taxi with the Supportive Tariff
    def click_order_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ORDER_BUTTON)).click()

    def is_car_search_modal_visible(self):
        return self.driver.find_element(*self.CAR_SEARCH_MODAL).is_displayed()