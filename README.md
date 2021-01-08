# The Malt Mention

![iamrespimg](https://github.com/pbtrad/ms3-mock3/blob/master/static/images/amirespimgms3.png)

Welcome to The Malt Mention, if you like your whiskey and want to consort with like minded whiskey critics, leave reviews of your best and worst whiskey experiences and become involved in a community of whiskey lovers.


## Contents:
<br>

* UX
  * Project Goals
  * Target User Goals
  * Site Owner Goals
  * User Stories
  * User Requirements and Expectations
* Design
  * Color
  * Layout
  * Images
* Wireframes
  * Website Layout
  * Account Creation Flowchart
  * Database Design
* Features
  * Current Features
  * Features yet to be implemented
* Technologies Used
* Planning and Testing
* Bugs
* Deployment
  * Heroku Deployment
  * Run project locally
* Credits and References

## User Experience:

### Project Goals:

The goal of this website is to bring about a community of whiskey lovers, where they can share experiences of whiskey they enjoy, or preferably, whiskey they hate!  Users who access the website will be able to create a profile and personalise that profile.  This website is only aimed at those who are of a suitable age to consume alcohol.

### Target User Goals:

* To be able to read whiskey reviews.
* To be able to create an account and post their own reviews.
* To join a community of like-minded avid fans of whiskey.
* To be able to use the website on all device sizes, from desktop to mobile.

### Site Owner Goals:

* Generate increased interest in all types of whiskeys.
* Collect user information for data analysis.
* Create a personal and fun community.

### User Stories:

Christine says: "I would like to find where whiskeys are reviewed by regular whiskey drinkers, without all the marketing promotions."

Conor says: "I am an avid whiskey fan and I like to try and review whiskeys, I'm looking for a website to post my opinions."

Tiarnan says: "I am looking for a tool that will not only work on my desktop computer but also on my phone for when I'm out and about.

### User Requirements and Expectations:

**Requirements**:

* Interact with a website that is visually appealing.
* Be able to navigate the website with ease.
* Find information on various whiskeys.
* Information laid out in a clear and effective manner.
* Leave reviews of whiskeys.

**Expectations**:

* The website is secure and protects the users information.
* The users can interact with the elements visible on the page.
* The website loads with sufficient speed.
* The website is responsively designed to work on desktop, tablet and mobile.
* The users feel informed and satisfied with the overall website experience.

## Design:

**Colors**:

The colors used are from a "whiskey" palette, a green (#94A356) for the navbar, and warm tones in gradient (#ee5a6f, #f29263) for profile container and accordion.

**Layout**:

The website is a community blog, with users posts publicly displayed, so posts are in blog style containers, with all relevent information, post authors username, date and time a review was created. The navbar is bootstrap and reponsive across all device sizes.
The profile page has a container positioned in the center of the page, with all relevent profile information - username, location, whiskey of choice.
All forms are bootstrap forms for responsive design.

**Images**:

Images used are of the inside of whiskey distilleries and give a warm homely feel, and welcoming to new users.

## Wireframes/Flowcharts:

Wireframes can be found here

Account creation flowchart can be found here

**Database Design**:

Using the NoSQL database MongoDB, I created the following collections.

Users collection:

| Title        | Data Type|
| ------------- |:-------------:|
| id:      | ObjectId |
| username      | string      |
| password | binary_hashed_string      |
| user_country | string |
| user_whiskey | string |

Posts collection:

| Title        | Data Type|
| ------------- |:-------------:|
| id:      | ObjectId |
| post_title      | string      |
| post_author | string      |
| post_content | string |
| date_posted | string |

## Features:

**Current Features**:

* Simple, clear and responsive navigation throughout website.
* Register account form, sign-in and sign-out functionality.
* Personalised profile page where users can see their own post history.
* Users can leave reviews, delete their reviews and read reviews from other website users.

**Features yet to be implemented**:

* A direct messaging service between users.
* A live chatroom using a new collection in the websites database.
* The addition of a whiskey API so users can use readily made data.
* Email authentication to provide extra security.
* Extra personalisation of profile page including avatar options.

## Technologies Used:

**Languages**:

* [HTML](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

**Tools and Libraries**:

* [jQuery](https://jquery.com/)
* [Git](https://git-scm.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Font-Awesome](https://fontawesome.com/)
* [MongoDB Atlas](https://www.mongodb.com/)
* [PyMongo](https://pypi.org/project/pymongo/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

## Planning and Testing:

**Register account**:

* **Plan**: I need to implement a form for account registration where users can perform actions on the website, and where these actions manipulate or create records within the MongoDB collections.
 
* **Implementation**: The session package was required to handle the request where usernames are checked for duplicates in the database, and if there are any typos are present on form. Werkzeug is used for password hashing for basic security.  The data posted on registration form is passed into the users collection in MongoDB.

* **Test**: To test the registration form I created temporary accounts and checked that the data was passed and stored in the database.

* **Result**: Test passed as data sent to database successfully, with user signed into session and passwords encrypted.

**Log in to Account**:

* **Plan**: I needed to build a page with a functioning log in form, so users can gain access to the features of the website.

* **Implementation**: The code checks the information from the log in form request and matches the information stored in the users database.  When matched the session is connected with the user. Flash messages are triggered whether log in is successful or not.

* **Test**: I created a several test accounts and attempted to log in.

* **Result**: Test passed, session was made and log in successful on every attempt.

**Log out of Account**:

* **Plan**: I needed to create a sign out feature.

* **Implementation**: Created route and method for logging out of session.

* **Test**: Using previously created accounts and attempted to log out.

* **Result**: Test passed, session cleared.

**Create Review**:

* **Plan**: I needed to build a page where users can create and post their own reviews and the post data passed to the database.

* **Implementation**: Created a form for text input and set up dictionary json with four sets of data- post-title, post_author, post_content and date_posted so to use insert_one pymongo command. Datetime imported for date_posted data. Flash message on successful post and redirect to home page.

* **Test**: Using test accounts I created several posts.

* **Result**: After submitting review, post appears on home page where it should and data successfully passed to post collection in MonogDB. Test successful.

**Edit Review**:

* **Plan**: I needed to provide the option for users to edit and update their own posts.

* **Implementation**: Created edit post functionality with proper route and methods.  The data to be passed to collection with .update. Flash message triggered on successful edit.

* **Test**: After creating and posting a review from a test account, I attempted to update it.

* **Result**: Post successfully edited and data updated in MongoDB collection.

**Delete Review**: 

* **Plan**: I needed to provide the option for user to delete reviews posted.

* **Implementation**: Created functionality for deletion and .remove command to also delete the corresponding data from MongoDB collection. Flash message triggered to inform of successful deletion.

* **Test**: After creating and posting a review with test account, I deleted it with created delete button. 

* **Result**: Post successfully deleted from review page and corresponding data deleted from MonogDB collection.

**Pop Up Modal**:

* **Plan**: I wanted to create an age disclaimer and small introduction to website on initial load of the page for new users.

* **Implementation**: I created a Bootstrap Modal with JavaScript to pop up on new user session using sessionStorage in JavaScript.

* **Test**: Loaded website from cleared cache in browser to check for modal.

* **Result**: Modal pops up successfully when new user sees the website.

**Front End Design**:

For the front end part of the websites design I planned on using bootstrap wherever possible in order to write less CSS and concentrate on the CRUD end of the project, without having to worry too much about responsiveness. This can be seen throughout the HTML.
I tested the responsiveness of the website using all device sizes and browsers and encountered no major issues.

## Bugs:

This being my first venture into programming with python most bugs I encountered were to do with proper syntax, indentation, and case-sensitive issues.
I used VSCode to build the website so with a python linting and debugging extension I was notified of incorrect syntax and errors with proper python layout.

When updating requirements.txt all packages within virtual environment were added causing problems with heroku deployment, I had to delete these unused often out of date packages for successful heroku build.

## Deployment:

The Malt Mention was developed on Visual Studio Code with WSL: Ubuntu and using git and GitHub to host the repository.

**Cloning The Malt Mention from GitHub:

Install the following:

* Git
* PIP
* Python3

Create an account at [MongoDB](https://www.mongodb.com/3) to construct database.

* 1: Clone the Malt Mention depository using Git by typing the following command into the terminal.

```
git clone https://github.com/pbtrad/ms3-mock3
```

* 2: Go to this folder in your terminal.
* 3: Enter the following command into your terminal.

```
python3 -m .venv venv
```

* 4: Intialize the environment by enetering the following command.

```
.venv\bin\activate
```

* 5: Install the requirements and dependancies from the requirements.txt file.

```
pip3 -r requirements.txt
```

* 6: In an IDE create file where SECRET_KEY and MONGO_URI can be stored, then follow the schema in the schema file.
* 7: Run the application by entering.

```
flask run
```

or

```
python3 app.py
```

**Deploying the website to Heroku**:

* 1: Create a requirements.txt file by entering the following command.

```
pip3 freeze > requirements.txt
```

* 2: Create a Procfile.

```
echo web: python app.py > Procfile
```

* 3: Push files to your repository.
* 4: On Heroku dashboard create a new app.
* 5: Select deployment method and select GitHub.
* 6: On the dashboard set config variables:

| Key  | Value |
| ------------- | ------------- |
| IP  | 0.0.0.0  |
| PORT  | 5000  |
| MONGO_URI | mongodb+srv://:@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority  |
| SECRET_KEY | "your_secret-key" |

* 7: Select the deploy button on the Heroku dashboard.
* 8: Your site is deployed by Heroku.

## Credits:

* [Corey Schafer Flask Tutorial](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) for design ideas for home page.
* [bbbootstrap](https://bbbootstrap.com) for profile page ideas.
* Forms are from [getbootstrap.com](https://getbootstrap.com/) with some required tweeking for the website.
* The humourous whiskey reviews are from [https://www.thespiritsbusiness.com/](https://www.thespiritsbusiness.com/2017/04/top-10-unusual-scotch-whisky-reviews/)

## Acknowledgements:
* Code Institute Slack channels and those who contributed to them.
* Adegbenga Adeye for mentoring support throughout the project.


