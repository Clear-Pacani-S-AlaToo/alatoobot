from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


#___Main menu___
button1= KeyboardButton("О нас")
button2= KeyboardButton("Обучение")
button3= KeyboardButton("Поступление")
button4= KeyboardButton("Программы")
button5 = KeyboardButton("Сообщество")
button6 = KeyboardButton("Жизнь в МУА")
button7 = KeyboardButton("Факультеты и Цены")
button8 = KeyboardButton("Финансовая поддержка")
button9 = KeyboardButton("Клубы")
button10 = KeyboardButton("Тур по кампусам")
mainMenu= ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1, button2).add(button3, button4).add(button5, button6).add(button7, button8).add(button9, button10)


#___other menu___
buttonMain=KeyboardButton('⬅️Главное Меню')
button3_1=KeyboardButton('Степень Бакалавра')
button3_2=KeyboardButton('Магистратура')
button3_3=KeyboardButton('Среднее - профессиональное образование')
otherMenu= ReplyKeyboardMarkup(resize_keyboard=True).add(button3_1, button3_2, button3_3).add(buttonMain)

#___other menu2__
buttonMain2=KeyboardButton('⬅️Главное Меню')
button4_1=KeyboardButton('Бакалавр')
button4_2=KeyboardButton('Cтепень Магистра')
button4_3=KeyboardButton('Среднее образование')
otherMenu2= ReplyKeyboardMarkup(resize_keyboard=True).add(button4_1, button4_2, button4_3).add(buttonMain2)

#__other menu3__
buttonMenu=KeyboardButton('⬅️Меню')
button4_1_1=KeyboardButton(" Инженерия и Информатика ")
button4_2_2=KeyboardButton(" Гуманитарные науки ")
button4_3_3=KeyboardButton(" Экономика и Управление ")
button4_4_4=KeyboardButton("Медицина")
otherMenu3= ReplyKeyboardMarkup(resize_keyboard=True).add(button4_1_1, button4_2_2).add( button4_3_3,button4_4_4 ).add(buttonMenu)


#__clubs menu__
buttonMenu2=KeyboardButton('⬅️Назад')
button9_1= KeyboardButton('Социальные клубы')
button9_2= KeyboardButton('Академические клубы')
otherMenu4= ReplyKeyboardMarkup(resize_keyboard=True).add(button9_1, button9_2).add(buttonMenu2)

#___clubs menu1_2__
buttonMenu3= KeyboardButton('⬅️Вернуться')
button_9_1_1= KeyboardButton('Студенческий совет')
button_9_1_2= KeyboardButton('V-Fund')
button_9_1_3= KeyboardButton('International student council')
button_9_1_4= KeyboardButton('Комуз клуб «Нур»')
button_9_1_5= KeyboardButton('Клуб Веселых и Находчивых')
button_9_1_6= KeyboardButton('Alatoo - dance')
button_9_1_7= KeyboardButton('Music club')
button_9_1_8= KeyboardButton('Спортивный клуб')
otherMenu5=ReplyKeyboardMarkup(resize_keyboard=True).add(button_9_1_1, button_9_1_2).add(button_9_1_3, button_9_1_4).add(button_9_1_5, button_9_1_6).add(button_9_1_7, button_9_1_8).add(buttonMenu3)

#___clubs menu2_2__
button_9_2_1= KeyboardButton('Клуб Международных Отношений')
button_9_2_2= KeyboardButton('SKILSPACE ')
button_9_2_3= KeyboardButton('Enactus')
button_9_2_4= KeyboardButton('AIESEC')
button_9_2_5= KeyboardButton('Финансовый клуб')
button_9_2_6= KeyboardButton(' CYBER SECURITY-MAT')
button_9_2_7= KeyboardButton('MEDIA CLUB')
button_9_2_8= KeyboardButton('SAB')
otherMenu6=ReplyKeyboardMarkup(resize_keyboard=True).add(button_9_2_1, button_9_2_2).add(button_9_2_3, button_9_2_4).add(button_9_2_5, button_9_2_6).add(button_9_2_7, button_9_2_8).add(buttonMenu3)
