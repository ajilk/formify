# Explanation
#### forms
this directory will contain all the forms that will be made.
#### public
this directory will contain public information such as css, static files,
audio, images and etc.
#### routes
this directory deals with routing the user to the right places depending
on what they clicked/typed. (express stuff).
#### views
this directory will contain template PUG files that are updated with 
information from the database.
#### app.js
this file glues all of it together.
#### package-lock.json and package.json
this file holds information about the package such as dependencies.

# To run
```
git clone https://github.com/eldorbekpulatov/formify.git
cd formify
git checkout express-version # switch to the right branch
cd app
npm install
node app.js
# go to localhost:3000/forms/01
```