# Set Up Models __Priority HIGH__

## Structure
## Collect App
This app 'collects' information using forms
## Patient
Patient is a Model
Patient has a PersonInfo
## PersonalInfo
PersonalInfo can come in many different versions. For example PersonalInfo_minimal
might only ask for first name and last name.
PersonalInfo has fields:
- patientid
- firstname
- lastname
- address
- email address
- phone number
- DOB
- sex


## Form contains Models (e.g Patient.PersonalInfo)


# IMPORTANT: We do not need to keep writing forms. We need to write once. 
# And that is it. Why because form is specified by a model and a model
# already specifies everything about the form. 
# Form are rendered always exactly the same. So go through the fields
# that model describes and display them.

# COPY!!!
https://simpleisbetterthancomplex.com/2015/12/04/package-of-the-week-django-widget-tweaks.html

Something was wrong
copy add_label_class function from github


