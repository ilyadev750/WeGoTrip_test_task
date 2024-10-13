## WeGoTrip тестовое задание
<p align="center">
  <img alt="Static Badge" src="https://img.shields.io/badge/python-3.11-blue">
  <img alt="Static Badge" src="https://img.shields.io/badge/Django-4.2-green">
  <img alt="Static Badge" src="https://img.shields.io/badge/DRF-3.15-purple">
  <img alt="Static Badge" src="https://img.shields.io/badge/SQLite-blue">
  <img alt="Static Badge" src="https://img.shields.io/badge/Flake8-red">
  <img alt="Static Badge" src="https://img.shields.io/badge/Docker-29C8DA">
</p>

## О проекте
Данный проект представляет собой тестовое задание для компании WeGoTrip

## Особенности

- проект работает в Docker контейнере
- при запуске через Docker-compose создаются администратор и два тестовых продукта через кастомные команды createadmin и addgoods
- тесты реализованы через Pytest и запускаются перед стартом работы сервера
- результаты тестов можно посмотреть в Docker Desktop после запуска контейнера
- в админ-панели добавлена кнопка подтверждения заказа, которая доступна в случае его оплаты
- после подтверждения заказа идет автоматический post-запрос на webhook.site

## Эндпоинты

- GET api/v1/goods - получить список всех товаров
- POST api/v1/orders/create - создать новый заказ. Пример тела запроса: <br />
{ 
    "order" : [
            {
                "good_pk": "1",
                "quantity": "2"
            },
            {
                "good_pk": "2",
                "quantity": "2"
            }
    ]
}
- POST api/v1/payments/create - создать платеж к созданномуз заказу. Пример тела запроса: <br />
{ 
    "order_id": "1",
    "payment_type": "карта"
}
- PATCH api/v1/payments/paid/{payment_id} - обозначить платеж как оплаченный

## Как пользоваться приложением

- склонировать данный репозиторий
- в корне проекта создать .env файл
- перейти на сайт webhook.site, найти your unique url и нажать open in new tab
- добавить в .env файл переменную webhook_url, значение которой равно your unique url
- запустить проект командой docker-compose up -d
- через Postman отправить GET запрос по эндпоинту api/v1/goods, чтобы получить список доступных товаров
- создать новый заказ, отправив POST запрос по эндпоинту api/v1/orders/create. Пример тела запроса выше в разделе Эндпоинты
- создать платеж к заказу, отправив POST запрос по эндпоинту api/v1/payments/create. В качестве "payment_type" могут быть только два значения: "карта" и 
"наличные"
- обозначить созданный платеж, как оплаченный, отправив PATCH запрос по эндпоинту api/v1/payments/paid/{payment_id}
- далее перейти в админ-панель. Username: root; Password: root
- перейти в раздел "Заказы"
- перейти внутрь формы заказа, нажав на кнопку "Подтвердить"
- в форме заказа нажать на доступную кнопку "Подтвердить"
- убедиться, что заказ подтвердился
- перейти на сайт webhook.site, там в списке должен появиться новый POST запрос с информацией о подтвержденном заказе
