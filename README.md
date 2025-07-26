# Finding Psychological Instability Using Machine Learning - README
    Features
        - Predict psychological state: Depressed, Stressed, or Positive
        - Analyze mental health trends
        - Visualize likes/dislikes and stress patterns
        - Built using Django, MySQL, and classic ML libraries
    Setup Instructions

# 1. Install Python 3.7.0
⚠️ Only Python 3.7.0 is supported. Do not use Python 3.13 or newer.

    Download Python 3.7.0 from: https://www.python.org/ftp/python/3.7.0/

Make sure to check "Add Python to PATH" during installation.

# 2. Install XAMPP Control Panel v3.3.0**
    - Download XAMPP v3.3.0 from: https://sourceforge.net/projects/xampp/
    - Install and open the XAMPP Control Panel
    - Click Start on both Apache and MySQL
    - Open phpMyAdmin and create a database called:
        psychological_db

⚠️ Use this name in your Django settings.py under DATABASES.

# 3. Clone the Repository
    git clone https://github.com/YOUR_USERNAME/finding-psychological-instability.git
    cd finding-psychological-instability

# 4. Install Python Dependencies
    Create a virtual environment
        py -3.7 -m venv venv
        venv\Scripts\activate

# Install packages
    pip install numpy==1.19.2
    pip install pandas==0.25.3
    pip install matplotlib==3.1.1
    pip install scikit-learn==0.22.2.post1
    pip install jupyter==1.0.0
    pip install jupyter-client==6.1.3
    pip install jupyter-console==6.4.0
    pip install jupyter-core==4.6.3
    pip install jupyterlab-widgets==1.0.0
    pip install seaborn==0.10.1
    pip install ipython==7.9.0
    pip install ipython-genutils==0.2.0
    pip install ipykernel==6.5.0
    pip install pygame==2.0.0
    pip install django


# 5. Upload the Dataset
Place the Psychological_DataSets.xlsx file into the appropriate folder.
Ensure it's read by your Django app as expected.

# 6. Run the Server
**Navigate to the Django project folder (where manage.py exists)**
    cd finding_psychological_instability

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

**Open in browser:**
http://127.0.0.1:8000

**Login for Service Provider (if applicable):**
    Username: SProvider
    Password: SProvider
    Notes
    - This app requires MySQL (via XAMPP), not SQLite
    - Data is classified using rules in views.py, not trained ML models
    - Dataset includes age, gender, remarks, likes/dislikes, etc.

# License
    This project is for academic or research use. Commercial use requires permission from the author.

# Author
    Developed by **Ambica Ujjaini** as part of a research/internship project on mental health and machine learning.
