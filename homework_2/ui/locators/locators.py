from selenium.webdriver.common.by import By


# Я так понял, что главная страница по совместительству является страницой кампании
# И я решил в нем же прописать локаторы проверки создания кампании
class CampaignsPageLocators:
    LOGO_BUTTON = (By.XPATH, '//a[contains(@class, "responseHead-module-logoLink")]')
    CAMPAIGNS_BUTTON = (By.CSS_SELECTOR, '[href="/dashboard"]')
    SEGMENTS_BUTTON = (By.CSS_SELECTOR, '[href="/segments"]')
    CREATE_CAMPAIGN_BEGIN = (By.XPATH, '//div[contains(@class, "button-module-textWrapper") and contains(text(), "Создать кампанию")]')
    CREATE_FIRST_CAMPAIGN_BEGIN = (By.XPATH, '//a[@href="/campaign/new"]')
    CHECK_NAME_OF_COMPANY = (By.CSS_SELECTOR, '[data-row-id="central-1"] [target="_blank"]')


class AuthPageLocators:
    AUTH_OPEN_BUTTON = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
    EMAIL_PLACEHOLDER = (By.NAME, 'email')
    PASSD_PLACEHOLDER = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, '//div[contains(@class, "authForm-module-button")]')
    EMAIL_AFTER_AUTH = (By.CSS_SELECTOR, '[title="bato_97_97@mail.ru"]')


class TrafficCampaignCreationLocators:
    TRAFFIC_BUTTON = (By.CSS_SELECTOR, '._traffic')

    # Инпуты до выбора баннера
    INPUT_URL = (By.XPATH, '//input[contains(@class, "mainUrl")]')
    INPUT_CAMPAIGN_NAME = (By.CSS_SELECTOR, '.campaign-name .input__inp')
    INPUT_DAILY_BUDGET = (By.CSS_SELECTOR, '.js-budget-setting-daily .input__inp')
    INPUT_DAILY_TOTAL = (By.CSS_SELECTOR, '.js-budget-setting-total .input__inp')

    # Опции баннера (выбрал мультиформат)
    MULTIFORMAT_BUTTON = (By.CSS_SELECTOR, '.banner-format-item:nth-child(2)')

    INPUT_TITLE = (By.CSS_SELECTOR, '[data-gtm-id="banner_form_title"]')
    INPUT_TEXT = (By.CSS_SELECTOR, '[data-gtm-id="banner_form_text"]')
    LOAD_CONTENT = (By.CSS_SELECTOR, '[data-gtm-id="load_image_btn_256_256"]')
    LOAD_PROMOCONTENT = (By.CSS_SELECTOR, '[data-gtm-id="load_image_btn_1080_607"]')
    LOAD_ICON = (By.CSS_SELECTOR, '[data-gtm-id="load_image_btn_600_600"]')

    CREATE_COMPANY_END_BUTTON = (By.CSS_SELECTOR, '.footer .button__text')


class SegmentsPageLocators:
    # Локаторы создания сегмента
    CREATE_FIRST_SEGMENT_BEGIN = (By.CSS_SELECTOR, '[href="/segments/segments_list/new/"]')
    CREATE_SEGMENT_BEGIN = (By.CSS_SELECTOR, '.segments-list__btn-wrap .button__text')
    APPS_N_GAMES = (By.XPATH, '//div[contains(text(), "Приложения и игры в соцсетях")]')
    PLATFROM_OPTIONS_BUTTON = (By.CLASS_NAME, 'adding-segments-source__header')
    CHECKBOX_PAY = (By.CSS_SELECTOR, '[value="pay"]')
    CREATE_SEGMENT_MIDDLE = (By.CSS_SELECTOR, '.adding-segments-modal__footer .button_submit')
    INPUT_NAME_SEGMENT = (By.CSS_SELECTOR, '.js-segment-name .input__inp')
    # Насколько верен такой локатор? По сути без модального окна он один, но если
    # произойдет ошибка, то не оч. Или и так норм?
    CREATE_SEGMENT_END = (By.CSS_SELECTOR, '.button_submit')

    # Локаторы проверки и удаления
    CHECK_LAST_ID_SEGMENT = (By.XPATH, '//div[@data-row-id="central-0" and starts-with(@data-test, "id-")]/div/span')
    DELETE_CROSS_BUTTON = (By.CSS_SELECTOR, '[data-row-id="central-0"] > .icon-cross')
    CONFIRM_DELETE_SEGMENT = (By.CLASS_NAME, 'button_confirm-remove')
    SEGMENT_NAME = (By.CSS_SELECTOR, '[data-row-id="central-0"] [title]')
