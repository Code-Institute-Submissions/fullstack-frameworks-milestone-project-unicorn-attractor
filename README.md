# Full Stack Frameworks Milestone Project - Unicorn Attractor App

![UA](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/ua.PNG)

The unicorn attractor is a modern startup venture.
The business model for this app centers loosely around the idea of an online, open source community contributing capital and ideas to its development. 
The unicorn attractor offers software development services and bug fixes for free, but a small fee from any user requesting an additional feature on the site. 
The applications primary means of collecting user information is in the form of issue/work tickets, not too dissimilar to what you might find in a modern CRM. 
Each ticket displays one of three different status'; assigned, in progress or completed. 
Issues or tickets are logged to two different categories; bugs/defects in the application which will be fixed for free, and feature additions which will only be implemented for a chargeable fee. 

The application facilitates the prioritisation of different tasks for the administrator, by implementing a mechanism for the user to 'up-vote' both bug fixes and feature additions. 
Upvoting bug fixes does not cost any money, but the addition of a new feature to the site, which requires a certain number of upvotes to be implemented, requires a small fee to cover labour costs. 
In return, the site administrator will pledge to spend a minimum amount of time working on the most popular voted highest-paid feature addition request. 

 
[![Build Status](https://travis-ci.org/bransfieldjack/fullstack-frameworks-milestone-project-unicorn-attractor.svg?branch=master)](https://travis-ci.org/bransfieldjack/fullstack-frameworks-milestone-project-unicorn-attractor)

 
## UX
 
This app is targeted towards the open source developer community. It is meant as a means for people to come together in an online community to discuss and share their ideas. As a start-up company project, the intention is to allow the user to have an input into the design of the web app, by allowing the facility for features requests to be voted upon/developed. 
###	User Stories:
-	As an open source developer, I am looking for a place to collaborate and share my ideas in relation to software development. 
-	My aim is to be able to learn from others and develop my skills to become a better developer. 
-	I need to be able to login to an app where I can use a commenting system to discuss features and bugs with other developers. 

### Wireframes: 

Landing Page:
![Landing Page](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/unicorn-attractor/github/ua_landing_page.PNG)

Login Page:
![Login Page](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/unicorn-attractor/github/ua_login_page.PNG)

Landing Page After Login:
![Landing Page After Login](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/unicorn-attractor/github/ua_landing_page_after_login.PNG)

Registration Page:
![Registration Page](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/unicorn-attractor/github/ua_registration_page.PNG)

Tickets Page:
![Tickets Page](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/unicorn-attractor/github/ua_tickets_page.PNG)

Add Bugs Page:
![Add Bugs](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/unicorn-attractor/github/ua_add_bug_page.PNG)

Add Features Page:
![Add Features](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/unicorn-attractor/github/ua_add_feature_page.PNG)

Bugs Page:
![Bugs Page](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/unicorn-attractor/github/ua_bugs_page.PNG)

Features Page:
![Features Page](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/unicorn-attractor/github/ua_features_page.PNG)

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

Installed django-bootstrap3.

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
- Django REST framework tutorial: ![Pretty Printed] https://www.youtube.com/watch?v=263xt_4mBNc
- Django REST framework with Chart.js tutorial: ![CodingEntrepreneurs] https://www.youtube.com/watch?v=B4Vmm3yZPgc
- Chart.js: https://www.chartjs.org/