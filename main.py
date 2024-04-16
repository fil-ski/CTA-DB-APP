#-------------------------------------------
# Project 2: Chicago Lobbyist Database App
# Course: CS 341, Spring 2024, UIC
# System: Visual Studio Code on Windows
# Author: Filip Petrev
# Presentation Tier Layer of the application
#
# This part of the project facilitates indirectly interacting
# with the chicago lobbyists db through a console based user interface.
# Users can perform various operations such as looking up
# lobbyists by name, viewing detailed information about a lobbyist,
# finding the top N lobbyists by total compensation for a given year,
# registering an existing lobbyist for a new year, and setting the
# salutation for a lobbyist. It serves as the front-end of the
# application which employs functionality from the object mapping 
# tier to retrieve data in the form of objects or process updates
# to the database. No SQL querries are written or conducted in this
# specific part of the application, this is handeled by the other
# layers. This layer merely responsbile for the presenation of the data.
#-------------------------------------------

import sqlite3
import objecttier



"""
This function is called at the start of the program in order to 
display basic statistics about the Chicago Lobbyist database such 
as the number of lobbyists, employers, and clients. Uses functions 
num_lobbyists, num_employers, num_clients from the objecttier layer 
in order to retrieve the required data
"""
def display_statistics(dbConn):
    print('** Welcome to the Chicago Lobbyist Database Application **')
    print()
    print("General Statistics:")
    num_lobbyists = objecttier.num_lobbyists(dbConn)
    num_employers = objecttier.num_employers(dbConn)
    num_clients = objecttier.num_clients(dbConn)
    print(f"  Number of Lobbyists: {num_lobbyists:,}")
    print(f"  Number of Employers: {num_employers:,}")
    print(f"  Number of Clients: {num_clients:,}")
    print()



"""
This function handles the logic for the first command of the application.
It prompts the user for a string that may contain SQL wildcards, and uses
this input as a parameter for the get_lobbyists function of the objecttier
layer of the application. Since the get_lobbyists function returns a list 
of Lobbyist objects in ascending order by the ID, it iterates through this 
list in order to output the data in the proper format. 
"""
def lookup_lobbyists_by_name(dbConn):
    #prompt the user for the string that may contain SQL wilcards
    print()
    name = input('Enter lobbyist name (first or last, wildcards _ and % supported): ')
    
    #utilize get_lobbyists functionality from the objecttier layer to retrieve list of lobbyists objects 
    print()
    lobbyists = objecttier.get_lobbyists(dbConn, name)
    
    #first condition is to check that the number of Lobbyist returned does not exceed 100
    if len(lobbyists) > 100:
        #output the number of Lobbyist retrieved and ask the user to try again with different search
        print(f"Number of lobbyists found: {len(lobbyists)}")
        print()
        print('There are too many lobbyists to display, please narrow your search and try again...')
        print()
    elif len(lobbyists)>=1:
        #conditional branch for 1 (inclusive) to 100 (exclusive) lobbyists returned in the list
        print(f"Number of lobbyists found: {len(lobbyists)}")
        print()
        #iterate through the list of lobbyists objects and output their data
        for lobbyist in lobbyists:
            print(f"{lobbyist.Lobbyist_ID} : {lobbyist.First_Name} {lobbyist.Last_Name} Phone: {lobbyist.Phone}")
        print()
    else:
        #final part of the conditional branch captures no lobbyists returned
        print("Number of lobbyists found: 0")
        print()



"""
This function handles the logic for the second command of the application, which
outputs detailed information about the lobbyist based on the inputted lobbyist id.
Utilizes the get_lobbyist_details function from the objecttier layer to retrieve a LobbyistDetails
object which contains the required data within its attributes. Since all of the data is 
already properly retrieved via the objecttier logic, this function predominately organizes 
the the result for the user through formatted strings created with the property methods
of the LobbyistDetails object in order to access attributes.
"""
def lookup_lobbyist_details(dbConn):
    #prompt user for lobbyist ID and typecast to int
    print() 
    lobbyist_id = int(input("Enter lobbyist ID: "))
    print()

    #call the get_lobbyist_details function from the objecttier with the user input as a parameter
    details = objecttier.get_lobbyist_details(dbConn, lobbyist_id)
    
    #condition if the objectier succesfully retrieves LobbyistDetails object
    if details:
        #each line below formats a string for the ouput by combining object attributes using property methods
        address = f"{details.Address_1} {details.Address_2} , {details.City} , {details.State_Initial} {details.Zip_Code} {details.Country}"
        full_name = f"{details.Salutation} {details.First_Name} {details.Middle_Initial} {details.Last_Name} {details.Suffix} "
        #iterate through, convert years to string, and join with commas
        years_registered = ", ".join(str(year) for year in details.Years_Registered) 
        employers = ", ".join(details.Employers)
        total_compensation = f"${details.Total_Compensation:,.2f}"

        #output results to user after formatting
        print(f"{details.Lobbyist_ID} :")
        print(f"  Full Name: {full_name}")
        print(f"  Address: {address}")
        print(f"  Email: {details.Email}")
        print(f"  Phone: {details.Phone}")
        print(f"  Fax: {details.Fax}")
        print(f"  Years Registered: {years_registered},")
        print(f"  Employers: {employers},")
        print(f"  Total Compensation: {total_compensation}")
        print()
    else:
        #case that handles objecttier not returning anything
        print(f"No lobbyist with that ID was found.")
        print()



"""
This function handles the logic for the third command of the application. Based on 
the users input of N and a year, it outputs the top N lobbyists of that year. Data 
is retrieved in the form of a list of 0 or more LobbyistClients objects using objecttier 
function get_top_N_lobbyists. Lobbyists are ordered by their total compensation in the output,
however this is already handled by the objecttier layer. This function mainly handles 
formatting the results to the user for presentation, and making sure their input is valid.
"""
def find_top_n_lobbyists(dbConn):
    #prompt user for val of n and typecast to int
    print()  
    n_input = int(input("Enter the value of N: "))
    
    #if n is 0 or negative than, print a message and exit the function
    if n_input <= 0:
        print("Please enter a positive value for N...")
        print()
        return

    #prompt user for year, remains as type string when passed as param in the objecttier function
    year_input = input("Enter the year: ")
    
    #make sure input is valid (not a large number or not digits)
    if not year_input.isdigit() or len(year_input) != 4:
        print()
        return
    
    year = int(year_input)  #convert to int and make sure year is within logical range
    if year < 0 or year > 9999:
        print()
        return
    print()
    
    #call the objectier layer function get_top_N_lobbyists with n as an int and year as a string after validating user input
    top_lobbyists = objecttier.get_top_N_lobbyists(dbConn, n_input, year_input)
    
    #if no lobbyists are returned leave the function
    if not top_lobbyists:
        return
    
    #iterates through the list of lobbyist objects, format strings for 
    #output using property methods to retrieve attribute info, and displays
    #the data to the user for each lobbyist
    for index, lobbyist in enumerate(top_lobbyists, start=1):
        full_name = f"{lobbyist.First_Name} {lobbyist.Last_Name}"
        clients = ", ".join(lobbyist.Clients)
        total_compensation = f"${lobbyist.Total_Compensation:,.2f}"
        
        print(f"{index} . {full_name.upper()}")
        print(f"  Phone: {lobbyist.Phone}")
        print(f"  Total Compensation: {total_compensation}")
        print(f"  Clients: {clients},")
    print()


"""
This function handles the logic for the fourth command of the application. It
registers an existing lobbyist for a new year based on the lobbyist id provided
by the user, and the year the user wants to register them for. Employs function
add_lobbyist_year from the objecttier in order to process the update for the db.
Includes error handling for both failure to update database and invalid entry
of lobbyist id (both cases return 0 from add_lobbyist_year) by making sure
result returned from objecttier layer is 1.
"""
def insert_new_lobbyist_year(dbConn):
    #prompt user for both a year and a lobbyist ID, and typecast them both to ints
    print() 
    year_input = int(input("Enter year: "))
    lobbyist_id = int(input("Enter the lobbyist ID: "))

    #attempt to add the year for the lobbyist by calling add_lobbyist_year from objecttier with the user input as params
    result = objecttier.add_lobbyist_year(dbConn, lobbyist_id, year_input)
    print()
    
    #display the appropriate message based on the result of objecttier call
    if result == 1:
        print("Lobbyist successfully registered.")
        print()
    else:
        print("No lobbyist with that ID was found.")
        print()


"""
This function handles the logic for the fifth command of the application.
It sets the salutation for a given lobbyist by prompting the user for a 
lobbyist id and a string, and calls the objecttier function set_salutation
with these inputs as parameters. Designed with extensive handeling for cases
of extremely high lobbyist_id values which cause SQL errors. If such an error
occurs it outputs that no lobbyist was found without crashing the program.
"""
def set_lobbyist_salutation(dbConn):
    print()
    
    #nested within try catch block incase input causes database errors and the program to crash
    try:
        #promt user for lobbyist id typecasted to an int, along with a salutation string
        lobbyist_id = int(input("Enter the lobbyist ID: "))
        salutation = input("Enter the salutation: ")
        print()
        
        #call objecttier function set_salutation with the users input as params
        result = objecttier.set_salutation(dbConn, lobbyist_id, salutation)
        
        if result == 1:
            print("Salutation successfully set.")
        else:
            #if the return from objectier is not 1 it means no lobbyist was found
            print("No lobbyist with that ID was found.")
    except ValueError:
        #this catches non-integer inputs
        print("No lobbyist with that ID was found.")
    except Exception as e:
        #this is a catch-all for any other potential exceptions
        print("No lobbyist with that ID was found.")
    print()




"""
Entry point of the program. Starts off by connecting to the Chicago_Lobbyists
database using sqlite3, and once this connection is established it passes the 
dbConn object into display_statistics to output the starting statistics. Then 
the program enters a loop, waiting for user input to execute one of five possible 
commands or x to quit the program. Uses dictionary with command number as key and
the corresponding function as the value to call whichever command the user wants to
run.
"""
def main():
    #connect to the database and display start stats
    dbConn = sqlite3.connect('Chicago_Lobbyists.db')
    display_statistics(dbConn)

    #dictionary with command # and function as key-value pairs
    command_handlers = {
        '1': lookup_lobbyists_by_name,
        '2': lookup_lobbyist_details,
        '3': find_top_n_lobbyists,
        '4': insert_new_lobbyist_year,
        '5': set_lobbyist_salutation
    }

    #continously prompt user for commands to execute until they press x to exit
    while True:
        cmd = input("Please enter a command (1-5, x to exit): ")
        if cmd == 'x':
            break
        elif cmd in command_handlers:
            #call function for inputted command with dbConn as param
            command_handlers[cmd](dbConn)
        else:
            print("**Error, unknown command, try again...")
            print()
            

if __name__ == "__main__":
    main()
