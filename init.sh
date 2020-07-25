sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf

sudo rm -rf /etc/nginx/sites-enabled/default

sudo /etc/init.d/nginx restart

Запуск gunicorn
sudo gunicorn -b 0.0.0.0:8080 hello:app

Для обновления до версии Django2.1 использую следующие команды:

sudo apt-get update

sudo apt-get install -y python3.5

sudo apt-get install -y python3.5-dev

sudo unlink /usr/bin/python3

sudo ln -s /usr/bin/python3.5 /usr/bin/python3

sudo pip3 install --upgrade pip

sudo pip3 install --upgrade django==2.1

sudo pip3 install --upgrade gunicorn
