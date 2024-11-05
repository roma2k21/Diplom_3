class TestLKPage:
    # выход из аĸĸаунта
    def test_exit_profile(self, authorization_user, header_page, lk_page, repair_page):
        header_page.click_lk_page()
        lk_page.click_exit_from_account()

        assert repair_page.check_button_visibility().is_displayed()

    # переход в раздел «История заĸазов»
    def test_history_order(self, authorization_user, header_page, lk_page):
        header_page.click_lk_page()
        lk_page.click_history_page()

        assert lk_page.transfer_to_history_page().is_displayed()
