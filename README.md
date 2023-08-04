# 🚀 Project Setup

This README.md file will guide you through the setup process so you can quickly get up and running.

## Prerequisites 📋

Before you start, make sure you have the following installed:

1. Python 3.x: [Python Download](https://www.python.org/downloads/)

## Getting Started 🏁

1. Clone this repository to your local machine:

   git clone https://github.com/aman162000/onetap-backend.git

2. Create a virtual environment and activate it:

   ```
   python -m venv env
   ```

- On Windows:

  ```sh
  env\Scripts\activate
  ```

- On macOS and Linux:

  ```sh
  source env/bin/activate
  ```

3. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Perform database migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser to access the Django admin:
   ```sh
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```sh
   python manage.py runserver
   ```

### 🎉 Your Django project is now running locally at `http://127.0.0.1:8000/`.

## Configuring the Project ⚙️

Open `onetap/settings.py` to configure various settings such as database setup, static files, media files, timezone, etc.

## Creating Apps 📱

To create a new app, run the following command:

```sh
python manage.py startapp app_name
```

This will create a new app directory with the necessary files.

## Contributing 🤝

We welcome contributions! If you find any issues or have ideas for improvements, feel free to open a pull request.

## Deployment 🚀

When deploying the project to production, make sure to set the `DEBUG` variable to `False` in `settings.py`, configure your web server (e.g., Nginx, Apache) and database accordingly.

## Troubleshooting ❗

If you encounter any issues during the setup or development process, don't hesitate to reach out to us or check the project's documentation.
