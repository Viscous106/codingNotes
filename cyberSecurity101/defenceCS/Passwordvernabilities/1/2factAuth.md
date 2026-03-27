# Two-Factor & Multi-Factor Authentication (2FA/MFA)

While a strong password is a good first line of defense, a second factor of authentication makes your account significantly more secure. This is known as **Two-Factor Authentication (2FA)** or, more broadly, **Multi-Factor Authentication (MFA)**.

MFA relies on requiring proof from two or more of the following categories:

1.  **Knowledge**: Something only you *know* (e.g., your password).
2.  **Possession**: Something only you *have* (e.g., your phone or a hardware key).
3.  **Inherence**: Something only you *are* (e.g., your fingerprint or face).

## One-Time Passwords (OTPs)

A common way to implement the "Possession" factor is with a **One-Time Password (OTP)**. This is a temporary code used to verify your identity. However, not all OTP methods are equally secure.

### Methods of Delivering OTPs

#### 1. Text Message (SMS) based OTPs
This method sends a code to your phone via text message. As the lecture points out, this is the most vulnerable form of 2FA.

*   **Vulnerability: SIM Swapping**: An attacker can convince your mobile provider to transfer your phone number to a SIM card they control. Once they have your number, they receive your OTPs and can take over your accounts.

#### 2. Authenticator Apps
These apps (like Google Authenticator or Authy) are installed on your phone and generate a constantly refreshing OTP.

*   **Security**: This is far more secure than SMS because the code is generated on your device and is not transmitted over a vulnerable network.

#### 3. Key Fobs / Hardware Tokens
These are small physical devices, separate from your phone, that generate OTPs. You press a button on the device to get the code.

---

## The Threat of SIM Swapping

As mentioned, **SIM swapping** is a social engineering attack where a criminal obtains a clone of your SIM card, giving them access to your text messages and phone calls.

### How it Works
1.  **Information Gathering**: An attacker finds personal details about you.
2.  **Impersonation**: They contact your mobile provider, pretending to be you.
3.  **The Swap**: They convince the provider to activate a new SIM card that they control.
4.  **Takeover**: They can now intercept your SMS-based OTPs and compromise your accounts.

### Protection
*   **Avoid SMS-based 2FA**: Use authenticator apps or hardware keys instead.
*   **Set a PIN on your mobile account**: This adds another layer of verification that an attacker would need to know.