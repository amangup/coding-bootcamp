# Assignments

There is one assignment, in which we are going to modify the quiz app and make it more fully featured. Add the following features to the webapp.

- Make available quizzes on multiple subjects.
  - Whenever someone adds a question, they can also type in a **subject** the question is about. 
  - When an user comes to the home page, they should first be asked the subject they want to take the quiz on (from the list of subjects we have questions on - this list will be dynamically generated), and then they should be asked the questions belonging only to that subject.
- Create a leaderboard.
  - Whenever someone submits a quiz, store the score in the DB. 
  - Using this, create a page which shows the top 5 scorers in each subject (the **leaderboard**). 
  - After any new user submits the quiz answers, along with the score and right/wrong answers, show them _their position_ in the leaderboard for that subject.
- Allow quiz creators to update or delete questions.
  - Add a question update page which lists all the questions (maybe only the question text only along with the subject), with update or delete buttons alongside each question.
  - When someone clicks on delete, delete that question and show a confirmation to the user.
  - When someone clicks on update, show a form like the add question page (with the entries already filled with the question details), and allow the user to update the submit the form.

Note that I've not added any details if you need to learn something new to accomplish this (for example, querying all questions with a specific subject, or changing an existing row in the DB) - you need to figure out the unknowns yourself and use the web to get answers.