# Slack App - User stories

## Login Improvements

**[FEATURE] - As an admin user, I would like to login into the admin panel to keep private data from the outside**

**Scenario 1 - User logs into the application.**

- Given an admin user is on the login page, When the user fills the fields with their credentials And clicks the "Login" button, the user gets redirected.

**Scenario 2 - User can not access.**

- Given an admin user is in the log in the form of the web app, When the user fills the form with invalid credentials And clicks the "Login" button, the web app pops up an error message that says "Invalid credentials."

**[FEATURE] - As an admin user, I would like to reset my password if I forget it, To enter my admin panel.**

**Scenario 1 - User requests password reset**

- Given an admin user is on the login page, When the user clicks on “Forgot my password,” the user is redirected to the “Reset password” page and enters its email; the user receives an email.

**Scenario 2 - User resets its password.**

- Given scenario 1, When the user clicks on “Reset my password” from the email, the user gets redirected to “Reset password” and enters a new password. The user gets redirected to the login page.

**[CHORE] - The current login logic is not safe enough.**

**[CHORE] - Change the login form’s current design and colors.**

## Server improvements

**[CHORE] - Web Serverless configuration**

**Tasks:**

- Create AWS Lambda function

- Create a Serverless config

**[CHORE] - Deployment methods**

**Tasks:**

- Create environment files

- Crate commands send the changes and update the Lambda.

**[CHORE] - Check why the admin panel stops working**

**[CHORE] - Put SSL certificate in the server slack-submission-checklist**

## Dashboard improvements

**[FEATURE] - As an admin user, I would like to see the app metrics to view my measures quickly.**

**Scenario 1 - User enters into the admin panel.**

- Given the user logs in, the first thing the user sees is the metrics.

**Tasks:**

- Metrics are the following:

- Total users

- Total users using the slack app

- Total points assigned

**[FEATURE] - As an admin user, I would like to see the most valuable players on the dashboard to see their progress**

**Scenario 1 - User enters into the admin panel.**

- Given the user logs in, the first thing the user sees is the MVP list.

**[FEATURE] - As an admin user, I would like to see a preview of the leaderboard to check the progress of the entire team**

**Scenario 1 - User goes to the “Users” section.**

- Given the user clicks on “Users,” the user sees a user list.

**Tasks:**

- The list has to have:

- Name

- Level

- Total points

- Action buttons

**[FEATURE] - As an admin user, I would like to post the leaderboard to share the entire team’s progress.**

**Scenario 1 - User posts the leaderboard**

- Given the user clicks on “User”, the user sees the “Post Leaderboard” button and clicks on it, then a pop up appears asking about post the leaderboard to the slack channel if the user clicks “yes” then post the leaderboard.

- NOTE: Talk about user photos.

**[FEATURE] - As an admin user, I would like to see the assignations to check if they are valid or not.**

**Scenario 1 - User goes to the “Timeline” section.**

- Given the user clicks on “Timeline,” the user sees the assignation list.

**Scenario - User deletes an assignation.**

- Given the user clicks on an assignation delete button, the user removes the assignation.

**Tasks:**

- The list has to have:

- The user that creates the assignation

- The user that receives the points

- Reason

- Date

**[FEATURE] - As an admin user, I would like to have the reports In one section to check them faster**

**[CHORE] - Change the dashboard design and colors**

## Leaderboard improvements

**[FEATURE] - As an admin user, I would like to change the leaderboard messages to reach my specific workers.**

**[CHORE] - Change the dashboard design**

**[FEATURE] - Change the leaderboard form design and colors**

## Slack integration improvements

**[FEATURE] - As a slack user, I would like to know my current points and levels to know my progress**

**Scenario 1 - User gets their information.**

- Given the user types “player” on the slack channel, then their information appears.

**Tasks:**

- The information has to be:

- Level

- Total points

- Points to assign

**[FEATURE] - As a slack user, I would like to assign points to my partners to recognize their effort.**

**Scenario 1 - User assigns a point.**

- Given the user types “recognize” on the slack channel, then a form appears, and the user fulfills the fields and assigns a point, and the assignation appears on the slack channel.

**Scenario 2 - User can not assign a point.**

- Given the user types “recognize” on the slack channel, then a form appears.

- The user can not assign a point if:

- There are no users to assign.

- There is no category.

- The reason is blank.

**[FEATURE] - As a slack user, I would like to remove my last assignment if I commit a mistake.**

**Scenario - User undo his last point.**

- Given the user is assigned a point and the user types “undo” in the slack channel, the assignment disappears.

**[FEATURE] - As a slack user, I would like a new way to create a reminder to know that I'm making a new reminder.**

**Scenario 1 - User creates reminders.**

- Given the user types “reminder” and the user has 0 points to assign, then a form appears, and the user fulfills the information as an assignment.

**[FEATURE] - As a slack user, I would like to put emojis on my assignment to make it more joyful.**

**Scenario 1 - User creates an assignation.**

- Given the user types “recognize [reason]”, the form appears with the reason already written.

**[FEATURE] - As a slack user, I would like that the bot responds to my personal messages slack-submission-checklist**

**Tasks:**

- For every user message, the bot must respond with a help message.

**[FEATURE] - As a slack user, I would like to know how the commands work slack-submission-checklist**

**Tasks:**

- For every command on slack, there must have a “help” parameter.

- Workplace settings features

**[FEATURE] - As an admin user, I would like to change the categories to decide the points I want to measure.**

**Scenario 1 - User goes to categories settings.**

- Given the user clicks on “Settings”, a categories list appears.

**Scenario 2 - User changes the categories.**

- Given scenario 1, the user clicks on a category and changes the input field.

**[ FEATURE ] - As an admin user, I would like to write the levels and the points that the user will gain to make my workplace own.**

**Scenario 1 - User goes to level settings.**

- Given the user clicks on “Settings”, the level list appears.

**Scenario 2 - User changes the levels.**

- Given scenario 1, the user clicks on a level and changes the input field.

**[FEATURE] - As an admin user, I would like to change the head, standard, and admin assignation system to choose if every user can only assign 'x' points**

**Tasks:**

- Needs to configure the user type.

