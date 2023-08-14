from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
def num_button_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    number = KeyboardButton("Поделиться контактом", request_contact=True)
    kb.add(number)
    return kb
def canceling():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    cancel = KeyboardButton("Отмена❌")
    kb.add(cancel)
    return kb
def categories_button_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    volunteer = KeyboardButton("Волонтёр")
    nurse = KeyboardButton("Сиделка")
    another = KeyboardButton("Другое")
    kb.add(volunteer, nurse, another)
    return kb
def main_menu_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    about = InlineKeyboardButton(text="О проекте", callback_data="about")
    vacancies = InlineKeyboardButton(text="Вакансии", callback_data="vacancies")
    change_category = InlineKeyboardButton(text="Сменить категорию", callback_data="change_category")
    kb.row(about)
    kb.row(vacancies)
    kb.row(change_category)
    return kb
def vol_main_menu_kb():
    kb = InlineKeyboardMarkup(row_width=1)
    change_category = InlineKeyboardButton(text="Сменить категорию", callback_data="change_category")
    kb.row(change_category)
    return kb
def main_menu_call_kb():
    kb = InlineKeyboardMarkup(row_width=1)
    mm = InlineKeyboardButton(text="Главное меню", callback_data="main menu")
    kb.row(mm)
    return kb
def another_main_menu_kb(check_vac):
    kb = InlineKeyboardMarkup(row_width=3)
    about = InlineKeyboardButton(text="О проекте", callback_data="about")
    add_vacancies = InlineKeyboardButton(text="Добавить вакансию", callback_data="new vacancies")
    delete_vacancies = InlineKeyboardButton(text="Удалить вакансию", callback_data="delete vacancies")
    change_category = InlineKeyboardButton(text="Сменить категорию", callback_data="change_category")
    kb.row(about)
    if check_vac == False:
        kb.add(add_vacancies)
    elif check_vac == True:
        kb.add(delete_vacancies)
    kb.row(change_category)
    return kb
def main_admin_menu():
    kb = InlineKeyboardMarkup(row_width=1)
    add_admin = InlineKeyboardButton(text="Добавить администратора", callback_data="add_admin")
    delete_admin = InlineKeyboardButton(text="Удалить администратора", callback_data="del_admin")
    # delete_vac = InlineKeyboardButton(text="Удалить вакансию", callback_data="del_vac")
    mailing = InlineKeyboardButton(text="Создать рассылку", callback_data="mailing")
    kb.row(add_admin)
    kb.row(delete_admin)
    # kb.row(delete_vac)
    kb.row(mailing)
    return kb
def second_admin_menu():
    kb = InlineKeyboardMarkup(row_width=1)
    delete_vac = InlineKeyboardButton(text="Удалить вакансию", callback_data="del_admin")
    chating = InlineKeyboardButton(text="Создать рассылку", callback_data="mailing")
    kb.row(delete_vac)
    kb.row(chating)
    return kb
def accept():
    kb = InlineKeyboardMarkup(row_width=2)
    yes = InlineKeyboardButton(text="Да, удалить", callback_data="yes")
    mm = InlineKeyboardButton(text="Не удалять", callback_data="main menu")
    kb.row(yes, mm)
    return kb
def mailing_targets():
    kb = InlineKeyboardMarkup(row_width=2)
    volunteers = InlineKeyboardButton(text="Волонтёры", callback_data="mailing_volunteers")
    nurses = InlineKeyboardButton(text="Сиделки", callback_data="mailing_nurses")
    anothers = InlineKeyboardButton(text="Другие", callback_data="mailing_anothers")
    all = InlineKeyboardButton(text="Все", callback_data="mailing_all")
    kb.row(volunteers, nurses)
    kb.row(anothers, all)
    return kb
def ch_admin_category():
    kb = InlineKeyboardMarkup(row_width=2)
    first = InlineKeyboardButton(text="1", callback_data="1")
    second = InlineKeyboardButton(text="2", callback_data="2")
    kb.row(first, second)
    return kb
def vac_show():
    kb = InlineKeyboardMarkup(row_width=2)
    next = InlineKeyboardButton(text=">", callback_data=">")
    back = InlineKeyboardButton(text="<", callback_data="<")
    mm = InlineKeyboardButton(text="Главное меню", callback_data="main menu")
    kb.row(back, next)
    kb.row(mm)
    return kb
def change_cat_menu():
    kb = InlineKeyboardMarkup(row_width=2)
    vol_change = InlineKeyboardButton(text="Волонтёр", callback_data="vol_change")
    nurse_change = InlineKeyboardButton(text="Сиделка", callback_data="nurse_change")
    another_change = InlineKeyboardButton(text="Другое", callback_data="another_change")
    kb.row(vol_change)
    kb.row(nurse_change)
    kb.row(another_change)
    return kb
