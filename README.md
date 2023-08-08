## Дипломный проект автоматизации тестирования на Python для сайта https://en.wikipedia.org/

### Проект содержит UI и API тесты
* UI тесты
    * User authorization through user interface
    * Search an article
    * Add article
* API тесты
    * User authorization through API
    * Search article through API


## Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="resources\logo\pycharm.png"></code>
  <code><img width="5%" title="Python" src="resources/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="resources/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="resources/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="resources/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="resources/logo/Github.png"></code>
  <code><img width="5%" title="Jenkins" src="resources/logo/Jenkins.png"></code>
  <code><img width="5%" title="selenoid" src="resources/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="resources/logo/allure.png"></code>
</p>


## Запуск тестов


## <img width="6%" title="Jenkins" src="resources/logo/Jenkins.png"> Запуск тестов из [Jenkins](https://jenkins.autotests.cloud/job/Kastro_Vilson_python_wikipedia_ui_api/)
#### После настройки  проекта в Jenkins и нажатия на кнопку "Собрать с параметрами", выбирать environment запуска, тип и название теста, далее начнется сборка тестов и их прохождение через виртуальную машину в Selenoid.

<p><img src="resources/screenshots/job_jenkins.png" alt="Jenkins"/></p>

<p><img src="resources/screenshots/start_job.png" alt="Jenkins"/></p>

#### После прохождения тестов, результат отображается в Allure отчете

## <img width="6%" title="Allure" src="resources/logo/allure.png"> Пример отчетов в [Allure](https://jenkins.autotests.cloud/job/Kastro_Vilson_python_wikipedia_ui_api/68/allure/)

## В отчетах Allure для каждого UI-теста прикреплен скриншот, лог, html-страницы и видео прохождения теста

<p><img src="resources/screenshots/allure_report.png" alt="alllure report"/></p>

### Пример прохождения теста на видео


<p align="center">
  <img title="Video" src="resources/video/test_video.mpg"/>
</p>


## Локальный запуск тестов

Локальный запуск происходит по команде:
```
python -m pytest tests/test_functionalities_api.py . --environment=local
```

## или
```
python -m pytest tests/test_functionalities_api.py::test_authorization_throug
h_api --environment=local

```

## Удаленный запуск
Удаленный запуск с параметрами происходит по команде:

```
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip 
pip install poetry
poetry update
if [ "$TEST_TYPE" = "ui+api" ]
then
	pytest tests . --environment=${ENVIRONMENT} --alluredir=allure-results
else
	pytest tests/test_functionalities_${TEST_TYPE}.py::${TEST_NAME} --environment=${ENVIRONMENT} --alluredir=allure-results
fi
```