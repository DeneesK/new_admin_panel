### Перед запуском проекта:
1. Скопировать файл конфигурации для docker-compose: cat .env.example > .env
2. Скопировать файл с перемеными окружения для Django: cat movies-admin/config/.env.example > movies-admin/config/.env
3. В файле movies-admin/config/.env подставить актуальные значения
4. Теперь можно собирать, docker-compose up
5. docker-compose exec movies-admin python manage.py migrate
6. После можно будет открыть админку: http://127.0.0.1/admin