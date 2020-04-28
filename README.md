[![Build Status](https://travis-ci.org/ElaineArchbold/fullstack-milestone-project.svg?branch=master)](https://travis-ci.org/ElaineArchbold/fullstack-milestone-project)
## Elaine Archbold Full Stack Milestone Project

For this project, I created a website for Alio Prints which is a graphic design business I started a few years ago. I wanted the look of the site to be clean and simple, and make for a smooth online shopping experience.

## UX
My goal in the design was to create a very user friendly site where users could view and order their own custom print.

I kept the Navbar and footer simple, and the colour theme is subtle. 

*User A – As a new user, I want to be able to view all available prints and decide upon which one I prefer. I can select 'Gallery' (https://alio-prints.herokuapp.com/products/gallery) in the navigation menu to display a lightbox of all available designs. Each header is linked to the product page for that category.
*User B – As a user looking to order a print, I want to be able to do this easily.  I can select 'Shop' (https://alio-prints.herokuapp.com/products/shop) in the navigation menu to display the products availble. These are arranged by category or I can search all products by selecting 'All Products'. From here, I can add items to my cart. Once I have done this, I can either login or register to enable the checkout function.
*User C - As a user looking for a specific product, I can use the search bar in the navigation menu. The search function is based on the product description so I have many key words I can use to search. 
*User D - As an esisting user, I want to check what items I have in my cart from a previous visit to the site. I can select 'Cart' (https://alio-prints.herokuapp.com/products/cart) in the navigation menu to display the items stored in my cart.

The site can be viewed through Heroku: (https://alio-prints.herokuapp.com)

I created Wireframes of how I wanted the site to look before starting. See below:



## Features
### Existing Features
The HOME page features a scrolling parallax effect, with three sections. Section one is an introductory paragraph from Mrs Hinch, taken (and modified for the project) from her book introduction. Section two is a banner with quicklinks to each of the pages on the site. Section three contains iframes for YouTube and Instagram. The Instagram feed could be added here, with login details from Mrs Hinch.

The TO-DO page uses a MongoDB database to allow the user to add, edit, update and remove items from their to-do list. They can use this list directly on the website and edit it as they go. 

The SHOPPING page has a list of all of the most popular Mrs Hinch must have items, which are stored for the user once clicked using javascript. There is also a section at the end of the page where users can add to the list, storing the added items in a MongoDB database. There is a print button on the page should the user need to print the list.

The TIPS page has a video gallery of the most popular Mrs Hinch YouTube videos. I have also created and wired up a search bar which brings users directly the Mrs Hinch YouTube channel. I used Google developer tools on YouTube to find the correct code for this.

The INSPIRATION page contains images for interior design inspiration ideas. The images are divided into sections and there is a lightbox function added to improve the UX.

I used EmailJS on the contact page. When a user clicks on the email contact button in the footer, they are taken to an email contact page and the query is sent using EmailJS.

I also created a favicon in Photoshop which can be seen on the browser tab and can further be used for social media branding.

The navbar, footer and all buttons have hover states activated to change size/colour when the user hovers over them, to improve the UX.


## Technologies Used
1.	GitPod IDE
2.	HTML
3.	CSS
4.	Bootstrap (4)
5.  Django 1.11.29
6.	Photoshop
7.	Python
8.  Boto3
9.  AWS S3
10.	Jquery
11.	Stripe
12.	Google Fonts
13.	Font Awesome
14. 



## Testing
LINKS – I have tested all links. The Instagram, YouTube and Facebook links in the footer go the relevant accounts. I have set up EmailJS for the email link in the footer.

I used Google Developer Tools to check the responsiveness of the site. The navbar and footer are responsive and reduce on smaller screens. I have used media queries throughout to allow for better UX on mobile devices.

The site had been tested on Chrome, Firefox and Safari.

All HTML was checked on the W3C Mark-up Validation Service.

The CSS was checked on the W3C CSS Validation Service.

All HTML was formatted on https://freeformatter.com.

Screenshots of the responsive design can be seen here:

Tested on Travis.


## Deployment

I have set Heroku to link to GitHub, so each push to GitHub also pushes to Heroku.
I have set the IP and PORT as below, and saved the MongoDB URI details here also. I used an env.py file to save the MongoDB URI in GitPod and imported this to app.py so that the details were not on view to anyone looking at the site on GitHub.

Once the Heroku app is created with the details below, you click on ‘open app’ and you can view the site.

To run this project on your own IDE:

Download a copy of the file from GitHub at https://github.com/ElaineArchbold/DataCentricProject.git and open it up in your IDE. The following must be installed on your machine:
- dnspython
- flask
- flask-PyMongo
- pyMongo
- An account with MongoDB Atlas


## Heroku Deployment

1.	Create a requirements.txt file and a Procfile.
2.	Create a new app in Heroku.
3.	In "Settings" > "Reveal Config Vars" and set the IP to 0.0.0.0 and PORT to 5000. 
4.	IP | 0.0.0.0 and your MONGO_URI.
5.	Click Deploy.


## Credits
### Content


### Media
All of the photos used are from unsplash.com.

The YouTube videos on the Tips page are taken from the Mrs Hinch YouTube channel.

I used Photoshop to create the background image for Parallax one. I replaced the background on an image I found of ‘Mrs Hinch’. I also used Photoshop to edit all background images

### Acknowledgements
The footer and navbar were taken and amended from previous projects.

I found the scrolling parallax tutorial on: https://www.w3schools.com/howto/howto_css_parallax.asp

I found the lightbox snippet on the Inspiration page on: https://epicbootstrap.com/snippets/lightbox-gallery

I found the snippet for the gallery carousel on the Home page on: https://stackoverflow.com/questions/20007610/bootstrap-carousel-multiple-frames-at-once

