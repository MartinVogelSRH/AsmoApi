DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo 'Welcome to Asmo setup'
echo 'Please note that the initial setup requires an active internet connection.'
echo 'First, we will update the apt-get database'
sudo apt-get -qq update
echo '----------------'
echo 'Installing prerequisites for the ASMO Software: web.py and picamera'
sudo pip install web.py picamera
echo '----------------'
echo 'Activating needed settings using raspi-config: I2C, Camera and the default boot behaviour'
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_camera 0
sudo raspi-config nonint do_boot_behaviour B1
echo '----------------'
echo 'Making the pi ready to read DHT11 Sensors'
sudo apt-get -qq -y install build-essential python-dev
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
(cd $DIR/Adafruit_Python_DHT && exec sudo python setup.py install) >> /dev/null
echo '----------------'
echo 'Registering ASMO as a service for systemctl'
echo 'For this, we follow the instructions from https://www.raspberrypi.org/documentation/linux/usage/systemd.md'
SERVICE_FILE="/etc/systemd/system/AsmoAPI.service"
sudo echo "[Unit]" > $SERVICE_FILE
sudo echo "Description=Asmo Api" >> $SERVICE_FILE
sudo echo "After=network-online.target" >> $SERVICE_FILE
sudo echo "[Service]" >> $SERVICE_FILE
sudo echo "ExecStart=/usr/bin/python -u ${DIR}/AsmoApi.py" >> $SERVICE_FILE
sudo echo "WorkingDirectory=${DIR}" >> $SERVICE_FILE
sudo echo "StandardOutput=inherit" >> $SERVICE_FILE
sudo echo "StandardError=inherit" >> $SERVICE_FILE
sudo echo "Restart=always" >> $SERVICE_FILE
sudo echo "User=pi" >> $SERVICE_FILE
sudo echo "[Install]" >> $SERVICE_FILE
sudo echo "WantedBy=multi-user.target" >> $SERVICE_FILE

sudo systemctl daemon-reload
sudo systemctl start AsmoAPI.service
sudo systemctl enable AsmoAPI.service
echo 'ASMO is now installed as AsmoAPI.service in systemctl'
echo 'You can check the output by using systemctl status AsmoAPI.service'
echo '----------------'
echo 'Setting up the pi to run a WIFI Network'
echo 'For this, we follow the instructions from https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md'

sudo apt-get -qq -y install dnsmasq hostapd
sudo systemctl stop dnsmasq
sudo systemctl stop hostapd
NOW=$(date +"%m_%d_%Y")
sudo cp /etc/dhcpcd.conf /etc/dhcpcd_$NOW.conf.bak
sudo echo "interface wlan0" > /etc/dhcpcd.conf
sudo echo "static ip_address=10.0.0.1/24" >> /etc/dhcpcd.conf
sudo service dhcpcd restart
sudo cp /etc/dnsmasq.conf /etc/dnsmasq_$NOW.conf.bak  
sudo echo "interface=wlan0" > /etc/dnsmasq.conf
sudo echo "dhcp-range=10.0.0.1,10.0.0.255,255.255.255.0,24h" >> /etc/dnsmasq.conf

sudo echo "interface=wlan0" > /etc/hostapd/hostapd.conf
#sudo echo "driver=rtl8192cu" >> /etc/hostapd/hostapd.conf
sudo echo "ssid=asmo" >> /etc/hostapd/hostapd.conf
sudo echo "hw_mode=g" >> /etc/hostapd/hostapd.conf
sudo echo "channel=6" >> /etc/hostapd/hostapd.conf
sudo echo "macaddr_acl=0" >> /etc/hostapd/hostapd.conf
sudo echo "auth_algs=1" >> /etc/hostapd/hostapd.conf
sudo echo "ignore_broadcast_ssid=0" >> /etc/hostapd/hostapd.conf
sudo echo "wpa=2" >> /etc/hostapd/hostapd.conf
sudo echo "wpa_passphrase=12345678" >> /etc/hostapd/hostapd.conf
sudo echo "wpa_key_mgmt=WPA-PSK" >> /etc/hostapd/hostapd.conf
sudo echo "wpa_pairwise=TKIP" >> /etc/hostapd/hostapd.conf
sudo echo "rsn_pairwise=CCMP" >> /etc/hostapd/hostapd.conf

sudo cp /etc/default/hostapd /etc/default/hostapd_$NOW.bak  
sudo echo "DAEMON_CONF=\"/etc/hostapd/hostapd.conf\"" > /etc/default/hostapd

sudo systemctl start hostapd
sudo systemctl start dnsmasq
echo '----------------'
echo 'Everything done. It is recommended to reboot now by using sudo reboot now'