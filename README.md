# Chicago Lobbyist Database App

## Overview
This application facilitates indirect interactions with the Chicago Lobbyists database through a console-based user interface. Users can perform various operations such as looking up lobbyists by name, viewing detailed information about a lobbyist, finding the top N lobbyists by total compensation for a given year, registering an existing lobbyist for a new year, and setting the salutation for a lobbyist.

## Features
- **Lookup Lobbyists by Name**: Allows users to search for lobbyists using their first or last names, with support for SQL wildcards.
- **Detailed Lobbyist Information**: Users can view detailed information about a lobbyist, including contact details and registration history.
- **Top N Lobbyists by Compensation**: Finds the top N lobbyists based on total compensation for a specified year.
- **Register Lobbyist for New Year**: Allows adding a lobbyist to the database for a new registration year.
- **Set Salutation for a Lobbyist**: Users can update or set the salutation for a lobbyist.

## Installation
To set up the Chicago Lobbyist Database App, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/fil-ski/CTA-DB-APP.git
2. Navigate to the project directory:
    ```bash
   cd CTA-DB-APP
3. To start the application
   ```bash
   python main.py

## How to Use
Below are step-by-step instructions for each feature of the application.

### **Lookup Lobbyists by Name**
1. **Enter the command `1` when prompted.**
2. **Input the name or partial name with wildcards.**
3. **View the list of matching lobbyists.**

![Usage of Lookup Lobbyists](Images/command1.png)

### **Detailed Lobbyist Information**
1. **Enter the command `2` when prompted.**
2. **Input the lobbyist ID to fetch their detailed profile.**

![Detailed Information View](Images/command2.png)

### **Top N Lobbyists**
1. **Enter the command `3` when prompted.**
2. **Input the number `N` and the year to retrieve the top N lobbyists for that year.**

![Top N Lobbyists](Images/command3.png)

### **Register a Lobbyist**
1. **Enter the command `4` when prompted.**
2. **Provide the lobbyist ID and the new year they should be registered for.**

### **Set Salutation**
1. **Enter the command `5` when prompted.**
2. **Input the lobbyist ID and the new salutation.**

### **Screenshots**
Include screenshots of your application in use here.








