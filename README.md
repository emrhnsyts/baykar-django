
##### not - Haftasonu sınavlarım olduğundan dolayı sadece arka yüz kısmını geliştirebildim. İlerleyen süreçlerde bir React ön yüzü tasarlayıp teslim edebilirim.

## libraries

django=5.0.6

djangorestframework=3.15.1

django-filter=24.2

djoser=2.2.2

djangorestframework-simplejwt=5.3.1

drf-yasg==1.21.7

## endpoints

-  **REGISTER**

-  *POST, auth/users*

- body = (username, email(isteğe bağlı), password, re_password)

-  **LOGIN**

-  *POST, auth/jwt/create*

- body = (username, password)

-  **IHA**

-  *GET api/v1/ihas/*

- response = all the IHAs registered (brand, model, weight, category)

-  *POST api/v1/ihas/*

- response = IHA registered (id, brand, model, weight, category)

-  *GET, PUT, DELETE api/v1/ihas/[id]*

- response = PUT and GET returns the IHA, DELETE does not return anything

-  **Rent**

-  *GET, POST api/v1/rents/*

- response = GET returns all the rent registers for the authenticated user (list(id, iha(id, brand, model, weight, category), rent_end_date, rent_start_date), POST returns the iha rented

-  *GET, PUT, DELETE api/v1/rents/[id]*

- response = PUT and GET returns the Rent, DELETE does not return anything

## relationships
- IHA to User = many to many