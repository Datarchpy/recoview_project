DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'recoview_db',  # データベース名（自分で設定）
        'USER': 'postgres',  # インストール時に設定したPostgreSQLのユーザー名
        'PASSWORD': 'dapy2011gc',  # 設定したPostgreSQLのパスワード
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
