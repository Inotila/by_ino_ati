 The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

<img src="./assets/images/logo-yellow.jpg" width="320px">

To run a frontend (HTML, CSS, JavaScript only) application in Gitpod, in the terminal, type:

python3 -m http.server

To run the webpage click on this link: <a href="https://by-ino-ati.herokuapp.com/" target="_blank">by_ino_ati</a>

<img src="./assets/images/reponsive.png" width="700">

# by_ino_ati(Portfolio 4)

This project is for my final submission for my forth milestone. The aim of the project is to code and deploy a responsive website using Java Script, python+ django, HTML and CSS. 

## About by_ino_ati

Is a web application where users can view and interact with art by artist Inotila Nghaamwa(the owner of the page). 

The site owner is an artist, and would like to offer users a platform where they can view and interact with his art work. The owner would like to keep adding features to the site and updating to increase the way in which site users can engage with the content.

The users are primarily art enthusists, art collectors, and other peopler in the artist commuinity.

## Value

users can view and interact with his art work by liking and commenting on it.

In addition, the UI is easy to understand and navigate. Furthermore, the site offers the user interaction, alerting the users on wconsequence of their actions are.

## Potential features (before starting)

1. a grid view of art works
2. like content and view number of likes a post has.
3. Comment on post and view comments from other users and the amount of comments a post recieved.
4. An easy to understand UI.
5. An easy signup process to be authenticated.
6. view detials about the art work.
7. See the availabilty to purchase the art work
8. live bids.
9. Users will be able to bid on art works.
10. Share button to allow users to share posts on other social medias.
11. A booking page where site users can book artist for a commision.

## Actual Features (end product)
1. Welcome/home page -

<img src="./assets/images/homepage.png" width="700">

On this page the user is welcomed, and the tone/vibe of the game is set. From this page first-time users will be able to know that this is a game. 

In addition, the home page offers navigation buttons that are simply titled in order for them to easily understand what exactly it is that the button will do/take them to. 

2. Play page - 

<img src="./assets/images/gamepage.png" width="700">

This is where the game is played. The UI is simple and users should be able to clear identify the various elements of the page.

The page has player and master score. These two elements are the total score keeper for the game. They update after every end of turn and re-set to zero when the game has come to an end. To show the increment of the score, it numbers font becomes bold for a few seconds when whoever’s turn it is has ended. 

In addition to the player and master score, there is a current score element. This keeps the score of the roll of whoever’s turn it is and re-sets to zero when their turn has come to an end. Furthermore, the current score background also switches colors to represent bonus or a zero score. I the player rolls a 500 and above the background-color becomes white. Id the player gets a score of zero, the background-color turns red. This is to give the player positive feedback when they have a bonus score, or let them know they got a bad score/zero.

The page has dice images that show exactly what the player or the CPU got on each roll. And they are displayed on a wooden background to make the user feel like they are playing on a game board.

The page also has buttons for the game play. The roll dice button is where the player rolls for his/her turn. The keep dice button is how the play increments his/her total score, and the pass dice buttons starts the CPU/other players turn.


3. Rule page - 

<img src="./assets/images/rulepage.png" width="700">

A page that has information about the rule of the game and how it is played.

In addition, the rules page offers navigation buttons that are simply titled in order for them to easily understand what exactly it is that the button will do/take them to. 

4. About page - 

<img src="./assets/images/aboutpage.png" width="700">

A page that has information about the games developer. And clearly states that copying this game is not permitted, as it is an original game by the developer.

In addition, the about page offers navigation buttons that are simply titled in order for them to easily understand what exactly it is that the button will do/take them to. 



4. Responsive feedback -

<img src="./assets/images/feedback.png" width="700">

All the buttons on the page have a hover feature that turns them green. However, most of the responsive features are found in the play page, some of these have already been mentioned in the above text. In addition to those that have already been mentioned, there is a pop-up to indicate who's turn it is. There is also a winner popup to show that the game has ended and announces the winner. The winner announcing popup also give the user an option to play again or return home. These features make the user feel less isolated.


5. Logo - 

<img src="./assets/images/game-logo.png"  width="200">

A nice logo that also serves as a home button.

6. Footer and social media links-

<img src="./assets/images/footer.png" width="700">

A footer to keep social media links. These links are links that open in new tabs so as to not take the user away from the website.

The social media links are useful for the users because they encourage the user to get in contact with the developer on other platforms (Facebook, Instagram and YouTube).


## Future Features
1. 

## Testing


## Bugs and fixes


### Solved bugs

## Unfixed bugs

## Validator testing

Html - No errors returned from the official w3c validator

CSS - No errors returned from the official (jigsaw) validator

<img src="./assets/images/validator-one.png" width="700">

<img src="./assets/images/validator-two.png" width="700">

<img src="./assets/images/validator-three.png" width="700">

<img src="./assets/images/validator-four.png" width="700">

Accessibility - Confirmation that the colors content is easy to read and the sight is accessible  by running it through lighthouse in DevTools.

<img src="./assets/images/lighthouse.png" width="700">

Furthermore, I have ran my JavaScript file through jshint and have no major issues apart from ES6 warnings. No errors are reported in the DevTools either.

## User testing and feedback



## Deployment
This project has been deployed on heroku. The live link to project is: <a href="https://by-ino-ati.herokuapp.com/" target="_blank">by_ino_ati</a>
The steps to deploy this project are:

From the GitHub repository navigate to the settings option.

Select the Main Branch, from the source section.

And after selecting the Main Branch, provide the link to the website.


## Credits/Reference 
This work is the original work of Inotila Nghaamwa, however the following resources were used to supplement:

### Code
I used similar coding approaches to that which was used for the love maths run-through. Particularly the event listeners. Furthermore, i used the social media links from the love-running run-through and made a few small changes to it. 

### Media
All images used are the property of Inotila Nghaamwa, I created them images using adobe software. The sound clip used was downloaded on a site that offers free sound clips.

### Credits 

Content -
Text-Written by Inotila Nghaamwa.

Images - All images used are the property of Inotila Nghaamwa.
