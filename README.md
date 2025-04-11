# 🏡 Airbnb Clone (Makers Bootcamp)

This is a minimal full-stack clone of Airbnb, built in a one-week sprint during the Makers Bootcamp. It enables users to sign up, log in, view available rental listings, and make bookings by selecting date ranges. The focus was on building a working MVP using Python and Flask, applying Agile workflows and TDD.

## 🔧 Tech Stack

- **Backend**: Python, Flask
- **Database**: PostgreSQL
- **Authentication**: Flask-Login
- **Testing**: PyTest
- **Tools**: Git, GitHub, Agile (daily standups, pair programming)

---

## 🚀 Key Features

- User registration and login
- Listing of rental spaces
- Booking form with date range selection
- Secure account access per user
- Database-backed availability tracking

---

## 👨‍💻 My Contributions

- Built the **date availability system** for rental spaces (including date range logic)
- Implemented **user authentication** (login, logout, sessions)
- Participated in sprint planning, retros, and team-based code reviews

---

## 🧠 What I Learned

- How to structure a full-stack app using Flask and PostgreSQL
- Implementing session-based login in Python
- Handling date selection logic for bookings
- Using PyTest for isolated unit and integration tests
- Working under time constraints in a fast-paced Agile sprint

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/doowmot/Airbnb.git
cd Airbnb
```

### 2. Set Up the Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Set Up the PostgreSQL Databases

```sql
CREATE DATABASE airbnb_dev;
CREATE DATABASE airbnb_test;
```

### 4. Run the App

```bash
flask run
```

Visit [http://localhost:5000](http://localhost:5000)

---

## ✅ Running Tests

```bash
pytest
```

---

## ⚙️ Future Improvements

- Add calendar-style date picker UI
- Improve booking conflict validation logic
- Enhance front-end design and layout
- Deploy with Docker and CI pipeline

---

## 📜 License

MIT – see `LICENSE` file for details.
