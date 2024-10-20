DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'recoview_db',  # データベース名（自分で設定）
        'USER': 'postgres',  # インストール時に設定したPostgreSQLのユーザー名
        'PASSWORD': 'dapy2011gc',  # 設定したPostgreSQLのパスワード
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'client_encoding': 'UTF8',
        }
    }
}

# settings.py
DEBUG = False  # または True (開発時)

ALLOWED_HOSTS = ['localhost', '127.0.0.1']