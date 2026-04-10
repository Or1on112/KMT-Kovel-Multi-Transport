import os

nav_template = """
    <header class="site-header">
        <a href="index.html" class="logo">
            <img src="../assets/images/KMT_logo.png" alt="KMT">
        </a>
        <nav class="main-nav">
            <ul>
                <li><a href="about.html">Про термінал</a></li>
                <li><a href="services.html">Послуги</a></li>
                <li><a href="infrastructure.html">Інфраструктура</a></li>
                <li><a href="advantages.html">Переваги</a></li>
                <li><a href="info.html">Корисна інформація</a></li>
                <li><a href="contact.html">Контакти</a></li>
            </ul>
        </nav>
        <div class="header-actions">
            <div class="lang-switch"><span class="active">UA</span> / <span>EN</span></div>
            <a href="contact.html" class="btn btn-primary">Отримати консультацію</a>
        </div>
    </header>
"""

footer_template = """
    <footer class="site-footer">
        <div class="footer-grid">
            <div class="footer-nav">
                <h4 class="label-md">Навігація</h4>
                <ul>
                    <li><a href="about.html">Про термінал</a></li>
                    <li><a href="services.html">Послуги</a></li>
                </ul>
            </div>
            <div class="footer-contacts">
                <h4 class="label-md">Контакти</h4>
                <p>м. Ковель, вул. Варшавська, 1</p>
            </div>
            <div class="footer-legal">
                <h4 class="label-md">Юридична інформація</h4>
                <p><a href="#privacy">Політика конфіденційності</a></p>
                <p>© 2024 Kovel Multi Transport (KMT)</p>
            </div>
        </div>
    </footer>
"""

page_base = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | KMT</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Manrope:wght@600;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
    <style>
       .content-block {{ max-width: 900px; margin: 0 auto; padding-bottom: var(--spacing-8); }}
       .content-block h2 {{ margin-top: var(--spacing-8); margin-bottom: var(--spacing-4); font-family: var(--font-display); font-size: 1.5rem; }}
       .content-block p {{ margin-bottom: var(--spacing-4); color: var(--on-surface-variant); font-size: 1rem; line-height: 1.6; }}
       .content-block ul {{ margin-left: var(--spacing-8); margin-bottom: var(--spacing-4); }}
       .content-block li {{ margin-bottom: var(--spacing-2); color: var(--on-surface-variant); line-height: 1.6; }}
       .page-header {{ background: var(--primary); color: white; padding: var(--spacing-16) var(--spacing-24); margin-bottom: var(--spacing-16); }}
       .page-header h1 {{ font-family: var(--font-display); font-size: 3rem; margin:0; }}
       .action-btn {{ display: inline-block; margin-top: var(--spacing-4); }}
    </style>
</head>
<body>
{nav}
    <main>
        <div class="page-header">
            <h1>{title}</h1>
        </div>
        <section class="section-padding content-block">
            {content}
        </section>
    </main>
{footer}
</body>
</html>
"""

pages = {
    "about.html": {
        "title": "Про нас",
        "content": """
            <p>Термінал ТОВ «Сільмашторг» - сучасний митно-логістичний комплекс, розташований у місті Ковель, одному з ключових транспортних вузлів на шляху між Україною та країнами Європейського Союзу.</p>
            <p>Завдяки вигідному розташуванню поруч із міжнародною трасою Київ - Ягодин, наш термінал є важливою ланкою логістичної інфраструктури для компаній, що здійснюють зовнішньоекономічну діяльність.</p>
            <h2>Наші ключові особливості</h2>
            <ul>
                <li>Близькість до пунктів пропуску Ягодин - Дорогуськ (60 км) та Устилуг - Зосин.</li>
                <li>Залізничні колії українського стандарту (1520 мм) та європейського (1435 мм).</li>
                <li>Митний пост на території для швидкого розмитнення без переміщення вантажу.</li>
                <li>Служби ветеринарного та фітосанітарного контролю на території.</li>
                <li>Комплексна WMS-система для управління складськими запасами.</li>
            </ul>
        """
    },
    "services.html": {
        "title": "Послуги",
        "content": """
            <p>Термінал ТОВ «Сільмашторг» надає повний спектр послуг для обробки міжнародних автомобільних та залізничних вантажів.</p>
            <h2>Митне оформлення</h2>
            <p>На території терміналу працює підрозділ Волинської митниці та служби ветеринарного й фітосанітарного контролю.</p>
            <a href="form-customs.html" class="btn btn-primary-dark action-btn">Розрахувати митне оформлення</a>
            
            <h2>Митний склад</h2>
            <p>Закрите приміщення площею 345 м² і відкритий майданчик 6000 м² для зберігання товарів під митним контролем із відстрочкою платежів до 3-х років.</p>
            <a href="form-warehouse.html" class="btn btn-primary-dark action-btn">Замовити митний склад</a>

            <h2>Залізничні перевантаження</h2>
            <p>Прийом вагонів європейської та української колії, перевантаження вагон-вагон або вагон-автомобіль.</p>
            <a href="form-rail.html" class="btn btn-primary-dark action-btn">Замовити перевантаження</a>

            <h2>Контейнерний майданчик</h2>
            <p>Приймання, обробка, зберігання та стафірування контейнерів.</p>
            <a href="form-container.html" class="btn btn-primary-dark action-btn">Замовити обробку контейнера</a>

            <h2>Паркінг</h2>
            <p>Спеціальна зона для великовантажного транспорту, що очікує оформлення.</p>
            <a href="form-parking.html" class="btn btn-primary-dark action-btn">Забронювати місце</a>
        """
    },
    "infrastructure.html": {
        "title": "Інфраструктура",
        "content": """
            <p>Наш термінал – це сучасний митно-логістичний комплекс, що поєднує продуману інфраструктуру та передові технології.</p>
            <ul>
                <li><strong>Митна інфраструктура:</strong> Митний пост, ветеринарний/фітосанітарний контроль (єдине вікно).</li>
                <li><strong>Митний склад:</strong> Закрите приміщення (345 м²) та відкритий майданчик (6000 м²).</li>
                <li><strong>Паркінг:</strong> Облаштований майданчик для вантажного транспорту.</li>
                <li><strong>Залізнична інфраструктура:</strong> Колії 1520 мм та 1435 мм.</li>
                <li><strong>Контейнерна зона:</strong> Зручне приймання та відвантаження контейнерів.</li>
                <li><strong>Безпека:</strong> Цілодобове відеоспостереження та Warehouse Management System (WMS).</li>
            </ul>
        """
    },
    "advantages.html": {
        "title": "Наші переваги",
        "content": """
            <h2>Чому обирають нас?</h2>
            <p>Ми забезпечуємо швидкість, безпеку та ефективність у кожній логістичній операції.</p>
            <ul>
                <li><strong>Стратегічне розташування:</strong> Ковель - ключовий транспортний вузол. 60 км до ЄС.</li>
                <li><strong>Інтермодальна логістика:</strong> Поєднання автомобільного та залізничного транспорту різних стандартів.</li>
                <li><strong>Комплексні послуги:</strong> Митний пост, всі служби контролю в одному місці. Брокерський супровід.</li>
                <li><strong>Сучасні технології:</strong> Автоматизоване управління складами (WMS). Повний контроль руху.</li>
            </ul>
        """
    },
    "info.html": {
        "title": "Корисна інформація",
        "content": """
            <h2>Як проходить оформлення автотранспорту</h2>
            <ol style="margin-left: 2rem; color: var(--on-surface-variant); line-height: 1.6; margin-bottom: 2rem;">
                <li>Прибуття транспорту та реєстрація в системі.</li>
                <li>Документальне оформлення (перевірка документів, підготовка декларацій).</li>
                <li>Митні процедури та контроль на терміналі.</li>
                <li>Складські операції (за потреби зберігання).</li>
                <li>Завершення процедур та виїзд.</li>
            </ol>
            <p><em>Середній час оформлення: від 2 до 8 годин.</em></p>
        """
    },
    "contact.html": {
        "title": "Контакти",
        "content": """
            <p><strong>Адреса:</strong> м. Ковель, Волинська область, вул. Варшавська, 1</p>
            <p><strong>Телефон:</strong> [Вкажіть номер]</p>
            <p><strong>Email:</strong> [Вкажіть Email]</p>
            
            <form style="margin-top: 2rem; display: flex; flex-direction: column; gap: 1rem; max-width: 500px;">
                <input type="text" placeholder="Ім'я" class="form-input" style="padding: 1rem; background: var(--surface-container-low); border: none; border-bottom: 2px solid transparent;">
                <input type="text" placeholder="Компанія" class="form-input" style="padding: 1rem; background: var(--surface-container-low); border: none; border-bottom: 2px solid transparent;">
                <input type="tel" placeholder="Телефон" class="form-input" style="padding: 1rem; background: var(--surface-container-low); border: none; border-bottom: 2px solid transparent;">
                <textarea placeholder="Повідомлення" rows="4" style="padding: 1rem; background: var(--surface-container-low); border: none; border-bottom: 2px solid transparent;"></textarea>
                <button type="button" class="btn btn-primary" style="margin-top: 1rem;">Відправити</button>
            </form>
        """
    }
}

for filename, data in pages.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(page_base.format(
            title=data["title"],
            content=data["content"],
            nav=nav_template,
            footer=footer_template
        ))

# Now create Tailwind-based Forms based on code.html
tailwind_form_base = """<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title} | KMT Форма</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Inter:wght@400;500;700&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<script>
      tailwind.config = {{
        darkMode: "class",
        theme: {{
          extend: {{
            colors: {{
              "surface-bright": "#f7faf4",
              "primary": "#005015",
              "primary-container": "#006b1f",
              "on-primary": "#ffffff",
              "on-primary-container": "#8de98d",
              "surface-container-low": "#f2f5ee",
              "surface-container-highest": "#e0e3dd",
              "surface-container-lowest": "#ffffff",
              "on-surface": "#191d19",
              "on-surface-variant": "#3f493d",
              "outline": "#6f7a6c",
              "outline-variant": "#bfcaba"
            }},
            fontFamily: {{
              "headline": ["Manrope"],
              "body": ["Inter"],
              "label": ["Inter"]
            }},
            borderRadius: {{"DEFAULT": "0rem", "lg": "0rem", "xl": "0rem", "full": "9999px"}},
          }},
        }},
      }}
</script>
<style>
    .material-symbols-outlined {{ font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }}
    body {{ font-family: 'Inter', sans-serif; }}
    h1, h2, h3 {{ font-family: 'Manrope', sans-serif; }}
</style>
</head>
<body class="bg-surface-bright text-on-surface selection:bg-primary selection:text-on-primary">
<nav class="bg-[#f7faf4] flex justify-between items-center w-full px-24 py-4 max-w-full fixed top-0 z-50 border-b border-outline-variant">
    <a href="index.html" class="text-xl font-black text-[#005015] uppercase tracking-tighter">Термінал ТОВ «Сільмашторг»</a>
    <div class="hidden md:flex gap-8 items-center">
        <a class="font-bold uppercase tracking-tighter text-sm text-[#2d312d] hover:bg-[#e0e3dd] px-2 py-1" href="about.html">Про нас</a>
        <a class="font-bold uppercase tracking-tighter text-sm text-[#2d312d] hover:bg-[#e0e3dd] px-2 py-1" href="services.html">Послуги</a>
        <a class="font-bold uppercase tracking-tighter text-sm text-[#2d312d] hover:bg-[#e0e3dd] px-2 py-1" href="infrastructure.html">Інфраструктура</a>
    </div>
    <div class="flex items-center gap-6">
        <a href="contact.html" class="bg-primary text-on-primary font-bold uppercase tracking-tighter text-sm px-6 py-3 hover:bg-primary-container active:bg-primary transition-none">Отримати консультацію</a>
    </div>
</nav>

<main class="pt-32 pb-24 px-24">
    <div class="grid grid-cols-12 gap-0 mb-16">
        <div class="col-span-12 lg:col-span-6 bg-primary p-12 flex flex-col justify-center min-h-[240px]">
            <h1 class="text-white text-4xl font-extrabold tracking-tighter leading-tight mb-4">{hero_title}</h1>
            <p class="text-on-primary-container font-medium text-base max-w-md">{hero_subtitle}</p>
        </div>
        <div class="col-span-12 lg:col-span-6 relative overflow-hidden h-[240px] bg-[#2d312d]">
        </div>
    </div>
    
    <div class="grid grid-cols-12 gap-16">
        <div class="col-span-12 lg:col-span-8">
            <form class="space-y-16">
                <!-- Section: Client Data always present -->
                <section>
                    <h2 class="text-2xl font-bold uppercase tracking-tight mb-8 border-l-4 border-primary pl-4">Контактна інформація</h2>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                        <div class="flex flex-col gap-2">
                            <label class="text-[0.75rem] font-medium uppercase tracking-widest text-on-surface-variant">Назва компанії</label>
                            <input class="bg-surface-container-highest border-none border-b-2 border-transparent focus:ring-0 focus:border-primary p-4 transition-none" type="text" />
                        </div>
                        <div class="flex flex-col gap-2">
                            <label class="text-[0.75rem] font-medium uppercase tracking-widest text-on-surface-variant">Контактна особа</label>
                            <input class="bg-surface-container-highest border-none border-b-2 border-transparent focus:ring-0 focus:border-primary p-4 transition-none" type="text" />
                        </div>
                        <div class="flex flex-col gap-2">
                            <label class="text-[0.75rem] font-medium uppercase tracking-widest text-on-surface-variant">Телефон</label>
                            <input class="bg-surface-container-highest border-none border-b-2 border-transparent focus:ring-0 focus:border-primary p-4 transition-none" type="tel" />
                        </div>
                        <div class="flex flex-col gap-2">
                            <label class="text-[0.75rem] font-medium uppercase tracking-widest text-on-surface-variant">Email</label>
                            <input class="bg-surface-container-highest border-none border-b-2 border-transparent focus:ring-0 focus:border-primary p-4 transition-none" type="email" />
                        </div>
                    </div>
                </section>
                
                {form_specifics}
                
                <div class="pt-8">
                    <button class="w-full md:w-auto bg-primary text-on-primary px-16 py-6 text-lg font-bold uppercase tracking-widest hover:bg-primary-container active:scale-[0.98] transition-all" type="button">
                        {btn_text}
                    </button>
                </div>
            </form>
        </div>
        
        <aside class="col-span-12 lg:col-span-4 space-y-12">
            <div class="p-12 bg-surface-container-highest">
                <h3 class="text-xl font-bold uppercase mb-6 tracking-widest">Потрібна допомога?</h3>
                <p class="text-sm mb-8">Наші консультанти готові відповісти на всі ваші запитання.</p>
                <div class="space-y-2">
                    <p class="text-lg font-black">+38 (050) 123-45-67</p>
                </div>
            </div>
        </aside>
    </div>
</main>
</body>
</html>
"""

forms = {
    "form-rail.html": {
        "title": "Залізничні перевантаження",
        "hero_title": "ФОРМА ЗАЯВКИ<br/>«ЗАЛІЗНИЧНІ ПЕРЕВАНТАЖЕННЯ»",
        "hero_subtitle": "Організація перевантажень з європейської на українську колію.",
        "btn_text": "Замовити перевантаження",
        "form_specifics": """
            <section class="bg-surface-container-low p-12">
                <h2 class="text-2xl font-bold uppercase tracking-tight mb-8 border-l-4 border-primary pl-4">Інформація про вантаж та перевезення</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div class="flex flex-col gap-2 relative">
                        <label class="text-[0.75rem] font-medium uppercase tracking-widest text-on-surface-variant">Тип операцій</label>
                        <select class="bg-surface-container-lowest border-none border-b-2 border-transparent p-4 uppercase text-xs font-bold w-full">
                            <option>вагон → вагон</option>
                            <option>вагон → автомобіль</option>
                            <option>автомобіль → вагон</option>
                            <option>перевантаження контейнерів</option>
                        </select>
                    </div>
                    <div class="flex flex-col gap-2">
                        <label class="text-[0.75rem] font-medium uppercase tracking-widest text-on-surface-variant">Тип колії</label>
                        <select class="bg-surface-container-lowest border-none border-b-2 border-transparent p-4 uppercase text-xs font-bold">
                            <option>з європейської на українську</option>
                            <option>з української на європейську</option>
                        </select>
                    </div>
                </div>
            </section>
        """
    },
    "form-container.html": {
        "title": "Обробка контейнерів",
        "hero_title": "ФОРМА ЗАЯВКИ<br/>«ОБРОБКА КОНТЕЙНЕРІВ»",
        "hero_subtitle": "Послуги щодо приймання, зберігання та відвантаження.",
        "btn_text": "Отримати пропозицію",
        "form_specifics": """
            <section class="bg-surface-container-low p-12">
                <h2 class="text-2xl font-bold uppercase tracking-tight mb-8 border-l-4 border-primary pl-4">Параметри</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div class="flex flex-col gap-2">
                        <label class="text-[0.75rem] font-medium uppercase tracking-widest text-on-surface-variant">Тип контейнера</label>
                        <div class="flex gap-4">
                            <label class="flex items-center gap-2 p-4 bg-surface-container-lowest"><input type="radio" name="ctype"> 20'</label>
                            <label class="flex items-center gap-2 p-4 bg-surface-container-lowest"><input type="radio" name="ctype"> 40'</label>
                        </div>
                    </div>
                    <div class="flex flex-col gap-2">
                        <label class="text-[0.75rem] font-medium uppercase tracking-widest text-on-surface-variant">Кількість</label>
                        <input type="number" class="bg-surface-container-lowest p-4 border-none border-b-2 border-transparent">
                    </div>
                </div>
            </section>
        """
    },
    "form-warehouse.html": {
        "title": "Митний склад",
        "hero_title": "ФОРМА ЗАЯВКИ<br/>«МИТНИЙ СКЛАД»",
        "hero_subtitle": "Зберігання товарів під митним контролем.",
        "btn_text": "Отримати пропозицію",
        "form_specifics": """
            <section class="bg-surface-container-low p-12">
                <h2 class="text-2xl font-bold uppercase tracking-tight mb-8 border-l-4 border-primary pl-4">Товар</h2>
                <div class="grid grid-cols-1 gap-8">
                    <input type="text" placeholder="Назва товару" class="bg-surface-container-lowest p-4">
                    <input type="text" placeholder="Код УКТЗЕД" class="bg-surface-container-lowest p-4">
                </div>
            </section>
        """
    },
    "form-customs.html": {
        "title": "Митне оформлення",
        "hero_title": "ФОРМА ЗАЯВКИ<br/>«МИТНЕ ОФОРМЛЕННЯ»",
        "hero_subtitle": "Професійне супроводження вантажів.",
        "btn_text": "Розрахувати митне оформлення",
        "form_specifics": """
            <!-- Section: Procedure Type -->
            <section>
                <h2 class="text-2xl font-bold uppercase tracking-tight mb-8 border-l-4 border-primary pl-4">Тип процедури</h2>
                <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <label class="flex items-center gap-3 p-6 bg-surface-container-low cursor-pointer"><input type="radio" name="proc"> <span class="uppercase text-xs font-bold">Імпорт</span></label>
                    <label class="flex items-center gap-3 p-6 bg-surface-container-low cursor-pointer"><input type="radio" name="proc"> <span class="uppercase text-xs font-bold">Експорт</span></label>
                    <label class="flex items-center gap-3 p-6 bg-surface-container-low cursor-pointer"><input type="radio" name="proc"> <span class="uppercase text-xs font-bold">Транзит</span></label>
                </div>
            </section>
        """
    },
    "form-parking.html": {
        "title": "Паркінг",
        "hero_title": "ФОРМА ЗАЯВКИ<br/>«БРОНЮВАННЯ ПАРКІНГУ»",
        "hero_subtitle": "Забронювати місце для вантажного транспорту.",
        "btn_text": "Забронювати місце",
        "form_specifics": """
            <section class="bg-surface-container-low p-12">
                <h2 class="text-2xl font-bold uppercase tracking-tight mb-8 border-l-4 border-primary pl-4">Автомобіль</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <input type="text" placeholder="Номер авто" class="bg-surface-container-lowest p-4 border-none border-b-2 border-transparent">
                    <input type="date" class="bg-surface-container-lowest p-4 border-none border-b-2 border-transparent">
                </div>
            </section>
        """
    }
}

for filename, data in forms.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(tailwind_form_base.format(
            title=data["title"],
            hero_title=data["hero_title"],
            hero_subtitle=data["hero_subtitle"],
            btn_text=data["btn_text"],
            form_specifics=data["form_specifics"]
        ))
