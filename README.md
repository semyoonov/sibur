# sibur_monitoring

> Система оповещения о проблемах на производстве
> Пользователи могут зарегестрироваться, сообщить о проблеме на сайте или в tg-боте, а затем получать оповещения о проблемах на email или в tg

Для запуска нужно из корня директории проекта запустить:

```
docker-compose build
docker-compose up
```

<details>

<summary>Тестирование</summary>

Стрельба яндекс танком, конфиги в папке `tests`. Результаты:
- [GET](https://overload.yandex.net/729829#tab=test_data&tags=&plot_groups=main&machines=&metrics=&slider_start=1730160110&slider_end=1730160335)
- [POST](https://overload.yandex.net/729827#tab=test_data&tags=&plot_groups=main&machines=&metrics=&slider_start=1730159393&slider_end=1730159505)

</details>

[Макет дизайна можно найти здесь](https://pixso.net/app/editor/PuZalxzDhabtS7raL_GR8Q?icon_type=1&page-id=0%3A1)(или [pdf](./design.pdf))

[Презентация](./slides.pdf)
