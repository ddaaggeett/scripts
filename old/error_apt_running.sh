# common error
# answered: https://askubuntu.com/a/1109989
# E: Could not get lock /var/lib/dpkg/lock-frontend - open (11: Resource temporarily unavailable)  
# E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), is another process using it?

sudo killall apt apt-get
sudo rm /var/lib/apt/lists/lock
sudo rm /var/cache/apt/archives/lock
sudo rm /var/lib/dpkg/lock*
sudo dpkg --configure -a
sudo apt update
