How to test:

1. Install the dependencies (either globally or on a virtualenv)
```shell
$ pip install -r requirements.txt
```
2. Run the migrations
```shell
$ python manage.py migrate
```
3. Create a superuser
```shell
$ python manage.py createsuperuser
```
4. Run the server
```shell
$ python manage.py runserver
```
5. Create a `NotificationTemplate` from the admin
6. Go to `http://localhost:8000/polls/`
7. On your terminal, you'll see the email that was "sent" (console mailer)
8. Go to `http://localhost:8000/graphql/` and run the following query:
```graphql
query Notifs {
  notificationTemplates {
    edges {
      node {
        type
        translations {
          bodyHtml
          bodyText
          preview
        }
      }
    }
  }
}
```
