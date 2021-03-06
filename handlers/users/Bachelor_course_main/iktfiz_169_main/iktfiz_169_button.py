from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from loader import dp

from keyboards.inline.Bachelor_course_inline.iktfiz_169_inline.iktfiz_169_button import menu_169iktfiz_button

from aiogram.dispatcher import FSMContext
import logging


# Ирэт
@dp.callback_query_handler(text="IREF-CT_2")
async def IANT_1(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("Вы выбрали <b><ins>Институт Радиоэлектроники, фотоники и цифровых технологий</ins></b>\n\n"
                           "Направления:", reply_markup=menu_169iktfiz_button)


# 169
@dp.callback_query_handler(text="Transmission_systems_iktfiz_1")
async def iret_iktfiz_1(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(
        f"Вы выбрали <em><b>Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы</b></em>\n\n"
        f"🗓<b>Срок обучения</b>: 5,5 лет\n\n"
        f"💂‍♂️<b>Военная кафедра</b> - <ins>есть</ins>\n\n"
        f"🆓<b>Количество бюджетных мест</b>: <ins>46</ins>\n\n"
        f"💯<b>Проходной балл в 2020</b>: 169\n\n"
        f"🔖Государственная аккредитация: есть\n\n"
        f"🏠Дирекция:учебный корпус №5; ул. Карла Маркса, 31/7, ауд. 302\n\n"
        f"🏛Обучение проводится в учебных корпусах №: 5, 7, 8\n\n"
        f"💼Выпускающая кафедра: радиоэлектронных и телекоммуникационных систем\n\n"
        f"<b>Контактное лицо по работе с абитуриентами</b>:\n"
        f"👨🏼‍🦳Надеев Адель Фирадович - +7 (843) 231 59 11\n"
        f"E-mail - afnadeev@kai.ru\n\n")

    await c.message.answer(
        f"Данная специальность развивает лучшие традиции отечественной системы подготовки инженерных кадров и в течение полноценного 5,5 летнего цикла обеспечивает подготовку настоящих инженеров в области радиоэлектронных систем.\n"
        f"Полноценная физико-математическая подготовка, знания специализированных дисциплин, профессиональное владение современными средствами компьютерного проектирования радиоэлектронных устройств и систем, обеспечивают высокую конкурентоспособность и востребованность выпускников в самых высокотехнологичных и динамично развивающихся отраслях. С каждым годом стремительно расширяется масштаб применения радиоэлектронных систем во всех сферах человеческой деятельности:\n"
        f"• телекоммуникации\n"
        f"• транспорт\n"
        f"• авиация\n"
        f"• космос\n"
        f"• энергетика\n"
        f"• медицина\n"
        f"• строительство\n"
        f"• городская инфраструктура и многое другое\n"
        f"Передача и обработка сигналов, навигация, локация, управление, робототехника раскрывают фантастические возможности современной микроэлектроники, микропроцессорной техники, информационных технологий.\n\n"
        f"🖥Ключевые дисциплины учебного плана:\n"
        f"• Физика\n"
        f"• Инженерная и компьютерная графика\n"
        f"• Радиоматериалы и компоненты\n"
        f"• Прикладные информационные технологии\n"
        f"• Основы теории цепей\n"
        f"• Электроника\n"
        f"• Радиотехнические цепи и сигналы\n"
        f"• Электромагнитные поля и волны\n"
        f"• Основы теории систем\n"
        f"• Радиоизмерения\n"
        f"• Схемотехника аналоговых электронных устройств\n"
        f"• Модемы и кодеки радиосистем\n"
        f"• Устройства генерирования и формирования сигналов\n"
        f"• Основы компьютерного проектирования и моделирования РЭС\n"
        f"• Геоинформационные технологии\n"
        f"• Основы физического и математического моделирования\n"
        f"• Радиоавтоматика\n"
        f"• Устройства приема и преобразования сигналов\n"
        f"• Электродинамика и распространение радиоволн\n"
        f"• Электропреобразовательные устройства радиоэлектронных средств\n"
        f"• Статистическая радиотехника\n"
        f"• Цифровые устройства и микропроцессоры\n"
        f"• Устройства сверхвысоких частот и антенны\n"
        f"• Статистические методы обработки сигналов\n"
        f"• Цифровая обработка сигналов\n"
        f"• Измерительные системы\n"
        f"• Основы теории радиолокационных систем и комплексов\n"
        f"• Телевизионные системы\n"
        f"• Основы конструирования и производства радиоэлектронных средств\n"
        f"• Вычислительные устройства и системы\n"
        f"• Основы теории радионавигационных систем и комплексов\n"
        f"• Основы теории радиосистем и комплексов управления\n"
        f"• Основы теории радиосистем передачи информации\n"
        f"• Введение в системотехническое проектирование\n"
        f"• Надежность радиотехнических систем\n"
        f"• Основы теории систем и комплексов радиоэлектронной борьбы\n"
        f"• Электромагнитная совместимость\n"
        f"• Антенны летательных аппаратов\n"
        f"• Методы и устройства синхронизации в радиосистемах передачи информации\n"
        f"• Широкополосные системы передачи информации\n"
        f"• Квантовые системы\n"
        f"• Мобильные системы передачи информации\n")

    await c.message.answer(f"Преподаватели:\n"
                           f"<em>Профессора</em>:\n"
                           f"академик АН РТ Чабдаров Ш.М.\n"
                           f"д.т.н. Даутов О.Ш.\n"
                           f"д.т.н. Морозов Г.А.\n"
                           f"д.ф-м.н. Надеев А.Ф.\n"
                           f"д.т.н. Боголюбов В.М.\n"
                           f"д.т.н. Седельников Ю.Е.\n"
                           f"д.т.н. Козлов С.В.\n"
                           f"к.т.н. Щербаков Г.И.\n"
                           f"<em>Доценты</em>:\n"
                           f"к.т.н. Чони Ю.И.\n"
                           f"к.т.н. Авксентьев А.А.\n"
                           f"к.т.н. Горохов С.Н.\n"
                           f"к.т.н. Карловский А.П.\n"
                           f"к.т.н. Карманов И.В.\n"
                           f"к.т.н. Коробков А.А.\n"
                           f"к.т.н. Лаврушев В.Н.\n"
                           f"к.т.н. Можгинский В.Л.\n"
                           f"к.т.н. Потапова О.В.\n"
                           f"к.т.н. Седов С.С.\n"
                           f"к.т.н. Скачков В.А.\n"
                           f"д.т.н. Спирина Е.А.\n"
                           f"к.т.н. Стахова Н.Е.\n"
                           f"к.т.н. Фадеева Л.Ю.\n"
                           f"к.т.н. Щербакова Т.Ф.\n\n"
                           f"📕Темы выпускных работ:\n"
                           f"• Разработка автомобильного радара предотвращения столкновений\n"
                           f"• Разработка программно-определяемой радиосистемы передачи информации\n"
                           f"• Разработка системы навигации и передачи видеоинформации с борта беспилотного летательного аппарата\n"
                           f"• Разработка береговой радиолокационной системы управления судами в проливах и акваториях морских портов\n"
                           f"• Разработка бортовой РЛС обнаружения и автосопровождения низколетящих целей\n"
                           f"• Разработка мобильной метеорологической РЛС изучения атмосферы Земли\n"
                           f"• Разработка вертолетного радиолокационного комплекса\n"
                           f"• Разработка авиационного радиовысотомера\n"
                           f"• Разработка системы спутниковой связи с подвижными наземными объектами\n"
                           f"• Разработка радиоэлектронной системы контроля функционального состояния водителя транспортного средства\n\n"
                           f"👩‍🏫Практика и стажировки:\n"
                           f"• ПАО «Научно-производственное объединение «Радиоэлектроника» им. В.И. Шимко (г. Казань)\n"
                           f"• ПАО «Радиоприбор» (г. Казань)\n"
                           f"• АО «ЭЛЕКОН» (г. Казань)\n"
                           f"• АО «Ижевский радиозавод»\n"
                           f"• Региональный центр National Instruments (г. Казань, КНИТУ-КАИ)\n"
                           f"• ПАО «Туполев» (г. Казань)\n"
                           f"• «Рубеж-М» (г. Москва) и многих других, а также на научно-производственных предприятиях целевой подготовки выпускников\n\n"
                           f"👨🏽‍🔧⚙️Трудоустройство:\n"
                           f"<b>Выпускники</b> данного направления уже более 60 лет обеспечивают развитие радиоэлектронной отрасли нашей страны, составляют основу кадрового обеспечения высокотехнологичных научно-производственных объединений, осуществляющих разработку, производство и эксплуатацию радиоэлектронной аппаратуры. Среди выпускников данной специальности целая плеяда прославленных генеральных конструкторов, руководителей НИИ и предприятий, ученых, ведущих специалистов таких предприятий как:\n"
                           f"• ПАО «Научно-производственное объединение «Радиоэлектроника» им. В.И. Шимко (г. Казань)\n"
                           f"• ПАО «Радиоприбор» (г. Казань)\n"
                           f"• ПАО «Казанский электротехнический завод»\n"
                           f"• ОАО «Казанский завод «Электроприбор»\n"
                           f"• ПАО «Туполев» (г. Казань)\n"
                           f"• ПАО «Казанский вертолетный завод»\n"
                           f"• АО «Научно-производственное объединение «Государственный институт прикладной оптики» (г. Казань)\n"
                           f"• АО «Ижевский радиозавод»\n"
                           f"• АО «Ижевский электромеханический завод «Купол»\n"
                           f"• ПАО «МТС»\n"
                           f"• ПАО «МТС»\n"
                           f"• ПАО «Мегафон»\n"
                           f"• АО «Информационные спутниковые системы» им. М.Ф. Решетнева (г. Красноярск) и многих других\n"
                           f"Многие наши выпускники организуют собственные инжиниринговые компании, высокотехнологичные фирмы и предприятия.")
