# ShopApi

This is `Django` project. Is a **Virtual Shop** where the user can `register` or `login` to see the available `products`
and add then to his shopping car.

## Configure API

### Migrations

To execute migrations run:

```
python manage.py migrate
```

### Seeds

To put seeds run: 
```
python manage.py loaddata seeds/shop_seed.json
```

## Development server

For a dev server run:

```
python manage.py runserver
```

Then you can send petitions to `http://127.0.0.1:8000/`. [This are the endpoints](#endpoints).

## EndPoints

This are the **API Endpoints**:

- Users: `/shop/users/` (GET, POST), `/shop/users/<id>/` (GET, PUT, DELETE)
- Categories: `/shop/categories/` (GET, POST), `/shop/categories/<id>/` (GET, PUT, DELETE)
- Products: `/shop/products/` (GET, POST), `/shop/products/<id>/` (GET, PUT, DELETE)
- Login: `/auth/token/login/` (POST)
- Logout: `/auth/token/logout` (POST)

### Functional Requirements:

1. **User Model**: There should be a User model that represents the users of your application. This model should include the following properties:

   - `username`: A string that represents the unique username for each user.
   - `email`: A string that represents the user's email.
   - `password`: A string that represents the user's password.
   - `is_admin`: A boolean value that indicates whether the user is an administrator or not.

2. **Token-Based User Authentication**: Users should be able to register, log in, and log out. A token-based authentication should be implemented for API requests. Upon successful login, the user should receive a token which needs to be sent with each subsequent request to access the protected endpoints.

3. **Category Management**: Only administrator users can create, update, and delete Categories. All users can read the Categories. Each category has the following properties:

   - `name`: A string that represents the name of the category.
   - `description`: A string that provides a description of the category.

4. **Product Management**: Only administrator users can create, update, and delete Products. All users can read the Products. Each product has the following properties:

   - `name`: A string that represents the name of the product.
   - `description`: A string that provides a description of the product.
   - `price`: A decimal number that represents the price of the product.
   - `image`: One image of the product.

5. **Product Purchase Endpoint**: Users should be able to make a purchase by sending a POST request to a specific endpoint. This endpoint should accept a list of product IDs and quantities for each product to be purchased.

6. **API Endpoints**: You should have separate endpoints for each of the models (Users, Categories, Products) that allow CRUD (Create, Read, Update, Delete) operations.

### Non-Functional Requirements:

1. **API Security**: Implement security measures such as rate limiting, CORS, and protection against brute force attacks.

2. **API Documentation**: Provide clear and comprehensive API documentation, including the endpoints, the allowed HTTP methods for each endpoint, and the formats of the input and output data.

3. **Performance**: The API should be capable of handling a large number of simultaneous requests without significantly degrading performance.

4. **Compatibility**: The API should be compatible with different versions of Django and with different operating systems where Django can be deployed.
