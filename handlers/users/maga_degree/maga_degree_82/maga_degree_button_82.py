from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from loader import dp

from keyboards.inline.maga_degree_inline.maga_degree_inbut_82.maga_degree_inl_82 import menu_maga_degreet_82, \
    menu_maga_degreet_82_1, back_maga_degree_82
from keyboards.inline.maga_degree_inline.maga_degee_main_inbut import menu_maga_degree_82

from aiogram.dispatcher import FSMContext
import logging


# ИАЭП
@dp.callback_query_handler(text="IANT_maga_degree_4")
async def IANT_2(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("Вы выбрали <b><ins>Институт авиации, наземного транспорта и энергетики</ins></b>\n"
                           "Направления:", reply_markup=menu_maga_degreet_82)


# 62,1
@dp.callback_query_handler(text="Materials_science_and_technology_of_materials_maga_degree_4")
async def iret_iktfiz_1(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("<ins><em><b>Вступительные испытания</b></em></ins> - междисциплинарный экзамен\n\n"
                           "<em><b>Образовательные программы</b></em>: \n\n"
                           "• Материаловедение и технология новых материалов\n"
                           "• Конструирование и производство изделий из композиционных материалов")
    await c.message.answer(
        f"Вы выбрали <em><b>Материаловедение и технология материалов</b></em>\n\n"
        f"🗓<b>Срок обучения</b>: <ins>2 года</ins>\n\n"
        f"🆓<b>Количество бюджетных мест</b>: <ins>33</ins>\n\n"
        f"🎩<b>Проходной балл по целевому приему в 2020 году</b>: 62,1\n\n"
        f"💰<b>Количество платных мест</b>: 10\n\n"
        f"🔖Государственная аккредитация: есть\n\n"
        f"🏠Дирекция:учебный корпус №3; ул. Толстого, 15, ауд. 508\n\n"
        f"🏛Обучение проводится в учебных корпусах №: 1, 2, 3, 7, 8\n\n"
        f"💼Выпускающая кафедра: производства летательных аппаратов; материаловедения, сварки и производственной безопасности\n\n"
        f"<b>Контактное лицо по работе с абитуриентами по образовательной программе <em>Конструирование и производство изделий из композиционных материалов</em></b>:\n"
        f"👱🏻‍Копач Алла Владимировна- +7 (917) 867 51 23\n"
        f"E-mail - avkopach@kai.ru\n\n"
        f"<b>Контактное лицо по работе с абитуриентами по образовательной программе <em>Материаловедение и технологии новых материалов</em></b>:\n"
        f"👨🏼‍🦱Давлетбаев Руслан Сагитович- +7 (917) 904 77 22\n"
        f"WhatsApp - https://api.whatsapp.com/send?phone=79046634210\n"
        f"E-mail - darus@rambler.ru\n\n")

    await c.message.answer(
        f"<b>Конструирование и производство изделий из композиционных материалов</b> <em>(кафедра ПЛА)</em>\n"
        f"Основная цель учебных дисциплин – подготовка молодого специалиста к самостоятельному решению технологических проблем и задач в процессе конструкторско-технологической подготовки и постановки производства изделий из композитов. Всю учебную и научно-исследовательскую работу кафедра тесно связывает с нуждами и запросами авиационной и машиностроительной промышленности. Признанием научно-технических результатов является интерес к работе кафедры иностранных специалистов и выполнение работ по заказу европейских аэрокосмических фирм Airbus, EADS, Aero-Cabin и другие.\n\n"
        f"<b>Материаловедение и технологии новых материалов</b> <em>(кафедра МСиПБ)</em>\n"
        f"Программа направлена на подготовку магистров в области основных типов современных конструкционных и функциональных неорганических (металлических и неметаллических) и органических (полимерных) материалов, пленок и покрытий. Изучаются методы и средства испытаний, диагностики, исследования и контроля качества материалов, полуфабрикатов, заготовок, деталей и изделий. Материаловедение входит в перечень приоритетных направлений разработок во всех развитых странах мира и сама по себе является одной из наиболее востребованных отраслей.\n\n"
        f"🏵Ключевые дисциплины учебного плана:\n"
        f"• Методы исследования и моделирования материалов и процессов. Композитные материалы в технике\n"
        f"• Механическая обработка элементов конструкций\n"
        f"• Технологические процессы производства материалов\n"
        f"• Математическое моделирование материалов и технологических процессов и др.\n\n"
        f"Преподаватели:\n"
        f"• 👤Ильинкова Татьяна Александровна, д.т.н., профессор\n"
        f"• 👤Давлетбаев Руслан Сагитович, д.х.н., профессор\n"
        f"• 👤Курынцев Сергей Вячеславович, к.э.н., доцент\n"
        f"• 👤Максумова Айзада Фазыляновна, к.т.н., доцент и др.\n\n"
        f"📕Темы выпускных работ:\n"
        f"• Компьютерное проектирование технологической оснастки и процессов композитного производства в авиа- и машиностроении\n"
        f"• Разработка теоретических основ нанесения защитных покрытий и формирования неразъёмных соединений методом погружения\n"
        f"• Исследование влияния внешних факторов на эксплуатационные показатели полимерных порошковых покрытий\n"
        f"• Выявление закономерностей процессов изготовления образцов методом селективного лазерного спекания и др.\n\n"
        f"🏙🧠Практика и стажировки:\n"
        f"<b>Практика</b>\n"
        f"• Казанский авиационный завод им. С.П. Горбунова – филиал ПАО Туполев\n"
        f"• ОАО «Композит» (г. Королев, Московская обл.)\n"
        f"• Казанский вертолетный завод\n"
        f"• ООО «Приволжское монтажное управление» и др.\n\n"
        f"<b>Стажировка</b>\n"
        f"• Центр композитных технологий КНИТУ-КАИ\n\n"
        f"🌬🛰Трудоустройство:\n"
        f"Основными местами трудоустройства выпускников являются:\n"
        f"• предприятия машиностроения, самолето- и ракетостроения\n"
        f"• центры сертификации\n"
        f"• предприятия энергетики, нефте- и газоперерабатывающей промышленности и т.д.\n\n"
        f"<b>Выпускникам</b> делают предложения о трудоустройстве предприятия:\n"
        f"• АО КМПО\n"
        f"• МиГ – Российская самолетостроительная корпорация г. Москва\n"
        f"• АО «Холдинговая компания «Композит», г. Москва\n"
        f"• АО «Зеленодольский завод им. Горького» и др.",
        reply_markup=back_maga_degree_82)


# 74,15
@dp.callback_query_handler(text="Design_and_technological_support_maga_degree_4")
async def iret_iktfiz_1(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("<ins><em><b>Вступительные испытания</b></em></ins> - междисциплинарный экзамен\n\n"
                           "<em><b>Образовательные программы</b></em>: \n\n"
                           "• Технология автоматизированного машиностроения")
    await c.message.answer(
        f"Вы выбрали <em><b>Конструкторско-технологическое обеспечение машиностроительных производств</b></em>\n\n"
        f"🗓<b>Срок обучения</b>: <ins>2 года</ins>\n\n"
        f"🆓<b>Количество бюджетных мест</b>: <ins>35</ins>\n\n"
        f"🎩<b>Проходной балл по целевому приему в 2020 году</b>: 74.15\n\n"
        f"💰<b>Количество платных мест</b>: 10\n\n"
        f"🔖Государственная аккредитация: есть\n\n"
        f"🏠Дирекция:учебный корпус №3; ул. Толстого, 15, ауд. 508\n\n"
        f"🏛Обучение проводится в учебных корпусах №: 2, 7, 8\n\n"
        f"💼Выпускающая кафедра: технологии машиностроительных производств\n\n"
        f"<b>Контактное лицо по работе с абитуриентами</b>:\n"
        f"👩🏼‍🦱Козлова Анна Вилениновна - +7 (917) 281 72 97\n"
        f"E-mail - аkashnenkova@mail.ru\n\n")

    await c.message.answer(
        f"Программа направлена на подготовку высококвалифицированных специалистов, готовых к применению современных методов для проектирования технологических процессов и средств технологического оснащения и способных решать профессиональные задачи для достижения финансовой устойчивости и стратегической эффективности деятельности машиностроительного предприятия, а также для обеспечения эффективности проектирования, изготовления, технического обслуживания, ремонта и утилизации продукции машиностроения на разных этапах ее жизненного цикла.\n\n"
        f"🏵Ключевые дисциплины учебного плана:\n"
        f"• Технологические процессы в машиностроении\n"
        f"• Технологические процессы изготовления деталей из листов, профилей и труб\n"
        f"• Металлообрабатывающие станки\n"
        f"• Проектирование литейных цехов и др.\n\n"
        f"Преподаватели:\n"
        f"• 👤Лунёв Александр Николаевич, д.т.н., профессор\n"
        f"• 👤Печенкин Михаил Владимирович, старший преподаватель\n"
        f"• 👤Абзалов Артур Рудольфович, к.т.н., доцент\n"
        f"• 👤Иевлев Валерий Олегович, к.т.н., доцент и др.\n\n"
        f"📕Темы выпускных работ:\n"
        f"• Модернизация технологического процесса изготовления детали «Корпус» с разработкой управляющих программ для станков с ЧПУ\n"
        f"• Совершенствование техпроцесса производства детали «Крышка» с разработкой литейной (штамповой) оснастки для получения заготовки\n\n"
        f"🏙🧠Практика и стажировки:\n"
        f"<b>Практика</b>:\n"
        f"• ОАО «КВЗ»\n"
        f"• ОАО КМПО\n"
        f"• ОАО «Элекон»\n\n"
        f"<b>Стажировка</b>:\n"
        f"• ОАО «КАИ-Лазер»\n\n"
        f"💼📌Трудоустройство:\n"
        f"Выпускник может работать на должностях:\n"
        f"• инженера-технолога с перспективой роста до главного технолога\n"
        f"• мастера с перспективой роста до начальника участка, цеха, производства, главного инженера\n"
        f"• менеджера действующих производств и др.\n\n"
        f"<b>Выпускники кафедры</b> успешно работают на крупнейших промышленных отечественных и зарубежных предприятиях:\n"
        f"• ПАО «Казанский вертолетный завод»\n"
        f"• ОАО «КМПО»\n"
        f"• ПАО Машиностроительный завод им. М.П.Калинина г. Екатеринбург\n"
        f"• ОАО Зеленодольский завод им. Горького\n"
        f"• ФГБОУ ВО «КНИТУ-КАИ» и другие ведущие промышленные предприятия, научно-исследовательских и образовательные учреждения РТ и РФ и др.",
        reply_markup=back_maga_degree_82)


# 74,6
@dp.callback_query_handler(text="Aircraft_construction_maga_degeree_4")
async def iret_iktfiz_1(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("<ins><em><b>Вступительные испытания</b></em></ins> - междисциплинарный экзамен\n\n"
                           "<em><b>Образовательные программы</b></em>: \n\n"
                           "• Вертолетостроение\n"
                           "• Самолетостроение\n"
                           "• Технология производства самолетов")
    await c.message.answer(
        f"Вы выбрали <em><b>Авиастроение</b></em>\n\n"
        f"🗓<b>Срок обучения</b>: <ins>2 года</ins>\n\n"
        f"🆓<b>Количество бюджетных мест</b>: <ins>51</ins>\n\n"
        f"🎩<b>Проходной балл по целевому приему в 2020 году</b>: 74.6\n\n"
        f"💰<b>Количество платных мест</b>: 10\n\n"
        f"🔖Государственная аккредитация: есть\n\n"
        f"🏠Дирекция:учебный корпус №3; ул. Толстого, 15, ауд. 508\n\n"
        f"🏛Обучение проводится в учебных корпусах №: 1, 3, 7, 8\n\n"
        f"💼Выпускающая кафедра: производства летательных аппаратов; конструкции и проектирования летательных аппаратов; аэрогидродинамики\n\n"
        f"<b>Контактное лицо по работе с абитуриентами</b>:\n"
        f"👱🏻‍Романова Елена Владимировна- +7 (917) 283 00 58\n"
        f"E-mail - EVRomanova@kai.ru\n\n")

    await c.message.answer(
        f"Осуществляется обучение студентов компьютерному моделированию в области самолетостроения, формированию навыков и умений использования современных компьютерных редакторов и пакетов прикладных программ при проектировании технологических процессов, оснащения и программирования автоматизированного оборудования в системе технологической подготовки авиационного производства. Изучается конструирование и расчет на прочность всех типов летательных аппаратов, современные технологии производства и конструирования воздушных судов. Направление подготовки является востребованным. По окончании обучения выпускники становятся специалистами с глубокими техническими данными в области технологии производства, проектирования и конструирования летательных аппаратов.\n\n"
        f"Наши партнеры:\n"
        f"• МГТУ им. Э.И. Баумана\n"
        f"• МГУ им М.В. Ломоносова\n"
        f"• СГАУ им С.П. Королева\n"
        f"• Университет им П. Сабатье (г. Тулуза Франция)\n\n"
        f"🏵Ключевые дисциплины учебного плана:\n"
        f"• Технология производства самолетов\n"
        f"• Конструирование агрегатов самолетов\n"
        f"• Основные агрегаты и элементы конструктивно-силовой схемы летательных аппаратов\n"
        f"• Сертификация вертолетов и др.\n\n"
        f"Преподаватели:\n"
        f"• 👤Сосов А.В., кандидат технических наук, профессор\n"
        f"• 👤Людоговский П.Л., кандидат технических наук, доцент\n"
        f"• 👤Федоров И.И., кандидат технических наук, доцент\n"
        f"• 👤Петрушенко Р.Ю., кандидат технических наук, доцент и др.\n\n"
        f"📕Темы выпускных работ:\n"
        f"• Разработка конструкции и технологии изготовления продуваемой аэродинамической оболочки пилотируемого корабля «Федерация»\n"
        f"• Проектирование хвостовой балки среднего транспортно-десантного вертолета\n"
        f"• Проект летательного аппарата с заданными требованиями\n"
        f"• Специальные темы по желанию обучающихся  и др.\n\n"
        f"🏙🧠Практика и стажировки:\n"
        f"• КАПО – Композит, Казанский вертолетный\n"
        f"• АО Научно-производственное объединение «Опытно-конструкторское бюро имени М.П. Симонова», г. Казань\n"
        f"• ООО «фирма МВЕН»\n"
        f"• Новосибирский авиационный завод имени В.П. Чкалова и др.\n\n"
        f"💼📌Трудоустройство:\n"
        f"• АО Научно-производственное объединение «Опытно-конструкторское бюро имени М.П. Симонова», г. Казань\n"
        f"• Казанский вертолетный завод\n"
        f"• ОАО «ОКБ Сухой», г. Москва\n"
        f"• АО Авиастар – СП, г. Ульяновск\n"
        f"• Компания Boeing Russia и других государственных и коммерческих структурах и др.",
        reply_markup=back_maga_degree_82)


# ИАЭП
@dp.callback_query_handler(text="IAAP_maga_degree_4")
async def IANT_2(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("Вы выбрали <b><ins>Институт автоматики и электронного приборостроения</ins></b>\n\n"
                           "Направления:", reply_markup=menu_maga_degreet_82_1)


# 82
@dp.callback_query_handler(text="Electric_power_and_electrical_engineering_maga_degree_4")
async def iret_iktfiz_1(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("<ins><em><b>Вступительные испытания</b></em></ins> - междисциплинарный экзамен\n\n"
                           "<em><b>Образовательные программы</b></em>: \n\n"
                           "• Релейная защита и автоматика интеллектуальных электроэнергетических систем\n"
                           "• Электрооборудование летательных аппаратов\n"
                           "• Электрооборудование и электроснабжение предприятий\n"
                           "• Electrical Engineering and Information Technology 🛫(ГРИНТ)🛫")
    await c.message.answer(
        f"Вы выбрали <em><b>Электроэнергетика и электротехника</b></em>\n\n"
        f"🗓<b>Срок обучения</b>: <ins>2 года</ins>\n\n"
        f"🆓<b>Количество бюджетных мест</b>: <ins>40</ins>\n\n"
        f"🎩<b>Проходной балл по целевому приему в 2020 году</b>: 82\n\n"
        f"💰<b>Количество платных мест</b>: 13\n\n"
        f"🔖Государственная аккредитация: есть\n\n"
        f"🏠Дирекция:учебный корпус №3; ул. Толстого, 15, ауд. 201\n\n"
        f"🏛Обучение проводится в учебных корпусах №: 3, 8\n\n"
        f"💼Выпускающая кафедра: электрооборудования\n\n"
        f"<b>Контактное лицо по работе с абитуриентами</b>:\n"
        f"👨Ференец Андрей Валентинович - +7 (843) 231 03 63\n"
        f"+7 (843) 231 59 22\n"
        f"E-mail - avferenets@kai.ru\n\n")

    await c.message.answer(
        f"Образовательная программа по направлению подготовки 13.04.02 «Электроэнергетика и электротехника» является программой магистратуры. Выпускники программы готовятся к научно-исследовательской и проектно-конструкторской деятельности в области разработки и эксплуатации средств электротехнического и электронного оборудования предприятий, организаций и учреждений, создания и эксплуатации средств электронного и электротехнического оборудования автомобилей и тракторов, создания и эксплуатации электротехнического оборудования летательных аппаратов. Направление подготовки магистров 13.04.02 «Электроэнергетика и электротехника» относится к приоритетным направлениям развития науки, технологий и техники в Российской Федерации и рынкам EnergyNet, AvtoNet и AeroNet национальной технологической инициативы.\n\n"
        f"🎇Ключевые дисциплины учебного плана:\n"
        f"• Моделирование электронных и электротехнических устройств\n"
        f"• CAD/CAM/CAE в электротехническом инжиниринге\n"
        f"• Системы управления электроснабжением предприятия\n"
        f"• Микропроцессорные системы управления электрооборудованием летательных аппаратов\n"
        f"• Перспективные системы электрооборудования летательных аппаратов\n"
        f"• Проектирование и функционирование сети электроснабжения и др.\n\n"
        f"Преподаватели:\n"
        f"• 👤Ференец Андрей Валентинович, заведующий кафедрой\n"
        f"• 👤Палис Штефан, профессор\n"
        f"• 👤Федоров Евгений Юрьевич, доцент\n"
        f"• 👤Гильманшин Искандер Рафаилевич, доцент и др.\n\n" 
        f"📕Темы выпускных работ:\n"
        f"• Моделирование взаимодействия плоской волны с нелинейно нагруженными сетями электропередачи во временной области\n"
        f"• Аналитический расчет и моделирование наведения стохастического электромагнитного поля на многожильный кабель в свободном пространстве\n"
        f"• Параметры наблюдаемости силовых сетей: управление СТАТКОМом как функция его внутренних характеристик и внешних характеристик сети высокого и сверхвысокого напряжения и др.\n\n"
        f"👩‍🏫Практика и стажировки:\n"
        f"• учебно-производственный центр Казанского авиационного завода ПАО «Туполев»\n"
        f"• ПАО «Казаньоргсинтез»\n"
        f"• ПАО «Казанский вертолетный завод»\n"
        f"• инженерный центр «Энергоразвитие» и других предприятиях и организациях и др.\n\n"
        f"🏛📍Трудоустройство:\n"
        f"Выпускники кафедры электрооборудования востребованы на всех предприятиях, имеющих электрооборудование, в том числе:\n\n"
        f"• ОАО «Сетевая компания РТ»\n"
        f"• ПАО КАМАЗ\n"
        f"• ПАО Казанский вертолетный завод\n"
        f"• ПАО «ОКБ им. М.П. Симонова»\n"
        f"• ICL-НПО ВС и др.",
        reply_markup=back_maga_degree_82)


# назад
@dp.callback_query_handler(text="back_maga_degree_82")
async def b_177(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.answer(f"Выбери факультет", reply_markup=menu_maga_degree_82)


# исклик то назад к факультетам
@dp.callback_query_handler(text="back_maga_degree_82_4")
async def b_177(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Выбери факультет", reply_markup=menu_maga_degree_82)
