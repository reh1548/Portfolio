# MyPortfolio

A Django-based portfolio website with PostgreSQL as the database. This project includes a blog, user accounts, and various static and media files.

## Features

- User authentication
- Blog
- Admin panel
- Static files handling
- Media files handling

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/myportfolio.git
    cd myportfolio
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your environment variables**:
    Create a `.env` file in the project root and configure your environment variables, including PostgreSQL database settings.

5. **Apply migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Collect static files**:
    ```bash
    python manage.py collectstatic
    ```

## Usage

1. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

2. **Optional: Run the application with Docker**:
    Ensure Docker and Docker Compose are installed on your machine.
    In case of running on docker no need to go through Step: 2 and 3
    **Build and run the Docker containers**:
    ```bash
    docker-compose up --build
    ```

## Project Structure

```plaintext
├───accounts
│   ├───migrations
│   ├───templates
│   │   └───accounts
├───base
│   ├───migrations
│   ├───templates
│   │   └───base
├───blog
│   ├───migrations
│   ├───templates
│   │   └───blog
├───media
│   └───blog_images
├───myportfolio
├───static
├───staticfiles
├───requirements.txt
├───.env
├───Dockerfile
├───docker-compose.yml

