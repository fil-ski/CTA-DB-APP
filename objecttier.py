#-------------------------------------------
# Project 2: Chicago Lobbyist Database App
# Course: CS 341, Spring 2024, UIC
# System: Visual Studio Code on Windows
# Author: Filip Petrev
# Objecttier Layer of the application
# Builds Lobbyist-related objects from data retrieved through 
# the data tier.
# Credit to original author Ellen Kidane for the starter code
#-------------------------------------------
import datatier


"""
A class used to represent a Lobbyist.

Attributes:
    _Lobbyist_ID (int): An integer ID that uniquely identifies the lobbyist.
    _First_Name (str): The first name of the lobbyist.
    _Last_Name (str): The last name of the lobbyist.
     _Phone (str): The phone number of the lobbyist.

    Methods:
        Lobbyist_ID (property): Returns the lobbyist's ID.
        First_Name (property): Returns the lobbyist's first name.
        Last_Name (property): Returns the lobbyist's last name.
        Phone (property): Returns the lobbyist's phone number.
"""
class Lobbyist:
    def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone):
        """
        The constructor for Lobbyist class.

        Parameters:
            Lobbyist_ID (int): The unique identifier for the lobbyist.
            First_Name (str): The first name of the lobbyist.
            Last_Name (str): The last name of the lobbyist.
            Phone (str): The contact phone number for the lobbyist.
        """
        self._Lobbyist_ID = Lobbyist_ID
        self._First_Name = First_Name
        self._Last_Name = Last_Name
        self._Phone = Phone

    @property
    def Lobbyist_ID(self):
        """Gets the lobbyist's ID"""
        return self._Lobbyist_ID

    @property
    def First_Name(self):
        """Gets the lobbyist's first name"""
        return self._First_Name

    @property
    def Last_Name(self):
        """Gets the lobbyist's last name"""
        return self._Last_Name

    @property
    def Phone(self):
        """Gets the lobbyist's phone number"""
        return self._Phone



"""
A class used to represent the detailed information of a Lobbyist.

Attributes:
    _Lobbyist_ID (int): Unique identifier for the lobbyist.
    _Salutation (str): Salutation of the lobbyist (e.g., Mr., Mrs., Dr.).
    _First_Name (str): First name of the lobbyist.
    _Middle_Initial (str): Middle initial of the lobbyist.
    _Last_Name (str): Last name of the lobbyist.
    _Suffix (str): Suffix for the lobbyist (e.g., Jr., Sr., III).
    _Address_1 (str): Primary street address for the lobbyist.
    _Address_2 (str): Secondary street address for the lobbyist.
    _City (str): City of the lobbyist's address.
    _State_Initial (str): State initials of the lobbyist's address.
    _Zip_Code (int): Zip code of the lobbyist's address.
    _Country (str): Country of the lobbyist's address.
    _Email (str): Email address of the lobbyist.
    _Phone (str): Contact phone number of the lobbyist.
    _Fax (str): Fax number of the lobbyist.
    _Years_Registered (list): List of years the lobbyist was registered.
    _Employers (list): List of lobbyist's employers.
    _Total_Compensation (float): Total compensation received by the lobbyist.

    Methods:
        All properties have getter methods to return individual attributes.
"""
class LobbyistDetails:
    

    def __init__(self, Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix,Address_1, Address_2, City, State_Initial, Zip_Code, Country, Email, Phone, Fax,Years_Registered, Employers, Total_Compensation):
        """
        The constructor for LobbyistDetails class.

        Parameters:
            Lobbyist_ID (int): The unique identifier for the lobbyist.
            Salutation (str): The salutation of the lobbyist.
            First_Name (str): The first name of the lobbyist.
            Middle_Initial (str): The middle initial of the lobbyist.
            Last_Name (str): The last name of the lobbyist.
            Suffix (str): The suffix if applicable for the lobbyist.
            Address_1 (str): The primary street address for the lobbyist.
            Address_2 (str): The secondary street address for the lobbyist.
            City (str): The city of the lobbyist's address.
            State_Initial (str): The state initials of the lobbyist's address.
            Zip_Code (int): The zip code of the lobbyist's address.
            Country (str): The country of the lobbyist's address.
            Email (str): The email address of the lobbyist.
            Phone (str): The contact phone number of the lobbyist.
            Fax (str): The fax number of the lobbyist.
            Years_Registered (list): The list of years the lobbyist was registered.
            Employers (list): The list of employers for the lobbyist.
            Total_Compensation (float): The total compensation received by the lobbyist.
        """
        self._Lobbyist_ID = Lobbyist_ID
        self._Salutation = Salutation
        self._First_Name = First_Name
        self._Middle_Initial = Middle_Initial
        self._Last_Name = Last_Name
        self._Suffix = Suffix
        self._Address_1 = Address_1
        self._Address_2 = Address_2
        self._City = City
        self._State_Initial = State_Initial
        self._Zip_Code = Zip_Code
        self._Country = Country
        self._Email = Email
        self._Phone = Phone
        self._Fax = Fax
        self._Years_Registered = Years_Registered
        self._Employers = Employers
        self._Total_Compensation = Total_Compensation

    # Following are the property methods for each attribute.
    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID

    @property
    def Salutation(self):
        return self._Salutation

    @property
    def First_Name(self):
        return self._First_Name

    @property
    def Middle_Initial(self):
        return self._Middle_Initial

    @property
    def Last_Name(self):
        return self._Last_Name

    @property
    def Suffix(self):
        return self._Suffix

    @property
    def Address_1(self):
        return self._Address_1

    @property
    def Address_2(self):
        return self._Address_2

    @property
    def City(self):
        return self._City

    @property
    def State_Initial(self):
        return self._State_Initial

    @property
    def Zip_Code(self):
        return self._Zip_Code

    @property
    def Country(self):
        return self._Country

    @property
    def Email(self):
        return self._Email

    @property
    def Phone(self):
        return self._Phone

    @property
    def Fax(self):
        return self._Fax

    @property
    def Years_Registered(self):
        return self._Years_Registered

    @property
    def Employers(self):
        return self._Employers

    @property
    def Total_Compensation(self):
        return self._Total_Compensation



"""
A class used to represent a lobbyist along with their compensation and client information.

Attributes:
    _Lobbyist_ID (int): Unique identifier for the lobbyist.
    _First_Name (str): First name of the lobbyist.
    _Last_Name (str): Last name of the lobbyist.
    _Phone (str): Contact phone number of the lobbyist.
    _Total_Compensation (float): Total compensation amount received by the lobbyist.
    _Clients (list of str): List of clients associated with the lobbyist.

    Methods:
        Each attribute has a corresponding property getter method that returns its value.
"""
class LobbyistClients:
   

    def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone, Total_Compensation, Clients):
        """
        The constructor for LobbyistClients class.

        Parameters:
            Lobbyist_ID (int): The unique identifier for the lobbyist.
            First_Name (str): The first name of the lobbyist.
            Last_Name (str): The last name of the lobbyist.
            Phone (str): The contact phone number of the lobbyist.
            Total_Compensation (float): The total compensation received by the lobbyist.
            Clients (list of str): The list of clients associated with the lobbyist.
        """
        self._Lobbyist_ID = Lobbyist_ID
        self._First_Name = First_Name
        self._Last_Name = Last_Name
        self._Phone = Phone
        self._Total_Compensation = Total_Compensation
        self._Clients = Clients
        
    #Following are the property methods for each attribute.    
    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID

    @property
    def First_Name(self):
        return self._First_Name

    @property
    def Last_Name(self):
        return self._Last_Name

    @property
    def Phone(self):
        return self._Phone

    @property
    def Total_Compensation(self):
        return self._Total_Compensation

    @property
    def Clients(self):
        return self._Clients



"""
Calculate the total number of lobbyists present in the LobbyistInfo table.

Function executes a SQL query that counts all entries in the LobbyistInfo. Uses datatier
layer function select_one_row to retrieve data.

Parameters:
    dbConn: The database connection object
Returns:
    An integer representing the total number of lobbyists. If an error occurs during 
    the database query execution, -1 is returned to indicate the failure.
 """
def num_lobbyists(dbConn):
    sql = "SELECT COUNT(*) FROM LobbyistInfo"
    result = datatier.select_one_row(dbConn, sql)
    return result[0] if result else -1



"""
Calculate the total number of employers listed in the EmployerInfo table.

Runs a SQL query to count all entries in the EmployerInfo table. Uses datatier
layer function select_one_row to retrieve data.

Parameters:
    dbConn: The database connection object
Returns:
    number of employers in the database
    If an error occurs, the function returns -1
"""
def num_employers(dbConn):
    sql = "SELECT COUNT(*) FROM EmployerInfo"
    result = datatier.select_one_row(dbConn, sql)
    return result[0] if result else -1



"""
Retrieves the total number of clients from the ClientInfo table.

Runs a SQL query to count all entries in the ClientInfo table. Uses datatier
layer function select_one_row to retrieve data.

Parameters:
    dbConn: The database connection object 

Returns:
    number of clients in the database
    If an error occurs, the function returns -1
"""
def num_clients(dbConn):
    sql = "SELECT COUNT(*) FROM ClientInfo"
    result = datatier.select_one_row(dbConn, sql)
    return result[0] if result else -1



"""
Gets and returns all lobbyists whose first or last name are "like"
the pattern. Patterns are based on SQL, which allow the _ and % 
wildcards.

Parameters:
    dbConn: The database connection object 
    pattern: string containing potential sql wild cards and lobbyist name used as param in datatier select_n_rows function

Returns:
    list of lobbyists in ascending order by ID; 
    an empty list means the query did not retrieve
    any data (or an internal error occurred, in
    which case an error msg is already output).
"""
def get_lobbyists(dbConn, pattern):
    sql = """
    SELECT Lobbyist_ID, First_Name, Last_Name, Phone
    FROM LobbyistInfo
    WHERE First_Name LIKE ? OR Last_Name LIKE ?
    ORDER BY Lobbyist_ID ASC
    """
    #store as a list in order to query both first or last name
    parameters = [pattern, pattern]
    result = datatier.select_n_rows(dbConn, sql, parameters)
    return [Lobbyist(*row) for row in result] if result is not None else []



"""
Gets and returns details about the given lobbyist
the lobbyist id is passed as a parameter

Parameters:
    dbConn: The database connection object 
    lobbyist_id: int containing the lobbiest id to querry for

Returns:
    if the search was successful, a LobbyistDetails object
    is returned. If the search did not find a matching
    lobbyist, None is returned; note that None is also 
    returned if an internal error occurred (in which
    case an error msg is already output).
"""
def get_lobbyist_details(dbConn, lobbyist_id):
    #SQL query to select lobbyist details by ID
    sql = '''
    SELECT Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, 
    Address_1, Address_2, City, State_Initial, ZipCode, Country, Email, Phone, Fax
    FROM LobbyistInfo
    WHERE Lobbyist_ID = ?
    '''
    #execute the query with the provided lobbyist ID param
    result = datatier.select_one_row(dbConn, sql, [lobbyist_id])
    
    #create a LobbyistDetails object with additional queries for Years_Registered and Employers if a result is found
    if result:
        #extract years registered
        years_sql = "SELECT Year FROM LobbyistYears WHERE Lobbyist_ID = ? ORDER BY Year"
        years_result = datatier.select_n_rows(dbConn, years_sql, [lobbyist_id])
        years_registered = [year[0] for year in years_result] if years_result else []

        #querry to extract distinct employer names based on the lobbiest id via joining LobbyistAndEmployer and EmployerInfo tables
        employers_sql = '''
        SELECT DISTINCT Employer_Name
         FROM EmployerInfo
         JOIN LobbyistAndEmployer ON EmployerInfo.Employer_ID = LobbyistAndEmployer.Employer_ID
         WHERE LobbyistAndEmployer.Lobbyist_ID = ?
         ORDER BY Employer_Name ASC
        '''
        
        #executes the employer querry with the provided lobbyist_id param using the datatier layer select_n_rows function
        employers_result = datatier.select_n_rows(dbConn, employers_sql, [lobbyist_id])
        employers = [employer[0] for employer in employers_result] if employers_result else []

        #extract total compensation
        compensation_sql = "SELECT SUM(Compensation_Amount) FROM Compensation WHERE Lobbyist_ID = ?"
        compensation_result = datatier.select_one_row(dbConn, compensation_sql, [lobbyist_id])
        total_compensation = float(compensation_result[0]) if compensation_result and compensation_result[0] is not None else 0.0

        #create and return the LobbyistDetails object
        #formatted to ensure the order of parameters matches the class constructor
        return LobbyistDetails(
            result[0],  # Lobbyist_ID
            result[1],  # Salutation
            result[2],  # First_Name
            result[3],  # Middle_Initial
            result[4],  # Last_Name
            result[5],  # Suffix
            result[6],  # Address_1
            result[7],  # Address_2
            result[8],  # City
            result[9],  # State_Initial
            result[10], # ZipCode
            result[11], # Country
            result[12], # Email
            result[13], # Phone
            result[14], # Fax
            years_registered,  # Years_Registered
            employers,         # Employers
            total_compensation # Total_Compensation
        )
    
    #return None if the result is not found or an error occurred
    return None


         
"""
gets and returns the top N lobbyists based on their total 
compensation, given a particular year

Parameters:
    dbConn: The database connection object 
    N: number of rows to retrive from the database:
    year: the year to querry for
    

Returns:
    returns a list of 0 or more LobbyistClients objects;
    the list could be empty if the year is invalid. 
    An empty list is also returned if an internal error 
    occurs (in which case an error msg is already output).
"""
def get_top_N_lobbyists(dbConn, N, year):
    #string with the SQL query to fetch the top N lobbyists based on total compensation for the given year
    sql = '''
    SELECT li.Lobbyist_ID, li.First_Name, li.Last_Name, li.Phone, SUM(c.Compensation_Amount) as Total_Compensation
    FROM LobbyistInfo li
    JOIN Compensation c ON li.Lobbyist_ID = c.Lobbyist_ID
    WHERE strftime('%Y', c.Period_Start) <= ? AND strftime('%Y', c.Period_End) >= ?
    GROUP BY li.Lobbyist_ID, li.First_Name, li.Last_Name, li.Phone
    ORDER BY Total_Compensation DESC, li.Last_Name ASC
    LIMIT ?
    '''
    
    #execute the query with the given year and limit N
    result = datatier.select_n_rows(dbConn, sql, [year, year, N])
    
    #create a list of LobbyistClients objects if results are found after executing the querry with the datatier function
    if result:
        top_lobbyists = [] #declare list to store the lobbyists objects beforing iterating the results of the querry
        for row in result:
            #for each lobbyist, fetch the list of unique clients for the given year
            clients_sql = '''
            SELECT ci.Client_Name
            FROM ClientInfo ci
            JOIN Compensation c ON ci.Client_ID = c.Client_ID
            WHERE c.Lobbyist_ID = ? AND strftime('%Y', c.Period_Start) <= ? AND strftime('%Y', c.Period_End) >= ?
            GROUP BY c.Client_ID
            ORDER BY ci.Client_Name
            '''
            #execute the query with the given lobbyist ID and year
            clients_result = datatier.select_n_rows(dbConn, clients_sql, [row[0], year, year])
            clients = [client[0] for client in clients_result] if clients_result else []
            
            #create LobbyistClients object with the unique list of clients
            lobbyist = LobbyistClients(row[0], row[1], row[2], row[3], float(row[4]), clients)
            top_lobbyists.append(lobbyist)
        
        return top_lobbyists
    
    #return an empty list if no results are found or if an error occurs
    return []



"""
Inserts the given year into the database for the given lobbyist.
It is considered an error if the lobbyist does not exist and the year is not inserted.

Parameters:
    dbConn: The database connection object 
    lobbyist_id: int of lobbyist id to insert data for
    year: the year add in the database for the lobbyist
    

Returns:
    returns a list of 0 or more LobbyistClients objects;
    the list could be empty if the year is invalid. 
    An empty list is also returned if an internal error 
    occurs (in which case an error msg is already output).
"""
def add_lobbyist_year(dbConn, lobbyist_id, year):
    #assert that the provided lobbyist_id actually maps to a lobbyist in the table
    lobbyist_exists_sql = "SELECT COUNT(*) FROM LobbyistInfo WHERE Lobbyist_ID = ?"
    result = datatier.select_one_row(dbConn, lobbyist_exists_sql, [lobbyist_id])
    if result and result[0] == 1: #make sure the result is not empty and there is no error
        
        #Action querry to insert the given year and lobbyist_ID parameters of the function into the LobbyistYears table
        insert_year_sql = "INSERT INTO LobbyistYears (Lobbyist_ID, Year) VALUES (?, ?)"
        
        #check if the year already exists for the lobbyist to avoid duplicates
        year_exists_sql = "SELECT COUNT(*) FROM LobbyistYears WHERE Lobbyist_ID = ? AND Year = ?"
        year_exists_result = datatier.select_one_row(dbConn, year_exists_sql, [lobbyist_id, year])
        
        if year_exists_result and year_exists_result[0] == 0:
            #year does not exist, insert the new year with the datatier perform action function
            rows_modified = datatier.perform_action(dbConn, insert_year_sql, [lobbyist_id, year])
            return 1 if rows_modified > 0 else 0
        else:
            #this case means year already exists for this lobbyist
            return 0
    else:
        #lobbyist does not exist or an error occurred during the check
        return 0



"""
Sets the salutation for the given lobbyist.
If the lobbyist already has a salutation, it will be replaced by
this new value. Passing a salutation of "" effectively 
deletes the existing salutation. It is considered an error
if the lobbyist does not exist the salutation is not set.

Parameters:
    dbConn: The database connection object 
    lobbyist_id: int of lobbyist id to update data for
    salutation: the string of salutation to update for given lobbyist
    
Returns:
    1 if the salutation was successfully set,
    0 if not (e.g. if the lobbyist does not exist, or if
    an internal error occurred).
"""
def set_salutation(dbConn, lobbyist_id, salutation):
    #check if the lobbyist exists using the datatier layer functionality and passing the lobbyist ID as param for the querry
    lobbyist_exists_sql = "SELECT COUNT(*) FROM LobbyistInfo WHERE Lobbyist_ID = ?"
    result = datatier.select_one_row(dbConn, lobbyist_exists_sql, [lobbyist_id])
    
    if result and result[0] == 1:
        #after making sure that the lobbyist exists and there was no error while executing querry, update the salutation
        update_salutation_sql = "UPDATE LobbyistInfo SET Salutation = ? WHERE Lobbyist_ID = ?"
        rows_modified = datatier.perform_action(dbConn, update_salutation_sql, [salutation, lobbyist_id])
        
        return 1 if rows_modified > 0 else 0 #makes sure the update querry succesfully modifes the database
    else:
        #lobbyist does not exist or an error occurred during the check
        return 0
