## HBNB Console: Manage Your AirBnB Clone Objects Easily

This guide introduces the HBNB Console, a command-line tool for managing your AirBnB clone project. It empowers you to:

* **Create new objects:** Generate new entities like users and places.
* **Retrieve existing objects:** Access stored information about users, places, and more.
* **Perform operations:** Analyze data, calculate statistics, and manipulate objects.
* **Update object attributes:** Modify details associated with objects.
* **Delete objects:** Remove objects from your project.

### Getting Started

**Usage:**

1. Open your terminal.
2. Run the console: `./console.py` or `python3 console.py`.
3. The prompt `(hbnb)` signifies a ready console.

### Available Commands

* **create <class name>**: Creates a new object of a specific class (e.g., `create User`).
* **show <class name> <id>**: Displays details of an object based on its class and ID.
* **destroy <class name> <id>**: Removes an object from the project.
* **all**: Lists all objects (optionally filtered by class).
* **update <class name> <id> <attribute name> "<attribute value>"**: Updates an object's attribute with a new value.
* **quit or EOF**: Exits the console.

**Example Usage:**

```
(hbnb) create User
(hbnb) show User user_id
(hbnb) all User
(hbnb) update User user_id email "aibnb@holbertonschool.com"
(hbnb) destroy User user_id
```

### Contributing

We encourage contributions to the HBNB Console! Fork the repository, create a branch for your changes, and submit a pull request.

### Supported Classes

* **BaseModel:** Serves as the foundation for other classes, defining common attributes and methods.
* **User:** Represents users within your AirBnB clone system.
* **State:** Stores information about states or regions.
* **City:** Provides details about cities within specific states.
* **Amenity:** Defines various amenities offered by places.
* **Place:** Represents individual places users can book on your platform.
* **Review:** Captures feedback and ratings associated with places.

