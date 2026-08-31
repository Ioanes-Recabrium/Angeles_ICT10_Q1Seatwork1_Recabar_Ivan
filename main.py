from pyscript import document
name = "ivan" # str
age = 15 # int
height = 175.26 # float
country = ["sparta", "tahiti", "ussr", "botswana"] # list
student_type = False #bool
mydict = {
  "color": "blue",
  "car_brand": "Mustang",
  "shoe_size": "44",
  "best_friend": "error no friends"
} # dict
fruity = {
    "apple", 
    "banana", 
    "cherry",
    "watermelon",
    "razzbery"
    } # set
thetupelware = (
    "monday",
    "tuesday",
    "wendesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
    ) # tuple
output = f"""
<h1> hey these are my characteristics </h1>
<p> age: {age} ({type(age).__name__}) </p>
<p> height: {height} ({type(height).__name__}) </p>
<p> country: {country} ({type(country).__name__}) </p>
<p> student_type: {student_type} ({type(student_type).__name__}) </p>
<p> mydict: {mydict} ({type(mydict).__name__}) </p>
<p> fruity: {fruity} ({type(fruity).__name__}) </p>
<p> thetupelware: {thetupelware} ({type(thetupelware).__name__}) </p>
thanks
"""
document.querySelector("#output").innerHTML = output