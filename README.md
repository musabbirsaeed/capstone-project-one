# Capstone-Project-One #
## Macro counter and nutrition help ##

**1. What goal will your website be designed to achieve?**
	
The goal of the project is to allow users to enter a recipe with ingredients and be able to calculate a nutrition label for that recipe and also be able to give them an accurate macro breakdown.

**2. What kind of users will visit your site? In other words, what is the demographic of
your users?**
	
The main demographic for the users of my site is anyone in the fitness space that regularly meal preps or likes to plan out their macros for the day/week.

**3. What data do you plan on using?**

I plan on using data provided by the user along with the data pulled from the API. Ingredients would be from the user and the nutrition information would be from the API

**4. In brief, outline your approach to creating your project. Answer
questions like the ones below, but feel free to add more information:**

**a. What does your database schema look like?**

table users <br>
id SERIAL PRIMARY KEY <br>
username TEXT NOT NULL UNIQUE<br>
password TEXT NOT NULL<br>
name TEXT<br>

table recipes<br>
id SERIAL PRIMARY KEY<br>
name TEXT NOT NULL<br>
ingredients TEXT NOT NULL<br>
macro_count TEXT NOT NULL<br>

**b. What kinds of issues might you run into with your API?**

Ingredients not being in the API or nutrition information being wrong coming back from the API. The API being down for any reason. The API not acting in the way I would want it to. 

**c. Is there any sensitive information you need to secure?**

The API key and user information. 

**d. What functionality will your app include?**

A macro counter with a graph to show the breakdown, a user account creation to store already entered recipes, have links to the recipe page if pulling from another site. 

**e. What will the user flow look like?**

[https://drive.google.com/file/d/1V3GhjlpZclqkCf8kV3BsECtNicYw6ckB/view?usp=sharing](https://drive.google.com/file/d/1V3GhjlpZclqkCf8kV3BsECtNicYw6ckB/view?usp=sharing)

**f. What features make your site more than CRUD? Do you have any stretch
goals?**

Having the ability to store new recipes and users. Update existing recipes and users. Delete any recipe that a user wants or delete the users own account. 

I would want to be able to link to the fitness app API's in order to import the data into other apps for ease of use. Way stretch goal would be to create a custom API to show preparation for ingredients that can link right the the ingredient name and a pop up window
