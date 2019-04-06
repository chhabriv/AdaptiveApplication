## Starting MongoDB server

Run command : "mongod --dbpath <path to a data folder>" (For Windows)
              "./mongod --dbpath <path to a data folder>" (For *nix/ MacOS)

{create a data folder anywhere you want}

## Mongo import

1. Run the mongo server first
2. Run the command
  (For Windows)
  "mongoimport --db <database name(where you want to import)> --collection <collection name(the collection where you want to import the documents)> --file <json/bson file you want to import> < --jsonArray (in case importing a file with json array strucutre of documents)>"
  (For *nix/ MacOS)
  "./mongoimport --db <database name(where you want to import)> --collection <collection name(the collection where you want to import the documents)> --file <json/bson file you want to import> < --jsonArray (in case importing a file with json array strucutre of documents)>"

## Accessing the mongo database
  
   Run the command 
   
  1."mongo" (For Windows)
    "./mongo" (For *nix/ MacOS)    
  2. "show dbs" 
  3. "use <database name>"
  4. "show collections"
  5. "db.<collection name>.findOne()" / "db.<collection name>.find().pretty()"
  


