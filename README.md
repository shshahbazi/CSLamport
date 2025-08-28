# Lamport Authentication System (Django)

This project implements a **user authentication system** based on the **Lamport One-Time Password (OTP) protocol**.  
It was developed as the final project for the *Introduction to Cybersecurity* course.  

The system ensures secure login by preventing password reuse and replay attacks through iterative hashing of passwords.

---

##  Features

- **User Registration (Sign Up)**  
  - Users register with a username, a password, and an initial number of hashing iterations `n`.  
  - The system stores the username, the hash of the password (hashed `n` times using `SHA-256`), and the iteration count.  

- **User Login**  
  - A user provides their username and password.  
  - Before sending, the password is hashed `(n-1)` times and sent to the server.  
  - The server checks the submitted value against the stored hash.  
  - If valid, the server updates the stored hash and decreases the iteration count by one.  
  - If iterations reach zero, the user must reset their password.  

- **View Hash Iterations**  
  - Users can request to see how many iterations remain for their login credentials.  

- **Password Reset (Set New Password)**  
  - When the iteration count reaches `1`, users are directed to reset their password.  
  - A new password and iteration count `n` are set, and the database record is updated.  

---

##  Tech Stack

- **Backend**: [Django](https://www.djangoproject.com/)  
- **Hashing**: `SHA-256`  
- **Database**: Django default database (SQLite)  
- **Frontend**: HTML templates (Django Template Language)

---

##  Project Structure (Key Components)

- **Templates**  
  - `home.html` → Home page  
  - `signup.html` → User registration page  
  - `login.html` → Login page  
  - `success.html` → Login success  
  - `failure.html` → Login failure  
  - `set_new_password.html` → Password reset page  

- **Views** (`views.py`)  
  - `signup` → Handles registration logic  
  - `login` → Handles login validation and iteration updates  
  - `get_hash_iterations` → Returns the current iteration count  
  - `set_new_password` → Handles password reset  

- **Models**  
  - `LamportUser` → Stores username, hashed password, and iteration count  

---

##  Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/shshahbazi/CSLamport.git
   ```
   
2. **Create and activate a virtual environment (optional)**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
   ```
   
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
    python manage.py migrate
   ```

5. **Start the server**
   ```bash
    python manage.py runserver
   ```

6. **Access the app**

    Open your browser and go to:
  http://127.0.0.1:8000/


---

##  Security Insights

 - **No password is stored directly** – only iterative hashes are stored.


 - **Replay protection** – previously used hashes cannot be reused for authentication.


 - **Forward secrecy** – each login requires a new hash, making credential leaks less impactful.