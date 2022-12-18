# DRF × Vue.js 画像登録

## 概要

Vue.js と Django REST Framework を用いて、画像の登録及びプレビュー表示する。

## 各種バージョン

- Python 3.10.3
- Django 4.1.4
- Django REST Framework 3.14.0
- vue-cli 5.0.1
- Vue.js 3.2.13

## 起動手順

1. django の開発用サーバーを起動

    ```
    % pip install -r requirements.txt
    % python manage.py runserver
    ```

2. Vue の開発用サーバーを起動

    ```
    % cd frontend
    % npm install
    % npm run serve
    ```

3. ブラウザで`https://localhost:8080`にアクセス

