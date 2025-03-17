# Control Module

This is an (incomplete) Flask app to communicate with the rover directly. The application will collect required data from the user and will relay the information to the rover's Arduino/Raspberry Pi controller using Python. Imagine this as a control room for the rover. Use necessary files and code from the `Sensor Integration/` as required.

## Working Idea
Flask is a light-weight web framework that can be used to build simple web applications based on python. Before running the code, make sure to install Flask on a virual environment. A brief description of the files used are: 
- `app.py`: Sets up a server on the local machine to host the main application. The inital plan was to use sliders and numerical input boxes to control motor angles and other parameters.
- `templates/`: Contains all the HTML templates for the front-end.
- `web/`: Contains any required data that the application needs to read/write onto.

## Scope of Improvement
- `requirements.txt` file to be added.
