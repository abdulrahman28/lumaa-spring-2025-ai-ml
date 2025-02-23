# Lumaa Intern Code Challenge
Code Challenge Work Project: Movie Recommendation System

* Created a Virtual environment for the project (To include all the libraries I need for the project exclude other libraries): interncodechallenge. The virtual environment was created to ensure all the requirements are solely for the project.

The movie dataset is from a public repository Kaggle: https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system/data

# Algorithm development
* The user input was converted to TF-IDF vectors.
* A cosine similarity algorithm was adopted to process the user input and movie descriptions.
* The algorithm was implemented in movie_recommendation.py

# Python programming language was used to develop the project
* I started the program development as a command line interface (CLI) (i.e. main.py), I ensured the program is:
* Simple and easy to read by adding comments and explaining the process in the comments.
* Functional and reliable by testing the program several times.
* User-friendly by making it as simple as possible.
* Scalable, modular, extensible, well-structured, and easy to maintain and understand: datacleaning.py process the data input, and movie_recommendation.py handles the recommendation which enables the development and improvement of each section.
* Good performance and isolates assumptions. The program can fail gracefully during exit and address security vulnerabilities.
* Execution time was included for evaluating the movie recommendation algorithm's performance, which is very important when improving the algorithm. The developers or researchers will project the running performance on different interfaces.

# Graphical User Interface

* To ensure the program is User-friendly and robust, I introduced the graphical user interface (GUI) for users to easily interact with the program (main_gui.py).
* The functions from the CLI were reused for the GUI, making it extensible and scalable.
* I subjected it to several tests to ensure its efficiency and reliability.
* The program code has been compiled as an executable program and can be distributed for User use. The executable program is main_gui.exe and a backup copy is at dist/main_gui.exe.
* Ensure the movies.csv is in the same folder as the executable file when running and more movies can be added to improve the recommendation algorithm.
* The average execution time is 1.6 s.

# Web application for Remote access
* The program was deployed as a web application using HTML, CSS for the front-end, and Flask python framework for the back-end development.
* The program code for the web application is in the folder (web app). The web app is deployed on pythonanywhere web server for testing and ensuring its functionality. 
* The application has been deployed and is currently active: [pythonanywhere with ](https://abdul58.pythonanywhere.com/) 
* I ensured to keep it simple and user-friendly and did several tests to ensure the full operation of the project.
* The web server is very slow since it is free, and the available resources are very limited. The average execution  time for the web app is 13 s.

# Future update
* The execution time for the web app can be reduced by using an optimized paid service.
* Improving the movie recommendation algorithm using deep learning algorithms such as neural network.
* Deploying database for the movie dataset and user information and preferences.
* Developing cross-platform applications such as mobile apps using Swift for iOS, java for Android, and Visual C# for Windows that can communicate with the web server using API such as REST API.
* Improve User-friendliness, conduct more testing, search for vulnerabilities, and improve the application.
* Keep updating the application and improving the movie recommendation algorithm!!!

# Video on the program operation, explanation and code:

 https://wmich-my.sharepoint.com/:f:/g/personal/cjw2577_wmich_edu/Eh8324OwjY1DpYYj2gR31_4BkZw30qHMKU7SV2hGa6_vMg?e=NpGEU8

