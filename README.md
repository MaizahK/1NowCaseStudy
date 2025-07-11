# 🚗 LahoreCarRental.com — Backend API Sample Project

This is a **RESTful backend API** built with **Django** and **Django REST Framework**.  
It powers **LahoreCarRental.com**, a fictional car rental platform .  
Users can **register**, **login**, **manage vehicles**, and **create/view bookings** — all through secure JWT-based endpoints.

---

## ✅ Features

### 📝 API Documentation

| Endpoint   | Method | Description                                                     |
| ---------- | ------ | --------------------------------------------------------------- |
| `/swagger` | GET    | UI based auto-generated documentation for all project endpoints |

---

### 📌 Authentication

| Endpoint    | Method | Description                   |
| ----------- | ------ | ----------------------------- |
| `/register` | POST   | Register a new user           |
| `/login`    | POST   | Login and get a **JWT token** |

---

### 🚙 Vehicle Management

| Endpoint          | Method | Description                          |
| ----------------- | ------ | ------------------------------------ |
| `/vehicles/`      | POST   | Add a car (make, model, year, plate) |
| `/vehicles/{id}/` | PUT    | Update a car                         |
| `/vehicles/{id}/` | DELETE | Delete a car                         |
| `/vehicles/`      | GET    | List user vehicles                   |

---

### 📅 Booking Management

| Endpoint     | Method | Description                                                  |
| ------------ | ------ | ------------------------------------------------------------ |
| `/bookings/` | POST   | Book a vehicle (select car, start/end dates, deposit_amount) |
| `/bookings/` | GET    | List user bookings                                           |

---

## 📂 Sample Requests & Responses

### ✅ Register

**POST** `/register`

```json
{
	"username": "testuser",
	"email": "testuser@email.com",
	"password": "testpassword"
}
```

✅ **Response**

```json
{
	"username": "testuser",
	"email": "testuser@email.com"
}
```

---

### ✅ Login

**POST** `/login`

```json
{
	"username": "testuser",
	"password": "testpassword"
}
```

✅ **Response**

```json
{
	"access": "<your-jwt-access-token>",
	"refresh": "<your-jwt-refresh-token>"
}
```

---

### ✅ List Vehicles

**GET** `/vehicles/`  
Headers: `Authorization: Bearer <access-token>`

✅ **Response**

```json
{
	"count": 1,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"make": "Toyota",
			"model": "Corolla",
			"year": 2021,
			"plate": "ABC-123",
			"owner": 1
		}
	]
}
```

---

## ⚙️ How to Run

1️⃣ **Clone the Repo**

```bash
git clone https://github.com/MaizahK/1NowCaseStudy.git
cd 1NowCaseStudy
```

2️⃣ **Create Virtual Env & Install Dependencies**

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

3️⃣ **Add a .env file to the project base directory**

```bash
# 1NowCaseStudy/.env
SECRET_KEY=mysupersecretkey
JWT_SECRET=mysupersecretjwtkey
DEBUG=True #must be a bool value: True or False
```

4️⃣ **Apply Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5️⃣ **Run Dev Server**

```bash
python manage.py runserver
```

6️⃣ **Create Admin**

```bash
python manage.py createsuperuser
```

Access: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## ✅ Tests

Run all tests:

```bash
python manage.py test
```

There are **unit tests for all three modules** covering core features and edge cases.

---

## ✅ Product Research

The project contains **product_research.txt** that contains the product context as was asked as an assignment requirement.

---

## ✅ Deliverables

-   The project consists of three modular REST apps: User, Vehicles, Booking.
-   All apps use APIViews from Django Rest Framework including builtin APIs with mixins and generics.
-   The project uses Django provided JWT Authentication which is required for all API calls except for User and Token creation and Swagger documentation.
-   All application calls can only be accessed with an authorization token.
-   Request data is serialized and validated with REST serializers, including custom validators and provides clear error message in case of request failure.
-   The project handles all errors gracefully, only providing error details if DEBUG is set to False in the .env file.
-   API Documentation is provided through the **/swagger** endpoint.
-   Unit tests are added to each module to test the happy flow and edge cases.
-   The project has been uploaded as a public GitHub repository with a detailed **README.md**.

---

## ✅ Assumptions

-   The project was built with Python 3.12.2.
-   The backend uses **SQLite** for quick development; switch to PostgreSQL for production.
-   **Stripe payments** are mocked with a placeholder — no real payment processing.
-   No overlapping bookings are allowed for the same vehicle.
-   Only **authenticated users** can manage their own cars/bookings.
-   JWT secret and expiry settings should be configured securely in `settings.py` before deploying.

---
