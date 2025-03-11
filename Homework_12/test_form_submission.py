import allure
from selene import have, command
from pathlib import Path

@allure.title("done")
def test_fill_form(setup_browser):
    browser = setup_browser


    with allure.step("открываю браузер"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element("#firstName").type("Анастасия")
        browser.element("#lastName").type("Кузнецова")
        browser.element("#userEmail").type("kuznetsova@mail.com")

    with allure.step("выбираю пол"):
        browser.element('[for="gender-radio-2"]').click()

    with allure.step("ввожу номер телефона"):
        browser.element("#userNumber").type("1234567890")

    with allure.step("выбираю дату рождения"):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").type("1984")
        browser.element(".react-datepicker__month-select").type("May")
        browser.element(".react-datepicker__day--009").click()

    with allure.step("ввожу предметы"):
        browser.element("#subjectsInput").type("Math").press_enter()

    with allure.step("выбираю хобби"):
        browser.element('[for="hobbies-checkbox-2"]').perform(command.js.scroll_into_view).click()

    with allure.step("загружаю изображение"):
        # browser.element("#uploadPicture").send_keys("/Users/kuznetsova/PycharmProjects/Homework_L11/Homework_11/download.jpg")
        file_path = str(Path(__file__).parent / "download.jpg")
        browser.element('#uploadPicture').send_keys(file_path)

    with allure.step("ввожу адрес"):
        browser.element("#currentAddress").type("Ростов-на-Дону, ул.Города Волос")

    with allure.step("отправляю форму"):
        browser.element("#submit").press_enter()

    with allure.step("проверка, что форма отправлена"):
        browser.element(".modal-title").should(have.text("Thanks for submitting the form"))