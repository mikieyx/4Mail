# 4Mail README

# Functionality

The following are the main features of 4Mail:

1. To-Do List: Users can create and manage their to-do list on the 4Mail website, adding tasks with details, due dates, and notes, and marking them as completed when finished. [Michael]
2. News Articles API: Users can access external news articles through the 4Mail website, with the system gathering and organizing articles in a user-friendly format. [Michael]
3. Account Creation: Users can easily create a new account on the 4Mail website by filling in a registration form with a username, email address, and password. [Cedric]
4. Email Sending: Users can send emails to one or multiple recipients by composing a message, selecting recipients by email address, and clicking the "send" button. [Cedric]
5. Account Login/Logout: Users can securely log in to their 4Mail account by entering their username and password on the login page. Also, users can easily log out of their 4Mail account by clicking on the "Log Out" button in their profile/account page, which will securely log them out and redirect them to the login page or homepage. [Alex]
6. Chat Messaging: Users can send chat messages to other 4Mail users by composing a message, selecting recipients by username, and clicking the "send" button, with recipients receiving notifications of new chat messages. [Van]
7. Star Important Email: Users can mark important emails by clicking on the star icon next to the email subject or sender. This will add the email to a "Starred" folder for easy access and reference. [Van]
8. Account Deletion: Users can choose to delete their 4Mail account by clicking on the "delete account" button in their account settings page and confirming the deletion, which will remove all associated data and log them out. [Alex]

# Installation

- pip install flask
- pip install Flask-WTF
- pip install Flask-Login
- pip install Werkzeug
- pip install SQLAlchemy
- pip install PyJWT
- pip install requests

# How to use

1. Install Python 3.x on your computer (if it's not already installed). You can download Python from the official website: https://www.python.org/downloads/
2. Install the required Python packages that listed in Installation above.
3. Run the run.py script to start the program. You can do this by running the following command in your terminal or command prompt: python3 run.py
4. Follow the prompts in the program to select your options and input your information.
5. Once you have finished using the program, you can exit it by selecting the appropriate option in the menu or by pressing CTRL + C in your terminal or command prompt.

# Usage

1.Add a task to the todo list:

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

- Navigate to the 4Mail website.
- Click on the "create account" button.
- Fill in the registration form that asks for a username, email address, and password.
- Submit the form.
- The system will check the validity of the input and create the account.
- The system will redirect you to the login page.

4. Send an email:

- Navigate to the 4Mail website.
- Log in to your account.
- Click on the "send" button.
- Enter a message in the text box.
- Select one or more recipients by inputting their email addresses.
- Click on the "send" button.
- The system will check the validity of the email address(es) and send the message.

5. Log In/Log Out:

- Navigate to the 4Mail website.
- To log in, click on the "Log In" button and enter your login credentials (username and password).
- If successful, the system will redirect you to your account page.
- To log out, click on the "Log Out" button in your account/your profile in the corner of the webpage.
- The system will log you out and redirect you to the login page or 4Mail's homepage.

6. Send a chat message:

- Navigate to the 4Mail website.
- Log in to your account.
- Click on the "chat" button.
- Enter a message in the text box.
- Select one or more recipients by inputting their usernames.
- Click on the "send" button.
- The system will check the validity of the username(s) and send the message.
- The recipients will receive a notification that they have received a new chat message.
- The recipients can then log in to their accounts and click on the "chat" button to see and reply to the message(s).

7. Star Important Email:

- Log in to your 4Mail account.
- Navigate to your inbox.
- Find the email that you want to mark as important.
- Click on the star icon next to the email.
- The star will turn yellow to indicate that the email has been marked as important.
- To remove the star, simply click on the star icon again, and it will turn back to gray.

8. Delete Account:

- Navigate to the 4Mail website.
- Log in to your account.
- Click on the "account settings" page.
- Click on the "delete account" button.
- The system will prompt you to confirm the deletion of your account.
- If you confirm the deletion, the system will delete all data associated with your account and log you out.

# Contributors

- Michael Pavlik (@mikieyx) Team Lead
- Cedric Briones (@cedricJB07)
- Anh Nguyen (@AlexNguyenSJSU)
- Van Duong (@vduong421)
