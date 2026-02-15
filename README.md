# Django Social Blog

A social blog platform built with Django and PostgreSQL.

Users can create posts, manage their own content, explore user profiles, and search for posts or other users.

---

## Features

- User authentication (Register / Login / Logout)
- Create, update, and delete posts
- Author-based permission control
- User profile pages
- Post search (title & content)
- User search
- Pagination
- PostgreSQL database integration
- Environment-based configuration (.env)

---

## Tech Stack

- Python 3
- Django
- PostgreSQL 15
- HTML5 / CSS3

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/cnrydn/fullstack-blog-system.git
cd fullstack-blog-system
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:

```env
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

---

## Permission Logic

- Only authenticated users can create posts.
- Only the author of a post can update or delete it.
- Other users can view author profiles.

---

## Notes

- PostgreSQL is used as the primary database.
- Database credentials are managed via environment variables.
- The `.env` file is excluded from version control for security.

---

## License

This project is intended for educational and portfolio purposes.
