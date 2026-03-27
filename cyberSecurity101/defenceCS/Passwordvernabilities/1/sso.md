# Single Sign-On (SSO)

With so many different online services, each with its own password requirements, it's difficult to follow the advice of using a unique password for every site. **Single Sign-On (SSO)** is a service that helps solve this problem.

SSO allows you to use a single, trusted login (like your Google, Facebook, or work account) to sign in to many other third-party services. This provides greater security and convenience, as you can have one very strong, well-protected account that acts as a key to your other accounts.

---

## Technical Details of SSO

SSO is an authentication scheme that allows a user to log in with a single set of credentials to multiple independent software systems. Instead of having to remember and manage separate passwords for every application, the user authenticates once with a central authority and is then automatically granted access to all connected services without needing to log in again.

### How SSO Works: A Simple Analogy

Think of SSO like a theme park wristband.

1.  **Authentication**: You arrive at the main gate of the theme park (the central authority, or **Identity Provider - IdP**) and show your ticket. They verify who you are and give you a wristband.
2.  **Access**: Now, instead of showing your ticket at every single ride and food stall (each being a separate application, or **Service Provider - SP**), you just show your wristband. The ride operators trust the wristband because they trust the main gate that issued it.

In the digital world:
1.  You log in to your company's SSO portal (the IdP).
2.  The SSO portal confirms your identity and creates a secure token (the wristband) for your session.
3.  When you click to open an application like Salesforce or Slack (the SP), it redirects you to the IdP. The IdP sees your valid token and tells the application, "This user is verified, let them in."
4.  You are logged in automatically without entering another password.

### Key Benefits of SSO:

*   **Improved User Experience**: Users only need to remember one strong password, reducing password fatigue and the time spent on logins.
*   **Enhanced Security**:
    *   **Reduces weak passwords**: Since users have fewer passwords to remember, they are more likely to create one strong, complex password for their SSO account.
    *   **Centralized control**: Security teams can enforce strong password policies, multi-factor authentication (MFA), and other security measures in one central place.
    *   **Streamlined offboarding**: When an employee leaves, access to all connected applications can be revoked instantly by disabling a single SSO account.
*   **Increased Productivity**: Less time is spent on password-related issues, such as help desk calls for password resets.

### Risks and Drawbacks of SSO:

*   **Single Point of Failure**: If the Identity Provider (IdP) goes down, users may lose access to all connected applications.
*   **Single Point of Compromise**: If an attacker gains access to a user's SSO account, they potentially gain access to *all* applications linked to it. This makes protecting the SSO account extremely critical.
*   **Implementation Complexity**: Setting up and integrating SSO across various applications can be a complex and resource-intensive process.

**Mitigation**: The primary risk of a single point of compromise is why **SSO should always be paired with strong Multi-Factor Authentication (MFA)**.

### Common SSO Protocols:

*   **SAML (Security Assertion Markup Language)**: An open standard primarily used for enterprise and web-based applications. It's like a highly secure, digitally signed letter that the IdP sends to the SP, vouching for the user's identity.
*   **OAuth 2.0 (Open Authorization)**: An open standard focused on **authorization**, not authentication. It's used to grant third-party applications limited access to a user's resources without sharing their credentials (e.g., "Log in with Google" or allowing an app to access your contacts).
*   **OpenID Connect (OIDC)**: A modern identity layer built on top of OAuth 2.0. It adds the **authentication** piece that OAuth lacks, providing information about who the user is. OIDC is commonly used for consumer-facing applications and mobile apps.