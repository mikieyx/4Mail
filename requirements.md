## Functional Requirements

1. Create an account (register) [Cedric]
2. Log in/Log out [Alex]
3. Delete User Account [Alex]
4. Password reset [Alex]
5. Connect to external News Articles API [Michael]
6. Send an email [Cedric]
7. Delete emails [Cedric]
8. Add a task to the do list [Michael]
9. Cross something off the todo list [Michael]
10. Send a message to a chat room [Van]
11. Receive a message from chat room [Van]
12. Leave the chat room [Van]

## Non Functional Requirements

1. Web app runs on chrome
2. Each web page loads within 5 seconds

## Use Cases

#1. Add a task to the todo list

- **Summary:** The user creates adds a task to his/her todo list

- **Precondition:** The user has logged in, on the todo list page

- **Trigger:** The user clicks the add task button

- **Primary Sequence:**

  1. The user writes the name of the task to be completed
  2. The user writes any details/notes about the task (This can be optional)
  3. The user writes the date that the task should be completed
  4. The user clicks create button

- **Primary Post-conditions:** The task is added to the todo list, the task is added to the database as well

- **Alternative Sequence:**

  1. The task name and/or date are blank
  2. The system prompts the user to fill in the blank

#2. Connect to external News Articles API

- **Summary** The user can access news articles as 4mail uses an API to gather articles

- **Precondition:** The user has logged in and the system has already registered an api key with the provider

- **Trigger:** The use clicks on the news page

- **Primary Sequence:**

  1. The systems makes a request to the media stack api's endpoint for general articles
  2. The page loads as the backend communicates with API
  3. The page opens and the user can see several different news articles

- **Primary Post-conditions:** The user can see and click on multiple news articles

#3. Create an account (register)

- **Summary:** A user who has internet access creates a 4Mail account

- **Pre-condition:** User has internet access

- **Trigger:** User clicks on create account button

- **Primary Sequence:**

  1. The system gives out a registration form that asks for a username, email address and password.
  2. User inputs a username, email address, and a password.
  3. The system checks the validity of the username, email address, and password.
  4. The system creates the account.
  5. The system redirects the user to the log in page.

- **Alternate Sequence:**

  4. a: A user’s input is invalid, so the website gives out an error message to ask the user to correct the invalid input.
  5. b: A user already has an existing account, so the website will give an error message saying that the email address already has an existing account.

- **Primary Post-conditions:** The user is able to register for an account and can now log in to send and receive chats and emails from or to other users. / The user is not able to register and has to re-do the registration form.

#4. Send an email

- **Summary:** A user who has a 4mail account will send an email to a recipient.

- **Pre-condition:**

  1. The user has a 4mail account
  2. The user has internet access
  3. The user is logged into their account
  4. The user has one or more recipients in mind

- **Trigger:** User clicks on “compose” button

- **Primary Sequence:**

  1. The user selects a recipient by inputting their email addresses
  2. The user writes the subject and then writes the message on the text box
  3. The user clicks on the “send” button
  4. The system checks the validity of the email address(es)
  5. The system sends the message to the recipient(s)
  6. The system shows a message indicating that the message has been sent successfully

- **Alternate Sequence:**

  5. a: The user inputs an invalid recipient email address so the system shows an error message saying that the email address does not exist.

- **Primary Post-conditions:** The user is able to send a message to the recipient / The user is not able to send a message and has to re-enter a valid recipient email address

#5. Log In/ Log Out

- **Summary:** The users go to the website to use their registered accounts to log in their account to do operations inside their accounts like sending, receiving emails, and crossing or inserting to-do works. After that, they can log out of their account on 4Mail.

- **Pre-condition:** The users have the Internet access, and they already register successfully the accounts for 4Mail

- **Trigger:** The user click on the “Log In” button in order to log in their accounts and then click “Log Out” button to exit their accounts in the webpage

- **Primary Sequence:**

  1. The users navigate to the website which requires the users login to their accounts first (login page of 4Mail).
  2. The users enter their username and passwords of their account to the website (login page of 4Mail), and then click 'Log In'.
  3. If it is successful in logging in, then the website will redirect the users to the page of their account (maybe their profile or their mail boxes).
  4. Then if the users want to log out, they will navigate to the “Log Out” button to click the “Log Out” button in their account/their profile in the corner of the webpage.
  5. If it is successful in logging out, 4Mail will log the users out and redirects them to the login page or 4Mail's homepage.

- **Primary Post-conditions:**

  1. After logging in successfully, 4Mail stores the users’ login information securely.
  2. After logging out successfully, 4Mail clears the users’ current session data, and redirects them to the login page or the website’s homepage.
  3. After logging in successfully or logging out successfully, the users can access or close all the features of the website 4Mail, mainly sending, receiving emails, and organizing their to-do tasks.

- **Alternate Sequence:**

  1. Log In: If the users enter the invalid username or password, then the website automatically displays an error message to notify the users and reminds them to input the correct ones like “Invalid username, please type the correct one!” or “Invalid password, please type the correct one!”.
  2. Log Out: 4Mail automatically logs the user out if the user's session in this web page times out due to inactivity for a long time like 30 minutes or 1 hour.

#6. Password Reset (When the users forget their password)

- **Summary:** When the users forget their password during logging in or just not remember it, they can go to the 4Mail signing in page and then reset their account’s password.

- **Pre-condition:** The users have Internet access, and they already register successfully the accounts for 4Mail.

- **Primary Sequence:**

  1. The users click the button “Forgot Password?” below the ‘Log In’ button.
  2. The users input their email address associated with their account and click the ‘Reset via Email’ button, then 4Mail sends a password reset link to the users’ email.
  3. If it is successful in receiving password reset link email, The users click on the password reset link in their associated email address, then it redirects them to the password reset website of 4Mail.
  4. The users input the new password which meets 4Mail's password requirements like the required numbers of lowercase, uppercase letters, integers, and special characters. Then they click the ‘Confirm’ button to confirm their new passwords.
  5. If it is successful in checking the new password, 4Mail automatically updates the new password for the users’ account and then redirects them to their account webpage.

- **Primary Post-conditions:**

  1. After password requirements verification successfully, the 4Mail website stores the users’ new password securely.
  2. After resetting the password successfully, the users can access their account and use all of the 4Mail’s features like receiving and sending the email, or organizing their to-do tasks with their new password.

- **Alternate Sequence:**

  1. Input Wrong Email Address: If the users type the invalid email address, then 4Mail displays the error message like ‘Invalid Email Address, please type other email address!’, and let them type again.
  2. Enter the Password which Doesn’t meet the password requirements of 4 Mail: If the users enter a Password which Doesn’t meet the password requirements of the 4Mail website, it displays the error message like ‘Password DOES not meet Requirements’, then notifies them why their new one is wrong; for example, it likes “Please type 6-8 lowercase letters” when the users input less than 6 lowercase letters.

#7. Send a Message to a Chat Room

- **Summary:** Users can send a chat message to a recipient who is also registered on 4Mail.

- **Actors:** The users, the chat room members (and 4Mail)

- **Pre-condition:** The users have Internet access and have successfully logged in to their account on 4Mail, and they have joined a chat room.

- **Primary Sequence:**

  1. The user navigates to the 4Mail website and logs in to their account.
  2. The user clicks on the "Join a Room" button.
  3. The user enters their name and creates a new chat room or joins an existing one.
  4. The chat room window opens up, and the user types the message they want to send in the message field.
  5. The user can format the message using text formatting tools such as bold, italic, or underline, and can also attach files or images if necessary.
  6. The user clicks the send button to send the message to the chat room.
  7. If successful, the message is sent to the chat room and appears in the chat window.

- **Post-conditions:** The message is sent to the chat room, and all members in the chat room can see the message and respond to it.

- **Alternate Sequence:**

  8.  If the user encounters an error while typing the message, such as exceeding the character limit, the user will be prompted with an error message.
  9.  If there is a connection issue or a problem with the 4Mail server, the chat message may not be delivered successfully.prompted with an error message.

#8. Receive a Chat from Chat Room

- **Summary:** Users can receive a chat message from a chat room after joining it.

- **Actors:** The user, other users in the chat room (and 4Mail)

- **Pre-condition:** The user has Internet access and has successfully logged in to their 4Mail account. The user has joined the chat room.

- **Primary Sequence:**

  1. The user logs in to their 4Mail account.
  2. The user clicks on the chat icon or button, which is usually located in the navigation menu or the top bar.
  3. The user clicks on the "Join a Room" button.
  4. The user The user enters their name and selects the chat room they want to join
  5. The user clicks on the "Join" button to join existing room.
  6. The user sees the chat messages from other users in the chat room and responds to them by typing a reply in the message field.
  7. The user clicks the send button to send the reply to the chat room.
  8. If successful, the reply is sent to the chat room and appears in the chat window.

**Post-conditions:** Other users in the chat room receive the reply message and can respond to it. The chat message and reply are saved in the chat history of the chat room.

- **Alternate Sequence:**

  9. If the user encounters an error while joining the chat room or sending the reply message, such as exceeding the character limit, the user will be prompted with an error message.
  10. If there is a connection issue or a problem with the 4Mail server, the chat message may not be delivered successfully.
