#!/usr/bin/bash

source init_alias.sh
source init_binpack.sh

sudo apt install curl -y
sudo apt install net-tools -y
sudo apt install pip -y
sudo apt install ffmpeg -y
sudo apt install gphoto2 -y
sudo apt install git -y

# nvm - node.js
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
exec bash # TODO: does this work? reopens bash?
nvm install --lts

# yt-dlp
sudo wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp  # Make executable

# install brave-browser
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list
sudo apt update
sudo apt install brave-browser

# install atom text editor
curl -O https://github.com/atom/atom/releases/download/v1.60.0/atom-amd64.deb
sudo dpkg -i atom-amd64.deb
sudo apt-get install -f

# setting savorite applications 1.terminal 2. text editor 3. browser 4. files
gsettings set org.gnome.shell favorite-apps "['org.gnome.Terminal.desktop', 'atom.desktop', 'brave-browser.desktop', 'org.gnome.Nautilus.desktop']"

# generate ssh
ssh-keygen -t ed25519 -C "your_example_name"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/your_example_name
echo -e "\ncopy/paste the following into github SSH:\n"
cat ~/.ssh/your_example_name.pub
echo -e "\nafter SSH saved to github, run: sh ./secondary.sh\n"
