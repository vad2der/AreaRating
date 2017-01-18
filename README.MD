Area Rating App
===================

How To Run:
-------------
Python should be installed on the system to use `pip` for modules installation.
Clone the repository. Git has to be installed. In Git Bash navigate to the folder you would like to store the repository (use `cd` command) type:
`git clone https://github.com/vad2der/AreaRating`

Recomentadion is to use virtual environment. Traditionally, it is to be installed in a folder right beside our repository.
Once been installed, activate it. This app uses python 2.7. 

navigate into repository folder:
`cd AreaRating`

install necessary python modules by:
`pip install -r requirements.txt`

To run the app type:
`python wsgi.py`

Example request:
-------------
`http://localhost:5000/api/v1/coord/?lat=60.61&lng=62.28`

Anticipated type of response:
-------------
`{
    "area_code": 6, 
    "lat": 60.61, 
    "lng": 62.28
}`