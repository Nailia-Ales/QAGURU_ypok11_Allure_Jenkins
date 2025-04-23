import allure
from allure_commons.types import Severity

from model.pages.registration_page import RegistrationPage


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Nailia-Ales')
@allure.feature("Сборка Allure-отчета о тестировании в Jenkins")
@allure.story("Успешная отправка полной формы регистрации")
@allure.link('https://github.com/', 'Testing')
def test_form_submitted():
    practice_form = RegistrationPage()
    (practice_form.open()

    .fill_first_name("Maria")
    .fill_last_name("Lopez")
    .fill_email("MLopez@gmail.com")
    .select_gender("Female")
    .fill_mobile_number("0123456789")
    .fill_date_of_birth(9, 1996, 10)
    .fill_subject('Biology')
    .set_avatar("unnamed.jpg")
    .select_hobbies("Reading")
    .fill_current_address("Main street, 55 bld, 10 apt.")
    .select_state("Rajasthan")
    .select_city("Jaipur")
    .submit_form()
    .should_have_registered_user(
        "Maria", "Lopez", "MLopez@gmail.com", "Female", "0123456789", "10 October,1996", "Biology", "Reading",
        "unnamed.jpg", "Main street, 55 bld, 10 apt.", "Rajasthan", "Jaipur"
    ))


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label('owner', 'Nailia-Ales')
@allure.feature("Сборка Allure-отчета о тестировании в Jenkins")
@allure.story("Успешная отправка формы только с обязат. полями")
@allure.link('https://github.com/', 'Testing')
def test_form_required_fields_only(today_date):
    practice_form = RegistrationPage()
    (practice_form.open()
    .fill_first_name("Maria")
    .fill_last_name("Lopez")
    .select_gender("Female")
    .fill_mobile_number("0123456789")
    .submit_form()
    .should_have_registered_user(
        "Maria", "Lopez", "", "Female", "0123456789", f"", "", "",
        "", "", "", ""
    ))


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Nailia-Ales')
@allure.feature("Сборка Allure-отчета о тестировании в Jenkins")
@allure.story("Проверка на наличие валидации по заполнению обязательных полей")
@allure.link('https://github.com/', 'Testing')
def test_form_error_required_fields_not_filled():
    practice_form = RegistrationPage()
    (practice_form.open()

     .fill_first_name("Maria")
     .select_gender("Female")
     .submit_form()
     .check_if_required_fields_not_filled())


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Nailia-Ales')
@allure.feature("Сборка Allure-отчета о тестировании в Jenkins")
@allure.story("Проверка на наличие валидации в поле Mobile")
@allure.link('https://github.com/', 'Testing')
def test_form_required_fields_but_wrong_number():
    practice_form = RegistrationPage()
    (practice_form.open()

     .fill_first_name("Maria")
     .fill_last_name("Lopez")
     .select_gender("Female")
     .fill_mobile_number("123456789")
     .submit_form()
     .check_if_required_fields_not_filled())