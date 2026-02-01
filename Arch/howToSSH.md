# how to setup

## via termux in android

1.  Setting up SSH on Termux (Android)

    Termux doesn't use standard Linux ports by default because it runs in user space. Instead of the standard port 22, it uses 8022.
    Installation & Setup

    *   Install the package:
        ```bash
        pkg upgrade
        pkg install openssh
        ```

    *   Set a password: You need a password to log in. Run `passwd` and enter a secure one.

    *   Find your username: Run `whoami`. Usually, it’s something like `u0_a123`.

    *   Find your IP address: Run `ifconfig` and look for the `inet` address under `wlan0`.

    *   Start the server:
        ```bash
        sshd
        ```

    > [!TIP] To stop the server at any time, use `pkill sshd`.