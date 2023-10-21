# webapps

erm also we can use template inheritance to ensure that layouts stay the same throughout. it's pretty cool

### check the comments baby!
when doing user input, how do you ensure security? because if i enter my password it's over for us all

## We use POST requests comme ca:
POST /submit HTTP/1.0
User-Agent: HTTPTool/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 27

module=comp2011&year=2022

### what is csrf bbaby talk
go read s4 again

# each flask form has a respective template, is there a directory we can use for this?
######
When the user completes the web form and presses the submit button the browser makes a POST request, in this post request is all the data entered into the form. The data is encoded in the message body. Flask-WTF makes it easy to retrieve the data encoded in the body. The data is automatically decoded and placed in the data attribute or the field attribute of the form class. An example will help. In the file app/views.py modify the calculate method to the following.