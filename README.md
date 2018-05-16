# Djangoのquickstartをやってみたもの

http://www.django-rest-framework.org/tutorial/quickstart/

# コマンドなど

 - django-admin.py startproject tutorial .
 - django-admin.py startapp quickstart
 - python manage.py migrate
 - python manage.py createsuperuser --email admin@example.com --username admin
 - python manage.py runserver


# わかったこと

 - static提供したければSTATICFILES_DIRSを定義すること
 - index.htmlを提供するの結構大変（renderせずに返す方法もある気がする）
 - HyperlinkedModelSerializerが良く分からん。もう少しリレーション周りを探るべきかな
