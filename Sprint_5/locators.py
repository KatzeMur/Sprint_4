from selenium.webdriver.common.by import By

# Кнопка "Разместить объявление"
CREATE_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")

# Кнопка "Вход и регистрация" в шапке
HEADER_AUTH_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")

# Кнопка перехода к форме регистрации в модальном окне
NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")

# Поле ввода Email в форме регистрации
REG_EMAIL_FIELD = (By.NAME, "email")

# Поле ввода "Пароль" в форме регистрации
REG_PASSWORD_FIELD = (By.NAME, "password")

# Поле ввода "Повторите пароль" в форме регистрации
REG_REPEAT_PASSWORD_FIELD = (By.NAME, "submitPassword")

# Кнопка "Создать аккаунт" в форме регистрации
CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")

# Имя пользователя на главной странице после входа
MAIN_PAGE_USERNAME = (By.CSS_SELECTOR, "h3.name")

# Имя пользователя на главной странице после входа
HEADER_AVATAR_BUTTON = (By.CSS_SELECTOR, "button.circleSmall")

# Кнопка "Разместить объявление" на главной странице
POST_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")

# Сообщение об ошибке под полем Email
REG_EMAIL_ERROR_MESSAGE = (By.XPATH, "//span[text()='Ошибка']")

# Форма входа
LOGIN_EMAIL_FIELD = (By.NAME, "email")

# Поле ввода "Пароль" в форме входа
LOGIN_PASSWORD_FIELD = (By.NAME, "password")

# Кнопка "Войти" в форме авторизации
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

# Кнопка "Выйти" в шапке профиля
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")

# Поле "Название" в форме объявления
AD_NAME_FIELD = (By.NAME, "name")

# Поле "Описание" в форме объявления
AD_DESCRIPTION_FIELD = (By.CSS_SELECTOR, "textarea[placeholder='Описание товара']")

# Кнопка "Опубликовать" в форме объявления
AD_PUBLISH_BUTTON = (By.CSS_SELECTOR, "button[type='submit'].buttonPrimary")

# Поле "Категория" (выпадающий список)
AD_CATEGORY_DROPDOWN = (By.CSS_SELECTOR, "button[class*='dropDownMenu_arrowDown']")

# Вариант «Садоводство» в выпадающем списке «Категория»
AD_CATEGORY_OPTION = (By.XPATH, "//span[text()='Садоводство']/parent::button")

# Вариант «Новосибирск» в выпадающем списке «Категория»
AD_CITY_OPTION = (By.XPATH, "//span[text()='Москва']/parent::button")

# Поле "Город" (выпадающий список)
AD_CITY_DROPDOWN = (By.XPATH, "//input[@name='city']/following-sibling::button[contains(@class, 'dropDownMenu_arrowDown')]")

# Радио-кнопка «Состояние товара: Б/У»
AD_CONDITION_USED_RADIO = (By.XPATH, "//input[@value='Б/У']/following-sibling::div[1]")

# Заголовок моего объявления 
AD_TITLE_IN_LIST = (By.XPATH, "//h2")

# Заголовок модального окна при попытке создать объявление без авторизации
AUTH_MODAL_TITLE = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")

# Заголовок раздела «Мои объявления» в профиле
PROFILE_ADS_HEADER = (By.XPATH, "//h1[text()='Мои объявления']")

# Контейнер формы создания объявления
AD_FORM_CONTAINER = (By.XPATH, "//button[text()='Опубликовать']/..")

# Input name name - поле название
AD_NAME_FIELD2 = (By.CSS_SELECTOR, "input[name='name']")

# Поле "Стоимость" в форме объявления
AD_PRICE_FIELD = (By.CSS_SELECTOR, "input[name='price']")

# Т.к. карточка единственная, проверяем что она есть в списке
AD_CARD = (By.CSS_SELECTOR, "div.card")