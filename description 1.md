# GCP more realistic exemple

- Store it as a repo in our AzDO project
- Cloud function that lists products or adds products to a catalog
- Function will authenticate with our PostgreSQL using a secret stored in our GCP secret manager
- The responses of the function will be in json, like before
- Region, same as before
- Function size/power, same as before
- Security: Allow unautheticated requests (open on the cloud run if needed)

## Listing products
- When we want to list, we want to use the http method GET
- Returns: a json list with the products and their details
- If possible, list means we will run a SELECT query against the Database

## Adding one product
- When we want to add a product, we want to use http method POST
- For add, a status (insertion went ok) and a copy of the added product
- If possible, list means we will run a INSERT SQL statement against the Database

# Testing
We will need a client to run some requets and see if they work

# Important notes
1. Everyone will be using the same DB

## Client python:
    - just sends http request to a cloud function

## Initial local function
    - will do what our function will later do

## Phase 1 - my_poc_function(action, product) 
- Connects to postgreSQL (install python package for this)
- Don't worry about requets at all
- Write a python file that connects to postgreSQL and:
    1. lists all products in a table (name to be provided)
    2. adds a product to the same table
- Make sure you never send the user and password to your repo (they should live in a file that is gitignored): usually either a .env/.ini file with the passwords that is loaded by pyhon but that is ignored when pushing
- Receives an input:
    - action: either 'list' or 'add'
    - if it is add, has to also receive a product (name, description, cost_of_manufature)
- Returns(as json string):
    - for list returns a list of all products
    - for 'add' returns a status (insertion went ok) and a copy of the added product

## Phase 2 - adapt it to run as a gcp function
