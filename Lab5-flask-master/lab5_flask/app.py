from flask import Flask, render_template, url_for

app = Flask(__name__)
menu = [{
    'name': 'Головна сторінка',
    'url': '/',
},
    {
        'name': 'Послуги',
        'url': '/products',
    },
    {
        'name': 'Прайс-лист',
        'url': '/price',
    },
    {
        'name': 'Контакти',
        'url': '/about',
    },
]
products = [{
    'subject': 'Графічний дизайн',
    'pib': 'Писарчук Олексій Олександрович',
    'course': '3',
    'task': 'Детальне вивчення інтерфейсу, інструментів, принципу роботи шарів. Робота з шарами, '
            'з растровим зображенням, текстом, формою, кольором, ефектами та фільтрами Adobe Photoshop.'
    },
    {
        'subject': 'QA-automation',
        'pib': 'Алещенко Олексій Вадимович',
        'course': '1',
        'task': 'Впевнені базові знання Java та автоматизованого тестування.'
    },
    {
        'subject': 'PHP Web-development',
        'pib': 'Сімоненко Валерій Павлович',
        'course': '1',
        'task': 'Специфіка мови програмування PHP: синтаксис, змінні, константи, типи даних, вирази, операції, '
                'пріоритет виконання операцій, оператори інкременту та декременту, регулярні вирази.'
    },
    {
        'subject': 'Node.js',
        'pib': 'Шемсединов Тимур Гафарович',
        'course': '2',
        'task': 'Розуміння принципів роботи асинхронного JavaScript. Вивчіть Express.js framework та Node.js.'
    },
    {
        'subject': 'Kotlin',
        'pib': 'Антонюк Андрій Іванович',
        'course': '2',
        'task': 'Ви почнете писати програму на Java на базових архітектурних патернах MVP (MVVM) з наступною міграцією '
                'на Kotlin та імплементацією вже на Kotlin-e архітектури Clean Architecture.'
    },
    {
        'subject': 'React.js',
        'pib': 'Габінет Артем Вікторович',
        'course': '2',
        'task': 'Розуміння особливостей компонентного підходу у проектуванні веб-додатків. '
                'Розуміння архітектури Single Page додатків.'
    },
    {
        'subject': 'iT Project Management',
        'pib': 'Болдак Андрій Олександрович',
        'course': '3',
        'task': 'Навчіться планувати бюджет та терміни проекту та складати план управління. '
                'Працюватимете в критичних умовах і в умовах обмежених ресурсів, делегуватимете завдання.'
    },
    {
        'subject': 'Тестування ПЗ (QA)',
        'pib': 'Ткаченко Валентина Василівна',
        'course': '4',
        'task': 'Вивчіть інструментарій тестувальника (система управління дефектами, '
                'система управління проектами, дів консоль, інструменти автоматизації).'
    },

    {
        'subject': 'Java',
        'pib': 'Корочкін Олександр Володимирович',
        'course': '2',
        'task': 'Навчіться застосовувати ключові принципи проектування та шаблони проектування (design patterns) '
                'та читати базові типи UML-діаграм. Отримайте навички роботи з базами даних, веб-технологіями.'
    }

]
post = [{
    'name': 'Графічний дизайн',
    'price': '1200грн',
    'contact': 'Придбати'
},
    {
        'name': 'QA-automation',
        'price': '1500грн',
        'contact': 'Придбати'
    },
    {
        'name': 'PHP Web-development',
        'price': '1700грн',
        'contact': 'Придбати'
    },
    {
        'name': 'Node.js',
        'price': '1200грн',
        'contact': 'Придбати'
    },
    {
        'name': 'Kotlin',
        'price': '1500грн',
        'contact': 'Придбати'
    },
    {
        'name': 'React.js',
        'price': '1700грн',
        'contact': 'Придбати'
    },
    {
        'name': 'iT Project Management',
        'price': '1700грн',
        'contact': 'Придбати'
    },
    {
        'name': 'Тестування ПЗ (QA)',
        'price': '1500грн',
        'contact': 'Придбати'
    },
    {
        'name': 'Java',
        'price': '1700грн',
        'contact': 'Придбати'
    }
]


@app.route('/')
def index():
    return render_template("index.html", menu=menu)


@app.route('/products')
def product():
    return render_template("product.html", products=products, menu=menu)


@app.route('/price')
def price_list():
    return render_template("price.html", menu=menu, post=post)


@app.route('/about')
def about():
    return render_template("about.html", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
