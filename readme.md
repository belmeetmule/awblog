# AWBLOG

## Description

A simple blog app where users can post their articles and read what others have posted !!

## Screenshot

## Live demo
[No live link yet]

## Built with

### Front-End
    - Bootstrap
    - HTML
    - CSS
    - Javascript
### Backend
    - Django
    - Python
    - PostgreSQL

## Running the Project Locally
### prerequisites
    - [Python]("#")
    - [pip]("#")
    
### Setup
1. First, clone the repository to your local machine:

```bash 
    git clone https://github.com/belmeetmule/awblog.git 
```

2. Get into the cloned directory
    ```bash
        cd awblog
    ```
3. Create vertual environemt
    ```bash
        pip3 -m venv blog-venv
    ```

4. Run program under virtual environment:

```bash
    source blog-venv/bin/activate
```
5. Install the requirements:

```bash 
    pip install -r requirements.txt
```
6. Create the database:

```bash
    python manage.py migrate
```
7. Finally, run the development server:

```bash 
    python manage.py runserver
```
The project will be available at 127.0.0.1:8000.