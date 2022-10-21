# DEM PUMPKINS: Emily Ortiz, Diana Akhmedova, May Qiu
* SoftDev
* K12 -- Take and Give
* 2022-10-17
* time spent: 0.5 hours

# DISCO:
* A GET request retrieves information and user input from the webserver
  * Uses request.args.
* A POST request places the HTML information retrieved from the user's input on the webserver.
  * Uses request.form.
* methods=['GET', 'POST'] allow you to use GET and POST methods.
* You must include method="post" in the form tag of the HTML file if you want to use POST methods.
* request.form.get('username') retrieves the user's input of the id with the name "username".
  * You can set this equal to a variable that can be used in another HTML file via curly braces, ex: {{ username }}.
  * You can also use request.form['username'] to retrieve the user's input.
* request.method retrieves the type of request method used, which was POST in this case.

# QCC:
* A thorough explanation of the differences between GET and POST would be helpful.
* What are the reasons for using GET over POST, and vice versa?
* Why do we have to do request.form.get() to get the username, while we only have to do request.method to get the method?
