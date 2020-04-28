[![Build Status](https://travis-ci.org/ElaineArchbold/fullstack-milestone-project.svg?branch=master)](https://travis-ci.org/ElaineArchbold/fullstack-milestone-project)

<h1 align="center">
  <a href="https://alioprints.s3-eu-west-1.amazonaws.com/media/images/full-logo.jpg" target="_blank"><img src="https://alioprints.s3-eu-west-1.amazonaws.com/media/images/full-logo.jpg" alt="Alio Prints Logo"/></a>
</h1>
<h4 align="center">
The site can be viewed through Heroku [Here](https://alio-prints.herokuapp.com)
</h4>


## Elaine Archbold Full Stack Milestone Project

For this project, I created a website for Alio Prints which is a graphic design business I started a few years ago. I wanted the look of the site to be clean and simple, and make for a smooth online shopping experience.

## UX
My goal in the design was to create a very user friendly site where users could view and order their own custom print. I kept the Navbar and footer simple, and the colour theme is subtle. 

* User A – As a new user, I want to be able to browse all available prints. 
* User B – As a new user looking to order a print, I want to be able to do this easily.  
* User C - As a new user I want to be able to seach for a specific product easily. 
* User D - As an existing user, I want to check what items I have in my cart from a previous visit to the site. 
* User E - As an employee of Alio Prints, I want to be able to login to the admin portal and update/add products. 

I created Wireframes of how I wanted the site to look before starting. See below:







## Features
### Existing Features
The [Home](https://alio-prints.herokuapp.com) page features a scrolling parallax effect, with four sections. 
- Section one is background image I created in Photoshop as a wall mock-up of some of the prints. I feel like the background image gives a good introduction to the site and the colour theme is based around this.
- Section two is a brief description about what we do with a button link to the Gallery.
- Section three is a description of the order process, with a link to the contact page.
- Section four is a carousel of a few of our best-selling prints. On large screens, this displays 4 images in a row, and a different carousel is active on smaller screens to show one image in a row. This was accomplished through media queries and JavaScript.

The [Gallery](https://alio-prints.herokuapp.com/gallery) page shows all of the prints in a lightbox, divided up by category. Each header is a link to that category's shop page.

The [Shop](https://alio-prints.herokuapp.com/products) displays a view of all products. From the dropdown in the navigation menu, you can select a category, or view all products.

The [Cart](https://alio-prints.herokuapp.com/cart) displays the items in your cart. The icon next to cart in the navbar will show the number of products in your cart once you have added them. You must be a registered user to checkout your cart. If you have not already registered or logged in, the 'checkout' button is hidden until you do so. Once you login or register, you will be able to checkout your cart. I have added a value of '1' to the cart input. The user can either just click 'Add' or enter a larger number should they wish to order more prints.

The 'Account' link on the navigation menu will allow you to either login or out and view your profile if you are a registered user, or register as a new user.  Once logged in, the link will display profile or logout options, and if not logged in, it will display a register or login option.

The 'Search' function uses the product description information to ensure that it is easier for users to find what they are looking for.

The footer links are set to those brand URLs, and the 'Contact' page uses Django forms to display messages in the terminal window.

I have added a custom 404 page with a link back to the Home page.

I also created a favicon in Photoshop which can be seen on the browser tab.

I have added a scroll to top button on all of the product pages with JavaScript for easier navigation.

All links and buttons have hover states activated to change size/colour when the user hovers over them, to improve the UX.

## Technologies Used
1.  GitPod IDE
2.  HTML
3.  CSS
4.  JavaScript
5.  jQuery
4.  Bootstrap (4)
5.  Django 1.11.29
6.  Python3
7.  AWS S3
8.  Boto3
9.  AWS S3
10. Pillow
11. Stripe
13. Font Awesome
14. Photoshop

## Testing
Using Stripe developer testing, I have tested the payment functionality with the test card number: 4242 4242 4242 4242 and this is working correctly. No errors are coming back through the Stripe dashboard.

I used Google Developer Tools to check the responsiveness of the site. The navbar and footer are responsive and reduce on smaller screens. I have used media queries throughout to allow for better UX on mobile devices.

The site had been tested on Chrome, Firefox and Safari.

The code has been tested on Travis and is passing.

I have one Django test complete in the products app. Further tests are yet to be developed.

All HTML was checked on the W3C Mark-up Validation Service.

The CSS was checked on the W3C CSS Validation Service.

All JavaScript was checked on jshint.com.

All code was formatted on https://freeformatter.com.

I have tested all links. The Instagram, YouTube and Facebook links in the footer go the relevant accounts.

The contact form has been tested and user inputs are sent to the terminal.

<h6 align="center">
 ![Desktop View1](media/images/responsive.png)
</h6>



### Client stories testing:

Most common path through the website: 
- Home > Shop > All Products > Add to Cart > Login > Checkout 
- Each of these pages points clearly to the next one with a call to action button. 

Some pages offer two possible paths in their call to action buttons: 
- From Home Section 2 > Gallery 
- From Home Section 3 > Contact Page
- From Gallery > Category Header > Product Category Shop Page


### Testing client stories

* User A – As a new user, I want to be able to view all available prints and decide upon which one I prefer. 
    - From the navigation bar on every page, I can select [Gallery](https://alio-prints.herokuapp.com/products/gallery) in the navigation menu to display a lightbox of all available designs. This shows a page with all products divided into sections. When an image is clicked, it opens up a scrolling lightbox effect. Also, each category header is linked to the shop for that category.
* User B – As a new user looking to order a print, I want to be able to do this easily.  
    - From the navigation bar on every page, I can select 'Shop' and a dropdown menu appears which displays all of the categories of available products. I can either choose a category or I can search all products by selecting [All Product](https://alio-prints.herokuapp.com/products). From here, I can add items to my cart. Once I have done this, I can either login or register to enable the checkout function.
* User C - As a user looking for a specific product, I can use the search bar in the navigation menu. 
    - From the navigation bar on every page, I can use the search function. I type in my keyword and the search returns the results and redirects me to the relevant page. The search is based on the product description so there are many keywords I can use to search. 
* User D - As an existing user, I want to check what items I have in my cart from a previous visit to the site. 
    - From the navigation bar on every page, I can select [Cart](https://alio-prints.herokuapp.com/products/cart). This will take me to the Cart page with a list of the products in my cart. There is also an icon that appears on the navigation bar to display any current items in the cart.
* User E - As an employee of Alio Prints, I want to be able to login to the admin portal and update/add products. 
    - I can do this by adding '/admin' to the end of the URL and enter my login details. From here, I can add or ammend products.


## Deployment

I have set Heroku to link to GitHub, so each push to GitHub also pushes to Heroku.
I have set the IP and PORT as below, and saved the MongoDB URI details here also. I used an env.py file to save the MongoDB URI in GitPod and imported this to app.py so that the details were not on view to anyone looking at the site on GitHub.

Once the Heroku app is created with the details below, you click on ‘open app’ and you can view the site.

To run this project on your own IDE:

Download a copy of the file from [GitHub] https://github.com/ElaineArchbold/fullstack-milestone-project and open it up in your IDE. The following must be installed on your machine:


## Heroku Deployment

1.  Create a requirements.txt file and a Procfile.
2.  Create a new app in Heroku.
3.  In "Settings" > "Reveal Config Vars" and set the IP to 0.0.0.0 and PORT to 5000. 
4.  IP | 0.0.0.0 and your MONGO_URI.
5.  Click Deploy.


COLLECT STATIC

## Credits
### Content

### Media
The background images on the homepage parallax two and three on the home page are from [Unsplash](https://unsplash.com/)

The print designs, logos and backdrop on parallax one on the home page were created by me using Photoshop/Publisher.

I used Photoshop to create the background image for Parallax one. I replaced the background on an image I found of ‘Mrs Hinch’. I also used Photoshop to edit all background images

### Acknowledgements
The footer, navbar and parallax effect were taken and amended from previous projects.

I found the lightbox snippet on the Inspiration page on: https://epicbootstrap.com/snippets/lightbox-gallery

I found the snippet for the gallery carousel on the Home page on: https://stackoverflow.com/questions/20007610/bootstrap-carousel-multiple-frames-at-once

I found the snippet for the contact form on: https://hellowebbooks.com/news/tutorial-setting-up-a-contact-form-with-django/

