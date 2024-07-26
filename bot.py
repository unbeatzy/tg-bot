from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, CallbackContext

# Ваш токен от BotFather
TOKEN = 'YOUR_API_KEY'

async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Проекты на заказ", callback_data='projects')],
        [InlineKeyboardButton("Примеры работ", callback_data='examples')],
        [InlineKeyboardButton("Связаться", url='https://t.me/unbtzy')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.message:
        await update.message.reply_text(
            'Привет! 👋🏻\nМеня зовут Андрей, я — частный разработчик.\n'
            'Могу сделать для тебя: сайт (лендинг, интернет-магазин или многостраничник), а так же — телеграм бота любого формата: от супер простого до бота со сложной логикой и отработкой запросов. 😊\n'
            'Мой стэк: PHP, React, Vue, Angular, JavaScript, Python, С#, Java, MongoDB, MySQL, Node.js.\n\n'
            'Ниже ты можешь ознакомиться с проектами, которые можно заказать, а так же — с примерами моих работ.😉\n'
            'Жми на кнопку и бот отобразит тебе всю информацию.\n\n'
            'Чтобы связаться со мной, нажми на соответствующую кнопку. 🙈\n'
            'Удачи!😚', reply_markup=reply_markup
        )
    elif update.callback_query:
        await update.callback_query.message.reply_text(
            'Выбирай, не стесняйся😉', reply_markup=reply_markup
        )

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == 'projects':
        keyboard = [
            [InlineKeyboardButton("Многофункциональный сайт", callback_data='multi_site')],
            [InlineKeyboardButton("Интернет-магазин", callback_data='online_store')],
            [InlineKeyboardButton("Лендинг", callback_data='landing')],
            [InlineKeyboardButton("Телеграм бот", callback_data='telegram_bot')],
            [InlineKeyboardButton("Телеграм шоп", callback_data='telegram_shop')],
            [InlineKeyboardButton("Назад", callback_data='start')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Выберите тип проекта:", reply_markup=reply_markup)

    elif data == 'examples':
        keyboard = [
            [InlineKeyboardButton("Многофункциональные сайты", callback_data='examples_multi_sites')],
            [InlineKeyboardButton("Интернет-магазины", callback_data='examples_online_stores')],
            [InlineKeyboardButton("Лендинги", callback_data='examples_landings')],
            [InlineKeyboardButton("Телеграм боты", callback_data='examples_telegram_bots')],
            [InlineKeyboardButton("Телеграм шопы", callback_data='examples_telegram_shops')],
            [InlineKeyboardButton("Назад", callback_data='start')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Выберите категорию примеров:", reply_markup=reply_markup)

    elif data == 'multi_site':
        keyboard = [
            [InlineKeyboardButton("Связаться", url='https://t.me/unbtzy')],
            [InlineKeyboardButton("Назад", callback_data='projects')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=(
            "Вы можете заказать многофункциональный сайт через данный бот. "
            "Под многофункциональным сайтом подразумевается, что это многостраничный ресурс с различным функционалом. "
            "Все условия обговариваются отдельно, включая стоимость разработки и ведения (если требуется). "
            "Вы можете нажать на соответствующую кнопку ниже, чтобы связаться со мной и обсудить детали."
        ), reply_markup=reply_markup)

    elif data == 'online_store':
        keyboard = [
            [InlineKeyboardButton("Связаться", url='https://t.me/unbtzy')],
            [InlineKeyboardButton("Назад", callback_data='projects')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=(
            "Вы можете заказать стандартный интернет-магазин, который будет выполнен под все ваши задачи. "
            "В данный проект уже включена админ-панель, с помощью которой вы сможете управлять вашим магазином: "
            "отслеживать остаток, загружать новый товар, оформлять карточки товара (добавлять название, описание, цену, "
            "загружать картинки товара), отслеживать работу платежной системы, следить за доходами, редактировать цены, "
            "выставлять скидки и запускать акции в вашем магазине.\n\n"
            "Вы можете нажать на соответствующую кнопку ниже, чтобы связаться со мной и обсудить детали."
        ), reply_markup=reply_markup)

    elif data == 'landing':
        keyboard = [
            [InlineKeyboardButton("Связаться", url='https://t.me/unbtzy')],
            [InlineKeyboardButton("Назад", callback_data='projects')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=(
            "Вы можете заказать одностраничный лендинг под разные проекты: реклама, основная услуга, "
            "информационное предложение, маркетинговые акции и многие другие варианты. При заказе вы получите "
            "самописную лендинговую страницу, которая будет разработана по вашему ТЗ. Будут учтены все анимации, текст, "
            "оформление, дизайн и функционал. К лендингу можно будет прикрутить страницу с оплатой, если вы предоставляете "
            "услуги, которые можно оплатить онлайн. Вы можете нажать на соответствующую кнопку ниже, чтобы связаться со мной и обсудить детали."
        ), reply_markup=reply_markup)

    elif data == 'telegram_bot':
        keyboard = [
            [InlineKeyboardButton("Связаться", url='https://t.me/unbtzy')],
            [InlineKeyboardButton("Назад", callback_data='projects')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=(
            "Под ваши требования и нужды разрабатывается многофункциональный телеграм бот с различной логикой. "
            "Вы можете использовать его так, как вам необходимо: консультации, квизы, вовлечение аудитории, "
            "коммуникация с вами и многие другие сценарии развития событий. Для того, чтобы заказать телеграм бота "
            "вы можете нажать на соответствующую кнопку ниже, чтобы связаться со мной и обсудить детали."
        ), reply_markup=reply_markup)

    elif data == 'telegram_shop':
        keyboard = [
            [InlineKeyboardButton("Связаться", url='https://t.me/unbtzy')],
            [InlineKeyboardButton("Назад", callback_data='projects')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=(
            "Разрабатывается телеграм шоп по той же логике, что и интернет-магазин. Пользователи могут приобрести товары "
            "сразу из телеграма: логика оплаты уже продумана и средства будут поступать на ваши счета. Будет реализована "
            "админ-панель, через которую вы сможете управлять ботом: остатки товара, добавление новых товаров, рассылка "
            "сообщений пользователям бота, отслеживание активности, редактирование ассортимента (удаление и добавление), "
            "акции, различные кампании. Можем разработать под ваши нужнды дополнительный функционал. Все обсуждается "
            "финально с вами. Вы можете нажать на соответствующую кнопку ниже, чтобы связаться со мной и обсудить детали."
        ), reply_markup=reply_markup)

    elif data == 'examples_multi_sites':
        keyboard = [
            [InlineKeyboardButton("Кафе \"Хац-Хаус\"", callback_data='example_multi_site_hats_haus')],
            [InlineKeyboardButton("Стоматология \"Кедр\"", callback_data='example_multi_site_kedr')],
            [InlineKeyboardButton("Стрелковый клуб \"Выстрел\"", callback_data='example_multi_site_vistrel')],
            [InlineKeyboardButton("Шиномонтаж \"ICESHINKA\"", callback_data='example_multi_site_iceshinka')],
            [InlineKeyboardButton("Отель \"Провинция\"", callback_data='example_multi_site_provincia')],
            [InlineKeyboardButton("Назад", callback_data='examples')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Примеры многофункциональных сайтов:", reply_markup=reply_markup)

    elif data == 'examples_online_stores':
        keyboard = [
            [InlineKeyboardButton("Магазин электроники \"Пульт\"", callback_data='example_online_store_pult')],
            [InlineKeyboardButton("Женская одежда \"Латрика\"", callback_data='example_online_store_latrika')],
            [InlineKeyboardButton("Косметика \"Натура\"", callback_data='example_online_store_natura')],
            [InlineKeyboardButton("Магазин игрушек \"Весёлый ларёк\"", callback_data='example_online_store_vesyoly_larok')],
            [InlineKeyboardButton("Назад", callback_data='examples')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Примеры интернет-магазинов:", reply_markup=reply_markup)

    elif data == 'examples_landings':
        keyboard = [
            [InlineKeyboardButton("Барбершоп \"163\"", callback_data='example_landing_163')],
            [InlineKeyboardButton("Ногтевая студия \"Queen\"", callback_data='example_landing_queen')],
            [InlineKeyboardButton("Барбершоп \"Chop-Chop\"", callback_data='example_landing_chop_chop')],
            [InlineKeyboardButton("Кальян-бар \"The Office Lounge\"", callback_data='example_landing_office_lounge')],
            [InlineKeyboardButton("Ресторан \"Утка Ли\"", callback_data='example_landing_utka_lee')],
            [InlineKeyboardButton("Назад", callback_data='examples')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Примеры лендингов:", reply_markup=reply_markup)

    elif data == 'examples_telegram_bots':
        keyboard = [
            [InlineKeyboardButton("Ключная компания \"Бобермастер\"", callback_data='example_telegram_bot_bobermaster')],
            [InlineKeyboardButton("Пранк-бот \"DRON\"", callback_data='example_telegram_bot_dron')],
            [InlineKeyboardButton("Пиар-бот \"MONSTRIK\"", callback_data='example_telegram_bot_monstrik')],
            [InlineKeyboardButton("Генератор подписей \"Signature\"", callback_data='example_telegram_bot_signature')],
            [InlineKeyboardButton("Шорт-линк \"WhatsApp Bot\"", callback_data='example_telegram_bot_whatsapp')],
            [InlineKeyboardButton("Назад", callback_data='examples')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Примеры телеграм ботов:", reply_markup=reply_markup)

    elif data == 'examples_telegram_shops':
        keyboard = [
            [InlineKeyboardButton("Кофейня \"Millor\"", callback_data='example_telegram_shop_millor')],
            [InlineKeyboardButton("Магазин \"SVELL SHOP\"", callback_data='example_telegram_shop_svell')],
            [InlineKeyboardButton("Назад", callback_data='examples')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Примеры телеграм шопов:", reply_markup=reply_markup)

    # Обработка конкретных примеров работ
    example_texts = {
        'example_multi_site_hats_haus': "Для ресторана \"Хац-Хус\" был разработан многостраничный сайт, который включает в себя функционал интернет-магазина, но реализован в виде оформления доставки. "
            "База сайта связана с Атолом, в который поступает заказ на ближайшую точку в зависимости от адреса заказа клиента. "
            "Ознакомиться с работой можно по ссылке: https://hats-haus.ru/",
        'example_multi_site_kedr': "Для стоматологической клиники \"Кедр\" был разработан многостраничный сайт с наполнением контента, реализацией админ панели и новостной ленты. "
            "Ознакомиться с работой можно по ссылке: https://kedr-stom.ru/",
        'example_multi_site_vistrel': "Для стрелкового клуба \"Выстрел\" был разработан многофункциональный и многостраничный сайт. "
            "Была реализована админ панель и форма онлайн-записи на услуги компании в разных городах. "
            "Ознакомиться с работой можно по ссылке: https://vistrel.club/",
        'example_multi_site_iceshinka': "Для шиномонтажной компании \"ICESHINKA\" был реализован многостраничный сайт со сложной структурой в виду старой платформы. "
            "Был натянут дизайн и переработана логика работы, оформлен прайс. "
            "Ознакомиться с работой можно по ссылке: https://iceshinka.ru/",
        'example_multi_site_provincia': "Для гостиницы \"Провинция\" был реализован многостраничный сайт с различными анимациями и возможностью забронировать номер в режиме онлайн без звонка. "
            "Добавлена админ панель и статистика посещений. Сайт связан с системами гостиницы, чтобы в режиме онлайн получать заявки на бронирование. "
            "Ознакомиться с работой можно по ссылке: http://provinciahotel.ru/",
        'example_online_store_pult': "Для магазина электроники был разработан с нуля интернет-магазин, который включает в себя следующий функционал: обработка остатков в 1С в режиме онлайн, админ-панель для управления сайтом (добавление товаров, редактор кода, удаление товаров, редактирование товара, загрузка контента и прочий функционал), "
            "формы обратной связи обрабатывающихся в мессенджерах, подвязка нескольких платежных систем, аварийное выключение через панель. "
            "Ознакомиться с работой можно по ссылке: https://www.pult.ru/",
        'example_online_store_latrika': "Для магазина женской одежды был разработан интернет-магазин по готовому шаблону, но модернизирован функционалом: добавлен личный кабинет (регистрация и вход), онлайн-корзина из которой можно сразу оплатить товар, панель менеджера и администратора с разными уровнями прав, подключена система обращений через мессенджеры. "
            "Ознакомиться с работой можно по ссылке: https://latrika.com/",
        'example_landing_163': "Для локального барбершопа была разработана простая лендинговая страница с анимациями, примерами работ и онлайн-записью прямо с сайта. "
            "Ознакомиться с работой можно по ссылке: https://www.barbershop163.ru/",
        'example_landing_queen': "Для локальной ногтевой студии был разработан простой лендинг с гиперссылками по странице. Реализована функция выгрузки постов из Instagram прямо на сайт, реализована форма онлайн-записи. "
            "Ознакомиться с работой можно по ссылке: https://www.queensrp.ru/",
        'example_landing_chop_chop': "Для сети барбершопов \"Chop-Chop\" был реализован простой видео-лендинг с переходом на несколько страниц. Была реализована онлайн-запись и оптимизация видеоматериала на сайте, чтобы он не нагружал клиентскую сторону. "
            "Ознакомиться с работой можно по ссылке: https://chopchop.me/",
        'example_landing_office_lounge': "Для локального кальян-бара был реализован лендинг с несколькими страницами. Основной упор сайта идет именно на лендинг, а страницы - лишь дополнение. Реализован перенос меню с текста в электронный формат на отдельную страницу сайта. "
            "Ознакомиться с работой можно по ссылке: https://theofficearh.ru/menu/",
        'example_landing_utka_lee': "Для локального ресторана с определенной концепцией был разработан лендинг с дальнешим ведением и доработкой. В процессе ведения заказчик захотел расширить лендинг несколькими страницами. Основываясь на желаниях заказчика был разработан, практически, полноценный сайт, но упор оставили на главной странице, которая и являлась лендингом в прошлом. Реализованы форма обратной связи и онлайн бронирование при условии, что ресторан работает. "
            "Ознакомиться с работой можно по ссылке: https://utka-lee.ru/",
        'example_telegram_bot_bobermaster':  "Для ключной сети \"Бобермастер\" был разработан бот, который разделял клиентов и сотрудников. Для клиентов был реализован онлайн-заказ услуги консультации, обращение и запись в точку продаж, запись на обучение (оффлайн/онлайн). "
            "Для сотрудников был реализован функционал базы знаний, где они могли ознакомиться с корпоративным материалом. Для администраторов бота была сделана админ-панель для удобного управления. Авторизация клиентов и сотрудников происходила по внутреннему номеру сотрудника и номеру телефона, который привязан к Телеграму. "
            "Ознакомиться с ботом можно по ссылке: https://t.me/bobermasterbot",
        'example_telegram_bot_dron': "Для частного клиента (ИП) был реализован бот, через которого можно разыгрывать друзей и знакомых. Суть бота заключается в том, что он отправляет запросы в разные сервисы для обратного звонка, оставляя там номер того, кого необходимо разыграть. "
            "Была привязана оплата через платежную систему: по банковской карте, СБП и по номеру телефона. Ознакомиться с работой можно по ссылке: https://t.me/bomberdronbot",
        'example_telegram_bot_monstrik': "Для частного клиента (ИП) был разработан специальный квиз-бот, в котором можно выполнять задания и получать внутреннюю валюту. Бот был нацелен на взаимный пиар за внутреннюю валюту. Пользователи могли покупать подписчиков в канал, просмотры на посты в каналах или обменивать игровую валюту на реальную. "
            "Была реализована админ-панель для отслеживания валюты, обработки запросов от пользователей и автоматизированный обмен игровой валюты на реальную. "
            "Ознакомиться с работой можно по ссылке: https://t.me/pr_monstrik_bot",
        'example_telegram_bot_signature': "Для частного клиента (ИП) был разработан бот, который генерирует подписи на основе ФИО пользователя, которые он укажет. Сам бот подвязан на технологии базовой ИИ, которая работает на бесплатном тарифе. Реализована форма заказа, с которой заявки уходят в CRM-систему. "
            "Ознакомиться с работой можно по ссылке: https://t.me/signature_maker_bot",
        'example_telegram_bot_whatsapp': "Для компании был реализован шорт-линк бот, который преобразует номер телефона в линк на диалог. Ознакомиться с работой можно по ссылке: https://t.me/WhatsApp_createlink_bot",
        'example_telegram_shop_millor': "Для локальной сети кофеен был реализован бот, в котором можно зарегистрироваться в программе лояльности и оформить заказ онлайн на вынос выбрав ближайшую кофейню. Бот был связан с Атолом и присылал заказ из телеграма сразу в систему бариста, откуда сотрудник уже мог выставлять статусы, которые отображались клиенту в боте (присылал отдельным сообщением итог по статусам: \"Взят в работу\", \"Готовится\", \"Готов\"). Помимо этого, бот рассчитывал среднее время готовности заказа на основе времени чеков бариста. Была прикручена система оплаты сразу на расчетный счет. Оплатить можно: СБП, банковской картой. Ознакомиться с работой можно по ссылке: https://t.me/Coffee_Millor_bot",
        'example_telegram_shop_svell': "Для частного клиента (ИП) был разработан магазин цифровых товаров. Была реализована админ-панель, через которую можно было добавлять товары, редактировать остатки, обновлять и редактировать описание, добавлять менеджеров (с разными уровнями прав) и переподключать платежную систему (с одной на другую). Было привязано несколько платежных систем (Тинькофф и CloudPayments). Ознакомиться с работой можно по ссылке: https://t.me/svellshop_bot",
        # Добавьте остальные примеры здесь
    }

    if data in example_texts:
        category = 'multi_sites'  # Обратите внимание, что для примеров мы указываем категорию 'multi_sites'
        keyboard = [
            [InlineKeyboardButton("Назад", callback_data=f'examples_{category}')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=example_texts[data], reply_markup=reply_markup)

    # Обработка кнопки "Назад" на главной странице
    if data == 'start':
        await start(update, context)

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == '__main__':
    main()
