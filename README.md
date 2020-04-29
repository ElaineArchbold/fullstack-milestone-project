[![Build Status](https://travis-ci.org/ElaineArchbold/fullstack-milestone-project.svg?branch=master)](https://travis-ci.org/ElaineArchbold/fullstack-milestone-project)

<h1 align="center">
  <a href="https://alioprints.s3-eu-west-1.amazonaws.com/media/images/full-logo.jpg" target="_blank"><img src="https://alioprints.s3-eu-west-1.amazonaws.com/media/images/full-logo.jpg" alt="Alio Prints Logo"/></a>
</h1>



## Elaine Archbold - Full Stack Frameworks with Django Milestone Project

For this project, I created a website for Alio Prints which is a graphic design business I started a few years ago. 
What I do is design A4 prints, which would be customised and framed, for all occasions. Baby prints are by far the most popular, hence why I have more products for that category.
Previously, I used Social Media to showcase my designs, and I also had a stall at a weekly craft market. 
This was a great way of showcasing the designs, but as I got busier, I needed a with a better way of taking orders from customers.
 
The designs are displayed on the site in the gallery page and shop pages, and customers can browse the designs and choose which ones they would like to order. 
They can then add the items to their cart and on the checkout form, they can add in the information they want added to their print.  
I would then customise the design and send a proof to the customer for them to sign off. Once signed off, it would be printed and framed and posted out.

## UX
My goal in the design was to create a very user friendly site where users could view the designs available and place orders easily. 
I also wanted to make it quick and easy for repeat customers to find their favourites and re-order.
I kept the Navbar and footer simple, and the colour theme is subtle. 
I wanted the look of the site to be clean and simple, and make for a smooth online shopping experience.
The backdrop image on the homepage is a mock-up of a stylish living room with my prints hanging on the wall. 
The colour theme for the site is based around this image, making for a clean and fresh feel to the site.

### Client stories
* User A – As a new user, I want to be able to browse all available prints. 
* User B – As a new user I am looking to order a print and I want to be able to do this easily.  
* User C - As an existing user, I want to be able to search for my favourite product easily to re-order.
* User D - As an existing user, I want to check what items I have in my cart from a previous visit to the site. 
* User E - As an employee of Alio Prints, I want to be able to login to the admin portal and update/add products. 

The site can be viewed [here](https://alio-prints.herokuapp.com)

I created Wireframes of how I wanted the site to look before starting. See below:

<h4 align="center">
Mobile View:
  <a href="https://alioprints.s3-eu-west-1.amazonaws.com/media/images/WireframesMobile.jpg" target="_blank"><img src="https://alioprints.s3-eu-west-1.amazonaws.com/media/images/WireframesMobile.jpg" alt="Mobile View"/></a>
</h4>

<h4 align="center">
Tablet View
  <a href="https://alioprints.s3-eu-west-1.amazonaws.com/media/images/WireframesTablet.jpg" target="_blank"><img src="https://alioprints.s3-eu-west-1.amazonaws.com/media/images/WireframesTablet.jpg" alt="Tablet View"/></a>
</h4>

<h4 align="center">
Desktop View:
  <a href="https://alioprints.s3-eu-west-1.amazonaws.com/media/images/WireframesPC.jpg" target="_blank"><img src="https://alioprints.s3-eu-west-1.amazonaws.com/media/images/WireframesPC.jpg" alt="Desktop View"/></a>
</h4>


## Features
### Existing Features
-   The [Home](https://alio-prints.herokuapp.com) page features a scrolling parallax effect, with four sections. 
    *   Section one is background image I created in Photoshop as a wall mock-up of some of the prints. I feel like the background image gives a good introduction to what the site is all about and the colour theme is based around this.
    *   Section two is a brief description about what we do with a button link to the Gallery page.
    *   Section three is a description of the order process, with a link to the Contact page.
    *   Section four is a carousel of a few of our best-selling prints. On large screens, this displays four images in a row, and a different carousel is active on smaller screens to show one image in a row. This was accomplished through media queries and JavaScript.

-   The Navbar is sticky and collapses on small screens.

-   The [Gallery](https://alio-prints.herokuapp.com/gallery) page shows all of the prints in a lightbox, divided up by category. Each header is a link to that category's shop page.

-   The [Shop](https://alio-prints.herokuapp.com/products) page displays a view of all products. From the dropdown in the navigation menu, you can select a category, or view all products. I have added a 'scroll to top' button to the shop pages for easier navigation. Each individual shop page comes from the 'product_category' page, where I used tags to iterate through each product category and create individual pages for each category. I have also added a category breadcrumb menu to the top of the shop pages for better functionality.

-   The [Cart](https://alio-prints.herokuapp.com/cart) page displays the items in your cart. The icon next to cart in the navbar will show the number of products in your cart once you have added them. You must be a registered user to checkout your cart. If you have not already registered or logged in, the 'checkout' button is hidden until you do so. Once you login or register, you will be able to checkout your cart. I have added a value of '1' to the cart input. The user can either just click 'Add' or enter a larger number should they wish to order more prints.

-   The 'Account' link on the navigation menu will allow you to either login or out and view your profile if you are a registered user, or register if you are a new user.  Once logged in, the link will display profile or logout options, and if not logged in, it will display a register or login option.

-   The 'Search' function uses the product description information to ensure that it is easier for users to find what they are looking for.

-   I have used AWS S3 buckets for hosting my static and media files. 

-   The footer links are set to the Alio Prints social media pages, and the 'Contact' page uses Django forms to display messages in the terminal window.

-   I have added a custom 404 page with a link back to the Home page.

-   I also created a favicon in Photoshop which can be seen on the browser tab.

-   I have added a 'scroll to top' button on all of the product pages with JavaScript for easier navigation.

-   All links and buttons have hover states activated to change when the user hovers over them, to improve the UX.

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
15. Heroku PostgreSQL Database

## Testing

I used Google Developer Tools to check the responsiveness of the site. The navbar and footer are responsive and reduce on smaller screens. I have used media queries throughout to allow for better UX on mobile devices.

The site had been tested on Chrome, Firefox and Safari.

The repository has been integrated with Travis and is passing. In order to test on Travis, I created a .yml file. I then linked my GitHub repository to Travis so for each git push, Travis would test the code.

I have one Django test complete in the products app. Further tests are yet to be developed.

Using Stripe developer testing, I have tested the payment functionality with the test card number: 4242 4242 4242 4242 and this is working correctly. No errors are coming back through the Stripe dashboard.

All HTML was checked on the W3C Mark-up Validation Service.

The CSS was checked on the W3C CSS Validation Service.

All JavaScript was checked on [jshint](https://jshint.com/)

All code was formatted on [Freeformatter](https://freeformatter.com)

I have tested all links. The Instagram, Twitter and Facebook links in the footer go the relevant accounts.

The contact form has been tested and user submissions are sent to the terminal.

<h4 align="center">
View the responsive design here:
  <a href="https://alioprints.s3-eu-west-1.amazonaws.com/media/images/responsive.png" target="_blank"><img src="https://alioprints.s3-eu-west-1.amazonaws.com/media/images/responsive.png" alt="Alio Prints Logo"/></a>
</h4>

### Manual Testing
1.  Home Page, Navbar and Footer:
    -   Navbar and Footer Display: I checked the navbar and footer on different screen sizes using developer tools on Chrome, Firefox and Safari. The navbar collapses on mobile. The display and footer icons have been resized for different screen sizes using media queries and these media queries are working correctly across all sites.
    -   Navbar and Footer Links: All navbar and footer links are working correctly.
    -   Account Links: The Account links are working correctly. I checked the login, logout, profile, register and reset password functions, which are all working as they should.
    -   Page Links: I checked site logo, 'View Gallery' and 'Get in Touch' links, and all links redirect to the correct URLs.
    -   Scrolling Parallax: I checked the section sizes which have been resized for tablets and mobiles for better UX using media queries. The column and font sizes have been adjusted to suit different screen sizes also and these were all checked using developer tools on Chrome, Firefox and Safari.
    -   Image Carousels: The carousel on section 4 is working correctly. On larger screens, it is a carousel with two sets of four images in a row which automatically scroll using JavaScript. The automatic scrolling and the 'next/previous' buttons are working. For small screens, this carousel does not appear, and a smaller one appears with one image at a time. The automatic scrolling and the 'next/previous' buttons are working.
    -   Contact Form: I tried to submit an empty form and received errors that the form fields were required. I submitted the form correctly and a success message appears.
    -   Search: I tested this with a random keyword and was redirected to the 'All Products' page, which is what I wanted.

2.  Gallery:
    -   Page Display: I checked that all media queries for better UX were working on different screen sizes using developer tools on Chrome, Firefox and Safari.
    -   Header Links: I checked each header linked to that category's shop page.
    -   Lightbox effect: I checked that on opening an image, it would appear in a lightbox with controls for next/previous image. I also checked that each image caption was display.

3.  Shop:
    -   Page Display: I checked that all media queries for better UX were working on different screen sizes using developer tools on Chrome, Firefox and Safari.
    -   Navbar Links: I checked the dropdown links for each category from the navbar. All links are working as they should.
    -   Product Breadcrumbs: I checked the category breadcrumb links at the top of the page to ensure they all direct to the correct URL.
    -   Add to Cart Function: I checked adding to cart by just clicking the 'Add' button, and also by entering a different integer in the quantity field, and this works correctly. If anything other than an integer is entered, an error message appears requiring the user to enter a number. This is working as it should.
    -   Scroll to Top Function: I tested the 'scroll to top' button which is activated once the user begins to scroll. This is working correctly.

4.  Cart:
    -   Page Display: I checked that all media queries for better UX were working on different screen sizes using developer tools on Chrome, Firefox and Safari.
    -   Amend Button: I tested entering text in the input field, and an error message appears requiring the user to enter a number. This is working as it should. If you enter a different number to what is currently in the cart and click 'Amend', the quantity is amended as per user entry.
    -   Remove Button: I tested that this button removes the item from the cart, and it does.
    -   Go to Checkout Function: If you are not logged in, the checkout button is not visible. The user is instructed to login or register to go to checkout. I tested these buttons and functions and they are working as they should. Once the user has logged in or registered, a success message appears and the checkout button appears and they can continue. 

5.  Checkout:
    -   Page Display: I checked that all media queries for better UX were working on different screen sizes using developer tools on Chrome, Firefox and Safari.
    -   Payment Form: I tested the payment form by submitting it incomplete (after filling in the card details below), and an error message appears.  
    -   Stripe Functionality: I tested a checkout using the Stripe test card 4242 4242 4242 4242 with any ccv code, and any future date for the expiry. Once the payment form is complete and these card details are entered, the test charge goes through and a success message appears. On the Stripe dashboard, I can see that the transaction was successful.

6.  404
    -   I tested adding to the URL with an URL not listed in the URL patterns, and it returned my custom 404 page. This page contains a link back to the Home page.

### Client stories testing:

Most common path through the website: 
- Home > Shop > All Products > Add to Cart > Login > Checkout 
- Each of these pages points clearly to the next one. 

Some pages offer two possible paths in their call to action buttons: 
- From Home Section 2 > Gallery 
- From Home Section 3 > Contact Page
- From Gallery > Click Product Category Header > Product Category Shop Page

### Testing client stories

* User A – As a new user, I want to be able to view all available prints and decide upon which one I prefer. 
    - From the navigation bar, I can select [Gallery](https://alio-prints.herokuapp.com/products/gallery) in the navigation menu to display a lightbox of all available designs. This shows a page with all products divided into sections. When an image is clicked, it opens up a lightbox effect with controls and displays the image name. Also, each category header is linked to the shop page for that category. All of these links and effects have been tested and are working.
* User B – As a new user I am looking to order a print and I want to be able to do this easily.    
    - From the navigation bar, I can select 'Shop' and a dropdown menu appears which displays all of the categories of available products. I can either choose a category or I can search all products by selecting [All Products](https://alio-prints.herokuapp.com/products). From here, I can add items to my cart. Once I have done this, I can either login or register to enable the checkout function. All of these links and functions have been tested and are working.
* User C - As an existing user, I want to be able to search for my favourite product easily to re-order.
    - From the navigation bar, I can use the search function. I type in the name of my favourite design and the search returns the results and redirects me to the relevant page. The search is based on the product description so there are many keywords I can use to search. If the keyword entered does not have any results, the user is redirected to 'All Products'. All of these links and functions have been tested and are working.
* User D - As an existing user, I want to check what items I have in my cart from a previous visit to the site. 
    - From the navigation bar, I can see an icon by the 'Cart' link displaying the number of items in my cart. I can select [Cart](https://alio-prints.herokuapp.com/products/cart). This will take me to the Cart page with a list of the products in my cart. All of these links and functions have been tested and are working.
* User E - As an employee of Alio Prints, I want to be able to login to the Django admin dashboard and update/add products. 
    - I can do this by adding '/admin' to the end of the URL and enter my login details. From here, I can add or amend products. This has been tested and is working.

## Deployment
1.  Download a copy of the file from [GitHub](https://github.com/ElaineArchbold/fullstack-milestone-project) and open it up in your IDE.
    -   (You will need to have access to env.py where the environment variables are stored. This file is in .gitignore so it won't be on GitHub. The variables are stored in my Heroku app so the deployment will work without the env.py file).

2. The following must be installed on your machine to run this app:
    -   python3
    -   boto3
    -   dj-database-url
    -   Django==1.11.29
    -   django-forms-bootstrap
    -   django-storages
    -   gunicorn
    -   Pillow
    -   psycopg2
    -   stripe

3.  The static files are stored in AWS AS Buckets under alioprints. If you make changes to any static files on the IDE, you must run: 'python3 manage.py collectstatic' from your IDE to push these changes to AWS.

## Heroku Deployment

1.  Create a requirements.txt file and a Procfile.
2.  Create a new app in Heroku.
3.  In "Settings" > "Reveal Config Vars" and add the variables for:
    -   AWS_ACCESS_KEY_ID
    -   AWS_SECRET_ACCESS_KEY
    -   DATABASE_URL
    -   SECRET_KEY
    -   STRIPE_PUBLISHABLE
    -   STRIPE_SECRET and set
    -   DISABLE_COLLECTSTATIC to 1 as we are using S3 to host our static files.
4.  In settings, link the GitHub repository to Heroku.
5.  Add the name of your Heroku app to ALLOWED_HOSTS in the settings file on your IDE.
6.  Under 'Deploy' click on 'Deploy Branch', which will pull your up to date repository.
7.  Select 'open app' once this has been built and your app should now be visible.
8.  From here, you can add: /admin to the URL to access the Django administration dashboard. Here you can view and change users, groups and products. Can also view all of the orders made on the app.

## Credits
### Content

### Media
- The background images on parallax two and three on the home page are from [Unsplash](https://unsplash.com/)

- The print designs, logos and backdrop on parallax one on the home page were created by me using Photoshop/Publisher.

- The background images on all other pages are the Alio Prints logo which I created in Photoshop.

### Acknowledgements
- The footer, navbar and parallax effect were taken and amended from previous projects.

- I found the lightbox snippet on the Inspiration page [here](https://epicbootstrap.com/snippets/lightbox-gallery)

- I found the snippet for the gallery carousel on the Home page [here](https://stackoverflow.com/questions/20007610/bootstrap-carousel-multiple-frames-at-once)

- I found the snippet for the contact form [here](https://hellowebbooks.com/news/tutorial-setting-up-a-contact-form-with-django/)

- The shopping functionality was taken from the Full stack Ecommerce mini project with the Code Institute.
