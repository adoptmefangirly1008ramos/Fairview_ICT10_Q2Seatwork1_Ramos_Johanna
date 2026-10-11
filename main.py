from pyscript import document, display

names = ['Enzo Ruiz', 'Logan Anaque', 'Johanna Ramos', 'Joshua Ortiz', 'Renn Santos', 'Jhoana Evangelista']

def check_name(e):
    
    document.getElementById("output1").innerHTML = " "

    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

    full_name = first_name + " " + last_name
    is_name = full_name in names

    message = {
        True: "Congratulations " + full_name + "! You are now part of the ICT club.",
        False: "Sorry " + full_name+ ", your name is not on the list."
    }

    display(message[is_name], target="output1")