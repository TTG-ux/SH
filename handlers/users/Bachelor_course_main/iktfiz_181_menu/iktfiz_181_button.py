from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from loader import dp

from keyboards.inline.Bachelor_course_inline.iktfiz_181_imlime.iktfiz_181_inbut import menu_181iktfiz_button, menu_181iktfiz_button_1, \
    menu_181iktfiz_button_2, back_181_button
from keyboards.inline.ikt_fiz_inline.ikt_fiziks_b import menu_iltfiz_button_181

from aiogram.dispatcher import FSMContext
import logging


# Ирэт
@dp.callback_query_handler(text="IREF-CT_4")
async def IANT_2(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("Вы выбрали <b><ins>Институт Радиоэлектроники, фотоники и цифровых технологий</ins></b>\n\n"
                           "Направления:", reply_markup=menu_181iktfiz_button)


# 169
@dp.callback_query_handler(text="Transmission_systems_iktfiz_3")
async def iret_iktfiz_1(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(
        f"Вы выбрали <em><b>Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы</b></em>\n\n"
        f"🗓<b>Срок обучения</b>: <ins>5,5 лет</ins>\n\n"
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
                           f"академик АН РТ 👤Чабдаров Ш.М.\n"
                           f"д.т.н. 👤Даутов О.Ш.\n"
                           f"д.т.н. 👤Морозов Г.А.\n"
                           f"д.ф-м.н. 👤Надеев А.Ф.\n"
                           f"д.т.н. 👤Боголюбов В.М.\n"
                           f"д.т.н. 👤Седельников Ю.Е.\n"
                           f"д.т.н. 👤Козлов С.В.\n"
                           f"к.т.н. 👤Щербаков Г.И.\n"
                           f"<em>Доценты</em>:\n"
                           f"к.т.н. 👤Чони Ю.И.\n"
                           f"к.т.н. 👤Авксентьев А.А.\n"
                           f"к.т.н. 👤Горохов С.Н.\n"
                           f"к.т.н. 👤Карловский А.П.\n"
                           f"к.т.н. 👤Карманов И.В.\n"
                           f"к.т.н. 👤Коробков А.А.\n"
                           f"к.т.н. 👤Лаврушев В.Н.\n"
                           f"к.т.н. 👤Можгинский В.Л.\n"
                           f"к.т.н. 👤Потапова О.В.\n"
                           f"к.т.н. 👤Седов С.С.\n"
                           f"к.т.н. 👤Скачков В.А.\n"
                           f"д.т.н. 👤Спирина Е.А.\n"
                           f"к.т.н. 👤Стахова Н.Е.\n"
                           f"к.т.н. 👤Фадеева Л.Ю.\n"
                           f"к.т.н. 👤Щербакова Т.Ф.\n\n"
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
                           f"Многие наши выпускники организуют собственные инжиниринговые компании, высокотехнологичные фирмы и предприятия.",
                           reply_markup=back_181_button)


# ИАЭП
@dp.callback_query_handler(text="IAP_4")
async def iaap_2(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Вы выбрали <b><ins>Институт автоматики и электронного приборостроения</ins></b>\n"
                           f"Направления:", reply_markup=menu_181iktfiz_button_1)


# 177
@dp.callback_query_handler(text="Optoelectronic_systems_3")
async def opto_2(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Вы выбрали <b><em>Оптико-электронные системы</em></b>\n\n"
                           f"🗓<b>Срок обучения</b>: <ins>4 года</ins>\n\n"
                           f"💂‍♂️<b>Военная кафедра</b> - <ins>есть</ins>\n\n"
                           f"🆓<b>Количество бюджетных мест</b>: <ins>15</ins>\n\n"
                           f"💯<b>Проходной балл в 2020</b>: 177\n\n"
                           f"🔖Государственная аккредитация: есть\n\n"
                           f"🏠Дирекция:учебный корпус №3; ул. Толстого, 15, ауд. 201\n\n"
                           f"🏛Обучение проводится в учебных корпусах №: 1, 2, 3, 5, 7, 8, а также в лабораториях базовых предприятий\n\n"
                           f"💼Выпускающая кафедра: оптико-электронных систем\n\n"
                           f"<b>Контактное лицо по работе с абитуриентами</b>:\n"
                           f"👨🏼‍🦳Лейченко Юрий Аркадьевич - +7 (843) 235 80 91\n"
                           f"+7 (905) 023 86 22\n"
                           f"E-mail - yualeychenko@kai.ru\n\n")

    await c.message.answer(
        f"Выпускники программы готовятся к научно-исследовательской и проектно-конструкторской деятельности в области электронного и оптико-электронного приборостроения для многих отраслей народного хозяйства.\n"
        f"Область профессиональной деятельности выпускников, освоивших программу, включает проектирование, моделирование, экспериментальные исследования, техническое обслуживание, производство и эксплуатация оптико-электронных приборов и систем военного, научного и общегражданского назначения, в том числе лазерных, тепловизионных и приборов ночного видения.\n"
        f"Кафедра ОЭС является базовой кафедрой для ведущих предприятий России в области разработок и производства оптико-электронных приборов – АО Научно-производственное объединение «Государственный институт прикладной оптики», АО «Казанский оптико-механический завод» и АО «Швабе – технологическая лаборатория».\n\n"
        f"🖥Ключевые дисциплины учебного плана:\n"
        f"• Информатика\n"
        f"• Пакеты прикладных программ в профессиональной деятельности\n"
        f"• Теоретические основы электротехники\n"
        f"• Основы оптики\n"
        f"• Проектирование оптико-электронных систем\n"
        f"• Математические основы теории автоматического управления оптико-электронных систем\n"
        f"• Микропроцессорная техника в ОЭП\n"
        f"• Оптические и оптико-электронные приборы\n"
        f"• Лазерная техника\n"
        f"• Источники и приемники оптического излучения\n"
        f"• Оптические измерения\n"
        f"• Электронная и микропроцессорная техника\n"
        f"• Прикладная оптика\n"
        f"• Цифровая обработка оптической информации\n"
        f"• Моделирование процессов стабилизации\n"
        f"• Лазерные оптико-электронные приборы и системы\n"
        f"• Оптические материалы и технологии\n"
        f"• Сборка, юстировка и испытания оптико-электронных приборов\n\n")

    await c.message.answer(f"Преподаватели:\n"
                           f"Большинство преподавателей кафедры ОЭС являются докторами и кандидатами наук и имеют большой опыт работы на базовых предприятиях, связанный с разработкой, исследованиями и внедрением в производство сложных оптико-электронных приборов. Кроме этого к преподавательской деятельности привлечены ведущие ученые и разработчики с базовых предприятий. В 2019 году выпускник кафедры ОЭС, \n"
                           f"доцент кафедры Э.Р. Муслимов (1988 г.р.!) защитил диссертацию на соискание ученой степени доктора технических наук.\n\n"
                           f"📕Темы выпускных работ:\n"
                           f"• Методы построения фотоприемных устройств на основе лавинных фотодиодов\n"
                           f"• Система стабилизации изображения морского комплексированного наблюдательного оптико-электронного прибора\n"
                           f"• Исследование световозвращающих покрытий на основе нарезных дифракционных решеток\n"
                           f"• Исследование возможности повышения точности измерения коэффициентов светопропускания и светорассеяния оптических систем\n"
                           f"• Исследование волноводных методик измерения на основе ПЗС матриц\n"
                           f"• Методика расчета дальности действия теплопеленгаторов с матричными приемниками излучения\n"
                           f"• Исследование путей увеличения дальности действия импульсных лазерных дальномеров\n"
                           f"• Стенд на основе микрозеркальной матрицы\n"
                           f"• Разработка малогабаритной установки с улучшенными энергетическими характеристиками для исследования дефектов оптического стекла теневым методом\n"
                           f"• Обзорный теплопеленгатор морского базирования\n"
                           f"• Модернизация фотоэлектрической системы регистрации малогабаритного спектрометра\n"
                           f"• Исследование возможности улучшения разрешающей способности оптико-электронных приборов с регулярными волоконно-оптическими жгутами\n"
                           f"• Разработка автоматизированного рефрактометра на базе ИРФ-454\n"
                           f"• Инженерная методика расчета дальности действия лазерных локационных дальномеров\n\n"
                           f"👩‍🏫Практика и стажировки:\n"
                           f"Все виды практик, предусмотренные учебным планом, осуществляются в лабораториях, отделах и цехах базовых предприятий кафедры – АО «Казанский оптико-механический завод», АО «Научно-производственное объединение «Государственный институт прикладной оптики», АО «Швабе – Технологическая Лаборатория», АО «Стелла – К». Начиная с третьего курса студенты кафедры имеют возможность трудоустройства на базовые предприятия.\n\n"
                           f"📺Трудоустройство:\n"
                           f"Наши <b>выпускники</b> успешно трудятся на предприятиях электронного и оптико-электронного приборостроения г. Казани, в том числе и базовых, и других городов России. Среди наших выпускников главный инженер и главный технолог АО «КОМЗ», главный технолог АО «НПО ГИПО», начальники отделов и ведущие специалисты АО «КОМЗ», АО «НПО ГИПО», АО «Швабе – ТЛ», начальник отдела разработки медицинского оптико-электронного оборудования ЦКБ АО Механический завод, г. Красногорск, и многие другие.",
                           reply_markup=back_181_button)


# 181
@dp.callback_query_handler(text="Information_systems_3")
async def iaap_2(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Вы выбрали <b><em>Информационно-измерительные системы</em></b>\n\n"
                           f"🗓<b>Срок обучения</b>: <ins>4 года</ins>\n\n"
                           f"💂‍♂️<b>Военная кафедра</b> - <ins>есть</ins>\n\n"
                           f"🆓<b>Количество бюджетных мест</b>: <ins>15</ins>\n\n"
                           f"💯<b>Проходной балл в 2020</b>: 181\n\n"
                           f"🔖Государственная аккредитация: есть\n\n"
                           f"🏠Дирекция:учебный корпус №3; ул. Толстого, 15, ауд. 201\n\n"
                           f"🏛Обучение проводится в учебных корпусах №: 1, 2, 3, 5, 7, 8, а также в лабораториях базовых предприятий\n\n"
                           f"💼Выпускающая кафедра: оптико-электронных систем\n\n"
                           f"<b>Контактное лицо по работе с абитуриентами</b>:\n"
                           f"👨🏼‍🦰Солдаткин Владимир Михайлович - +7 (987) 290 81 48\n"
                           f"E-mail - w-soldatkin@mail.ru\n\n")

    await c.message.answer(
        f"Выпускники программы готовятся к выполнению проектно-конструкторской и научно-исследовательской основной профессиональной деятельности.\n"
        f"Область профессиональной деятельности выпускников включает: разработка, проектирование, конструирование, исследование и обеспечение производства приборов, измерительно-вычислительных систем и комплексов на основе цифровых технологий с широким использованием современного компьютерного и программного обеспечения для предприятий авиаприборостроения и авиастроения, медицинского и промышленного приборостроения, предназначенных для получения, регистрации и обработки информации об окружающей среде, подвижных, промышленных технических и биологических объектах, датчиков, приборов и систем для их реализации.\n\n"
        f"🖥Ключевые дисциплины учебного плана:\n"
        f"• Метрология, стандартизация и сертификация\n"
        f"• Теория решения изобретательских задач\n"
        f"• Компьютерная графика\n"
        f"• Инженерная графика\n"
        f"• Компьютерные технологии и математическое моделирование приборных устройств\n"
        f"• Пакеты прикладных программ в профессиональной деятельности\n"
        f"• Аналоговая и цифровая электроника\n"
        f"• Теория автоматического управления\n"
        f"• Теория изменений\n"
        f"• Физические основы получения информации\n"
        f"• Приборы первичной информации\n"
        f"• Основы проектирования приборов и систем\n"
        f"• Цифровые измерительные устройства\n"
        f"• Схемотехника измерительных устройств\n"
        f"• Информационно-статистическая теория измерений\n"
        f"• Точность измерительных устройств\n"
        f"• Системы отображения информации\n"
        f"• Электрические микромашины и электропривод\n"
        f"• Оптоэлектронные приборы\n"
        f"• Микропроцессорные устройства приборных комплексов\n"
        f"• Технология приборостроения\n"
        f"• Проектный менеджмент приборов и измерительно-вычислительных комплексов")

    await c.message.answer(f"Преподаватели:\n"
                           f"• 👤Солдаткин Вячеслав Владимирович, д.т.н., доцент\n"
                           f"• 👤Бердников Алексей Владимирович, к.т.н., доцент\n"
                           f"• 👤Ганеев Фарит Ахатович, к.т.н., доцент\n"
                           f"• 👤Смирнова Светлана Васильевна, к.т.н., доцент\n"
                           f"• 👤Тюрина Марина Михайловна, к.т.н., доцент\n"
                           f"• 👤Никитин Александр Владимирович, к.т.н., доцент\n"
                           f"• 👤Бельский Алексей Михайлович, старший преподаватель\n"
                           f"• 👤Ефремова Елена Сергеевна, старший преподаватель\n\n"
                           f"📕Темы выпускных работ:\n"
                           f"<b>Приборы и системы для ЖКХ</b>:\n"
                           f"• Система измерения массового расхода и количества потребляемой горячей воды.\n"
                           f"• Система измерения массового расхода и количества потребляемого теплоносителя.\n"
                           f"• Система измерения массового расхода и количества потребляемого природного газа.\n"
                           f"• Система контроля энергопотребления.\n\n"
                           f"<b>Информационно-измерительные системы и приборные комплексы самолета</b>:\n"
                           f"• Измерительно-вычислительный канал истинной воздушной скорости.\n"
                           f"• Измерительно-вычислительный канал барометрической высоты и температуры наружного воздуха.\n"
                           f"• Измерительно-вычислительный канал приборной скорости и числа Маха.\n"
                           f"• Измерительно-вычислительный канал истинного угла атаки.\n"
                           f"• Информационно-измерительные системы контроля параметров режима работы двигателей.\n"
                           f"• Информационно-измерительные системы предупреждения критических режимов полета.\n"
                           f"• Приемники и датчики первичной информации.\n\n"
                           f"<b>Информационно-измерительные системы и приборные комплексы вертолета</b>:\n"
                           f"• Измерительно-вычислительный канал истинной воздушной скорости.\n"
                           f"• Измерительно-вычислительный канал барометрической высоты и температуры наружного воздуха.\n"
                           f"• Измерительно-вычислительный канал приборной скорости.\n"
                           f"• Измерительно-вычислительный канал измерения скорости ветра на борту вертолета на различных режимах эксплуатации.\n"
                           f"• Измерительно-вычислительный канал измерения угла скольжения на борту вертолета на различных режимах эксплуатации.\n"
                           f"• Приемники и датчики первичной информации бортовых систем вертолета.\n\n"
                           f"<b>Информационно-измерительные системы и приборы малоразмерных, беспилотных и пилотируемых летательных аппаратов</b>.")

    await c.message.answer(f"👩‍🏫Практика и стажировки:\n"
                           f"• Научно-исследовательские лаборатории «Измерительные преобразователи» Учебно-научного комплекса «Авиаприборостроение» КНИТУ-КАИ\n"
                           f"• ОАО «Казанский завод «Электроприбор»\n"
                           f"• АО Научно-производственное объединение «Государственный институт прикладной оптики»\n"
                           f"• Казанский авиационный завод им. С.П.Горбунова - филиал ПАО «ТУПОЛЕВ»\n"
                           f"• АО «Казанский вертолетный завод»\n"
                           f"• АО «Теплоконтроль»\n"
                           f"• АО «Научно-производственный комплекс «ЭЛАРА» им. Г.А. Ильенко»\n"
                           f"• АО «Сарапульский электрогенераторный завод»\n\n"
                           f"📺Трудоустройство:\n"
                           f"Объектами профессиональной деятельности выпускников, освоивших программу, являются:\n"
                           f"• Бортовое радиоэлектронное оборудование перспективных самолетов различного класса и назначения\n"
                           f"• Информационно-измерительные системы и комплексы, приемники и датчики первичной информации перспективных самолетов\n"
                           f"• Бортовое радиоэлектронное оборудование перспективных вертолетов различного класса и назначения\n"
                           f"• Информационно-измерительные системы и комплексы, приемники и датчики первичной информации перспективных вертолетов\n"
                           f"• Информационно-измерительные системы малоразмерных, беспилотных и пилотируемых летательных аппаратов различного класса и назначения\n"
                           f"• Биотехнические и медицинские приборы и аппараты различного назначения\n"
                           f"• Приборы и измерительно-вычислительные системы для ЖКХ\n\n"
                           f"<b>Выпускники кафедры</b> успешно работают на крупнейших промышленных предприятиях:\n"
                           f"• ОАО «Казанский завод «Электроприбор»\n"
                           f"• Казанский авиационный завод им. С.П. Горбунова - филиал ПАО «ТУПОЛЕВ»\n"
                           f"• АО «Казанский моторостроительное производственное объединение»\n"
                           f"• ПАО «Казанский вертолетный завод»\n"
                           f"• Научно-производственное объединение «Государственный институт прикладной оптики (ГИПО)»\n"
                           f"• АО «Теплоконтроль»\n"
                           f"• АО «Завод Элекон»\n"
                           f"• АО «Радиоприбор»\n"
                           f"• ПАО «Казаньоргсинтез»\n"
                           f"• АО «Казанский медико-инструментальный завод»\n"
                           f"• ФГУП «Всероссийский научно-исследовательский институт расходометрии»\n"
                           f"• АО «Екатеринбургский завод гражданской авиации», филиал\n"
                           f"• малые инновационные предприятия и фирмы разработчики и производители профильной продукции в г. Казани\n"
                           f"а также приборостроительные предприятия в городах Ульяновск, Чебоксары, Сарапул, Арзамас, Саратов, Раменское, Дубна, Саров, Жуковский, Екатеринбург, Ижевск…",
                           reply_markup=back_181_button)


# ИАНТЭ
@dp.callback_query_handler(text="IANT_4")
async def iaap_2(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Вы выбрали <b><ins>Институт авиации, наземного транспорта и энергетики</ins></b>\n"
                           f"Направления:", reply_markup=menu_181iktfiz_button_2)


# 181
@dp.callback_query_handler(text="Aerospace_Science_3")
async def iant_1(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(
        f"Вы выбрали <b><em>Технологии производства авиакосмической и беспилотной техники из композиционных материалов. Авиокосмическое материаловедение</em></b>\n\n"
        f"🗓<b>Срок обучения</b>: <ins>4 года</ins>\n\n"
        f"💂‍♂️<b>Военная кафедра</b> - <ins>есть</ins>\n\n"
        f"🆓<b>Количество бюджетных мест</b>: <ins>65</ins>\n\n"
        f"💯<b>Проходной балл в 2020</b>: 181\n\n"
        f"🔖Государственная аккредитация: есть\n\n"
        f"🏠Дирекция:учебный корпус №3; ул. Толстого, 15, ауд. 508\n\n"
        f"🏛Обучение проводится в учебных корпусах №: 1, 2, 3, 7, 8\n\n"
        f"💼Выпускающая кафедра: производства летательных аппаратов; материаловедения, сварки и производственной безопасности\n\n"
        f"<b>Контактное лицо по работе с абитуриентами по образовательной программе <em>Конструирование и производство изделий из композиционных материалов</em></b>:\n"
        f"👩🏽Копач Алла Владимировна - +7 (917) 867 51 23\n"
        f"E-mail - avkopach@kai.ru\n\n"
        f"<b>Контактное лицо по работе с абитуриентами по образовательной программе <em>Материаловедение и технологии новых материалов</em></b>:\n"
        f"Шибаев Павел Борисович - +7 (996) 606 36 77\n"
        f"Telegram - https://teleg.run/MSWIS_KAI\n"
        f"Instagram - https://instagram.com/Mswis_kai\n"
        f"Facebook - https://www.facebook.com/groups/mswis/\n"
        f"E-mail - pbshibaev@kai.ru")

    await c.message.answer(
        f"<b>Конструирование и производство изделий из композиционных материалов</b> <em>(кафедра ПЛА)</em>\n"
        f"Основная цель учебных дисциплин – подготовка молодого специалиста к самостоятельному решению технологических проблем и задач в процессе конструкторско-технологической подготовки и постановки производства изделий из композитов. Всю учебную и научно-исследовательскую работу кафедра тесно связывает с нуждами и запросами авиационной и машиностроительной промышленности. Признанием научно-технических результатов является интерес к работе кафедры иностранных специалистов и выполнение работ по заказу европейских аэрокосмических фирм Airbus, EADS, Aero-Cabin и другие.\n\n"
        f"<b>Материаловедение и технологии новых материалов </b> <em>(кафедра МСиПБ)</em>\n"
        f"Программа направлена на подготовку бакалавров в области основных типов современных конструкционных и функциональных неорганических (металлических и неметаллических) и органических (полимерных) материалов, пленок и покрытий. Изучаются методы и средства испытаний, диагностики, исследования и контроля качества материалов, полуфабрикатов, заготовок, деталей и изделий. Материаловедение входит в перечень приоритетных направлений разработок во всех развитых странах мира, и сама по себе является одной из наиболее востребованных отраслей.\n\n"
        f"🖥Ключевые дисциплины учебного плана:\n"
        f"• Методы исследования и моделирования материалов и процессов. Композитные материалы в технике\n"
        f"• 3-Д моделирование\n"
        f"• Конструкционные и функциональные волокнистые композиты\n"
        f"• Общее материаловедение и технология материалов\n"
        f"• Механическая обработка элементов конструкций\n"
        f"• Новые материалы и технологии\n"
        f"• Теория сплавов\n"
        f"• Технологические процессы производства материалов\n"
        f"• Диагностика, контроль и управление качеством технологических процессов и материалов\n"
        f"• Материаловедение и технологии современных и перспективных материалов\n"
        f"• Математическое моделирование материалов и технологических процессов\n"
        f"• Технологическое оборудование в производстве, обработке и переработке материалов и покрытий")

    await c.message.answer(f"Преподаватели:\n"
                           f"• 👤Ильинкова Татьяна Александровна, д.т.н., профессор\n"
                           f"• 👤Федяев Владимир Леонидович, д.т.н., профессор\n"
                           f"• 👤Давлетбаев Руслан Сагитович, д.х.н., профессор\n"
                           f"• 👤Круглов Евгений Петрович, к.т.н., профессор\n"
                           f"• 👤Куртаева Фарида Наиловна, к.т.н., доцент\n"
                           f"• 👤Курынцев Сергей Вячеславович, к.э.н., доцент\n"
                           f"• 👤Беляев Алексей Витальевич, к.т.н., доцент\n"
                           f"• 👤Черноглазова Алевтина Валентиновна, к.т.н., доцент\n"
                           f"• 👤Максумова Айзада Фазыляновна, к.т.н., доцент\n"
                           f"• 👤Батраков Владимир Владимирович, к.т.н., доцент\n\n"
                           f"📕Темы выпускных работ:\n"
                           f"• Применение композитных материалов и технологий в современном авиа- и машиностроении\n"
                           f"• Компьютерное проектирование технологической оснастки и процессов композитного производства в авиа- и машиностроении\n"
                           f"• Исследование влияния технологических режимных параметров на формирование порошковых покрытий на основе термопластов\n"
                           f"• Разработка и исследование мембран для очистки промышленных газов.\n"
                           f"• Разработка теоретических основ нанесения защитных покрытий и формирования неразъёмных соединений методом погружения\n"
                           f"• Разработка и исследование полимерных пленочных сорбентов\n"
                           f"• Исследование влияния внешних факторов на эксплуатационные показатели полимерных порошковых покрытий\n"
                           f"• Исследование защитных свойств фосфорсодержащих полиуретановых покрытий\n"
                           f"• Модификация структуры алюминиевых сплавов при литье\n"
                           f"• Выявление закономерностей процессов изготовления образцов методом селективного лазерного спекания\n"
                           f"• Совершенствование методики определения остаточных напряжений поверхностного слоя металлов\n\n"
                           f"👩‍🏫Практика и стажировки:\n"
                           f"• Казанский авиационный завод им. С.П. Горбунова – филиал ПАО Туполев\n"
                           f"• КАПО – Композит\n"
                           f"• ОАО «Композит» (г. Королев, Московская обл.)\n"
                           f"• Центр композитных технологий КНИТУ-КАИ\n"
                           f"• ОАО «Казанькомпрессормаш»\n"
                           f"• Казанский вертолетный завод\n"
                           f"• ООО «Центр Приволжского региона»\n"
                           f"• ООО «Приволжское монтажное управление»\n"
                           f"<b>Стажировка</b> - Центр композитных технологий КНИТУ-КАИ\n\n"
                           f"📺Трудоустройство:\n"
                           f"Основными местами трудоустройства выпускников являются:\n"
                           f"• предприятия оборонно-промышленного комплекса\n"
                           f"• предприятия машиностроения, самолето- и ракетостроения\n"
                           f"• предприятия медицинской промышленности\n"
                           f"• центры сертификации\n"
                           f"• предприятия энергетики, нефте- и газоперерабатывающей промышленности и т.д.\n\n"
                           f"<b>Выпускникам</b> делают предложения о трудоустройстве предприятия:\n"
                           f"• Казанский авиационный завод им. С.П. Горбунова – филиал ПАО Туполев\n"
                           f"• Казанский вертолетный завод\n"
                           f"• АО КМПО\n"
                           f"• КАПО-Композит\n"
                           f"• ЗАО «Казанский Гипронииавиапром»\n"
                           f"• Центр композитных технологий КНИТУ-КАИ\n"
                           f"• МиГ – Российская самолетостроительная корпорация г. Москва\n"
                           f"• ОКБ «Сухой», г. Москва\n"
                           f"• ОАО «Сатурн», г. Рыбинск\n"
                           f"• АО «Холдинговая компания «Композит», г. Москва\n"
                           f"• АО «Климов», г. Санкт-Петербург\n"
                           f"• ОАО «Композит», г. Королев Московской обл.\n"
                           f"• ПАО РКК «Энергия», г. Королев Московской обл.\n"
                           f"• АО ОНПП «Технология» им. А.Г.Ромашина, г. Обнинск\n"
                           f"• Аэро Композит-Ульяновск»\n"
                           f"• АО «Информационные спутниковые системы» им М.Ф. Решетнева, г. Железногорск Красноярского края\n"
                           f"• АО «Зеленодольский завод им. Горького»\n"
                           f"• АО «Позис», г. Зеленодольск Республика Татарстан и многие другие государственные и коммерческие предприятия",
                           reply_markup=back_181_button)


# назад
@dp.callback_query_handler(text="back_181")
async def b_177(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.answer(f"Выбери факультет", reply_markup=menu_iltfiz_button_181)


# исклик то назад к факультетам
@dp.callback_query_handler(text="back_181_1")
async def b_177(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Выбери факультет", reply_markup=menu_iltfiz_button_181)
