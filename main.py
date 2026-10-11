from pyscript import document, display

names = ['Enzo Ruiz', 'Logan Anaque', 'Johanna Ramos', 'Joshua Ortiz', 'Renn Santos', 'Jhoana Evangelista'] #members of ict club

def check_name(e):
    
    document.getElementById("output1").innerHTML = " " #clears previous output

    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

    full_name = first_name + " " + last_name #combines the first and last name together
    is_name = full_name in names # checks if value exists in lists

    message = {
        True: "Congratulations " + full_name + "! You are now part of the ICT club.",
        False: "Sorry " + full_name+ ", your name is not on the list."
    } #results

    display(message[is_name], target="output1") #displays the results
