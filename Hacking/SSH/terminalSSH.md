# SSH from various operating systems

This document outlines how to connect to a remote server via SSH from different operating systems.

## Arch Linux / macOS / Termux (Android)

These operating systems typically come with OpenSSH client pre-installed or it's easily installable via their package managers.

1.  **Open a terminal.**
    *   **Arch Linux/macOS:** Search for "Terminal" in your applications.
    *   **Termux:** Launch the Termux app.

2.  **Use the `ssh` command:**
    The basic syntax for the `ssh` command is:
    ```bash
    ssh [username]@[remote_host]
    ```
    *   Replace `[username]` with your username on the remote server.
    *   Replace `[remote_host]` with the IP address or hostname of the remote server.

    **Example:**
    ```bash
    ssh user@192.168.1.100
    ssh admin@example.com
    ```

3.  **Enter your password:**
    The first time you connect, you might be asked to confirm the authenticity of the host. Type `yes` and press Enter. Then, you'll be prompted for your password for the remote user. Type it carefully (it won't show on screen) and press Enter.

### Using an SSH Key (Recommended)

For more secure and convenient access, especially for automation, use SSH keys.

1.  **Generate an SSH key pair (if you don't have one):**
    ```bash
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```
    Follow the prompts. It's recommended to set a strong passphrase for your private key.

2.  **Copy your public key to the remote server:**
    ```bash
    ssh-copy-id -i ~/.ssh/id_rsa.pub [username]@[remote_host]
    ```
    You will be asked for the password of the remote user once to copy the key.

    Alternatively, you can manually copy the public key content to `~/.ssh/authorized_keys` on the remote server.

3.  **Connect using the key:**
    If your key is in the default location (`~/.ssh/id_rsa`), SSH will automatically use it:
    ```bash
    ssh [username]@[remote_host]
    ```
    If your key has a passphrase, you will be prompted for it. If your private key is not in the default location, you can specify it:
    ```bash
    ssh -i /path/to/your/private_key [username]@[remote_host]
    ```

## Windows

Windows historically required third-party tools, but modern Windows 10/11 includes an OpenSSH client.

### Option 1: Using Built-in OpenSSH Client (Windows 10/11)

1.  **Open PowerShell or Command Prompt:**
    *   Search for "PowerShell" or "cmd" in the Start menu.

2.  **Use the `ssh` command:**
    The usage is identical to Arch Linux/macOS/Termux.
    ```bash
    ssh [username]@[remote_host]
    ```
    *   Replace `[username]` with your username on the remote server.
    *   Replace `[remote_host]` with the IP address or hostname of the remote server.

    **Example:**
    ```bash
    ssh user@192.168.1.100
    ssh admin@example.com
    ```

3.  **Enter your password (or use SSH key as described above).**

### Option 2: Using PuTTY (Third-party client)

PuTTY is a popular free and open-source SSH client for Windows.

1.  **Download and Install PuTTY:**
    Go to the [PuTTY download page](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) and download the appropriate installer.

2.  **Launch PuTTY:**
    *   Find "PuTTY" in your Start menu and open it.

3.  **Configure your connection:**
    *   In the "Session" category, enter the `[remote_host]` (IP address or hostname) in the "Host Name (or IP address)" field.
    *   Ensure "Port" is set to `22` (the default SSH port).
    *   Ensure "Connection type" is set to `SSH`.
    *   You can save the session by entering a name in the "Saved Sessions" field and clicking "Save".

4.  **Open the connection:**
    Click the "Open" button. A terminal window will appear.

5.  **Enter your username and password:**
    You will be prompted for your `[username]` and then your password.

### Using PuTTY with SSH Keys (PPK files)

PuTTY uses its own `.ppk` key format.

1.  **Generate/Convert Keys with PuTTYgen:**
    *   Launch `PuTTYgen` (usually installed alongside PuTTY).
    *   To generate a new key: Select `RSA` as the type, set the number of bits (e.g., 2048 or 4096), and click "Generate". Move your mouse randomly over the blank area to generate randomness.
    *   To convert an existing OpenSSH key (`id_rsa`): Click "Load", navigate to your private key file (e.g., `C:\Users\YourUser\.ssh\id_rsa`), and then click "Save private key" to save it as a `.ppk` file.
    *   Set a passphrase for your private key and remember it.

2.  **Configure PuTTY to use the PPK key:**
    *   Open PuTTY and load your saved session (or create a new one).
    *   Navigate to "Connection" > "SSH" > "Auth".
    *   Click "Browse..." and select your `.ppk` private key file.
    *   Go back to "Session", click "Save" to update your session, and then "Open".

3.  **Connect:**
    You will be prompted for the passphrase of your `.ppk` key if you set one.

---