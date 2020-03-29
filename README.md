# web challenges - CTF
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
- input handling.
- Obfuscation to client code.
- CSRF.
- Directory Traversal.
- Brute-Force Attacks (not only for passwords).
- certificates.

## Practical part : ( 1 / 2 day)
now we got to the fun part.
In the PATH_TO_SERVER_ON_FILESRV, you can find web server serve a simple
back site.
We created this site carefully with a lot of vulnerabilities,
Dig down, search and research for as many vulnerabilities as you can find.
For some of the exploits, you may find relevent solutions in the Attckes folder
(Please don't open this Attckes folder unless you have to get a clue)

After showing us the list of vulnerabilities and exploits,
Your next important mission is to fix the vulnerabilities.

You may commit changes is the client-side as well as in the server.
[ ! ] Pay attention, the server-side is written in Flask - python.
The solution we looking for is conceptual,
Try not to use Flasks library that makes the solution abstract.
Instead, implement the concept of the fixes / best practices and with python script.

You can find in PATH_TO_DOCKERTODOS, a full guide of instrection of running the server with preready docker

### known exploits :
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
