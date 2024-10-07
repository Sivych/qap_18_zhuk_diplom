# ***DemoWebShop.com Testing Project***

# О проекте
Этот проект представляет собой комплекс автоматизированных тестов для веб-платформы интернет-магазина DemoWebShop.com

Проект содержит тесты пользовательского интерфейса: вход в личный кабинет, проверка работы корзины, избранного, проверка добавления товара в корзину и избранное. 

# Разработка и технологии
*  Python
* Selenium WebDriver
* PyTest
* Page Object Pattern
* Allure

# Требования
Убедитесь, что у вас установлены следующие компоненты:
* Python версии 3.8 или выше
* pip (менеджер пакетов для Python, обычно устанавливается вместе с Python).

# Установка проекта
```bash
git clone https://github.com/Sivych/qap_18_zhuk_diplom.git
```

```bash
cd diplom
```

```bash
pip install -r requirements.txt
```
#### Линтер flake8:
```bash
pip install flake8
```

# Запуск тестов
### Run tests with pytest:
```bash
pytest
```
### Run all tests with make and allure:
```bash
make test-all
```



