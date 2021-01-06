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
* 




