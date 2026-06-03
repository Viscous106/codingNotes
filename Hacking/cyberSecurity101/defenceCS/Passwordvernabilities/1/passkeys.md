# Passkeys

**Passkeys** are an emerging, modern replacement for passwords. They are designed to be more secure and easier to use than traditional passwords.

Instead of you creating a password, a passkey is an automatically generated cryptographic key pair that is unique to each website or service.

## How Passkeys Work

Passkeys are based on a concept called **public-key cryptography**.

1.  **Key Pair Generation**: When you sign up for a new service, your device (e.g., your phone or computer) creates a unique pair of linked cryptographic keys:
    *   A **Public Key**: This key is shared with the website or service and is stored on their servers. It's not a secret.
    *   A **Private Key**: This key is stored securely *only on your device*. It is never shared with anyone.

2.  **Logging In**: When you want to log in, the website sends a challenge to your device. Your device uses its private key to "sign" the challenge and send it back. The website then uses your public key to verify the signature.

3.  **Authentication**: If the signature is valid, you are logged in. You never have to type a password. The authentication is typically authorized on your device using your fingerprint, face, or device PIN.

## Advantages of Passkeys

*   **No Passwords to Remember**: You no longer need to create, remember, or type passwords.
*   **Phishing Resistant**: Because the private key never leaves your device and is tied to a specific website, you cannot be tricked into entering it on a fake phishing site.
*   **Extremely Secure**: The cryptographic keys are extremely long and complex, making them resistant to brute-force attacks.

Passkeys are still an emerging technology, but they represent a significant step forward in account security and will likely become much more common in the future.
