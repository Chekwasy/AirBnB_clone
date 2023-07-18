# Airbnb Clone Project

This project aims to create a command interpreter and implement various functionalities for managing Airbnb-like objects.

## Project Description

The Airbnb Clone project focuses on building a command-line interface (CLI) that allows users to interact with and manage Airbnb objects such as listings, users, bookings, and more. The project involves creating classes for each object type and implementing CRUD (Create, Read, Update, Delete) operations.

The project involves the following tasks:

- Implementing a parent class, `BaseModel`, responsible for initialization, serialization, and deserialization of instances.
- Establishing a serialization/deserialization flow: Instance <-> Dictionary <-> JSON string <-> file.
- Creating various classes used in the AirBnB project, such as `User`, `State`, `City`, `Place`, etc., all of which inherit from `BaseModel`.
- Developing a file storage engine that abstracts storage operations.
- Writing unit tests to ensure the correctness of the classes and storage engine.

The command interpreter provides a means to manage AirBnB objects efficiently, enabling operations like creating new objects, retrieving objects, performing operations on objects, updating attributes, and deleting objects.
You can save 

## Requirements

- The first line of all the files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the project folder, is mandatory
- The code should adhere to the pycodestyle style guide
- The length of files will be tested using the wc command
- All modules, classes, and functions should be properly documented

## Usage

To use the Airbnb Clone command interpreter, follow the steps below:

1. Open your terminal or command prompt.

2. Navigate to the directory where the `console.py` script is located.

3. Run the following command to start the command interpreter:

   ```bash
   $ ./console.py
   ```
4. Once the command interpreter is running, you can start entering commands. The available commands are:
    - `quit` or `EOF`: Exits the program.
    - `help`: Shows the available commands and their descriptions.
    - `create <class_name>`: Creates a new instance of the specified class and saves it.
    - `show <class_name> <id>`: Prints the string representation of an instance based on the class name and ID.
    - `destroy <class_name> <id>`: Deletes an instance based on the class name and ID.
    - `all` or `all <class_name>`: Prints all instances or instances of a specific class.
    - `update <class_name> <id> <attribute_name> <attribute_value>`: Updates an instance's attribute based on the class name, ID, attribute name, and attribute value.
5. To execute a command, type it in the command prompt and press Enter. For example, to exit from the program you would enter:
   ```bash
   (hbnb) quit
   ```

## Project Files
The project consists of the following files:
- [x] [console.py](./console.py): Contains the command interpreter implementation.
- [x] [models/base_model.py](./models/base_model.py): Defines the BaseModel class responsible for initialization, serialization, and deserialization of instances.
- [x] [models/user.py](./models/user.py): Defines the User class that inherits from BaseModel.
- [x] [models/state.py](./models/state.py): Defines the State class that inherits from BaseModel.
- [x] [models/city.py](./models/city.py): Defines the City class that inherits from BaseModel.
- [x] [models/amenity.py](./models/amenity.py): Defines the Amenity class that inherits from BaseModel.
- [x] [models/place.py](./models/place.py): Defines the Place class that inherits from BaseModel.
- [x] [models/review.py](./models/review.py): Defines the Review class that inherits from BaseModel.
- [x] [models/__init__.py](./models/__init__.py): Initializes the models package

## Testing
The project includes unit tests to ensure the functionality of the implemented classes and operations. To run the tests, execute the following command in the terminal:

```bash
$ python -m unittest discover tests/
```

### Next Steps
The command interpreter serves as the foundation for the AirBnB Clone project. In the upcoming steps, we will continue building upon this foundation by incorporating HTML/CSS templating, database storage, API integration, and front-end development.
<br><br>


## Contributors
- [Richard Chukwuchekwa](https://github.com/Chekwasy)
- [Caleb Nyachwaya](https://github.com/CalebNyachwaya)
___
