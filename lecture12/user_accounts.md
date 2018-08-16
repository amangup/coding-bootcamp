# Websites with User accounts

We will learn how to allow for users to _register_ with the website and personalize their experience of their website by _logging_ into the website.

The HTTP protocol is _stateless_, i.e., when one user makes two requests, one after another, the HTTP server doesn't remember the details about the first request when it receives the second request, and connect the two requests to conclude that they are from the same user. The server doesn't maintain the state in which an user is.

To build a friendly user experience which allows users to remain log in once, and then spend time on the website without re-logging again, we need to create a _user session_ using **HTTP cookies**. That links one users' multiple requests to the web server and allows the server to know what kind of content to serve to the user.

Allowing user logins also means that our websites will deal with sensitive information, most notably the password. Transferring such information on the internet is not always secure, and we will learn about how we should insist on using HTTP**S** (S stands for _Secure_) when handling such information. 

As always, there is a lot to learn, so let's get started.

## HTTP Cookies and Sessions

HTTP Servers have don't remember history. As soon as they send the response to the clients they forget who the clients were. In most websites, though, it is important to remember who the user was, and to serve content knowing that (like showing your email inbox). The user then can read and reply to all their unread emails without having to identify tham again and again. This interaction across multiple HTTP requests and responses with the website and the user is called a **Session**.

From the understanding we already have about HTTP, we have no way to implement this. This is how an user interaction would look like:

![No Cookie](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture12/no_cookie.gif)

In HTTP, there is a way for HTTP servers to give the clients (a web browser) a token, once the user has logged in to the website. From then onwards, every time the user accesses that website, the client sends the token to the website. That token works as indentification, and the HTTP server then responds assuming the user is logged in. This token is called a **cookie**. From the point of view of the human using the web app, the experience feels like if the website knows who they are throughout the session (as they don't need to know about the token that's repeatedly sent by the client to the server.) 

With the cookie, here is how an interaction between the client and the server looks like:

![With Cookie](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture12/with_cookie.gif)

### What data does a cookie have?

A cookie is just a key-value pair. Here is an example of the cookie I got when I logged into the New York Times website:


```
GET https://www.nytimes.com/?login=email&auth=login-email HTTP/2.0
...
```

```
HTTP/2.0 200 OK
Content-type: text/html
...
set-cookie: nyt-a=bLuj-LiP-morejumble; Expires=Mon, 12 Aug 2019 19:41:19 GMT; Path=/; Domain=.nytimes.com
...
```

- The HTTP request has no mention of the cookie, the time I log in.
- The HTTP response has a header called `set-cookie`. The details of the cookie are set in the value of that header.
- The main part is the key-value pair which in this case is: `nyt-a=bLuj-JiQ-yumOlEbXze0wP`. This is used by new york times as an "Unique identifier to identify behavior on site." (The list of all cookies used by nytimes.com and their details are [listed here](https://www.nytimes.com/subscription/dg-cookie-policy/output.html)).
- The cookie has three more attributes:
  - There is an expiry date, and this instructs my browser to not delete this cookie until that date.
  - There is a `Domain` attribute, which tells the browser to send the cookie in the HTTP request sent to this domain.
  - The `Path` attribute is very similar to the `Domain` attribute, except that it specifies the path inside the domain.
  
When I send another request to nytimes.com now (let's say, I click on an article), the HTTP request contains the cookie:

```
GET https://www.nytimes.com/2018/08/11/science/parker-solar-probe-launch.html HTTP/2.0
...
Cookie: nyt-a=bLuj-LiP-morejumble
...
```

### Does it come in multiple flavors?

Cookies can have many attributes, that affect how it is used.

- **Expires** and **Max-Age**: As discussed above, these tell the browser how long should it keep this cookie around. This is an optional field, and if it is not present, then the browser will forget about this cookie once it is closed.
- **Domain** and **Path**: We've discussed this above as well. This too is an optional field and if it's not specified, browser assumes it to be the domain and path of the HTTP request that it sent.
- **Secure** and **HttpOnly**: These are both used for security purposes. **Secure** specifies that send this cookie only over _secure_ (encrypted) connections. **HttpOnly** specifies that it the cookie shouldn't be shared with anyone, but only sent as part of HTTP requests to the relevant domain and path (this means that client side javascript cannot access these cookies).

Cookies are highly personal information. If your cookie for a website is leaked, then an attacker can impersonate you on that website, and potentially steal a lot of your information (an attack called "Session side jacking").

Cookies are not just used for user sessions. Other uses include _personalization_ of an user session (cookies can store your choice of the background color, for example, in an online editor), and tracking users' web browsing habits (which has become quite controversial and the target of user data protection laws).

## Encryption

Encryption is the process of transforming meaningful information into a meaningless blob of data which, in a way that someone who has an appropriate key can undo that transformation. If that key is kept protected, then different parties can send information over unsecure channels without the fear of getting compromised.

Encryption can be implemented in two ways - Symmetric  Encryption and Asymmetric Encryption.

### Symmetric Encryption
An encryption scheme is called **symmetric** if the key that is used to encrypt some data is the same one used to decrypt it as well. 
- This works well if the two parties that are communicating already know that key.
- If they don't already know the password, the encryption mechanism doesn't help them to share _that key_. They would need to somehow find another secure communication channel to share the key.

The most common algorithm to implement Symmetric Encryption is called [**AES**](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)

### Asymmetric Encryption
An asymmetric encryption scheme uses two keys - a **private key** and a **public key**. Messages are encrypted using the public key, and once encrypted, the only way to decrypt them is by using the private key.

- The public and private keys are generated as matching pairs by the algorithm.
- One can share the public key with absolutely anyone who might want to send them a message (and that is what a website which implements HTTPS does). The private key must be kept secret.
- When someone has to send a message to the receiver, they can encrypt it using the public key and send it over an unsecure channel.
- The receiver can use the private key to decrypt. As long as private key is secret, that message is 

This way, two strangers who have no secure channel to communicate can also send each other messages without the fear of getting eavesdropped upon.

The standard algorithm used for Asymmetric Encryption is called [**RSA**](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

![Public Private key Cryptography](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture12/Public_key.svg)


### Strength of encryption
The strength of encryption is measured as the length of the keys, measured in bits. That means that if a key is 256 bits long, the message encrypted using that key is harder to decrypt than a message encrypted using a 128 bit key. The reason why it becomes harder as key length increases is because an attacker will have to guess the key to break encryption, and longer keys are harder to guess.

The standard for the length of keys keep changing, as computers become faster. Faster computers can guess and check more keys for whether they work or not, in a lesser amount of time. Thus, as time goes on, if we use the same encryption algorithm, we have to keep updating the length of the key.

The current standard for RSA key lengths is 4096 bits, and AES key lengths is 256 bits.

## Security on the internet

We've already discussed how a lot of information that is shared by the user with a website (and vice versa) is sensitive and shouldn't get into the wrong hands. The way we can hide our data from prying eyes is by using **encryption**.

When we send an HTTP request (without encryption), every character contained in it can be seen by many parties:
- Your internet provider can see what it contains.
- All the servers through which your data packet passes can see your information.
- If someone else is connected to your LAN, then they can sniff the data coming in and out of your computer.

Imagine creating a web form for username and password, and then sending that password as it is in an HTTP request (the way form data is sent in our websites right now). This is like writing your the website's address, your username and password down on a piece of paper and mailing the piece of paper in a _resealable_ envelope.

### Man in the middle attack

The type of attack where someone eavesdrop on your communication and then impersonates as you is called a **Man in The Middle** (or MiTM) attack. To prevent someone from eavesdropping, strong encryption of data is required.

Note that this is not the only type of MiTM attack. For example, attacks where the malicious entity installs malware on your computer to get information is also MiTM, but those and other MiTM attacks are out of the scope of current discussion. 

## HTTP Secure

HTTP Secure is an update on the HTTP protocol which adds additional steps to make sure that the communication between the client and the server is encrypted. These additional steps are defined int the **TLS** protocol, short for Transport Layer Security. 

It adds the following steps:
- A **handshake** happens between the client and the server, where they use assymetric encryption using the Server's private key to give information about each other (like version of protocol supported)
- The outcome of the handshake is a _new_ randomly generated key which is shared between the two parties.
- From then on, they use this new key to communicate, and as both now know this key, they can use symmetric encryption.
  * All HTTP Request and Responses are encrypted before they are sent across the internet.
- This new key is only valid for this session, and once the session ends (browser is closed, for example), if you connect to the same website, it starts with the handshake again.

### HTTPS certificate
Every website that uses HTTPS needs to create a certificate, the primary purpose of which is to share the public key of the server. Certificates are also verified by independent authorities, to ensure that the public key indeed belongs to your server and you do hold the corresponding private key.

When launching our website for public use, we need to obtain this certificate. Otherwise the browser will mark our website as untrustworthy.

 
## A writing web app

In this tutorial, we are going to write an app which allows authors to add articles to the platform, and let other users to view those articles. We will also allow readers to follow some specific authors and read articles from only those.

As we did for the quiz app, we start with the diagrams. Here are the page and the user flow diagrams for this webapp.

![Page diagrams](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture12/pages_uml1.svg)

![User flow diagrams](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture12/user_flow_uml1.svg)


- We have added another field called **Login Required**, because there are some pages which are meant only for logged-in users.
  * The value of "No only" means that logged-in users should never see that page.
- In the user flow diagrams, we have differentiated the flow for logged-in and anonymous users

**Exercise:** Some of the web app is similar to the quiz app we created in the last lecture. You need to create the **Home page** and the **Create Article Page**, and create a DB table where you store those articles.

