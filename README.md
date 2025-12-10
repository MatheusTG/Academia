# Academia

This project was developed for the Web Development course of the Integrated Technical Program in Computer Science at UTFPR. It consists of a gym website featuring workout management, membership sales, and user registration/login.

## 🚀 Technologies Used

| Technology                                                                                                        | Description                                                                           |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)             | General-purpose programming language used to build the project’s back-end logic.      |
| ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) | Language used for dynamic behavior and client-side interactions.                      |
| ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)                 | Markup language used to structure the application’s web pages.                        |
| ![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)                    | Styling language responsible for layout and visual presentation.                      |
| ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)                | Lightweight Python web framework used to build the application’s back-end and routes. |
| ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white) | ORM used for database modeling, queries, and data persistence.                        |
| ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white) | Relational database used to store and manage application data.                        |

## 📌 Requirements

- Python 3.10 or higher
- PostgreSQL 15+

## 🛠️ Installation & Usage

```bash
# Clone the repository to your computer
git clone https://github.com/MatheusTG/Academia.git .

# Create your virtual environment
python -m venv venv

# Activate your virtual environment
venv/Scripts/activate

# Install the libraries listed in requirements.txt
pip install -r requirements.txt
```

```py
# In infra/configs/connection.py configure the connection in self.**connection_string
self.**connection_string = 'postgresql://postgres:postgres123@localhost:5432/academia'
```

```bash
# Run the project
python run.py
```

## ▪️Project Structure

```bash
Academia/
├── docs/
│
├── data/
│   ├── images/
│
├── infra/
│   ├── configs/      → ORM Configuration (SQLAlchemy)
│   ├── entities/     → Database table entities
│   └── repository/   → Data access and persistence (CRUD)
│
├── static/
│   ├── css/
│   ├── img/
│   └── js/
│
├── templates/        → HTML page templates
│
└── package.json
```

## ▪️Screenshots

![Exemplo de imagem/screenshot do projeto](./docs/images/homepage.avif)

![Exemplo de imagem/screenshot do projeto](./docs/images/workout-page.avif)

![Exemplo de imagem/screenshot do projeto](./docs/images/plans-page.avif)

![Exemplo de imagem/screenshot do projeto](./docs/images/login-page.avif)

![Exemplo de imagem/screenshot do projeto](./docs/images/register-page.avif)
