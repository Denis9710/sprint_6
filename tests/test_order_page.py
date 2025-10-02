import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import User_1, User_2


class TestOrder:
    
    @allure.title('Проверка успешного оформления заказа через верхнюю кнопку')
    def test_successful_order_via_top_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.open()
        main_page.accept_cookies()
        main_page.click_order_button_top() 
        order_page.data_entry_first_form(User_1())
        order_page.data_entry_second_form(User_1())
        
        assert order_page.check_displaying_of_button_check_status_of_order()

    @allure.title('Проверка успешного оформления заказа через нижнюю кнопку')
    def test_successful_order_via_bottom_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.open()
        main_page.accept_cookies()
        main_page.click_order_button_bottom()  
        
        order_page.data_entry_first_form(User_2())
        order_page.data_entry_second_form(User_2())
        
        assert order_page.check_displaying_of_button_check_status_of_order()