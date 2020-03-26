Sample web CTF, in this CTF you will face with web vulnerabilities from the concepts of : authentication, access control, session management, input handling - XSS &amp; SQL injection and certificates

Today it seems like all the big important systems are on the web.
For example Facebook, Google, Amazon, Airport ...
As programmers, we have a huge mission:
Making the web more secure and less vulnerable to attacks.
For this mission, you will need to have theoretical knowledge as well as practical knowledge about these topics.

You have been selected to be one of the special programmers that fight along with this mission.

As a start :
Find the most 3 coolest and interesting web attacks committed in the last years in the world.

### Cool right?

## New for the theoretical part : ( 1 / 2 day)
Get familiar with the following topics :
- Authentication.
- Session management.
- Session hijacking
- HTML injection.
- JS injection.
- Reflected XSS.
- Stored XSS.
- DOM-based XSS.
- Obfuscation to client code
- CSRF
- Directory Traversal
- Brute-Force Attacks (not only for passwords)
- certificates

## Practical part : ( 1 / 2 day)
now we got to the fun part.
In the PATH_TO_SERVER_ON_FILESRV, you can find web server serve a simple
back site.
We created this site carefully with a lot of vulnerabilities,
Dig down, search and research for as many vulnerabilities as you can find.

### List of needed fixes :
	- Hash to passwords
	- Add token base authentication
		- Add JWT
	- Obfuscation to client code
	- The tokenId saves per session rather to by sent in etch request as cookie
	- Prevent Brute-Force Attacks
	- The token dose not change ones in a while
	- The token is very easy to guess
	- add ssl to site
	- Session IDs exposed on URL can lead to session fixation attack.
	- Session IDs same before and after logout and login.
	- Session Timeouts are not implemented correctly.
	- Application is assigning same session ID for each new session.
	- Authenticated parts of the application are protected using SSL and passwords are stored in hashed or
	encrypted format.
	- The session can be reused by a low privileged user.
	- Bypassing access control checks by modifying the URL.
	- Force browsing to authenticated pages as an unauthenticated user or to privileged pages as a standard user.

https://dzone.com/articles/cookies-vs-tokens-the-definitive-guide
