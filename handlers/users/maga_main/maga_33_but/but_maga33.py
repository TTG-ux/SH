from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from loader import dp

from keyboards.inline.maga_inline_main.inline_maga_33.in_maga_33 import menu_maga_inline_button_33, menu_maga_ineline_button_33_1,\
    back_maga_inline_button_33
from keyboards.inline.maga_inline_main.midle_maga_inline import menu_maga_button_33

from aiogram.dispatcher import FSMContext
import logging


# ИРЭФ-ЦТ
@dp.callback_query_handler(text="IREF_CT_maga_2")
async def IANT_2(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("Вы выбрали <b><ins>Институт Радиоэлектроники, фотоники и цифровых технологий</ins></b>\n\n"
                           "Направления:", reply_markup=menu_maga_inline_button_33)


# 30
@dp.callback_query_handler(text="Design_technology_maga_2")
async def iret_iktfiz_1(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("<ins><em><b>Вступительные испытания</b></em></ins> - компьютерное тестирование\n\n"
                           "<em><b>Образовательные программы</b></em>: \n\n"
                           "• Конструирование радиоэлектронных средств\n"
                           "• Проектирование и технология радиоэлектронных средств")
    await c.message.answer(
        f"Вы выбрали <em><b>Конструирование и технология электронных средств</b></em>\n\n"
        f"🗓<b>Срок обучения</b>: <ins>2 года</ins>\n\n"
        f"🆓<b>Количество бюджетных мест</b>: <ins>24</ins>\n\n"
        f"💯<b>Проходной балл в 2020</b>: 30\n\n"
        f"💰<b>Количество платных мест</b>: 5\n\n"
        f"🔖Государственная аккредитация: есть\n\n"
        f"🏠Дирекция:учебный корпус №5; ул. Карла Маркса, 31/7, ауд. 300\n\n"
        f"🏛Обучение проводится в учебных корпусах №: 5, 7, 8\n\n"
        f"💼Выпускающая кафедра: конструирования и технологии производства электронных средств\n\n"
        f"<b>Контактное лицо по работе с абитуриентами</b>:\n"
        f"🧔🏻‍Карамов Фидус Ахмадиевич - +7 (843) 231 59 20\n"
        f"+7 (843) 231 59 22\n"
        f"E-mail - fakaramov@kai.ru\n\n")

    await c.message.answer(
        f"В процессе обучения студенты магистратуры получают теоретическую и практическую подготовку в области конструирования и технологии производства радиоэлектронных, электронно-вычислительных, микро- и наноэлектронных средств, как гражданского, так и военного и двойного назначения, отвечающих целям их функционирования, требованиям надежности, дизайна, условиям эксплуатации и маркетинга. По окончании обучения выпускники подготовлены к научно-исследовательской, проектно-конструкторской, производственно-технологической, организационно-управленческой, монтажно-наладочной и сервисно-эксплуатационной видам практической деятельности на предприятиях радиоэлектронной отрасли и смежным производствам, т.е. везде, где есть электроника в составе продукции.\n\n"
        f"Учебная программа включает изучение языков программирования в том числе и прикладного, т.е. программирование микросхем и микропроцессоров, их прошивка, систем автоматизированного проектирования (САПР), принципов работы компонентов радиоэлектронной аппаратуры, микро- и наноэлектроники. При обучении широко используются информационные, вычислительные и измерительные технологии с практическим использованием компьютерной техники для создания моделей различных конструкций радиоэлектронных средств с последующим получением опытных образцов, в том числе методом прототипирования.\n\n"
        f"🕋Ключевые дисциплины учебного плана:\n"
        f"• САПР в электронике\n"
        f"• Схемотехническое проектирование электронных средств\n"
        f"• Современные методы компоновки электронных средств\n"
        f"• Математическое моделирование устройств и систем\n"
        f"• Технологические процессы микроэлектроники и др."
        f"Преподаватели:\n"
        f"• 👤Карамов Ф.А., д.т.н., профессор\n"
        f"• 👤Саиткулов В.Г., д.т.н., профессор\n"
        f"• 👤Крючатов В.И., д.т.н., профессор\n"
        f"• 👤Литвинов И.А., д.т.н., профессо\n"
        f"• 👤Галеев И.Г., д.ф.-м.н., профессор\n"
        f"• 👤Фазылзянов Р.Х., к.т.н., доцент\n"
        f"• 👤Кузнецов Д.И., к.т.н., доцент\n"
        f"📕Темы выпускных работ:\n"
        f"• Математическое моделирование электронных приборов, устройств различного функционального назначения и технологических процессов с использованием возможностей автоматизированного проектирования\n"
        f"• Разработка технологии монтажа на плате разноразмерных поверхностно-монтируемых изделий электронной техники\n"
        f"• Разработка методик исследования состава и структуры различных материалов электронной техники\n"
        f"• Исследование и разработка новых методов диагностики материалов электронной техники7n"
        f"• Разработка технологии изготовления электронного блока Blutooth для связи с телефоном на базе Android\n\n"
        f"👩‍🏫Практика и стажировки:\n"
        f"По окончании каждого курса студенты проходят различного вида практики на ведущих предприятиях Татарстана, в том числе входящих в АО «Концерн Радиоэлектронные технологии»:\n"
        f"• АО «Казанское приборостроительное конструкторское бюро»\n"
        f"• АО «Научно-производственное объединение «Радиоэлектроника» им. В.И. Шимко»\n"
        f"• ОАО «Радиоприбор»\n"
        f"• ОАО «Казанский научно-исследовательский технологический институт вычислительной техники»\n\n"
        f"👨🏽‍🔧⚙️Трудоустройство:\n"
        f"Выпускники, подготовленные по этой специальности, могут работать на инженерно-технических должностях, а также стать ведущими специалистами проектных, научно-исследовательских, производственно-управленческих структур и менеджерами сервисно-эксплуатационного отдела предприятий различных отраслей производства. Наиболее часто занимаемы должности:\n"
        f"• инженер-схемотехник\n"
        f"• инженер-электроник\n"
        f"• технолог\n"
        f"• инженер-конструктор\n"
        f"• инженер-проектировщик",
        reply_markup=back_maga_inline_button_33)


# ИАЭП
@dp.callback_query_handler(text="IANT_maga_2")
async def IANT_2(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("Вы выбрали <b><ins>Институт автоматики и электронного приборостроения</ins></b>\n\n"
                           "Направления:", reply_markup=menu_maga_ineline_button_33_1)


# 33
@dp.callback_query_handler(text="Equipment_Management_maga_2")
async def iret_iktfiz_1(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("<ins><em><b>Вступительные испытания</b></em></ins> - междисциплинарный экзамен\n\n"
                           "<em><b>Образовательные программы</b></em>: \n\n"
                           "• Управление и информатика в интеллектуальных технических системах\n"
                           "• Systems Engineering and Engineering Cybernetics 🛫(ГРИНТ)🛫")
    await c.message.answer(
        f"Вы выбрали <em><b>Управление в технических системах</b></em>\n\n"
        f"🗓<b>Срок обучения</b>: <ins>2 года</ins>\n\n"
        f"🆓<b>Количество бюджетных мест</b>: <ins>26</ins>\n\n"
        f"💯<b>Проходной балл в 2020</b>: 33\n\n"
        f"💰<b>Количество платных мест</b>: 14\n\n"
        f"🔖Государственная аккредитация: есть\n\n"
        f"🏠Дирекция:учебный корпус №3; ул. Толстого, 15, ауд. 201\n\n"
        f"🏛Обучение проводится в учебных корпусах №: 2, 3\n\n"
        f"💼Выпускающая кафедра: автоматики и управления\n\n"
        f"<b>Контактное лицо по работе с абитуриентами</b>:\n"
        f"🧔🏻‍Карамов Фидус Ахмадиевич - +7 (843) 231 59 20\n"
        f"+7 (843) 231 59 22\n"
        f"E-mail - fakaramov@kai.ru\n\n")

    await c.message.answer(
        f"В процессе обучения студенты магистратуры получают теоретическую и практическую подготовку в области конструирования и технологии производства радиоэлектронных, электронно-вычислительных, микро- и наноэлектронных средств, как гражданского, так и военного и двойного назначения, отвечающих целям их функционирования, требованиям надежности, дизайна, условиям эксплуатации и маркетинга. По окончании обучения выпускники подготовлены к научно-исследовательской, проектно-конструкторской, производственно-технологической, организационно-управленческой, монтажно-наладочной и сервисно-эксплуатационной видам практической деятельности на предприятиях радиоэлектронной отрасли и смежным производствам, т.е. везде, где есть электроника в составе продукции.\n\n"
        f"Учебная программа включает изучение языков программирования в том числе и прикладного, т.е. программирование микросхем и микропроцессоров, их прошивка, систем автоматизированного проектирования (САПР), принципов работы компонентов радиоэлектронной аппаратуры, микро- и наноэлектроники. При обучении широко используются информационные, вычислительные и измерительные технологии с практическим использованием компьютерной техники для создания моделей различных конструкций радиоэлектронных средств с последующим получением опытных образцов, в том числе методом прототипирования.\n\n"
        f"🕋Ключевые дисциплины учебного плана:\n"
        f"• САПР в электронике\n"
        f"• Схемотехническое проектирование электронных средств\n"
        f"• Современные методы компоновки электронных средств\n"
        f"• Математическое моделирование устройств и систем\n"
        f"• Технологические процессы микроэлектроники и др."
        f"Преподаватели:\n"
        f"• 👤Карамов Ф.А., д.т.н., профессор\n"
        f"• 👤Саиткулов В.Г., д.т.н., профессор\n"
        f"• 👤Крючатов В.И., д.т.н., профессор\n"
        f"• 👤Литвинов И.А., д.т.н., профессо\n"
        f"• 👤Галеев И.Г., д.ф.-м.н., профессор\n"
        f"• 👤Фазылзянов Р.Х., к.т.н., доцент\n"
        f"• 👤Кузнецов Д.И., к.т.н., доцент\n"
        f"📕Темы выпускных работ:\n"
        f"• Математическое моделирование электронных приборов, устройств различного функционального назначения и технологических процессов с использованием возможностей автоматизированного проектирования\n"
        f"• Разработка технологии монтажа на плате разноразмерных поверхностно-монтируемых изделий электронной техники\n"
        f"• Разработка методик исследования состава и структуры различных материалов электронной техники\n"
        f"• Исследование и разработка новых методов диагностики материалов электронной техники7n"
        f"• Разработка технологии изготовления электронного блока Blutooth для связи с телефоном на базе Android\n\n"
        f"👩‍🏫Практика и стажировки:\n"
        f"По окончании каждого курса студенты проходят различного вида практики на ведущих предприятиях Татарстана, в том числе входящих в АО «Концерн Радиоэлектронные технологии»:\n"
        f"• АО «Казанское приборостроительное конструкторское бюро»\n"
        f"• АО «Научно-производственное объединение «Радиоэлектроника» им. В.И. Шимко»\n"
        f"• ОАО «Радиоприбор»\n"
        f"• ОАО «Казанский научно-исследовательский технологический институт вычислительной техники»\n\n"
        f"👨🏽‍🔧⚙️Трудоустройство:\n"
        f"Выпускники, подготовленные по этой специальности, могут работать на инженерно-технических должностях, а также стать ведущими специалистами проектных, научно-исследовательских, производственно-управленческих структур и менеджерами сервисно-эксплуатационного отдела предприятий различных отраслей производства. Наиболее часто занимаемы должности:\n"
        f"• инженер-схемотехник\n"
        f"• инженер-электроник\n"
        f"• технолог\n"
        f"• инженер-конструктор\n"
        f"• инженер-проектировщик", reply_markup=back_maga_inline_button_33)


# назад
@dp.callback_query_handler(text="back_maga_33")
async def b_177(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.answer(f"Выбери факультет", reply_markup=menu_maga_button_33)


# исклик то назад к факультетам
@dp.callback_query_handler(text="back_maga_33_2")
async def b_177(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Выбери факультет", reply_markup=menu_maga_button_33)
