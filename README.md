# API-Online-Courses
OTUS Home Work 7

## Базовый бекенд для сайта с курсами на основе DRF

### Содержание:
+ [Краткое описание](#краткое-описание)
+ [Полезные ссылки](#полезные-ссылки)
+ [Requirements](#requirements)
+ [Сборка и запуск проекта](#сборка-и-запуск)
+ [Примеры](#примеры-ответа-от-сервера)
  * [Endpoint 1](#endpoint-1)
  * [Endpoint 2](#endpoint-2)
  * [Endpoint 3](#endpoint-3)
+ [License](#license)

### Краткое описание:
Проект представляет собой Django приложение на основе Django-rest-framework – удобного инструмента для работы с rest основанного на идеологии фреймворка Django, что позволяет создать полноценный
бекенд с использованием API(Application Programming Interface – интерфейс прикладного программирования) – это программное обеспечение, которое позволяет двум приложениям общаться друг с другом.

Rest(сокр. англ. Representational State Transfer, «передача состояния представления») - это архитектура используемая при создании распределённых приложений, при которой
данные передаются в небольшом количестве и в стандартных форматах (например HTML, XML, JSON).  
REST-подход обеспечивает масштабируемость системы и позволяет ей эволюционировать с новыми требованиями


### Полезные ссылки:
+ [Django documentation](https://docs.djangoproject.com/en/2.2/)
+ [Django rest framework](https://www.django-rest-framework.org/)
+ [API](https://ru.wikipedia.org/wiki/API)


### Requirements:
+ Django==2.2.3
+ django-cors-headers==3.0.2
+ django-debug-toolbar==2.0
+ djangorestframework==3.9.4
+ pycodestyle==2.5.0
+ autopep8==1.4.4


### Сборка и запуск:
```
git clone git@github.com:Bincha3000/API-Online-Courses.git
pip install virtualenv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pyhon api_courses/manage.py runserver
```


### Примеры ответа от сервера:

#### Endpoint 1:
> http://127.0.0.1:8000/api/v1/courses/2
```
{
    "id": 2,
    "category": {
        "id": 2,
        "title": "Web Development",
        "description": "You’re here because you’re ready to start building professional, career-boosting websites. Welcome!"
    },
    "title": "Full stack web developer",
    "short_description": "Ready to open new doors and become a smart, in-demand web developer?",
    "long_description": "The course starts with the fundamentals. I’ll show you insider tips to work quickly and efficiently with web technologies like HTML5, CSS3 and Python.",
    "price": "120000.00",
    "date_start": "2019-07-18",
    "date_end": "2019-07-20",
    "teacher": [
        {
            "id": 1,
            "first_name": "Vlad",
            "last_name": "Gladun",
            "info": "Junior Python Developer"
        }
    ],
    "lessons": [...]
}
```


#### Endpoint 2:
> http://127.0.0.1:8000/api/v1/courses/teachers
```
[
    {
        "id": 1,
        "first_name": "Vlad",
        "last_name": "Gladun",
        "info": "Junior Python Developer"
    }
]
```


#### Endpoint 3
> http://127.0.0.1:8000/api/v1/courses/categories
```
[
    {
        "id": 1,
        "title": "Design",
        "description": "Web Design Basics"
    },
    {
        "id": 2,
        "title": "Web Development",
        "description": "You’re here because you’re ready to start building professional, career-boosting websites. Welcome!"
    }
]
```



### License
This project is licensed under the terms of the MIT license
