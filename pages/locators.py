from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FROM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_SUBMIT = (By.NAME, "registration_submit")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REG_SUCCESS = (By.CSS_SELECTOR, ".alert > .alertinner.wicon:nth-child(2)")


class ProductPageLocator:
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    TITLE_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-4 > h3 a")
    TITLE_BOOK_ADDED = (By.CSS_SELECTOR, ".alertinner :first-child")
    TITLE_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".price_color.align-right")
    TOTAL_PRICE = (By.CSS_SELECTOR, "tbody > tr:nth-of-type(2) > th:nth-of-type(2)")
    PRICE_IN_DESC = (By.CSS_SELECTOR, ".product_main .price_color")
    NOTICE_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert.alert-safe.alert-success:first-child")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > .btn.btn-default:first-child")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_NOTICE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS_TABLE = (By.CSS_SELECTOR, ".basket_summary")
