# 📚 Library Management System

A simple full-stack assignment project built for the **Social Booster
Assessment**.

This app allows users to add books, view books, delete books, and manage
basic library data.\
Backend is in **Django**, frontend uses **HTML/CSS/JS**, and
authentication/data storage is handled using **Supabase**.

## 🚀 Tech Stack

### Frontend

-   HTML\
-   CSS\
-   JavaScript

### Backend

-   Python\
-   Django

### Database & Auth

-   **Supabase** (PostgreSQL + Auth + REST API)

## 📁 Project Structure

    .
    ├── manage.py  
    ├── fullstack_task/        
    └── products/              

## ⚙️ Features

✔ Add new books\
✔ Delete books\
✔ View all books\
✔ Supabase authentication\
✔ Supabase table for storing books\
✔ Simple UI\
✔ Fully deployed online
✔ Google Books API used

## 🛠️ Setup Instructions (Local)

### 1. Clone the Repository

    git clone <your-repo-url>
    cd <project-folder>

### 2. Install Dependencies

    pip install -r requirements.txt

### 3. Add Environment Variables

Create a `.env` file:

    SUPABASE_URL=your_supabase_project_url  
    SUPABASE_KEY=your_supabase_anon_key  
    SUPABASE_TABLE=books  

### 4. Run the Server

    python manage.py runserver

## 🗄️ Supabase Setup

1.  Create a Supabase project\
2.  Create a table named **books**
    -   id (uuid, primary key)
    -   title (text)
    -   author (text)
    -   year (int)
3.  Enable Row Level Security\
4.  Use anon key in backend


## 🌐 Running on Local
What this does is first installs the requirements and then sets up the 
database which is accessed across the application. Lastly run on the server 
so there is no error while running.  

- Pip install -r Requirements.txt
- Open the terminal and type in: **python manage.py makemigrations products**
- After that type in: **python manage.py migrate**
- After that type in: **python manage.py runserver**


## 🌐 Deployment

Provide: - GitHub repo link\
- Live deployed link

## 👨‍💻 Author

**Tanmay Potbhare**
