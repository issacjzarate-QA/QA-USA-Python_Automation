import data
import pytest
from selenium import webdriver
from pages import UrbanRoutesPage
import helpers

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import ChromeOptions

        options = ChromeOptions()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        cls.driver = webdriver.Chrome(options=options)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")


    #Setting the Address (To & From Fields)
    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_from(data.ADDRESS_FROM)
        page.set_to(data.ADDRESS_TO)

        assert page.get_from_value() == data.ADDRESS_FROM
        assert page.get_to_value() == data.ADDRESS_TO

    #Selecting the Supportive Plan
    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        #Enter addresses
        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        #Open tariff options
        page.click_call_taxi()
        #Select supportive plan
        page.click_supportive()
        #Assert supportive plan
        assert page.is_supportive_active() is True

    #Filling in the Phone Number
    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        #setup
        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi()
        page.click_supportive()
        #phone number
        page.click_phone_field()
        page.enter_phone_number(data.PHONE_NUMBER)
        #call the number from helpers to get the sms
        code = helpers.retrieve_phone_code(self.driver)
        page.enter_sms_code(code)
        #Assertion
        assert page.get_phone_value() == data.PHONE_NUMBER

    #Adding a Credit Card
    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi()
        page.click_supportive()
        #Adding the card flow.
        page.click_payment_method()
        page.click_add_card()
        page.enter_card_number(data.CARD_NUMBER)
        page.enter_card_code(data.CARD_CODE)
        page.click_title()
        page.click_link_button()
        page.close_card_modal()
        #Assertion
        assert page.get_payment_method_text() == "Card"

    #Writing a Comment for the Driver
    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi()
        page.click_supportive()
        #Adding a comment flow
        page.enter_comment(data.MESSAGE_FOR_DRIVER)
        #Assertion
        assert page.get_comment_value() == data.MESSAGE_FOR_DRIVER

    #Ordering a Blanket and Handkerchiefs
    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page=UrbanRoutesPage(self.driver)

        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi()
        page.click_supportive()
        page.toggle_blanket()
        assert page.is_blanket_selected() is True

    #Ordering 2 Ice Creams (Supportive Taxi)
    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi()
        page.click_supportive()
        #Add 2 ice creams
        for i in range(2):
            page.add_ice_cream()
        #Assertion
        assert page.get_ice_cream_count() == 2

    #Ordering a Taxi with the Supportive Tariff
    def test_car_search_modal_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        # Setup
        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi()
        page.click_supportive()

        # Phone number
        page.click_phone_field()
        page.enter_phone_number(data.PHONE_NUMBER)
        code = helpers.retrieve_phone_code(self.driver)
        page.enter_sms_code(code)

        # Comment
        page.enter_comment(data.MESSAGE_FOR_DRIVER)

        # Order taxi
        page.click_order_button()

        # Assertion
        assert page.is_car_search_modal_visible() is True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()