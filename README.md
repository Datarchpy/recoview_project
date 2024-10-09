# recoview_project
# レコビュ - レビューから次に読む本をレコメンド

## 概要
このプロジェクトは、ユーザーが本のレビューを投稿し、そのレビューに基づいて次に読むべき本をレコメンドするシステムです。

## セットアップ

1. 仮想環境をセットアップします。
```bash
python -m venv myenv
source myenv/bin/activate  # Mac/Linux
myenv\Scripts\activate  # Windows
```

2. 必要なパッケージをインストールします。
```bash
pip install -r requirements.txt
```

3. Djangoプロジェクトをセットアップします。
```bash
cd backend
python manage.py migrate
python manage.py runserver
```

4. Streamlitアプリを起動します。
```bash
streamlit run ../frontend/app.py
```


