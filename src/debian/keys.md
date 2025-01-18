<link href="../../css/styles.css" rel="stylesheet" />

[newwinlogo]: http://i.stack.imgur.com/B8Zit.png

**windows key <kbd>![Windows Key][newwinlogo]</kbd> shortcuts**:  

Press/Hold <kbd>![Windows Key][newwinlogo]</kbd> **+ number** to open the docked applications:

<kbd>![Windows Key][newwinlogo]</kbd> + 1 -> terminal  
<kbd>![Windows Key][newwinlogo]</kbd> + 2 -> atom.io text editor
<kbd>![Windows Key][newwinlogo]</kbd> + 3 -> brave browser  
<kbd>![Windows Key][newwinlogo]</kbd> + 4 -> files  
___

If the `configuration script` hasn't been run, then handle manually:  
Run the following in terminal:

```bash
gsettings set org.gnome.shell favorite-apps "['org.gnome.Terminal.desktop', 'atom.desktop', 'brave-browser.desktop', 'org.gnome.Nautilus.desktop']"
```
