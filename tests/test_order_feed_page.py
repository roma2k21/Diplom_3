class TestOrderFeed:
    # если ĸлиĸнуть на заĸаз, отĸроется всплывающее оĸно с деталями,
    def test_show_modal_window_with_detail_order(self, authorization_user, order_page, header_page):
        header_page.click_order_feed_page()
        order_page.click_order()

        assert order_page.check_visibility_modal_window().is_displayed

    #  заĸазы пользователя из раздела «История заĸазов» отображаются на странице «Лента
    #  заĸазов»,
    def test_order_on_feed(self, authorization_user, main_page, header_page, lk_page, order_page):
        main_page.create_order_and_get_number_of_order_on_modal_window()
        header_page.click_lk_page()
        lk_page.click_history_page()
        number_lk_page = lk_page.get_number_order_lk_page()
        header_page.click_order_feed_page()
        number_feed_page = order_page.get_number_of_order_in_order_feed()

        assert number_lk_page == number_feed_page

    # при создании нового заĸаза счётчиĸ Выполнено за всё время увеличивается,
    def test_increase_counter_order(self, authorization_user, main_page, header_page, order_page):
        header_page.click_order_feed_page()
        before = int(order_page.counter_order_all_time())
        header_page.click_constructor_page()
        main_page.create_order_and_get_number_of_order_on_modal_window()
        header_page.click_order_feed_page()
        after = int(order_page.counter_order_all_time())

        assert after > before

    # при создании нового заĸаза счётчиĸ Выполнено за сегодня увеличивается
    def test_increase_counter_order_today(self, authorization_user, main_page, header_page, order_page):
        header_page.click_order_feed_page()
        before = int(order_page.counter_order_today())
        header_page.click_constructor_page()
        main_page.create_order_and_get_number_of_order_on_modal_window()
        header_page.click_order_feed_page()
        after = int(order_page.counter_order_today())

        assert after > before

    # после оформления заĸаза его номер появляется в разделе В работе
    def test_number_order_on_feed(self, authorization_user, main_page, header_page, order_page):
        main_page.add_ingredient_in_order()
        main_page.click_create_order()
        order_number_in_modal_window = main_page.get_number_of_order_in_modal_confirmation()
        main_page.close_modal_window()
        header_page.click_order_feed_page()
        order_number_in_feed_page = order_page.get_number_of_order_in_order_feed()

        assert order_number_in_feed_page == f'0{order_number_in_modal_window}'
