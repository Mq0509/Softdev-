"""
M & (I)M: Matthew Yee, Ian Jiang, May Qiu
SoftDev pd7
k08 -- Occupations in Flask
2022-10-07
Time Spent: 2
"""

import random

from flask import Flask    

#opens file and stores in file var, then turns file into string
file = open("occupations.csv")
#rename to src if uncommented foo in un_csv()
foo = file.readlines()
#empty dictionary to be populated by un_csv()
d = {}

def un_csv():
    #splits based on newline, returns list of strings
    """
    commented out foo bc readlines() does it for us
    if want to make src.split() work, change range of for loop to -2
    """
    #foo is list of strings
    #foo = src.split("\n")
    #iterates through list of strings, but we ignore the first and last elements in list, since it's not actually part of the data set
    for n in range(1, len(foo) - 1):
        #list to store occupation and percent
        l = []
        #if the first char is ", then there is a comma somewhere inside the job class, so we can't just split
        if foo[n][0] == "\"":
            l = un_comma(foo[n])
        #else, we can just split and store the information in dictionary
        else:
            l = foo[n].split(",")
            #split converts into 2 strings, so we have to convert into int
            l[1] = float(l[1])
        d[l[0]] = l[1]
    return d

#very similar to what we did in 05, iterating through a string to find chars/strings we don't want
def un_comma(substring):
    #vars to store information
    occ = ""
    per = 0
    for n in range(1, len(substring)):
        if substring[n] == "\"":
            occ = substring[1:n]
            break
    per = float(substring[n+2:len(substring)])
    return [occ, per]

def rand_occ():
    #per = d.values()
    s = 0
    #loops through dictionary
    for n in d:
        #stores a random number from 0 to 99.9 - s
        #used random.uniform instead of randrange bc randrange takes integers
        r = random.uniform(0, 99.9 - s)
        #if the randomly generated number is less than the value, then we return the occupation
        if r < d[n]:
            return n
        #else, increment s by the value, so that we generate numbers from 0 to a lower bound
        else:
            s += d[n]


#main function to return html for the browser to contain hyperlinks
def main():
    un_csv()
    d_string = ""
    for x in d:
        d_string += x + "<br>"
    occ = rand_occ()
    url = ""
    tnpg = "M&(I)M: Ian Jiang, May Qiu, Matthew Yee<br>"
    #For cases where the name of occupation is not consistent with bls.gov, return link/links correlating with occupation
    if occ == "Business and Financial operations":
       return tnpg + 'Your job is <a href="https://www.bls.gov/ooh/business-and-financial/home.htm">'+ occ + "</a>" + "<br><br>Job List:<br>" + d_string
    elif occ == "Computer and Mathematical":
        return tnpg + 'Your job is <a href="https://www.bls.gov/ooh/computer-and-information-technology/home.htm">Computer</a> and <a href="https://www.bls.gov/ooh/math/home.htm">math</a>' + "<br><br>Job List:<br>" + d_string
    elif occ == "Arts, design, entertainment, sports and media":
        return tnpg + 'Your job is <a href="https://www.bls.gov/ooh/arts-and-design/home.htm">Arts, design</a>, <a href="https://www.bls.gov/ooh/entertainment-and-sports/home.htm">entertainment, sports</a> and <a href="https://www.bls.gov/ooh/media-and-communication/home.htm">media</a>' + "<br><br>Job List:<br>" + d_string
    elif (occ == "Healthcare support") or (occ == "Healthcare practioners and technical"):
        return tnpg + 'Your job is <a href="https://www.bls.gov/ooh/healthcare/home.htm">'+ occ + "</a>" + "<br><br>Job List:<br>" + d_string
    elif occ == "Building and grounds cleaning and maintenance":
        return tnpg + 'Your job is <a href="https://www.bls.gov/ooh/building-and-grounds-cleaning/home.htm">Building and grounds cleaning</a> and <a href="https://www.bls.gov/ooh/installation-maintenance-and-repair/home.htm">maintenance</a>' + "<br><br>Job List:<br>" + d_string
    else:
        #removes commas and replaces spaces with dashes for the url
        url = occ.replace(',','')
        url = url.replace(' ','-') 
    return(tnpg + 'Your job is <a href="https://www.bls.gov/ooh/' + url + '/home.htm">'+ occ + "</a>" + "<br><br>Job List:<br>" + d_string)


app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return main()

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
