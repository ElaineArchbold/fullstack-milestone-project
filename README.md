[![Build Status](https://travis-ci.org/ElaineArchbold/fullstack-milestone-project.svg?branch=master)](https://travis-ci.org/ElaineArchbold/fullstack-milestone-project)

<h1 align="center">
  <a href="https://alioprints.s3-eu-west-1.amazonaws.com/media/images/letterlogo.png" target="_blank"><img src="https://alioprints.s3-eu-west-1.amazonaws.com/media/images/letterlogo.jpg" alt="Alio Prints Logo"/></a>
</h1>


## Elaine Archbold Full Stack Milestone Project

For this project, I created a website for Alio Prints which is a graphic design business I started a few years ago. I wanted the look of the site to be clean and simple, and make for a smooth online shopping experience.

## UX
My goal in the design was to create a very user friendly site where users could view and order their own custom print. I kept the Navbar and footer simple, and the colour theme is subtle. 

*User A – As a new user, I want to be able to view all available prints and decide upon which one I prefer. I can select [Gallery](https://alio-prints.herokuapp.com/products/gallery) in the navigation menu to display a lightbox of all available designs. Each header is linked to the product page for that category.
*User B – As a new user looking to order a print, I want to be able to do this easily.  I can select 'Shop' and go to in the navigation menu to display the categories of products available. I can either choose a category or I can search all products by selecting [All Product](https://alio-prints.herokuapp.com/products) . From here, I can add items to my cart. Once I have done this, I can either login or register to enable the checkout function.
*User C - As a user looking for a specific product, I can use the search bar in the navigation menu. The search function is based on the product description so I have many key words I can use to search. 
*User D - As an existing user, I want to check what items I have in my cart from a previous visit to the site. I can select [Cart](https://alio-prints.herokuapp.com/products/cart) in the navigation menu to display the items stored in my cart.
*User E - As an employee of Alio Prints, I want to be able to login to the admin portal and update/add products. I can do this by adding '/admin' to the end of the URL and enter my login details.

The site can be viewed through Heroku [Here](https://alio-prints.herokuapp.com)

I created Wireframes of how I wanted the site to look before starting. See below:


## Features
### Existing Features
The [Home](https://alio-prints.herokuapp.com) page features a scrolling parallax effect, with four sections. 
..* Section one is background image I created in Photoshop as a wall mock-up of some of the prints. I feel like the background image gives a good introduction to the site and the colour theme is based around this.
..* Section two is a brief description about what we do with a button link to the Gallery.
..* Section three is a description of the order process, with a link to the contact page.
..* Section four is a carousel of a few of our best-selling prints. On large screens, this displays 4 images in a row, and a different carousel is active on smaller screens to show one image in a row. This was accomplished through media queries and JavaScript.

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








### Client stories testing:

Most common path through the website: 
- Home > Gallery > Pricing > How to Order > Contact 
- Each of these pages points clearly to the next one with a call to action button. In some places the customer may have a different question in their mind, so a second button is also provided. 

The About page is not necessarily part of the flow of the site for users, but it has been included 
to offer information about the artist for those who are curious about her. The information here is kept short as to not overload the user. 

Some pages offer two possible paths in their call to action buttons: 
- From About > Gallery OR How to Order
- From Gallery > Pricing OR How to Order

### Testing client stories from UX section of README.md

1. As a new visitor to the website, I want to easily navigate the site, so I can find what I need efficiently. 
    1. No matter what page the new visitor lands on, they can easily find and use the navigation bar. 
    2. The logo image always leads back to the home page (the starting place for most client stories).
    3. The home page call to action button leads the client through the gallery.
    
2. As a new visitor to the website, I want view this artist's gallery, and view their work in detail so I can decide if I want to commission their work. 
    1. At the bottom of the Home page and About page there is a clear call to action button leading the visitor to the gallery.
    2. A clearly labelled Gallery page is easy to find in the navigation on every page.. 
    
3. As a visitor to the website, I am curious to know more about the artist, so I can feel I connect with her as a person.
    1. A clearly labelled  How to About page is easy to find in the navigation on every page.. 
    2. The About page contains photos of the artist in her studio, and short but compelling text about what the artist enjoys about her work.

4. As a potential client, I want to know what past clients thought of their artwork and the service they received.
    1. On the home page, testimonials from past clients are easy to find and to read.

5. As a potential client, I want to view expected prices for a portrait, so I can decide if it is within my budget to order. 
    1. A clearly labelled  pricing page is easy to find in the navigation on every page.. 
    2. Once the visitor to the website has already been led by call to action buttons from the Home page, and through to the Gallery, they are then led to the Pricing page.
    
6. As an interested client, I want to understand the ordering process, so I know what steps to take next. 
    1. A clearly labelled  How to Order page is easy to find in the navigation on every page. 
    2. Once the visitor to the website has already been led by call to action buttons from the Home page, and through to the Gallery, and Pricing page, they are then led to the How to Order page.
    3. The How to Order page clearly and intuitively explains the steps involved in placing an order, using icons to add another level of clear communication to the explanation.
    4. At the bottom of the How to Order page, the first step in ordering is clearly marked as a call to action button. Which leads to the contact page.

7. As an interested client, I want an easy to fill in contact form, so I can make contact with the artist and place my order. 
    1. A clearly labelled  contact page is easy to find in the website navigation on every page.

8. As an interested observer and/or potential client, I want to follow the artist on social media, so I can keep up with her latest news. 
    1. 5 social media icons can be found in the footer on every page of the website.
    
9. As a returning visitor to the website, who has already decided to contact the artist, I want to be able to request a quote easily.
    1. There is a clearly marked "Request quote" button in the navigation bar, highlighted as a button so that it stands out from all the other menu items. It displays in the top right of desktop and tablet screens, and at the bottom of the dropdown menu on mobiles.


### Manual (logical) testing of all elements and functionality on every page.

#### Home Page:

1. Navigation bar:
    1. Go to the "Home" page from a desktop.
    2. Change the screen size from desktop to tablet to verify that the navigation bar is responsive and switches from in line menu to burger icon dropdown menu at the appropriate place.
    3. When checking responsiveness of navbar, verify that there is no overflow causing ugly size changes to menu items. _During testing there were overflow problems here. This was fixed by reducing size of the button and logo margins_
    4. Hover over the logo in the navigation bar and verify that the alt text appears. _During testing this did not happen, so I added a title attribute to the logo to fix_
    5. Click on the logo in the navigation bar and verify that it links to the home page. 
    6. Click on each navigation menu item and verify that it links to the correct page. 
    7. Hover over the "request quote" button and verify the hover colour change works as expected.
    8. Click on the "request quote" button and verify that it links to the contact page. 
    9. Change screen size to small and click burger icon, verify that the menu drops down and that the menu text is centred.
    10. Repeat verification of functionality and responsiveness on my mobile phone and tablet.

2. Hero image / video:
    1. Go to "Home" page from a desktop. 
    2. Confirm video is visible, autoplays on mute and is 100% width of the screen. 
    3. Reduce the width of the window to confirm that the video switches to static image in mobile.
    4. Reduce and expand width of window to confirm that the overlay on top of image / video responds correctly and does not obscure important features. 

3. Compelling copy section:
    1. Reduce and expand width of window to confirm that the text in this section responds correctly and looks good on all device widths. 

4. Testimonials:
    1. Reduce and expand width of window to confirm that 3 testimonials display on medium to large screens, but one is hidden on mobile devices.

5. Call to action button:
    1. Hover over call to action button and verify the hover colour change. 
    2. Click the call to action button and verify that it links to the correct page. 
    
6. Footer: 
    1. Hover over each social media icon and confirm colour and size transitions expected. 
    2. Click on each icon to confirm it opens a separate tab for it's link.
    3. Reduce and expand width of window to verify that the footer is responsive and looks good on all device widths. 

7. Review all functionality and responsiveness on my mobile phone and tablet.


#### About Page:

1. Navigation bar: 
    1. Repeat verification steps done for navbar on Home page.
    2. Confirm that navbar code is identical on all html pages. 

2. Hero image:
    1. Hover over hero image and confirm that alt title appears.
    2. Reduce and expand width of window to verify that the hero image behaves and centres the way expected, and that it looks good on all device widths.

3. Page images: 
    1. Hover over each image in the content and confirm that the alt title for each appears.
    2. Reduce and expand width of window to verify that each image behaves and centres the way expected, and that they look good on all device widths.

4. Page content: 
    1. Reduce and expand width of window to verify that each line of text behaves the way expected, and that the text arrangement looks good on all device widths.
    
5. Call to action buttons:
    1. Hover over each call to action button and verify the hover colour change. 
    2. Click each call to action button and verify that it links to its relevant correct page. 
    3. Reduce and expand width of window to verify that the call to action buttons spacing responds as expected. 
    4. Confirm that the two buttons move to stacked on top of each other for mobile devices and display next to each other for larger screens.

6. Footer:
    1. Repeat verification steps done for footer on Home page.
    2. Confirm that footer code is identical on all html pages.

7. Review all functionality and responsiveness on my mobile phone and tablet.


#### Gallery Page:

1. Navigation bar: 
    1. Navbar code is identical on all html pages. Testing already completed.

2. Hero image:
    1. Repeat verification steps done for hero image on About page.
    
3. Gallery:
    1. Hover over each gallery thumbnail and confirm the hover animation works as expected.
    2. Check code to confirm that each gallery thumbnail has a descriptive alt attribute. _Titles were deliberately *not* added here because they ruin the clean look of the gallery page. Because of the alt attribute the page is still navigable for visually impaired users_
    3. Click on each gallery thumbnail and confirm that the Fancybox gallery modal activates. 
    4. In the gallery modal test click forwards and backwards, play and pause functions and confirm they all work as expected. 
    5. Reduce and expand width of window to verify that each row of gallery images behave and centre the way expected, and that the grid of images looks good on all device widths.

4. Call to action buttons: 
    1. Repeat verification steps done for call to action buttons on About page.
    
5. Footer:
    1. Footer code is identical on all html pages. Testing already completed.
     
6. Review all functionality and responsiveness on my mobile phone and tablet.


#### Pricing Page:

1. Navigation bar: 
    1. Navbar code is identical on all html pages. Testing already completed.

2. Hero image:
    1. Repeat verification steps done for hero image on About page.

3. Pricing tables: 
    1. Reduce and expand width of window to verify that each table responds in the way expected, they display next to each other on desktop, but stacked on top of each other on mobile and tablet.
    2. Confirm the page looks good at all device widths.

4. Small print: 
    1. Reduce and expand width of window to verify that the small print text behaves and centres the way expected, and that it looks good on all device widths.
    
5. Call to action button: 
    1. Repeat verification steps done for call to action button on Home page.
    
6. Footer:
    1. Footer code is identical on all html pages. Testing already completed.
    
7. Review all functionality and responsiveness on my mobile phone and tablet.

#### How to Order Page:

1. Navigation bar: 
    1. Navbar code is identical on all html pages. Testing already completed.

2. Hero image:
    1. Repeat verification steps done for hero image on About page.

3. Steps to Order Section: 
    1. Reduce and expand width of window to verify that the steps containers, icons and text display the way expected, 
    2. Confirm that the steps look good on all device widths.

4. Completion times text: 
    1. Repeat verification steps done for small print on pricing page.

5. Call to action button: 
    1. Repeat verification steps done for call to action button on Home page.
    
6. Footer:
    1. Footer code is identical on all html pages. Testing already completed.
 
7. Review all functionality and responsiveness on my mobile phone and tablet.
    

#### Contact Page:

1. Navigation bar: 
    1. Navbar code is identical on all html pages. Testing already completed.

2. Hero image:
    1. Repeat verification steps done for hero image on About page.

3. Contact form: 
    1. Try to submit the empty form and verify that an error message about the required fields appears
    2. Try to submit the form with an invalid email address and verify that a relevant error message appears
    3. Try to submit the form with a file uploaded, verify that file selection process works.
    4. Try to submit the form with all inputs valid and verify that a success message appears.
    5. Reduce and expand width of window to verify that the form display behaves and centres the way expected, and that it looks good on all device widths.

4. Footer:
    1. Footer code is identical on all html pages. Testing already completed.

5. Review all functionality and responsiveness on my mobile phone and tablet.

## Further testing: 

1. Asked fellow students, friends and family to look at the site on their devices and report any issues they find. _margins were adjusted for navigation bar after feedback that "request quote" button was too close to nav menu on some devices_
2. I viewed my website on several devices at a local tech store, no further issues found.








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

