**Library Management System**

A full-fledged **Library Management System** using **Python (Tkinter)** for GUI and **MySQL** for backend. This system supports two user roles: **Students** and **Admin**, each with role-specific features like borrowing/returning books, viewing profiles, adding/removing books, and tracking issue logs.

---

**Student Features**

- **Login Interface** (via `login.py`)
- **Student Dashboard**:
  - 📖 Borrow Books (up to 3 at a time)
  - 📤 Return Books with due-date alerts
  - 👁️ View Borrowed Books
    - See book details, due dates (overdue books marked red)
  - 👤 Profile Management
    - Edit name, gender, country, phone, and username
- **GUI Notifications**: Errors and validations shown using message boxes
- **Session Management**: Session ends after logout or when limit exceeded

---

**Admin Features**

- **Admin Login**:
  - Login with username `admin`
  - Redirects to `Admin_dashboard`
- **Admin Dashboard** includes:
  - ➕ `addbook`: Add new books to the library
  - 🧾 `viewbook`: View/edit/delete books
  - ✏️ `edit`: Modify existing book info
  - ❌ `delete`: Remove books from library
  - 📊 `seebook`: View issued book records (user, book, dates)
  - ⚙️ `adminprofile`: Edit admin profile details

---

**Tech Stack**

| Component   | Technology             |
|-------------|-------------------------|
| Frontend    | Python with Tkinter     |
| Backend     | MySQL                   |
| Libraries   | `mysql.connector`, `tkinter`, `smtplib`, `datetime`, `random`, `os` |
| Email       | `smtplib` + `email.mime.text` (for notifications, optional)

---


**MySQL Setup**

Make sure MySQL is running, then create a database and the following tables:
logindata
bookdata
bookissue
loginissue
