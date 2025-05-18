# 🌍 Travel Log - Django App

The **Travel Log App** is a Django-based web application that allows users to create and manage trips. Users can log trip details including title, description, start date, and end date — making it ideal for travel enthusiasts or as a portfolio project.

## 🚀 Features

- 📝 Create and save trip entries
- 📅 Pick start and end dates
- 🗂 Organized trip forms with custom styling
- ✅ Secure form handling with CSRF protection
- 📦 Easily extensible for dashboards, maps, budgets, etc.


## 📸 Screenshots

> _Include screenshots of the app UI (like the create trip page)._  
> For example:  
> ![Create Trip Page](screenshots/create_trip.png)


## 🛠 Tech Stack

- **Backend**: Django 5.2.1
- **Frontend**: HTML5, CSS3
- **Database**: SQLite (default Django setup)
- **Other Tools**: Bootstrap (optional), VS Code, Git


## 📁 Project Structure

travel_log/
├── travel_log/ # Project settings
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── trips/ # Main app
│ ├── models.py
│ ├── views.py
│ ├── templates/
│ │ └── create_trip.html
│ ├── static/
│ │ └── trips/
│ │ └── styles.css
├── db.sqlite3
└── manage.py


## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/travel-log-django.git
   cd travel-log-django
Create virtual environment & activate it

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
Install dependencies


pip install django
Apply migrations


python manage.py migrate
Run the server


python manage.py runserver
Access the app
Open http://127.0.0.1:8000/admin/
     http://127.0.0.1:8000/create/
     http://127.0.0.1:8000/dashboard/
     http://127.0.0.1:8000/trip/1/map/

🧩 Future Enhancements
🗺 Map integration with trip locations

🏨 Hotel suggestions and room pricing

🍽 Restaurant and places to visit suggestions

📊 Budget planner and trip expense tracker

👤 User login and authentication

🤝 Contributing
Pull requests are welcome! Feel free to fork the repo and submit improvements.

📄 License
This project is open source and available under the MIT License.

💡 Author
POKALA PRATYUSHA– https://github.com/PRATYU124
