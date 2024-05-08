**Getting Started (After Cloning the Repository):**

1. **Create and Activate a Virtual Environment:**
    - Run `python -m venv env` to create a virtual environment named `env`.
    - Activate the environment with `source env/bin/activate` (Windows: `env\Scripts\activate`).
2. **Install Dependencies:**
    - Run `pip install -r requirements.txt` to install required libraries.
3. **Configure Database:**
    - Create your MySQL database and configure credentials in the `settings.py` file.
4. **Run Django Migrations:**
    - Run `python manage.py migrate` to apply database schema changes.
5. **Create a Superuser:**
    - Run `python manage.py createsuperuser` to create an initial superuser for administrative access.
6. **Start Development Server:**
    - Run `python manage.py runserver` to start the Django development server.
7. **Access Administration Panel:**
    - Open your web browser and navigate to `http://127.0.0.1:8000/admin/` to access the administration panel.
