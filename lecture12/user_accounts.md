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
- The main part is the key-value pair which in this case is: `nyt-a=bLuj-LiP-morejumble`. This is used by new york times as an "Unique identifier to identify behavior on site." (The list of all cookies used by nytimes.com and their details are [listed here](https://www.nytimes.com/subscription/dg-cookie-policy/output.html)).
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

![Page diagrams](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture12/pages_uml1.png)

![User flow diagrams](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture12/user_flow_uml1.png)


- We have added another field called **Login Required**, because there are some pages which are meant only for logged-in users.
  * The value of "No only" means that logged-in users should never see that page.
- In the user flow diagrams, we have differentiated the flow for logged-in and anonymous users

**Exercise:** Some of the web app is similar to the quiz app we created in the last lecture. You need to create the **Home page** and the **Create Article Page**, and create a DB table where you store those articles.

### The data model

As you can see in the diagrams above, there are two tables: `User` and `Posts` which are being referred to again and again for multiple pages. Let's look into what data they would contain.

Here is the **User** table:

| id | email | password_hash | name | following |
| --- | --- | --- | --- | --- |
| ac3 | hh@rockwell.town | 938prfsjkldh398 | Hogarth Hughes | ["b@c3"] |

- The `id` is not an incrementing integer. That is to make sure that if an user id leaks at some point, one cannot find the ids for other users or approximate how many users does the platform have (if they were incremental integers, both those things can be known).
- The password is not stored as it is in the DB. We _hash_ it before storing, i.e., convert into some form of jumbled string which cannot be used to derive the password back.
- The following column is stored as a JSON list of user ids whom an user is following. Storing JSON in DB columns is a common way to store structured data in them.

Now, the **Article** table:

| id | article_title| article_text | author_id | publish_date |
| --- | --- | --- | --- | --- |
| 2y32 | Flying robots | are coming| ac3 | 22 Aug 1953 |

- For the same reason as in **User** table, id is jumbled string. This id is visible to the user, as the View Post page have urls like `/post?id=2y32`.
- The `author_id` should map to one of rows in the **User** table. This is a _foreign key_ to the **User** table.


Here is the `db_tables.py` file for all of this:

```python
from flask_login import UserMixin
from writer import db, bcrypt


class User(UserMixin, db.Model):
    id = db.Column(db.String(32), primary_key=True)
    email = db.Column(db.String(320), unique=True, nullable=False)
    password_hash = db.Column(db.String(56), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    # We store the list of authors being followed as a JSON list of user ids
    following = db.Column(db.Text)

    articles_written = db.relationship("Article", lazy=True, backref="author")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    @classmethod
    def hash_password(cls, password):
        return bcrypt.generate_password_hash(password).decode('utf-8')
        
    def __repr__(self):
        return"{0}: {1}".format(self.email, self.name)       


class Article(db.Model):
    id = db.Column(db.String(16), primary_key=True)
    article_title = db.Column(db.Text)
    article_text = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    publish_date = db.Column(db.TIMESTAMP(timezone=True))

    def __repr__(self):
        return "{0}: {1}".format(self.id, self.article_title)
```

- The User table has a few new items:
  - First, let's look at the `check_password()` and `hash_password()` methods. We are using a library called `flask_bcrypt` to implement the functionality to hash the passwords. The `bcrypt` object is created in `__init__.py` as 

    ```python  
    from flask_bcrypt import Bcrypt
    
    app = Flask(__name__)
    bcrypt = Bcrypt(app)
    ```
  - The next item to look at the is the `db.relationship` function call. This creates a relationship between the current table (User), and the "Article" table.
  - This relationship gives both the table additional fields. In the User table, the field `articles_written` will create a list of Article objects written by this user.
  - The `backref="author"` keyword argument creates a field in the objects of the Article class - this field will contain the `User` object for the author who wrote this article.
  - For this to work, we must have a foreign key relationship, which we are defining in the `author_id` field of the `Article` class.
  - The kwarg `lazy=True` means that the _foreign_ object will be lazily loaded when it's used in the code. This is a good default to have.
  - The fact that it's inheriting from this class called `UserMixin` will be discussed in the next section.
  
- The Article table looks quite simple in comparison
  - The title and text columns are nullable. This is because we will provide the functionality to save an article and edit again later before publishing, and in that case some portions might be left incomplete.
  - As mentioned before, `author_id` field defines a foreign key to the User table.
  - `publish_date` is of type `TIMESTAMP`, which is how we store the time at which the article was published. We also use this field to know if an article is in _draft_ state, i.e., if publish_date is None, we can assume that this article is not published yet. This logic will be handled in the `create_post()` view function.
  
### Implementing user registration and login

The biggest change in this app compared to previous ones we've done is the fact we have user accounts.

To make it much easier to work with those, we will use a library called `Flask-Login`. 

#### Working model for Flask-Login

The primary function that this library performs is this:
 
1. Sets a cookie for the current user when you tell it that the user has logged in (using a function called `login_user()`). It extracts the value of the `id` column in the `User` table (by default, when using `UserMixin`. See below.), and creates a cookie using that.
2. While the user is logged in and sends another HTTP request, that cookie is sent to the HTTP server as part of the request. `Flask-Login` reads that cookie, extracts the user id, and asks us to fetch the corresponding User object (using a `user_loader` function).
3. While logged in, this user is made available to all view functions and in the jinja2 templates as the variable `current_user`.

This saves us from the effort of creating a cookie ourselves, and then getting the information about the user in every view function handling a request. By default, this cookie has none of the properties that we discussed before - only the key value pair.

Whatever class we use to define the User, Flask-Login requires that it implement some attributes to let Flask know the current status. These are:

- `is_authenticated` - set this to `True` if the user's password check has succeeded.
- `is_active` - if an user is inactive (say the platform has blocked them or some verification is pending), then you could set this to `False`.
- `is_anonymous` - set to `True` if this is an anonymous user.
- `get_id()` - this is a method, which you have to implement the user id.

`Flask-Login` also provides a couple of classes which implement these attributes:
- `UserMixin` - this is a class which always sets `is_authenticated` and `is_active` to `True`, and implements `get_id()` method by returning `self.id`.
  - You would login an user only if the authentication succeeds, thus it's reasonable to always set  `is_authenticated` and `is_active` to `True` for an user object representing a logged in user.
  - For the `User` model class, we can inherit from this class to not have to write these attributes ourselves. Our user id _must_ be set in the field called `id`.

- `AnonymousUserMixin` - this is used when no user is logged in, and it sets `is_authenticated` and `is_active` to `False`, and sets `is_anonymous` to True.
  - When a view function or template accesses the `current_user` object when no user is logged in, an object of type `AnonymousUserMixin` is returned. This, combined with the fact that `User` object inherits from `UserMixin` means that we can use properties like `is_authenticated` and `is_anonymous` to make our code do different things (like showing a link for "Login" if `is_anonymous` is `True`, or a link for `Logout` otherwise).

#### Login and Register Forms

The login and register forms need more validation than just `DataRequired()` that we have used before. Let's how that looks like:

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

SMALL_PASSWORD_MESSAGE = "A password must have at least 8 characters"


class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    login = SubmitField("Login")


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(),
                                                     Length(min=8,
                                                            message=SMALL_PASSWORD_MESSAGE)])
    repeat_password = PasswordField('Repeat Password',
                                    validators=[DataRequired(), EqualTo('password')])

    register = SubmitField("Register")
```

- In the `LoginForm`, 
   - the `email` field has additional validator for validating if the email entered by the user is a valid email id.
   - the `password` field is of type `PasswordField`. In a browser, it is rendered so that when the user types a password, the characters are hidden.

- In the `RegisterForm`
  - The `password` field has a check for minimum length. This is to ensure that the password is reasonably secure.
  - We ask for the password twice, which is done to reduce the chance that someone mistype their password. We can use a validator called `EqualTo()` which validates if the value of this field is the same as that other field.
    
#### Detailed form validation error messages

As we saw above in the form definitions, there is much more validation happening at the time of login and registration. It would frustrating to the user if one submits a form which fails validation, but is not told exactly why.

Fortunately, this is easy to implement. For each validation failure, `wtforms` generates an error message we can show to the user automatically. All we need to do is show that to the user - and that means a change is required in the templates.

At first, we create a macro which we can use for every field we need to show errors for:

```html
{% macro show_field_errors(field) %}
<span style="color:red">
    {% for error in field.errors %}
    {{ error }}
    {% endfor %}
</span>
{% endmacro %}
```
- Every `wtforms` field has an attribute called `errors` which contains these error messages.

As an example, this is how the login template looks like that uses this macro:

```html
<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>Login | Writer</title>
</head>
<body>
    {% from "macros.html" import show_flashed_messages, show_field_errors %}
    {{ show_flashed_messages() }}
    <form action="{{ url_for('login') }}" method="POST">
        {{ form.hidden_tag() }}
        <p>
            {{ form.email.label }}:<br>
            {{ form.email(size=75) }}<br>
            {{ show_field_errors(form.email) }}
        <p>
            {{ form.password.label }}:<br>
            {{ form.password(size=75) }}<br>
            {{ show_field_errors(form.password) }}

        <p>{{ form.login() }}
    </form>

    <a href="{{ url_for('register') }}">Not registered?</a>
</body>
</html>
```
- For the `email` and `password` fields, we call the `show_field_errors` macro. It lets the user know if they entered an invalid email address in this case (we have no validation for the `password` field in the `LoginForm`).

The usage in the template for registration is identical.
  
#### Login and Register view functions

Now that we know how `Flask-Login` works, and have the relevant forms ready, we can start writing the view functions.

To work with `Flask-Login`, we need to create an object of a class called `LoginManager`, which is used frequently. We would do this in `__init__.py`:

```python
from flask_login import LoginManager

#... create app object

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
```
- The `login_view` attribute tells `Flask-Login` what view to execute if it needs to redirect an anonymous user to login before accessing a "login required" page.

Next, we need to take care of the `user_loader` function. This function must return the `User` object given the user's id, as shown below:

```python
from writer import app, db, login_manager
from writer.db_tables import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
```

- As mentioned before, it is called when `Flask-Login` receives a cookie for an user session and it needs to get the corresponding `User` object.


The login page is implemented as below:

```python
from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required

from writer.forms import LoginForm, RegisterForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return _continue_browsing()

    form = LoginForm(request.form)

    if request.method == 'POST':
        if form.validate():
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None and user.check_password(form.password.data):
                login_user(user)
                return _continue_browsing()
            else:
                flash("No user with email-id found, or the password is "
                      "incorrect.")
        else:
            print("Invalid or incomplete input.")

    return render_template("login.html", form=form)
    
def _continue_browsing():
    return redirect(url_for('all_posts'))    
```
- Irrespective of the method of the request, if the user is already authenticated, then coming to this page is a mistake. We redirect them away automatically in that case.
- If the request method is not `POST`, we just respond with the login page that renders the `LoginForm`.
- If the method is `POST`, then we use the email from the form to find the corresponding user from the DB. If we find an user, and have ensured that the password matches, we can _log the user in_, i.e., ask `Flask-Login` to set the cookies.
- For that, we call a function called `login_user()` with the `user` object.

There is a corresponding logout view as well:

```python
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return _continue_browsing()
```
- Note that we have this page is decorated with `@login_required`. This tells `Flask-Login` that this view must only be rendered if the user is logged in, otherwise it automatically redirects the user to the login page (and we set that in the `login_manager.login_view` property in `__init__.py`). 


And finally, we have the view for registration, which adds new users to the platform (and to the DB).

```python
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return _continue_browsing()

    form = RegisterForm(request.form)

    if request.method == 'POST':
        if form.validate():
            try:
                return _add_user_to_db(form)
            except SQLAlchemyError:
                flash("We couldn't register you due to a technical issue"
                      " on our side. Please try again later.")
        else:
            flash("The form was not properly completed.")

    return render_template("register.html", form=form)


def _add_user_to_db(form):
    user = User(id=token_hex(32),
                email=form.email.data,
                password_hash=User.hash_password(form.password.data),
                name=form.name.data)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return _continue_browsing()
```

- As with the login page, a logged in user has no business being here.
- It's a `GET` request, we just render the form and send that back.
- Otherwise, once the form is validated, we create an `User` object and add that to the DB.
  - The user id is generated using this function called `token_hex()`, available in the `secrets` module in Python (needs version >= 3.6).
- In our app, we also log in the user who has registered. In most websites, this doesn't happen - they usually send a verification email to the email address and log the user in only after the user clicks on a link in that verification email.

### Creating articles

Adding new articles is not dissimilar from how we added new questions in the Quiz app in the last lecture.

There a couple of new things though. We mentioned before that users are allowed to save articles in the draft state. This means that the form needs two buttons - one for "Publish", another for "Save"

```python
class CreatePostForm(FlaskForm):
    title = StringField("Article Title", validators=[DataRequired()])
    text = TextAreaField("Article Text", validators=[DataRequired()])
    publish = SubmitField('Publish the article')
    save = SubmitField('Save the article')
```

Then, at the time of addition to the DB, we need to make sure we don't set the `publish_date` in case the user just saves the article but not publish it.

```python
from datetime import datetime, timezone
from secrets import token_urlsafe

# form is created as follows
# form = CreatePostForm(request.form)


def _add_post_to_db(form):
    article_id = token_urlsafe(16)
    is_draft = True if form.save.data else False
    publish_date = None if is_draft else datetime.now(timezone.utc)

    if not is_draft and not form.validate():
        flash("Not all required fields were filled.")
        return _render_form(form)

    article = Article(id=article_id,
                      article_title=form.title.data,
                      article_text=form.text.data,
                      author_id=current_user.id,
                      publish_date=publish_date)
    db.session.add(article)
    db.session.commit()

    if is_draft:
        flash("The article was saved.")
        return _render_form(form)
    else:
        return redirect(url_for('view_post', id=article_id))
```
- The `article_id` is generated using `token_urlsafe` from the `secrets` module.
- When there are two buttons, and the user submits the form using one of them, the `request.form` dictionary contains a key only for the button which was pressed. For example, if user pressed the `Save` button, then the dictionary will have the key `save` but not the key `publish`.
- Thus, if `form.save.data` is not None, user has clicked `Save`, or `Publish` otherwise. We use this to know if the article is in draft state.
- There are couple of things we need to differently if the article is in draft state:
  - `publish_date` is None in this case.
  - If it's not in the draft state, then we do form validation and make sure that both the title and the text of the article are present.
  
### Login required page

We've already seen that the decoration `@login_required` makes the view only accessible to users who are already logged in. In addition to `logout` view, we have also added it to the `create_post` view. 

For these pages, we need to redirect the user to login page (which `Flask-login` does automatically). After the user is logged in, we want to remember the page user was redirected from, and then redirected back.

`Flask-login` comes to our rescue again. When a user is redirected to the login page, `Flask-login` sets a query parameter called `next` in the URL. For example, if we our website is `www.writer.com`, the request URL would like `www.writer.com/login?next=/create` which is telling the login page to send the user to `/create` after they are logged in.

We can update our `login` given this knowledge:

```python
app.route('/login', methods=['GET', 'POST'])
def login():
    next_page = request.args.get('next')

    if current_user.is_authenticated:
        return _continue_browsing(next_page)

    form = LoginForm(request.form)

    if request.method == 'POST':
            # ... authenticate and login user
    
                return _continue_browsing(next_page)
            else:
    
    # ...
    
    login_action = (url_for('login') if next_page is None
                    else url_for('login', next=next_page))
    return render_template("login.html", form=form, login_action=login_action)


def _continue_browsing(next_page=None):
    # URL form: scheme://netloc/path;parameters?query#fragment
    # If netloc is empty, it means the URL is relative, which we want to ensure
    # so that we don't send our user to other domains.
    if next_page and not url_parse(next_page).netloc:
        return redirect(next_page)
    else:
        return redirect(url_for('all_posts'))    
```

- The query params can be extracted from the URL using `request.args.get()` method.
- We've updated the function `_continue_browsing()` to take `next_page` as an argument, which is `None` by default.
  - Since this is a user visible parameter, any malicious user/actor can change the value of next param. Before we use it, we need to ensure it's safe to use.
  - In case it's present and safe to use, we redirect the user to that page.
- An important thing to note is that you would receive the `next` param when you recieve a `GET` request for the login page. But, the redirection is required once the user submits the login form successfully. Thus, we need to persist the value of the `next` param till that happens.
- To do that, we add the next query param to the action URL of the form by providing the action URL to the template. The `url_for` function adds any keyword arguments that you provide to it as query parameters in the URL. In this case, passing an argument like `next='/create'` adds `?next=/create` to the URL.

The template can then set form action using this URL instead of it calling `url_for` itself, as follows:

```html
<form action="{{ login_action }}" method="POST">
```

### Viewing articles

For the view post page, we will use the same principle that we've applied before in assignments: that the link to the article should be sharable. This implies that the id of the article must be present in the url. The url to an article would look like: `www.writer.com/post?id=abcdef`, where `abcdef` is the article id we've assigned in the DB.

The view function then becomes quite easy - we just have to read the DB for the article id and pass it to the template to view it. Here is how it can be implemented:

```python
from flask import request, render_template

from writer import app
from writer.db_tables import Article


@app.route('/post', methods=['GET'])
def view_post():
    article_id = request.args.get('id')
    if article_id is None:
        return _article_not_found()

    article = Article.query.get(article_id)
    if article is None or article.publish_date is None:
        return _article_not_found()

    return render_template("view_post.html", article=article)


def _article_not_found():
    return "Article Not Found", 404
```

- There are three cases when we would return an "Article Not Found" message:
  1. The query parameter `id` is not present in the URL.
  2. There is no article corresponding to the value of the query parameter `id` in the URL (url is of the form ?id='blahblah').
  3. If the `publish_date` is `None` for this article (indicating that the article is in draft status), we don't expose it to the public.
- Note how you can specify the HTTP response code as the second argument of a tuple when returning a value to the view function.

Given this implementation of the View Post page, we need to make sure that any link to the article creates the URL accordingly.

### Navigation bar

In a website like this, it's impossible for the user to navigate through the website unless there is a set of links consistently shown on all pages of the website. Furthermore, in a dynamic website like this, the navigation bar is also dynamic. Depending on the whether the user is logged in or not, the links shown on that navigation bar will change.

The ideal way to implement the navigation bar is to write the code to generate it once, and then just include it in all the pages. Using the `{% include <filename> %}` directive in jinja2, that's exactly what we do.

At first, let's create the file `navigation.html`, which only contains the HTML and template elements specific to the navigation bar:

```html
<a href="{{ url_for('all_posts') }} ">Home</a> |
<a href="/not_implemented">Authors following</a> |
<a href="{{ url_for('create_post') }}">Write</a> |
{% if current_user.is_anonymous %}
    <a href="{{ url_for('login') }}">Login</a>
{% else %}
    Hi {{ current_user.name }}
    <a href="/not_implemented">Profile</a>
    <a href="{{ url_for('logout') }}">Logout</a>
{% endif %}
```

- This is just a set of links separated by the pipe character.
- We have access to the `current_user` object inside the template. 
- Using its `is_anonymous` property, we can either display the **Login** link if no user is logged in, or display the name of the user, link to the **Profile** page and a **Logout** link when the user is logged in.
- A couple of pages have the link `/not_implemented` because it's an exercise for you to implement those pages and update the navigation bar :-). (see below)

To use this navigation bar, here is the template for `posts_list.html` which I have used for the home page to list all articles.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>All Articles | Writer</title>
</head>
<body>
    {% include 'navigation.html' %}
    <hr>

    {% for article in articles %}
        <p>
            <b>
                <a href="{{ url_for('view_post', id=article.id) }}" >
                    {{ article.article_title }}</a>
            </b><br>
            Written By: {{ article.author.name }}
        </p>

    {% endfor %}

</body>
</html> 
```

- You can see that right after the `<body>` tag, I have the jinja directive `{% include 'navigation.html' %}` that simply copy pastes the contents of `navigation.html` here.
- The `<hr>` tag creates a horizontal rule which visually separates navigation bar from the page contents.
- I have added these two lines at the top of the `<body>` section in every template.


### Following and Profile pages

**Exercise:**

These two pages are left as an exercise. Some things to keep in mind:

- To add to the list of authors an user is following, a link is added to view post page close to author's name.
- If the user is already following that author, then they should also be allowed to unfollow.
- The `following` column in the `User` table is a JSON string containing the user ids of authors being followed. That means you'll be using the [json](https://docs.python.org/3/library/json.html) module.

- For the profile page, your implementation should allow them to update their name and email.
- It should also list all their articles, including the ones in draft mode (which label are labelel so) and give them an opportunity to 
   - update, delete or move the published ones to draft status 
   - update, delete or publish the ones in draft status.

   