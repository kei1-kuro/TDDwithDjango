# TDDwithDjango

sudo apt update
sudo apt upgrade

git clone https://XXX

git config --global user.name "kei1"
git config --global user.email "XXX"

pip3 -V

pip3 install virtualenv
virtualenv --version

virtualenv -p python3.6 django
. django/bin/activate

python3 --version

pip3 install "django<1.12" "selenium<4"

wget https://chromedriver.storage.googleapis.com/75.0.3770.90/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo cp chromedriver /usr/local/bin/
sudo chmod 755 /usr/local/bin/chromedriver 

sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo touch /etc/default/google-chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

sudo apt install libappindicator1
sudo apt --fix-broken install 

deactivate