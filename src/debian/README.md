[newwinlogo]: http://i.stack.imgur.com/B8Zit.png
1. Open terminal: Press/release <kbd>![Windows Key][newwinlogo]</kbd> and type `terminal`: select the application.

2. Enter the following in terminal:

    1. `su -` then enter root password (not user password).
    2. `visudo`
    3. add line `<your_user_name> ALL=(ALL:ALL) ALL` below `# User privilege specification`, where `<your_user_name>` = `dave` (for me) :

    ```
    # User privilege specification
    root    ALL=(ALL:ALL) ALL
    dave    ALL=(ALL:ALL) ALL
    ```

    4. `ctrl + O` - then enter
    5. `ctrl + X`

3. Copy + right-click `Paste` the following in your terminal. This will run the **`configuration script`**:

    ```bash
    wget https://github.com/ddaaggeett/scripts/archive/main.zip -P ~/github && cd ~/github
    sudo unzip main.zip && mv ./scripts-main ./scripts && cd ./scripts/src/debian/
    sudo chmod +x ./index.sh
    sudo ./index.sh
    ```
    Using your keyboard, accept all prompts.
 ___

This does the following:
- enables convenient [terminal commands](./init_alias.sh)
- enables custom executables with [path update](./init_binpack.sh)
- installs preferred [software](./software.md)
- sets preferred <kbd>![Windows Key][newwinlogo]</kbd> [key command shortcuts](./keys.md) for workflow
___
