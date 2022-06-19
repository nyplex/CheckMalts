<h1 align="center">CheckMalt</h1>

*This is the README file for CheckMalt web application. You will find here a bunch of information regarding the Design, the technologies used and some information regarding the code.*


CheckMalt is a fictive cocktail bar situed in London. Using their website, the clients will be able to order the drinks online. The clients also have to possiblity to book a the table directly from the application. They can have access their personnal account and see their post orders. Last but not least, checkmalt app have a feature called 'Cocktail Match', where the client who don't know what to order will have to asnwer a few questions and system will propose the perfect match with a selection of drinks depending of their taste.
The main goals of this application are for users to get information of the bar (menu, location, opening time ...), to order online, to book a table and finally to get the perfect match. 


<h1 align="center">UX</h1>
 
## User's needs


The main focus regarding the user's needs was to give the user a very simple and short way to order online. The second main focus was to have a stunning design and a layout to represent the company's culture. I wanted to application to aslso be friendly and interactive. 
 

## Website requirements
       
- Home page
- Ordering system
- checkout/payment system
- booking system
- cocktail match
- profile page
- menu page
- google login system


## Usage Scenario
       
- First-time Users

    When the user lands on the website for the first time, they will arrive on the home page and they will be welcomed by scroll-animated header. On the home page the user will be able to get the most important information about CheckMalt. From the home page, the user will be able to easily navigate through the entire application. My goal is that an user that lands on the home page for the first time coul easily and intuitivly navigate to the menu, order and match page. 
 
- Returning Users
 
    My goal for the returning users is for them to spend more time and the 'cocktail match' feature which is the bonus and original feature of this app. Also, returning user who already placed an order on the app, won't have to re-insert their details as they will be saved into the data base. My goal for the returning user was to make their journey on the app as smooth and as fast as possible. 
 
- User's Journey

    The user's journey on CheckMalt is very straighforward. There is 2 main scenarios regarding the user's journey. The first one is when an user wants to get some information about CheckMalt (check menu, get the location , check price etc...), in most cases, the users who are checking the webiste to get info will do some before going to the bar. They journey will start on home page where they will get a good idea of the bar's culture, style and ambiance from there, they can easily access the menu and price, get the location and opening time and they can also reserved a table. DUring their journey, the user should get as many information as possible. 

    The second scenario is for the user who are already in the bar and wants to orderr their drinks. Those user will generally lands on the home and from there they can with one click nivagate to the order page. On the order page, the will access the menu organised by categories and sub-categories. They can click on each item which will open a modal window. On this modal, the user will see the product's name, a description, price and they will be able to choose the quantity they want to order. The price will be updated live when the user change the quantity or size. Finally the user can add some special request and add the product to their basket. User do not need to be looged in to add product to their basket. 
    From the basket, the user can update or delete a product. When they are happy with their basket the go the checkout process. The first step to checkout will be to add the user's phone (only first-time user), add a table number (optional) and add a tips (optionnak). The second step is the actual payment. Once the payment is confirmed, user will be redirect to the confirmation page where they will get the order ID, and prep's time estimation. They will also receive an emaail and a sms.

    Once the user passed a order they can also access their profile account where they can find their previous orders and their personnal information. On the past orders page, they can see the full details of their past orders and which credit card they used to pay the order. On the account page, they can access their personnal information like their full name, email address and password. They have to possibity to update their information.  


    <h1 align="center">Design</h1>
 
## Wireframes
 
I used balsmiq to make the wireframe. 
You can find below a few screen shots of the wireframes. 

 
## Colors
 
The main colours used on the website are black, dark yellow and white. I have used those colors because I wantes to create a minilistic and contrasted look. 
These are the main colours used on the website:
 
  - light: "#F1FAEE",
  - secondary: "#A8DADC",
  - primary: "#1D3557",
  - text: "#323232",
  - Second variant: "#457B9D",
 
## Typography
 
I have used 1 font on this application, the main one is "Barlow".


<h1 align="center">Technologies</h1>

- HTML 5
- CSS 3
- TailwindCSS
- JavaScript ES6
- jQuery
- PostCSS
- Webpack 4
- GIT
- Django 
- DJango allAuth
- Heroku Postgres DB 
- Heroku 
- AWS S3 bucket 
- Twillio API
- Stripe API


<h1 align="center">Features</h1>

- FRONT-END

    On the front-end I have used JavaScript ES6, jQuery, tailwindCSS combined with webpack4. Webpack give me the possibility to split my JS code into multiples files and bundle them into 1 main JS file. Webpack will also get rid of unused code, minify my main file and remove any comment which will improve efficieny. 

    On top of jQuery, I have used 3 others librairies. The first one is intlTelInput, which allows to standardize the phone number the user will input. It gives the possiblity for the users to use international phone number. 

    The second library is validator.js which give the user real time feedback when he fillup a form. If the user make a mistake in a form, he will receive a form error immediatly without the need to submit the form. 

    The third one is GSAP which I used to animate the header on the home and menu page. 

    Finally, I have used mulitlple Ajax trhough the application (get the item modal, update item price...).

    Regarding CSS, I have used TailwindCSS combine with Webpack and PostCSS. TailwindCSS is a great css framework which really helped me to code less espiclly to implement thr dark/light mode. Webpack allows the bundle all my CSS files into 1 and minify it. PostCSS allows to automatically add the prefixer. 


- BACK-END & DATABASE

  On the back-end I have used the python framework Django. I splited my code into multiple apps. 
  
  - HOME app will render the home page and handle the booking feature. 
  - MENU app will render the menu page and fetch the data from the DB
  - ORDER app will render the order page, handle the item modal, handle the live price update, handle the order again function.
  - BASKET app will not render any views. It will only handle the basket mehtods (add items into session etc...).
  - CHECKOUT app will render the checkout page and handle the payment process, confirm the order, send sms/email confirmation.
  - MATCH app will render the match page and handle the match's form.
  - PROFILE app will render the profile page and handle user's data update, fetch user's past orders. 

  I have used mulitple python/django's librairies. The most important one is django-allauth which take care of the authentication system. It allows me to integrate google login very easily into the project. An other very important one is Twillio app which allows to send SMS to user using Twillio's API.

  Regarding the database, I have used sqlite in development POSTGRES in production which is the recommanded one for django. The postgres db has been deployed on a heroku server. Find here a link to the my database design. 


<h1 align="center">Testing</h1>

As this project is most complex project I have made so far, I have decided to spend more time on testing to avoid any bugs and make sure the application is full functional. You can find in each django app a file called tests.py. This file is a series of mini tests I wrote to test all functionality of my application and also test the code in case of any errors or wrong user's inputs. Find below how to run the test in the terminal. Most of the time I wrote the tests before coding the application and once the a feature was coded, I just run the test. 

I also used the google dev. tool to test the performance and the front-end code. 


<h1 align="center">Deployment</h1>

Flask BLog has been deployed on Heroku and AWS, click [here.](http://nyplex-flask-blog.herokuapp.com/) to check the live application.

This project use different technologies (webpack, tailwindCSS, jQuery etc..), in order to have a working version of the project on your local machine, please follow these steps using your terminal:

- Install python in your machine and node.js
- clone the git repo on your local machine (git clone https://github.com/nyplex/Flask_blog.git)
- cd into the project folder
- run "npm intall" , in order to install all the dependencies. 
- run "npm run build" in order to bundle all the files.
- run "pip3 install -r requirements.txt"
- run "python run.py"

You must have node.js & git install on your machine.

-----------------

CheckMalt has been deployed on Heroku and AWS. Heroku stored all the back-end code and AWS (S3 bucket) store all the static files (JS, CSS) and all the media. Finally the database is stored on a heroku-postgres server. 

This project use different technologies (webpack, tailwindCSS, jQuery etc..), in order to have a working version of the project on your local machine, please follow these steps using your terminal:

- Install python in your machine and node.js
- clone the git repo on your local machine (git clone https://github.com/nyplex/checkmalts)
- cd into the project folder
- run "npm intall" , in order to install all the dependencies.
- run "npm run build" in order to bundle all the files.
- run "pip3 install -r requirements.txt" or "pip install -r requirements.txt" depending on the version of python you have.
- run "python manage.py runserver" to start to development server. 
- run "python manage.py tests" to run the tests