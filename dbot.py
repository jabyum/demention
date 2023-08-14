import telebot
import ddatabase
import dbuttons
from telebot import types
import time

bot = telebot.TeleBot("6269391112:AAFlxxKYVCaFS6l2BS26nmMATi3bSCoQ1hg")

# тест
# ddatabase.add_vacancies("123", "Деменция", "60", "500$", "+9989123123")
# Добавить себя в админы
# ddatabase.add_admin(305896408, 1)
@bot.message_handler(commands=["start"])
def start_message(message):
    user_id = message.from_user.id
    checker = ddatabase.check_user(user_id)
    types.ReplyKeyboardRemove()
    if checker:
        category = ddatabase.get_user_category(user_id)
        if category == ("Волонтёр", ):
            bot.send_message(user_id, "Вы являетесь волонтёром. Мы будем уведомлять вас о предостоящих тренингах",
                             reply_markup=dbuttons.vol_main_menu_kb())
        elif category == ("Сиделка", ):
            bot.send_message(user_id, "Выберите пункт меню", reply_markup=dbuttons.main_menu_kb())
        elif category == ("Другое", ):
            check_vac = ddatabase.check_vac(user_id)
            bot.send_message(user_id, "Выберите пункт меню", reply_markup=dbuttons.another_main_menu_kb(check_vac=check_vac))
    elif not checker:
        bot.send_message(user_id, "Здравствуйте. Добро пожаловать в бот проекта 'Уход за больными с деменцией'"
                                  "\nОтправьте своё имя")
        bot.register_next_step_handler(message, get_name)
def get_name(message):
    user_id = message.from_user.id
    name = message.text
    bot.send_message(user_id, "Отлично, теперь отправьте номер", reply_markup=dbuttons.num_button_kb())
    bot.register_next_step_handler(message, get_number, name)
def get_number(message, name):
    user_id = message.from_user.id

    if message.contact:
        phone_number = message.contact.phone_number
        bot.send_message(user_id, "Номер принят. Выберите кем вы являетесь в нашем проекте?", reply_markup=dbuttons.categories_button_kb())
        bot.register_next_step_handler(message, get_category, name, phone_number)
    else:
        bot.send_message(user_id, "Отправьте свой номер через кнопку")
        bot.register_next_step_handler(message, get_number, name)
def get_category(message,name, phone_number):
    user_id = message.from_user.id
    if message.from_user == "Волонтёр" or "Сиделка" or "Другое":
        category = message.text
        bot.send_message(user_id, "Отлично, вы зарегистрированы", reply_markup=types.ReplyKeyboardRemove())
        ddatabase.register_user(user_id, name, phone_number, category)
        start_message(message)
    else:
        bot.send_message(user_id, "Выберите один из пунктов")
        bot.register_next_step_handler(message, get_number, name)
@bot.callback_query_handler(lambda call: call.data in ["about", "vacancies", "main menu", "new vacancies", "delete vacancies",
                                                       "yes", "mailing", "mailing_volunteers",
                                                       "mailing_nurses", "mailing_anothers", "mailing_all",
                                                       "add_admin", "<", ">", "change_category", "vol_change", "nurse_change",
                                                       "another_change", "1", "2", "del_admin"])
def calling(call):
    user_id = call.message.chat.id
    vacancies = ddatabase.get_vacancies()
    count = 0
    if call.data == "about":
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Мы в скором времени добавим всю информацию о проекте", reply_markup=dbuttons.main_menu_call_kb())
    elif call.data == "vacancies":
        bot.delete_message(user_id, call.message.message_id)
        sort_vacancies = f"Номер вакансии: {vacancies[count][0]}\nЗаболевания: {vacancies[count][1]}\nВозраст: {vacancies[count][2]}" \
                         f"\nЗП: {vacancies[count][3]}" \
                         f"\nНомер телефона: {vacancies[count][4]}"
        bot.send_message(user_id, sort_vacancies,
                         reply_markup=dbuttons.vac_show())
    elif call.data == ">":
        bot.delete_message(user_id, call.message.message_id)
        try:
            count += 1
            sort_vacancies = f"Номер вакансии: {vacancies[count][0]}\nЗаболевания: {vacancies[count][1]}\nВозраст: {vacancies[count][2]}" \
                             f"\nЗП: {vacancies[count][3]}" \
                         f"\nНомер телефона: {vacancies[count][4]}"
            bot.send_message(user_id, sort_vacancies,
                             reply_markup=dbuttons.vac_show())
        except:
            count = 0
            sort_vacancies = f"Номер вакансии: {vacancies[count][0]}\nЗаболевания: {vacancies[count][1]}\nВозраст: {vacancies[count][2]}" \
                             f"\nЗП: {vacancies[count][3]}" \
                             f"\nНомер телефона: {vacancies[count][4]}"
            bot.send_message(user_id, sort_vacancies,
                             reply_markup=dbuttons.vac_show())
    elif call.data == "<":
        bot.delete_message(user_id, call.message.message_id)
        try:
            count -= 1
            sort_vacancies = f"Номер вакансии: {vacancies[count][0]}\nЗаболевания: {vacancies[count][1]}\nВозраст: {vacancies[count][2]}" \
                             f"\nЗП: {vacancies[count][3]}" \
                         f"\nНомер телефона: {vacancies[count][4]}"
            bot.send_message(user_id, sort_vacancies,
                             reply_markup=dbuttons.vac_show())
        except:
            count = 0
            sort_vacancies = f"Номер вакансии: {vacancies[count][0]}\nЗаболевания: {vacancies[count][1]}\nВозраст: {vacancies[count][2]}" \
                             f"\nЗП: {vacancies[count][3]}" \
                             f"\nНомер телефона: {vacancies[count][4]}"
            bot.send_message(user_id, sort_vacancies,
                             reply_markup=dbuttons.vac_show())
    elif call.data == "main menu":
        bot.delete_message(user_id, call.message.message_id)
        start_message(call)
    elif call.data == "new vacancies":
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Вы можете открыть вакансию сиделки. Напишите заболевания человека, "
                                  "за которым нужно будет ухаживать")
        bot.register_next_step_handler(call.message, get_vac)
    elif call.data == "delete vacancies":
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Вы уверены, что хотите удалить свою вакансию?", reply_markup=dbuttons.accept())
    elif call.data == "yes":
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Вакансия удалена")
        ddatabase.delete_vacancies(user_id)
        start_message(call)
    elif call.data == "add_admin":
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Выберите категорию нового администратора", reply_markup=dbuttons.ch_admin_category())
    elif call.data == "1":
        bot.send_message(user_id, "Введите tg id нового администратора")
        bot.register_next_step_handler(call.message, add_admin_1cat)
    elif call.data == "2":
        bot.send_message(user_id, "Введите tg id нового администратора")
        bot.register_next_step_handler(call.message, add_admin_2cat)
    elif call.data == "mailing":
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Выберите цели для рассылки",
                         reply_markup=dbuttons.mailing_targets())
    elif call.data == "mailing_volunteers":
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Введите текст рассылки, либо отмените рассылку через кнопку в меню",
                         reply_markup=dbuttons.canceling())
        bot.register_next_step_handler(call.message, mailing_to_volunteers)
    elif call.data == "mailing_nurses":
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Введите текст рассылки, либо отмените рассылку через кнопку в меню",
                         reply_markup=dbuttons.canceling())
        bot.register_next_step_handler(call.message, mailing_to_nurses)
    elif call.data == "mailing_anothers":
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Введите текст рассылки, либо отмените рассылку через кнопку в меню",
                         reply_markup=dbuttons.canceling())
        bot.register_next_step_handler(call.message, mailing_to_anothers)
    elif call.data == "mailing_all":
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Введите текст рассылки, либо отмените рассылку через кнопку в меню",
                         reply_markup=dbuttons.canceling())
        bot.register_next_step_handler(call.message, mailing_to_all)
    elif call.data == "change_category":
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Выберите свою категорию",
                         reply_markup=dbuttons.change_cat_menu())
    elif call.data == "vol_change":
        new_category = "Волонтёр"
        ddatabase.update_category(new_category, user_id)
        bot.send_message(user_id, "Категория изменена")
        bot.delete_message(user_id, call.message.message_id)
        start_message(call)
    elif call.data == "nurse_change":
        new_category = "Сиделка"
        ddatabase.update_category(new_category, user_id)
        bot.send_message(user_id, "Категория изменена")
        bot.delete_message(user_id, call.message.message_id)
        start_message(call)
    elif call.data == "another_change":
        new_category = "Другое"
        ddatabase.update_category(new_category, user_id)
        bot.send_message(user_id, "Категория изменена")
        bot.delete_message(user_id, call.message.message_id)
        start_message(call)
    elif call.data == "del_admin":
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Введите tg id адмна",
                         reply_markup=dbuttons.canceling())
        bot.register_next_step_handler(call.message, delete_admin)
def add_admin_1cat(message):
    user_id = message.from_user.id
    new_admin_id = message.text
    rank = 1
    try:
        checker = ddatabase.check_admin(int(new_admin_id))
        if checker:
            bot.send_message(user_id, "Юзер уже является админом")
            admin_panel(message)
        else:
            ddatabase.add_admin(int(new_admin_id), rank)
            bot.send_message(user_id, "Админ добавлен")
            bot.send_message(int(new_admin_id), "Вы стали админом 1 ранга. Вступите в телеграмм группу админов\n"
                                                "https://t.me/+-OcXam-cp0MxY2My")

            admin_panel(message)
    except:
        bot.send_message(user_id, "Ошибка в id")
        admin_panel(message)
def add_admin_2cat(message):
    user_id = message.from_user.id
    new_admin_id = message.text
    rank = 2
    try:
        checker = ddatabase.check_admin(int(new_admin_id))
        if checker:
            bot.send_message(user_id, "Юзер уже является админом")
            admin_panel(message)
        else:
            ddatabase.add_admin(int(new_admin_id), rank)
            bot.send_message(user_id, "Админ добавлен")
            bot.send_message(int(new_admin_id), "Вы стали админом 2 ранга. Вступите в телеграмм группу админов\n"
                                                "https://t.me/+-OcXam-cp0MxY2My")
            admin_panel(message)
    except:
        bot.send_message(user_id, "Ошибка в id")
        admin_panel(message)
def delete_admin(message):
    user_id = message.from_user.id
    admin_id = message.text
    try:
        checker = ddatabase.check_admin(int(admin_id))
        if checker:
            ddatabase.delete_admin(int(admin_id))
            bot.send_message(user_id, "Админ удалён")
            bot.send_message(int(admin_id), "Вы больше не являетесь админом")
            bot.kick_chat_member(-1001806564382, int(admin_id))
            admin_panel(message)
        else:
            bot.send_message(user_id, "Юзер не является админом")
            admin_panel(message)
    except:
        bot.send_message(user_id, "Ошибка в id")
        admin_panel(message)
def mailing_to_volunteers(message):
    user_id = message.from_user.id
    targets = "Волонтёр"
    targets_id = ddatabase.mailing(targets)
    text = message.text
    if text == "Отмена❌":
         bot.send_message(user_id, "Рассылка отменена", reply_markup=types.ReplyKeyboardRemove())
    else:
        for i in targets_id:
            try:
                time.sleep(1)
                bot.send_message(i, text)
            except:
                continue
    bot.send_message(user_id, "Рассылка завершена", reply_markup=types.ReplyKeyboardRemove())
    admin_panel(message)

def mailing_to_nurses(message):
    user_id = message.from_user.id
    targets = "Сиделка"
    targets_id = ddatabase.mailing(targets)
    text = message.text
    if text == "Отмена❌":
         bot.send_message(user_id, "Рассылка отменена", reply_markup=types.ReplyKeyboardRemove())
    else:
        for i in targets_id:
            try:
                time.sleep(1)
                bot.send_message(i, text)
            except:
                continue
    bot.send_message(user_id, "Рассылка завершена", reply_markup=types.ReplyKeyboardRemove())
    admin_panel(message)
def mailing_to_anothers(message):
    user_id = message.from_user.id
    targets = "Другое"
    targets_id = ddatabase.mailing(targets)
    text = message.text
    if text == "Отмена❌":
         bot.send_message(user_id, "Рассылка отменена", reply_markup=types.ReplyKeyboardRemove())
    else:
        for i in targets_id:
            try:
                time.sleep(1)
                bot.send_message(i, text)
            except:
                continue
    bot.send_message(user_id, "Рассылка завершена", reply_markup=types.ReplyKeyboardRemove())
    admin_panel(message)
def mailing_to_all(message):
    user_id = message.from_user.id
    targets_id = ddatabase.mailing_all()
    text = message.text
    if text == "Отмена❌":
         bot.send_message(user_id, "Рассылка отменена", reply_markup=types.ReplyKeyboardRemove())
    else:
        for i in targets_id:
            try:
                time.sleep(1)
                bot.send_message(i, text)
            except:
                continue
    bot.send_message(user_id, "Рассылка завершена", reply_markup=types.ReplyKeyboardRemove())
    admin_panel(message)
def get_vac(message):
    user_id = message.from_user.id
    disease = message.text
    bot.send_message(user_id, "Введите возраст человека, нуждающегося в уходе")
    bot.register_next_step_handler(message, get_age, disease)
def get_age(message, disease):
    user_id = message.from_user.id
    age = message.text
    bot.send_message(user_id, "Введите сумму, которую вы готовы платить сиделке ежемесячно")
    bot.register_next_step_handler(message, get_salary, disease, age)
def get_salary(message, disease, age):
    user_id = message.from_user.id
    salary = message.text
    phone_number = ddatabase.get_user_number(user_id)[0]
    bot.send_message(user_id, "Отлично. Ваша вакансия сохранена")
    ddatabase.add_vacancies(user_id, disease, age, salary, phone_number)
    start_message(message)
@bot.message_handler(commands=["admin"])
def admin_panel(message):
    user_id = message.from_user.id
    checker = ddatabase.check_admin_rank(user_id)
    types.ReplyKeyboardRemove()
    if checker == (1, ):
        bot.send_message(user_id, "Админ панель. Выберите действие",
                         reply_markup=dbuttons.main_admin_menu())
    elif checker == (2, ):
        bot.send_message(user_id, "Админ панель",
                         reply_markup=dbuttons.second_admin_menu())



bot.polling(non_stop=True)