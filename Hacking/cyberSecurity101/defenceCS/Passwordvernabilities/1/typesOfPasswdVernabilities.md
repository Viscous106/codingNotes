# Introduction to Account Security

In the digital world, security is built on several foundational blocks. The primary goal is **authorization**: verifying that you are the person who should have access to an account. This is typically done with a combination of a **username** and a **password**. The core idea is that only the legitimate user should know both of these credentials.

However, attackers have developed numerous methods to try and defeat this system.

## Password Attacks

### Dictionary and Brute-Force Attacks

Attackers often try to guess your password. Two common methods are:

1.  **Dictionary Attacks**: Using a list of common words and phrases as potential passwords.
2.  **Brute-Force Attacks**: Systematically trying every possible combination of characters.

The lecture illustrates that as password complexity increases, the time it takes for a brute-force attack to succeed grows exponentially.

*   **4-digit PIN**: `10 x 10 x 10 x 10` = 10,000 possibilities. An attacker can generate these almost instantly.
*   **4-letter password (lowercase)**: `26 x 26 x 26 x 26` = 456,976 possibilities.
*   **4-letter password (upper and lowercase)**: `52 x 52 x 52 x 52` = Over 7 million possibilities. Still crackable in seconds.
*   **4-character password (letters, numbers, symbols)**: `~94 x ~94 x ~94 x ~94` = Over 78 million possibilities. This starts to take a noticeable amount of time for an attacker.

The key takeaway is that longer and more complex passwords raise the bar for attackers, making their job much more difficult and time-consuming.

### The Security vs. Usability Tradeoff

There is a constant balance between security and usability. A 30-character random password is very secure, but it's impossible to remember and difficult to type. A simple password is easy to use but offers little security. As you consider your security options, you must think about what makes the most sense for your use case.

## NIST Password Guidelines

The **National Institute of Standards and Technology (NIST)** provides best practices for password security. Here are some of their key recommendations:

*   **Length**: Passwords should be at least **8 characters** long.
*   **Character Set**: Allow for all printable ASCII characters and Unicode symbols, up to at least **64 characters**.
*   **Prohibited Passwords**: Check new passwords against lists of known breached passwords, dictionary words, and context-specific words (like the service name or username).
*   **No Password Hints**: Do not provide password hints to unauthenticated users.
*   **No Forced Periodic Changes**: Don't require users to change their passwords on a fixed schedule, as this often leads to weaker, more predictable passwords.
*   **Failed Attempt Limits**: Limit the number of failed login attempts to lock out attackers.