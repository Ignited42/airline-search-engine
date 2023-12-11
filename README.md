# airline-search-engine
WSU Fall 2023, Project

## Executing the program
**Prerequisites**
1. Install MongoDB Community Server, preferably by its default settings
2. Set its bin as part of the PATH environment variable.  (Example path: C:\Program Files\MongoDB\Server\7.0\bin)
3. Run the `start_mongodb_server.bat`` file on cmd.

Note: In case that the local database doesn't start, run `repair_mongodb_server.bat`.


**Running the program**

To run the program, you can double-click on the `main.bat`` file.

For developers, make sure you've downloaded your JSON credentials from the RealTime DB and save it in the current working directory as credentials.json:
```
./credentials.json
```

**Stopping the server**
1. Open MongoDB Compass.
2. Connect to the server (localhost:27017)
3. Open mongosh terminal at the bottom of the screen.
4. Run the following:
   - use admin
   - db.shutdownServer()
