import os

def init_db():
    os.system('python manage.py migrate')

if __name__ == "__main__":
    init_db()
