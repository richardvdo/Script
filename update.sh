ssh pi@192.168.1.54  sudo tee ~/update.sh #!/bin/sh
sudo apt-get update && sudo apt-get upgrade -y 
sudo rpi-update -y
sudo apt-get autoremove -y
sudo apt-get autoclean -y
sudo reboot
