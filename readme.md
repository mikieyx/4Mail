# 4Mail README

# Functionality

The following are the main features of 4Mail:

1. To-Do List: Users can create and manage their to-do list on the 4Mail website, adding tasks with details, due dates, and notes, and marking them as completed when finished. [Michael]
2. News Articles API: Users can access external news articles through the 4Mail website, with the system gathering and organizing articles in a user-friendly format. [Michael]
3. Account Creation: Users can easily create a new account on the 4Mail website by filling in a registration form with a username, email address, password, and confirming the password. [Cedric]
4. Email Sending: Users can send emails to a recipient by composing a message, writing a subject, selecting a recipient by email address, and clicking the "send" button. [Cedric]
5. Account Login/Logout: Users can securely log in to their 4Mail account by entering their username and password on the login page. Also, users can easily log out of their 4Mail account by clicking on the "Log Out" button in their profile/account page, which will securely log them out and redirect them to the login page or homepage. [Alex]
6. Send Chat: Users can send chat messages to other 4Mail users by create a chat room and create a message, and clicking the "send" button. [Van]
7. Receive Chat: Users can receive chat messages from other 4Mail users by viewing incoming messages in their chat room. [Van]
8. Account Deletion: Users can choose to delete their 4Mail account by clicking on the "delete account" button in their account settings page and confirming the deletion, which will remove all associated data and log them out. [Alex]

# Installation

- pip install alembic           1.10.4
- pip install pbidict           0.22.1
- pip install blinker           1.6.2
- pip install certifi           2022.6.15
- pip install cffi              1.15.1
- pip install click             8.1.3
- pip install colorama          0.4.5
- pip install config            0.5.1
- pip install cryptography      40.0.2
- pip install Deprecated        1.2.13
- pip install distlib           0.3.4
- pip install dnspython         2.3.0
- pip install dominate          2.7.0
- pip install email-validator   2.0.0.post2
- pip install filelock          3.7.1
- pip install Flask             2.2.3
- pip install Flask-Bootstrap   3.3.7.1
- pip install Flask-JWT         0.3.2
- pip install Flask-Login       0.6.2
- pip install Flask-Mail        0.9.1
- pip install Flask-Migrate     4.0.4
- pip install Flask-SocketIO    5.3.3
- pip install Flask-SQLAlchemy  3.0.3
- pip install Flask-WTF         1.1.1
- pip install greenlet          2.0.2
- pip install PyJWT             2.4.0
- pip install python-dotenv     1.0.0
- pip install python-engineio   4.4.1
- pip install python-jwt        4.0.0
- pip install python-socketio   5.8.0
- pip install stocket           
- pip install simple-websocket  0.10.0
- pip install six               1.16.0
- pip install SQLAlchemy        2.0.9
- pip install typing_extensions 4.5.0
- pip install virtualenv        20.15.1
- pip install virtualenv-clone  0.5.7
- pip install visitor           0.1.3
- pip install Werkzeug          2.2.3
- pip install wrapt             1.15.0
- pip install wsproto           1.2.0
- pip install WTForms           3.0.1

# How to use

1. Install Python 3.x on your computer (if it's not already installed). You can download Python from the official website: https://www.python.org/downloads/
2. Install the required Python packages that listed in Installation above.
3. Run the run.py script to start the program. You can do this by running the following command in your terminal or command prompt: python3 run.py
4. Follow the prompts in the program to select your options and input your information.
5. Once you have finished using the program, you can exit it by selecting the appropriate option in the menu or by pressing CTRL + C in your terminal or command prompt.

# Usage

1. Add a task to the todo list:

- Navigate to the 4Mail website.
- Log in to your account.
- Click on the "to-do list" page.
- Click the "add task" button.
- Write the name of the task to be completed.
- Write any details/notes about the task (optional).
- Write the date that the task should be completed.
- Click the "create" button.

2. Connect to external News Articles API:

- Navigate to the 4Mail website.
- Log in to your account.
- Click on the "news" page.
- The system will gather articles and display them in an organized fashion.

3. Create an account (register):

- Navigate to the 4Mail's register webpage.
- Fill in the registration form that asks for a username, email address, password, and confirm password.
- Click on the "create account" button to submit the form
- The system will check the validity of the input and create the account.
- The system will redirect you to the login page.

4. Send an email:

- Navigate to the 4Mail website.
- Log in to your account.
- Click on the "Send Email" button located on the nav bar.
- Enter a recipient by inputting their email address
- Write the subject of the email
- Write your message in the text box.
- Click on the "send" button.
- The system will send the message and give you an option to write another email or go to the homepage.

5. Delete an email:

- Navigate to the 4Mail website.
- Log in to your account.
- Click on the "Inbox" button located on the nav bar.
- Click the delete button next to the email you want to delete.
- The system will delete the email from your inbox and show the rest of your remaining emails.

6. Log In/Log Out:

- Navigate to the 4Mail website.
- To log in, click on the "Log In" button and enter your login credentials (username and password).
- If successful, the system will redirect you to your account page.
- To log out, click on the "Log Out" button in your account (in the navbar of the webpage).
- The system will log you out and redirect you to the login page or 4Mail's homepage.

7. Send A Chat Message:

- Navigate to the 4Mail website.
- Log in to your account.
- Click on the "Join Chat Room" button.
- Enter their name and click "Create A Room"
- Enter a message in the text box.
- Click on the "send" button.
- The system will send that message to everyone in the chat room.

8. Receive A Chat Message:

- Navigate to the 4Mail website.
- Log in to your account.
- Enter their name and click "Join Chat Room" button.
- Go to the chat section of your account.
- Wait for a new chat message to appear in the chat window.
- Once a new message appears, you can reply other people's message.

9. Leave The Chat Room:

- Navigate to the 4Mail website.
- Log in to your account.
- Enter their name and click "Join Chat Room" button.
- Go to the chat section of your account.
- Click "Leave Chat" to leave the room chat

10. Delete Account:

- Navigate to the 4Mail website.
- Log in to your account.
- Click on the "delete account" button in your account (in the navbar of the webpage).
- The system will delete all data associated with your account and log you out right after clicking the button.
- After that you will be in the homepage of 4Mail but for unregistered users.

11. Password Reset (When users forget their password to login):

- Navigate to the 4Mail's login website.
- Click "Reset via Email" button, then the system will redirect you to "reset_password_request" webpage.
- Type your email in the form, then click "password reset request" button.
- Then the system will send you the password reset email.
- In that email, clicking the link to set new password.
- After doing some validation, the system saves your new password into the database.
- Now you can use the new password to access your account.

# Contributors

- Michael Pavlik (@mikieyx) Team Lead
- Cedric Briones (@cedricJB07)
- Anh Nguyen (@AlexNguyenSJSU)
- Van Duong (@vduong421)
