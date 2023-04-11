## FUNCTIONAL REQUIREMENTS
1. Create an account (register) Cedric 
2. Log in/Log out Alex
3. Attach image/file to email  Alex
4. Password reset (When the users forget their password) Alex
5. Connect to external API  Michael
6. Send an email Cedric 
7. Delete emails Cedric
8. Send a chat to someone  Van
9. Add a task to the do list Michael
10. Cross something off the todo list Michael
11. Star important emails Van
12. Search Emails/Filter emails Van

## NONFUNCTIONAL REQUIREMENTS
1. Web app runs on Google Chrome
2. Sends emails and texts within 3 seconds

## 8 Use Cases

1. Create an account (register)
- **Summary:**
A user who has internet access creates a 4Mail account 

- **Pre-condition:** 
User has internet access

- **Trigger:** 
User clicks on create account button

- **Primary Sequence:**
  
    1. User who has internet access goes to the web site’s homepage
    2. The user clicks on the create account button
    3. The system gives out a registration form that asks for a username, email address and password
    4. User inputs a username, email address, and a password
    5. The system checks the validity of the username, email address, and password 
    6. The system creates the account
    7. The system redirects the user to the login page.

- **Alternate Sequence:** 
    1. A user’s input is invalid, so the website gives out an error message to ask the user to correct the invalid input. 
    2. A user already has an existing account, so the website will give an error message saying that the email address already has an existing account.

- **Primary Post-conditions:** 
The user is able to register for an account and can now log in to send and receive chats and emails from or to other users. / The user is not able to register and has to re-do the registration form.


2. Send an email
- **Summary:**
A user who has a 4mail account will send an email to a recipient. 

- **Pre-condition:** 
The user has a 4mail account
The user has internet access
The user is logged into their account
The user has one or more recipients in mind

- **Trigger:** 
User clicks on “compose” button

- **Primary Sequence:**
  
The user clicks on the “compose” button
The user enters a message on the text box
The user selects one or more recipients by inputting their email addresses 
The user clicks on the “send” button
The system checks the validity of the email address(es)
The system sends the message to the recipient(s)
The system shows a message indicating that the message has been sent successfully 

- **Alternate Sequence:** 
The user inputs an invalid recipient email address so the system shows an error message saying that the email address does not exist.


- **Primary Postconditions:** 
The user is able to send a message to the recipient(s) / The user is not able to send a message and has to re-enter a valid recipient email address


5. Log In/ Log Out
- **Summary:**  The users go to the website to use their registered accounts to log in their account to do operations inside their accounts like sending, receiving emails, and crossing or inserting to-do works. After that, they can log out of their account on 4Mail.

- **(Primary) Actors: **  The users (and 4Mail)

- **Pre-condition: **  The users have the Internet access, and they already register successfully the accounts for 4Mail

- **Trigger:**  The user click on the “Log In” button in order to log in their accounts and then click “Log Out” button to exit their accounts in the webpage

**Primary Sequence:** 

    1. The users navigate to the website which requires the users login to their accounts first (login page of 4Mail).
    2. The users enter their username and passwords of their account to the website (login page of 4Mail).
    3. The website authenticates the users’ right after they click the login button “Log In”. If it is successful, then the website will redirect the users to the page of their account (maybe their profile or their mail boxes).
    4. Now the users can access the features of this website, mainly sending, receiving emails, and organizing their to-do tasks.
    5. After they’re done operations in their account, the users will navigate to the “Log Out” button in their account/ their profile in the corner of the webpage.
    6. Then, the users click the “Log Out” button. 
    7. If it is successful, then 4Mail logs the users out and clears their current session data, and redirects them to the login page or the 4Mail’s homepage. 
    8. Now the users cannot access all of the features of this website unless they login their accounts again!

**Primary Postconditions:** 

    1. After logging in successfully, 4Mail stores the users’ login information securely. Furthermore, after logging out successfully, 4Mail clears the users’ current session data, and redirects them to the login page or the website’s homepage.
    2. After logging in successfully or logging out successfully, the users can access or close access to all of the features of 4Mail.

**Alternate Sequence (Log In):** 

If the users enter the invalid username or password, then the website automatically displays an error message to notify the users and reminds them to input the correct ones like “Invalid username, please type the correct one!” or “Invalid password, please type the correct one!”. 

**Alternate Sequence (Log Out):** 

4Mail automatically logs the user out if the user's session in this web page times out due to inactivity for a long time like 30 minutes or 1 hour.


6. Password Reset (When the users forget their password)
**Summary:**  When the users forget their password during logging in or just not remember it, they can go to the 4Mail signing in page and then reset their account’s password.

**(Primary) Actors:**  The users (and 4Mail).

**Pre-condition:**  The users have Internet access, and they already register successfully the accounts for 4Mail.

**Trigger:**  The users click on the “Forgot password?” button in order to type their email address to let 4Mail send the reset password link.

**Primary Sequence:**

    1. The users click the button “Forgot Password?” below the ‘Log In’ button. 
    2. The users input their email address associated with their account and click the ‘Reset via Email’ button, then 4Mail immediately verifies the users’ email address and sends a password reset link to the users’ email.
    3. The users click on the password reset link in their associated email address, then 4Mail redirects them to the password reset website.
    4. The users input the new password which meets 4Mail's password requirements like required numbers of lowercase, uppercase letters, integers, and special characters. Then they click the ‘Confirm’ button to confirm their new passwords.
    5. After successful password requirements verification of 4Mail, it automatically updates the new password for the users’ account.
    6. After step 5, 4Mail automatically redirects the users to their account page like the profile section to let them access all of the features of their accounts like receiving and sending the email, or organizing their to-do tasks in their account.

**Primary Postconditions:** 

    1. After password requirements verification successfully, the 4Mail website stores the users’ new password securely.
    2. After resetting the password successfully, the users can access their account and use all of the 4Mail’s features like receiving and sending the email, or organizing their to-do tasks with their new password.

**Alternate Sequence 1: Input Wrong Email Address:** 

    1. If the users type the invalid email address, 4Mail automatically displays the error message like ‘Invalid Email Address, please type other email address!’, then let them type again.

**Alternate Sequence 2: Enter the Password which Doesn’t meet the password requirements of 4 Mail:**

    1. If the users enter a Password which Doesn’t meet the password requirements of the 4Mail website, 4Mail automatically displays the error message like ‘Password DOES not meet Requirements’, then notifies them why their new one is wrong; for example, it likes “Please type 6-8 lowercase letters” when the users input less than 6 lowercase letters.


7. Send a Chat to Someone
Summary: Users can send a chat message to a recipient who is also registered on 4Mail.

Actors: The users, the recipient (and 4Mail)

Pre-condition: The users have logged in to their 4Mail account and know the recipient's username or email address.

Trigger: The user clicks on the chat icon or button to initiate a chat with the recipient.

Primary Sequence:

    1. The user navigates to the 4Mail website and logs in to their account.
    2. The user clicks on the chat icon or button, which is usually located in the navigation menu or the top bar of the webpage.
    3. The chat window opens up, and the user enters the recipient's username or email address in the "To" field.
    4. The user types the message they want to send in the message field.
    5. The user can format the message using text formatting tools such as bold, italic, or underline, and can also attach files or images if necessary.
    6. The user clicks the send button to send the message to the recipient.
    7. If successful, the message is sent to the recipient and appears in the chat window.

Post-conditions: The recipient receives the chat message and can respond to it. The chat message is saved in the chat history between the sender and the recipient.

Alternate Sequence:

    1. If the recipient is not registered on 4Mail, the user cannot send a chat message to them.
    2. If the user enters an incorrect username or email address, the chat message will not be sent to the intended recipient.
    3. If there is a connection issue or a problem with the 4Mail server, the chat message may not be delivered successfully.
    4. If the user encounters an error while typing the message, such as exceeding the character limit, the user will be prompted with an error message.

8. Star Important Emails:

Summary: Users can mark an email as "starred" to indicate that it is important or needs to be saved for later.

Actors: The users (and 4Mail)

Pre-condition: The users have logged in to their 4Mail account and have received an email.

Trigger: The user selects an email to mark as "starred".

Primary Sequence:

    1. The user navigates to their inbox and selects an email they want to mark as "starred".
    2. The user clicks on the star icon next to the email, which is usually located in the email header or preview pane.
    3. The star icon changes to indicate that the email has been marked as "starred".
    4. The user can also view all their starred emails by clicking on the "Starred" folder in their inbox or by using the search function to search for starred emails.
    5. If the user wants to remove the "starred" status from the email, they can click on the star icon again to deselect it.

Primary Post-conditions: The email is saved as "starred" and can be accessed later in the "Starred" folder. The user can easily find and retrieve important emails from the "Starred" folder.

Alternate Sequence:

    1. If the user accidentally clicks on the star icon or changes their mind, they can click on the star icon again to remove the "starred" status from the email.
    2. If there is a connection issue or a problem with the 4Mail server, the email may not be marked as "starred" successfully.
    3. If the user encounters an error while marking the email as "starred", such as the
    4. The system displays the matching emails based on the search criteria or filter options.
    5. The user can select the email to view its content.

Post-conditions: The matching emails are displayed, and the user can view their content.

Alternate Sequence: If no matching emails are found, the system displays a message to the user informing them of the lack of results.
