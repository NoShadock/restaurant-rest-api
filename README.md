# restaurant-rest-api

A REST api server based on django-rest-framework.

## run server

```bash
python manage.py runserver
```

Default address is: http://127.0.0.1:8000/

## Commands

### CREATE restaurant

```bash
curl -i -X POST 127.0.0.1:8000/restaurants/ -H "Content-Type: application/json" -d '{"name":"test-restaurant", "street":"somewhere", "city":"here", "code":"none"}'
```

### LIST restaurants

```bash
curl -i -X GET 127.0.0.1:8000/restaurants/
```

### GET restaurant

By id/url:

```bash
curl -i -X GET 127.0.0.1:8000/restaurants/11/
```

By name:

```bash
curl -i -X GET 127.0.0.1:8000/restaurants/?name=test-restaurant
```

Random one:

```bash
curl -i -X GET 127.0.0.1:8000/restaurants/random/
```

### UPDATE restaurant

```bash
curl -i -X PATCH 127.0.0.1:8000/restaurants/11/ -H "Content-Type: application/json" -d '{"street":"nowhere"}'
```

### DELETE restaurant

```bash
curl -i -X DELETE 127.0.0.1:8000/restaurants/11/
```
