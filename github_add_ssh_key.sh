ssh-keygen -t rsa -b 4096 -C "david.g.daggett@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
sudo apt-get install xclip -y
xclip -sel clip < ~/.ssh/id_rsa.pub
echo '\nkey is copied!\nnow, paste it here: https://github.com/settings/ssh/new\n'
