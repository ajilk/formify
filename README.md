# Express Version

#### Express 
Web Framework that uses node.js scripting language (like Django which uses
Python scripting language)

---
#### node.js  
Scripting language used. Works well with express

---
#### PUG
HTML Template Engine. No longer need to write in HTML.  
.pug file eventually turns into a regular HTML file with the help of express
##### Why PUG?
- simple
- variables that can be manipulated through framework
- can include other PUG files (object-oriented per se)
---
#### body-parser (express middleware)
npm module that takes responses and converts them to json 
(at least that is how it is used in this scenario)
This is the meat of the project

## Typical Flow
HTMLs that contain form can be made directly (manually), which gives 
more control and less confusion. A quick and easy option is to use 
an online form generator websites (protostrap.com) to generate a HTML form
that has been created through a drag and drop process. A better option is 
to use PUG. It is less uglier than HTML and it can be made out of smaller
PUG files to make one big one which is easier to debug and alter. The best
part of using PUG, since it is a template engine, it allows use of variable
which can be manipulated throught the scripting language or framework. 
What does that mean? It means we can "autofill" forms and tailor it 
for each and every user.

***Take a look at the source to get a better understanding****