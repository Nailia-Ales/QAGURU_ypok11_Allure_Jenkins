import allure
from selene import browser, have, command

from model.resource import path


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.email = browser.element("#userEmail")
        self.gender = browser.element("#gender-radio-1 + .custom-control-label")
        self.mobile_number = browser.element("#userNumber")

        self.date_of_birth_input = browser.element("#dateOfBirthInput")
        self.month = browser.element(".react-datepicker__month-select")
        self.year = browser.element(".react-datepicker__year-select")

        self.subject_input = browser.element('#subjectsInput')
        self.hobbies = browser.all('.custom-control-label')
        self.upload_avatar = browser.element('#uploadPicture')
        self.current_address = browser.element("#currentAddress")
        self.state = browser.element("#state")
        self.city = browser.element("#city")

    @allure.step('Открыть страницу с формой регистрации')
    def open(self):
        browser.open("/")
        browser.driver.execute_script("$('#RightSide_Advertisement').remove()")
        return self

    @allure.step('Ввести имя')
    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    @allure.step('Ввести фамилию')
    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    @allure.step('Ввести электронную почту')
    def fill_email(self, value):
        self.email.type(value)
        return self

    @allure.step('Выбрать пол')
    def select_gender(self, value):
        browser.element(f'[value={value}]').element('..').click()
        return self

    @allure.step('Ввести мобильный телефон')
    def fill_mobile_number(self, value):
        self.mobile_number.type(value)
        return self

    @allure.step('Указать дату рождения')
    def fill_date_of_birth(self, month, year, day):
        self.date_of_birth_input.click()
        self.month.click().element(f'[value="{month}"]').click()
        self.year.click().element(f'[value="{year}"]').click()
        browser.element(f".react-datepicker__day--0{day}").click()
        return self

    @allure.step('Выбрать предмет')
    def fill_subject(self, value):
        self.subject_input.send_keys(value).press_enter()
        return self

    @allure.step('Выбрать хобби')
    def select_hobbies(self, value):
        self.hobbies.element_by(have.text(value)).click()
        return self

    @allure.step('Загрузить фото')
    def set_avatar(self, value):
        self.upload_avatar.set_value(path(value))
        return self

    @allure.step('Ввести адрес')
    def fill_current_address(self, value):
        self.current_address.type(value)
        return self

    @allure.step('Выбрать штат')
    def select_state(self, value):
        self.state.click().all('[id^=react-select-3-option]').element_by(
            have.exact_text(value)).click()
        return self

    @allure.step('Выбрать город')
    def select_city(self, value):
        self.city.click().all('[id^=react-select-4-option]').element_by(have.text(value)).click()
        return self

    @allure.step('Отправить форму')
    def submit_form(self):
        browser.element("#submit").perform(command.js.scroll_into_view).click()
        return self

    @allure.step('Проверка отображения данных в отправленной форме')
    def should_have_registered_user(self, first_name, last_name, email, gender, mobile_number, date_of_birth, subjects,
                                    hobbies, file_name, address, state, city):
        browser.element(".table").should(have.text(f'{first_name} {last_name}'))
        browser.element(".table").should(have.text(email))
        browser.element(".table").should(have.text(gender))
        browser.element(".table").should(have.text(mobile_number))
        browser.element(".table").should(have.text(date_of_birth))
        browser.element(".table").should(have.text(subjects))
        browser.element(".table").should(have.text(hobbies))
        browser.element(".table").should(have.text(file_name))
        browser.element(".table").should(have.text(address))
        browser.element(".table").should(have.text(f'{state} {city}'))
        return self

    @allure.step('Проверка наличия валидации на незаполненных обязательных полях')
    def check_if_required_fields_not_filled(self):
        browser.element("#userForm").should(have.attribute("class").value("was-validated"))
        return self