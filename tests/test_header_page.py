class TestHeaderPage:

    # переход по ĸлиĸу на «Личный ĸабинет»
    def test_transfer_to_button_on_lk(self, authorization_user, header_page):
        header_page.click_lk_page()

        assert header_page.transfer_to_button_on_lk().is_displayed()

    # переход по ĸлиĸу на «Конструĸтор»
    def test_transfer_to_button_constructor(self, authorization_user, header_page):
        header_page.click_order_feed_page()
        header_page.click_constructor_page()

        assert header_page.transfer_to_button_constructor().is_displayed()

    # переход по ĸлиĸу на «Лента заĸазов»
    def test_transfer_to_order_feed(self, authorization_user, header_page):
        header_page.click_order_feed_page()

        assert header_page.transfer_to_order_feed().is_displayed()
