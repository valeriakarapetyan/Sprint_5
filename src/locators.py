from selenium.webdriver.common.by import By


class StellarBurgersLocators:
    # Главная страница
    # Кнопка Войти в аккаунт на главной странице
    LOGIN_ACCOUNT_BUTTON = By.XPATH, "//button[text() = 'Войти в аккаунт']"
    # Кнопка "Оформить заказ" на главной странице
    PLACE_AN_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"
    # Кнопка "Личный кабинет" на главной странице
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']"
    # Вкладка "Булки"
    BUNS_BUTTON = By.XPATH, "//span[text()='Булки']/parent::div"
    # Вкладка "Соусы"
    SAUCES_BUTTON = By.XPATH, "//span[text()='Соусы']/parent::div"
    # Вкладка "Начинки"
    FILLINGS_BUTTON = By.XPATH, "//span[text()='Начинки']/parent::div"

    # Форма регистрации
    # Поле ввода имени  в форме регистрации
    NAME_FIELD_ON_REGISTRATION_FORM = By.XPATH, "//label[text() = 'Имя']/parent::div//input"
    # Поле ввода email  в форме регистрации
    EMAIL_FIELD_ON_REGISTRATION_FORM = By.XPATH, "//label[text() = 'Email']/parent::div//input"
    # Поле ввода пароля в форме регистрации
    PASSWORD_FIELD_ON_REGISTRATION_FORM = By.NAME, "Пароль"
    # Кнопка подтверждения регистрации на форме регистрации
    SIGNUP_BUTTON_ON_REGISTRATION_FORM = By.XPATH, "//button[text() = 'Зарегистрироваться']"
    # Подпись "Некорректный пароль" на форме регистрации
    INCORRECT_PASS_ON_REGISTRATION_FORM = By.XPATH, "//label[text() = 'Пароль']/parent::div/parent::div//p"
    # Кнопка Войти на форме регистрации
    LOGIN_BUTTON_ON_REGISTRATION_FORM = By.XPATH, "//p[text() = 'Уже зарегистрированы?']//a"

    # Форма логина
    # Кнопка Зарегистрироваться в окне логина
    SIGNUP_ACCOUNT_BUTTON_ON_LOGIN_FORM = By.XPATH, "//a[text() = 'Зарегистрироваться']"
    # Кнопка Войти в форме логина
    LOGIN_BUTTON_ON_LOGIN_FORM = By.XPATH, "//button[text()='Войти']"
    # Поле ввода email  в форме логина
    EMAIL_FIELD_ON_LOGIN_FORM = By.XPATH, "//label[text() = 'Email']/parent::div//input"
    # Поле ввода пароля в форме логина
    PASSWORD_FIELD_ON_LOGIN_FORM = By.NAME, "Пароль"
    # Кнопка Восстановить пароль на форме логина
    PASSWORD_RECOVERY_BUTTON = By.XPATH, "//a[text() = 'Восстановить пароль']"

    # Форма восстановления пароля
    # Кнопка входа
    LOGIN_BUTTON_ON_RECOVERY_FORM = By.XPATH, "//a[text() = 'Войти']"

    # Личный Кабинет
    # Кнопка Выход
    LOGOUT_BUTTON_ON_ACCOUNT_PAGE = By.XPATH, "//button[text() = 'Выход']"
    # Кнопка Конструктор
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text() = 'Конструктор']"
    # Лейбл Stellar Burgers
    STELLAR_BURGERS_LABEL = By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']"
