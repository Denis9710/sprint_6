import allure
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocators
from .base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Кликнуть по предлагаемому варианту в выпадающем списке станций метро')
    def select_station(self, station_name):

        station_locator = (By.XPATH, f"//div[text()='{station_name}']")
        self.click_on_element(station_locator)

    @allure.step('Проверить отображение кнопки "Посмотреть статус" после создания заказа')
    def check_displaying_of_button_check_status_of_order(self):
       
        return self.check_displaying_of_element(OrderPageLocators.BUTTON_CHECK_STATUS_OF_ORDER)

    @allure.step('Заполнение первой части формы и нажатие кнопки "Далее"')
    def data_entry_first_form(self, user_data):

        self.wait_visibility_of_element(OrderPageLocators.INPUT_NAME)
        
        self.click_on_element(OrderPageLocators.INPUT_NAME)
        self.send_keys_to_input(OrderPageLocators.INPUT_NAME, user_data.name)
        
        self.click_on_element(OrderPageLocators.INPUT_LASTNAME)
        self.send_keys_to_input(OrderPageLocators.INPUT_LASTNAME, user_data.surname)
        
        self.click_on_element(OrderPageLocators.INPUT_ADDRESS)
        self.send_keys_to_input(OrderPageLocators.INPUT_ADDRESS, user_data.address)
        
        self.click_on_element(OrderPageLocators.INPUT_METRO)
        self.send_keys_to_input(OrderPageLocators.INPUT_METRO, user_data.station_name)
        self.select_station(user_data.station_name)
        
        self.click_on_element(OrderPageLocators.INPUT_PHONE)
        self.send_keys_to_input(OrderPageLocators.INPUT_PHONE, user_data.telephone)
        
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполнение второй части формы и окно подтверждения')
    def data_entry_second_form(self, user_data):

        self.wait_visibility_of_element(OrderPageLocators.INPUT_DATE)
        
        self.click_on_element(OrderPageLocators.INPUT_DATE)
        self.send_keys_to_input(OrderPageLocators.INPUT_DATE, user_data.date)
        
        if 'чёрный' in user_data.color:
            self.click_on_element(OrderPageLocators.CHECKBOX_BLACK_COLOR_SCOOTER)
        else:
            self.click_on_element(OrderPageLocators.CHECKBOX_GREY_COLOR_SCOOTER)
        
        self.click_on_element(OrderPageLocators.FIELD_RENTAL_PERIOD)
        period_locator = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{user_data.period}']")
        self.click_on_element(period_locator)
        
        self.click_on_element(OrderPageLocators.INPUT_COMMENT)
        self.send_keys_to_input(OrderPageLocators.INPUT_COMMENT, user_data.comment)
        
        self.click_on_element(OrderPageLocators.BUTTON_MAKE_ORDER)
        
        self.wait_visibility_of_element(OrderPageLocators.BUTTON_YES_CONFIRM_ORDER)
        
        self.click_on_element(OrderPageLocators.BUTTON_YES_CONFIRM_ORDER)