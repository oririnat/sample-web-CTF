public sample web CTF, in this CTF you will face with web vulnerabilities from the concepts of : authentication, access control, session management, input handling - XSS &amp; SQL injection and certificates

- Authentication
	- Hash to passwords
	- Add token base authentication
	- Add JWT
- Obfuscation to client code
- Cross site forgery attack
- Prevent Brute-Force Attacks
- XSS
- Access control
- Session management
- add ssl to site
- Directory Traversal Attacks using "DirBuster"

The tokenId saves per session rather to by sent in etch request as cookie
The token dose not change ones in a while
The token is very easy to guess

Session IDs exposed on URL can lead to session fixation attack.
Session IDs same before and after logout and login.
Session Timeouts are not implemented correctly.
Application is assigning same session ID for each new session.
Authenticated parts of the application are protected using SSL and passwords are stored in hashed or
encrypted format.
The session can be reused by a low privileged user.

HTML injection.
JS injection
Reflected XSS.
Stored XSS.
DOM based XSS.

Bypassing access control checks by modifying the URL.
Force browsing to authenticated pages as an unauthenticated user or to privileged pages as a standard user.
