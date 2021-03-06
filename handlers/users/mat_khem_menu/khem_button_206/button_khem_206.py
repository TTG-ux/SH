from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from loader import dp

from keyboards.inline.khem_inline.inline_khem_206.khem_206_inbut import menu_206khem_button, menu_206khem_button_1, \
    back_206_khem_button
from keyboards.inline.khem_inline.khem_buttons import menu_kchem_button_206

from aiogram.dispatcher import FSMContext
import logging


# ИАЭП
@dp.callback_query_handler(text="IANT_kchem_2")
async def IANT_2(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("Вы выбрали <b><ins>Институт Радиоэлектроники, фотоники и цифровых технологий</ins></b>\n\n"
                           "Направления:", reply_markup=menu_206khem_button)


# 181
@dp.callback_query_handler(text="Aerospace_Science_khem_2")
async def iant_1(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(
        f"Вы выбрали <b><em>Технологии производства авиакосмической и беспилотной техники из композиционных материалов. Авиокосмическое материаловедение</em></b>\n\n"
        f"🗓<b>Срок обучения</b>: <ins>4 года</ins>\n\n"
        f"💂‍♂️<b>Военная кафедра</b> - <ins>есть</ins>\n\n"
        f"🥺<b>Форма обучения</b> - <ins>очная</ins>\n\n"
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
        f"🧑🏻‍🦱Шибаев Павел Борисович - +7 (996) 606 36 77\n"
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
                           reply_markup = back_206_khem_button)


# ИАЭП
@dp.callback_query_handler(text="IAP_kchem_2")
async def iaap_2(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Вы выбрали <b><ins>Институт автоматики и электронного приборостроения</ins></b>\n"
                           f"Направления:", reply_markup=menu_206khem_button_1)


# 206
@dp.callback_query_handler(text="Environmental_engineering_khem_206")
async def iaap_2(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(
        f"Вы выбрали <b><em>Инженерная экология. Защита в чрезвычайных ситуациях</em></b>\n\n"
        f"🗓<b>Срок обучения</b>: <ins>4 года</ins>\n\n"
        f"💂‍♂️<b>Военная кафедра</b> - <ins>есть</ins>\n\n"
        f"🥺<b>Форма обучения</b> - <ins>очная</ins>\n\n"
        f"🆓<b>Количество бюджетных мест</b>: <ins>40</ins>\n\n"
        f"💯<b>Проходной балл в 2020</b>: 206\n\n"
        f"🎆<b>Проходной балл по целевому приему в 2020 году</b>: 187\n\n"
        f"🔖Государственная аккредитация: есть\n\n"
        f"🏠Дирекция:учебный корпус №3; ул. Толстого, 15, ауд. 201\n\n"
        f"🏛Обучение проводится в учебных корпусах №: 1, 2, 3, 7, 8\n\n"
        f"💼Выпускающая кафедра: промышленной и экологической безопасности; общей химии и экологии\n\n"
        f"<b>Контактное лицо по работе с абитуриентами по образовательной программе <em>Защита в чрезвычайных ситуациях</em></b>:\n"
        f"👩🏾‍🦱Муравьёва Елена Викторовна - +7 (843) 231 97 67\n"
        f"E-mail - elena-kzn@mail.ru\n\n"
        f"<b>Контактное лицо по работе с абитуриентами по образовательной программе <em>Защита в чрезвычайных ситуациях</em></b>:\n"
        f"👩🏼‍🦳Тунакова Юлия Алексеевна - +7 (843) 231 02 61\n"
        f"+7 (843) 231 02 62\n"
        f"E-mail - yuatunakova@kai.ru")

    await c.message.answer(
        f"<b>Защита в чрезвычайных ситуациях</b> <em>(кафедра ПЭБ)</em>\n"
        f"Защита населения и территорий от чрезвычайных ситуаций как природного, так и техногенного характера, была, есть и будет одной из важнейших задач государства. Решение ее требует наличия"
        f"высококвалифицированных кадров. В Республике Татарстан дипломированных кадров по направлению 20.03.01 Техносферная безопасность по профилю «Защита в ЧС» готовит только КНИТУ-КАИ им. А.Н. Туполева. Потребность в этих специалистах в связи с постоянным расширением функций МЧС России и почти ежедневными чрезвычайными ситуациями и природного, и производственного характера, весьма значительна. Выпускающей кафедрой по данному направлению является кафедра промышленной и экологической безопасности (ПЭБ).\n"
        f"Кафедра промышленной и экологической безопасности является выпускающей и входит в состав Института автоматики и электронного приборостроения Казанского Национального Исследовательского Технического Университета им. А.Н. Туполева-КАИ. Кафедра была образована в 2009 году профессором Муравьевой Еленой Викторовной, которая также является заведующей кафедры ПЭБ. Сегодня в штате кафедры 11 преподавателей, в основном профессора и доценты.\n"
        f"Основное направление деятельности кафедры промышленной и экологической безопасности – научно-исследовательские и передовые технологии в области техносферной безопасности внедрение их на предприятия. Особое внимание мы уделяем реализации проектов в рамках защиты от чрезвычайных ситуаций.\n"
        f"Лаборатория кафедры оснащена современной компьютерной техникой, приборами и установками, необходимыми для организации учебного процесса и проведения научных исследований на высоком уровне.\n\n"
        f"<b>Инжиниринг техносферы и экологическая безопасность </b> <em>(кафедра ОХиЭ)</em>\n"
        f"Потребность в инженерах-экологах растет год от года, в связи с высокими темпами строительства новых промышленных предприятий и реорганизацией старых, развитием инновационных технологий, модернизацией системы природоохранных органов в России.\n"
        f"Предметом инжиниринга (по ГОСТ Р 57306-2016) является интеллектуальный процесс решения творческих (инженерных) задач, связанных с проектированием и организацией процессов производства продукции (выполнения работ, оказания услуг).\n"
        f"Виды профессиональной деятельности:\n"
        f"• научно-исследовательская\n"
        f"• экспертная, надзорная и инспекционно-аудиторская\n"
        f"Наши выпускники работают в органах исполнительной власти по надзору и контролю в сфере обеспечения безопасности и защиты окружающей среды, а также на отечественных предприятиях и НИИ.\n"
        f"Выпускающей кафедрой по данному направлению является кафедра Общей химии и экологии (ОХиЭ), которая входит в состав Института автоматики и электронного приборостроения Казанского Национального Исследовательского Технического Университета им. А.Н. Туполева-КАИ. Это старейшая кафедру КНИТУ-КАИ, которая была образована в 1932 году! На кафедре реализуется трехуровневая система подготовки: бакалавриат-магистратура-аспирантура, работает докторантура. Задачей деятельности кафедры Общей химии и экологии является подготовка специалистов, способных находить оптимальные решения для обеспечения экологической безопасности производств, выбора наилучших доступных технологий для защиты окружающей среды, повышения энерго- и ресурсоэффективности, разработки и внедрения систем экологического менеджмента, проведения экологического аудита на предприятиях машиностроения, приборостроения, химии и нефтехимии и др.\n"
        f"Кафедра Общей химии и экологии проводит мультидисциплинарные исследования в области защиты окружающей среды в сотрудничестве с ведущими отечественными и зарубежными университетами и научно-исследовательскими институтами.\n"
        f"У студентов есть возможность участвовать в международных образовательных программах, конференциях и конкурсах, краткосрочных стажировках и летних школах и многих других мероприятиях.\n"
        f"На кафедре Общей химии и экологии функционируют 6 лабораторий: 4 лаборатории общего практикума, лаборатория математического моделирования в природно-техногенных системах, лаборатория физико-химических методов анализа состава веществ, материалов и изделий.")

    await c.message.answer(f"🖥Ключевые дисциплины учебного плана:\n"
                           f"<b>Защита в чрезвычайных ситуациях</b> <em>(кафедра ПЭБ)</em>\n"
                           f"• Экология\n"
                           f"• Информационные технологии в техносферной безопасности\n"
                           f"• Радиохимзащита\n"
                           f"• Пожаровзрывозащита и др.\n\n"
                           f"<b>Инжиниринг техносферы и экологическая безопасность </b> <em>(кафедра ОХиЭ)</em>\n"
                           f"• Личностное развитие\n"
                           f"• Прикладная экология\n"
                           f"• Средства контроля объектов окружающей среды\n"
                           f"• Надзор и контроль в сфере безопасности\n"
                           f"• Экологический мониторинг и производственный экологический контроль и др.")

    await c.message.answer(f"Преподаватели:\n"
                           f"<b>Защита в чрезвычайных ситуациях</b> <em>(кафедра ПЭБ)</em>\n"
                           f"• 👨Романовский Владимир Леонидович, заместитель заведующего кафедры, кандидат технических наук, профессор\n"
                           f"• 🧔Афанасьев Владимир Михайлович, доцент\n"
                           f"• 🧔‍Шакуров Рим Фатихович, доцент\n"
                           f"• 🧒Биктемирова Раиса Габдулловна, доктор медицинских наук, профессор\n"
                           f"• 👩Валеева Ксения Анатольевна, кандидат технических наук, доцент\n"
                           f"• 👩‍💼Загребина Екатерина Ильдусовна, кандидат педагогических наук, доцент\n"
                           f"• 👩‍⚕️Горбунова Оксана Анатольевна, старший преподаватель\n"
                           f"• 👩🏾‍🦱Миронова Маргарита Анатольевна, кандидат педагогических наук, доцент\n"
                           f"• 🤵Муравьев Геннадий Борисович, кандидат технических наук, доцент\n"
                           f"• 👱‍Сибгатулина Дина Шамилевна, доцент\n"
                           f"<b>Инжиниринг техносферы и экологическая безопасность </b> <em>(кафедра ОХиЭ)</em>\n"
                           f"• 👤Тунакова Юлия Алексеевна, д.х.н., профессор (член федерального учебно-методического объединения в системе высшего образования по укрупненной группе специальностей и направлений 20.00.00 – Техносферная безопасность и природообустройство, член Общественной палаты Республики Татарстан (зам. председателя комиссии по здравоохранению и экологии), член НТС Министерства экологии и природных ресурсов РТ, член редакционной коллегии журнала «Российский журнал прикладной экологии»)\n"
                           f"• 🧔‍Мингазетдинов Идгай Хасанович, к.т.н., доцент (руководитель кружка «Инженерное творчество», член-корреспондент Международной академии наук экологии, безопасности человека и природы МАНЭБ, заслуженный изобретатель РТ)\n"
                           f"• 👤Овчинников Виталий Витальевич, д.х.н., профессор (входит в сотню выдающихся химиков столетия по рейтингу Американского химического общества, «Заслуженный деятель науки РТ», «Соросовский профессор», Академик Международной педагогической академии)\n"
                           f"• 👤Кирсанов Владимир Васильевич, д.т.н., профессор («Почетный химик РФ», «Заслуженный эколог РФ», председатель регионального отделения Международной академии наук экологии, безопасности человека и природы МАНЭБ)\n"
                           f"• 👤Галимова Алина Раисовна к.х.н., доцент (куратор 1 курса, отв. за НИР, НИРС) Гумерова Гузель Ильдаровна, к.т.н., доцент\n"
                           f"• 👤Григорьева Ирина Геннадьевна, ст. преподаватель (отв. за учебную работу)\n"
                           f"• 👤Гоголь Эллина Владимировна, к.х.н., доцент, доктор агрохимии университета г. Перпиньян, Франция (отв. за международную деятельность, куратор 3 курса)\n"
                           f"• 👤Кулаков Алексей Алексеевич, к.б.н., доцент (член-корреспондент МАНЭБ, заслуженный изобретатель РТ)\n"
                           f"• 👤Кремлева Наталия Викторовна, к.х.н., доцент\n"
                           f"• 👤Лавриненко Ольга Васильевна, к.х.н., доцент (отв. за реализацию лабораторного практикума)\n"
                           f"• 👤Мальцева Светлана Александровна, к.х.н., доцент (отв. за учебно-методическую работу, руководитель группы ИППК, руководитель группы ИДПО)\n"
                           f"• 👤Шавалеева Светлана Минневагизовна, к.х.н., доцент (отв. за профориентационную деятельность)\n"
                           f"• 👤Желовицкая Алла Всеволодовна, к.х.н., доцент (куратор 4 курса)\n"
                           f"• 👤Чудакова Оксана Геннадьевна, к.х.н., доцент\n"
                           f"• 👤Сибгатуллина Ольга Сергеевна, старший преподаватель (куратор заочников)\n"
                           f"• 👤Шипилова Римма Рустемовна, ст. преподаватель (отв. за электронный документооборот кафедры и СМК)")

    await c.message.answer(f"📕Темы выпускных работ:\n"
                           f"<b>Защита в чрезвычайных ситуациях</b> <em>(кафедра ПЭБ)</em>\n"
                           f"• Расчет сил и средств для ликвидации последствий при взрыве газовоздушной смеси в промышленном здании\n"
                           f"• Методологические подходы к проектированию ситуационного центра главы субъекта РФ\n"
                           f"• Минимизация последствий ЧС при перевозке опасных грузов автомобильным транспортом\n\n"
                           f"<b>Инжиниринг техносферы и экологическая безопасность </b> <em>(кафедра ОХиЭ)</em>\n"
                           f"• Обратно-осмотический модуль в системе очистки сточных вод нефтехимического предприятия\n"
                           f"• Система оценки качества атмосферного воздуха на территории зоны активного загрязнения стационарного источника г. Казани\n"
                           f"• Вторичный радиальный отстойник для разделения иловой смеси в системе биологической очистки\n"
                           f"• Система очистки выбросов мусоросжигательного завода\n"
                           f"• Роторная дробилка для переработки строительных отходов")
    await c.message.answer(f"👩‍🏫Практика и стажировки:\n"
                           f"<b>Защита в чрезвычайных ситуациях</b> <em>(кафедра ПЭБ)</em>\n"
                           f"• МЧС РТ\n"
                           f"• Главное управление МЧС по РТ\n"
                           f"• ГИБДД РТ\n"
                           f"• Подготовка к участию во всероссийских, международных конференция\n"
                           f"• Выезды на учения, проводимые МЧС РТ\n"
                           f"• Участие в обучении населения поведению при ЧС\n"
                           f"• Участие конкурсах художественной самодеятельности\n\n"
                           f"<b>Инжиниринг техносферы и экологическая безопасность </b> <em>(кафедра ОХиЭ)</em>\n"
                           f"• Научно-исследовательская лаборатория «Экология и техносферная безопасность» КНИТУ-КАИ\n"
                           f"• Министерство экологии и природных ресурсов РТ\n"
                           f"• Управление федеральной службы по надзору в сфере природопользования по РТ\n"
                           f"• Институт проблем экологии и недропользования АН РТ\n"
                           f"• ПАО «Оргсинтез» и др.\n\n"
                           f"📺Трудоустройство:\n"
                           f"<b>Защита в чрезвычайных ситуациях</b> <em>(кафедра ПЭБ)</em>\n"
                           f"Выпускники кафедры работают в структурах МЧС, подразделениях противопожарной службы, на предприятиях в отделах промышленной безопасности, гражданской обороны, охраны труда. Выпускники, склонные к динамичной жизни, могут найти свое достойное место в частях и аварийно-спасательных отрядах МЧС России. Выпускников ждет работа:\n"
                           f"• в местных, региональных, федеральных и международных структурах МЧС России и других стран\n"
                           f"• в отделах производственной безопасности предприятий\n"
                           f"• поисково-спасательных службах и формированиях регионов\n"
                           f"• проектных институтах Хабаровска и Дальнего Востока и др.\n\n"
                           f"<b>Инжиниринг техносферы и экологическая безопасность </b> <em>(кафедра ОХиЭ)</em>\n"
                           f"• экологические службы уже функционирующих предприятий и компаний (согласно требованиям природоохранного законодательства, наличие отдела и сотрудников с профильным образованием по охране окружающей среды является ОБЯЗАТЕЛЬНЫМ)\n"
                           f"• на предприятиях-экспортерах (согласно требований ВТО и ЕС, для получения сертификата ИСО 14000-18000 для предприятий-экспортеров является ОБЯЗАТЕЛЬНЫМ наличие системы управления охраной окружающей среды, в которой работают специалисты в области экологической безопасности)\n"
                           f"• проектные организации (согласно требований СРО, наличие дипломированных выпускников программ образования в сфере экологической безопасности и защиты окружающей среды является ОБЯЗАТЕЛЬНЫМ для сертифицированных проектных структур)\n"
                           f"• государственные структуры (надзорные федеральные органы, министерства, территориальные управления, природоохранная прокуратура)\n"
                           f"• коммерческие и некоммерческие структуры экологической направленности\n"
                           f"• образовательные учреждения, в том числе учреждения дополнительного образования",
                           reply_markup=back_206_khem_button)


# назад
@dp.callback_query_handler(text="back_khem_206")
async def b_177(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.answer(f"Выбери факультет", reply_markup=menu_kchem_button_206)


# исклик то назад к факультетам
@dp.callback_query_handler(text="back_khem_206_2")
async def b_177(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Выбери факультет", reply_markup=menu_kchem_button_206)
