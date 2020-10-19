# Multi-DIC Project
The objective of this project is to extend the Python code from two dimensional deformation measurement to three dimensional derformation measurement.Our project was supposed to perform the same functionality as that of given MATLAB code. 

## Set up
First run `python3 -m venv venv`  to create a virtual environment.

Then run `python3 -m pip install -r requirements.txt` to install the necessary packages into the virtual environment.

## Using by a program
For step-1, the code for calculating the 11 DLT parameters is in step1 folder. It also includes the images that we will use to calculate the 11 DLT parameters.
For step-2. the code for calculating the 2D-DIC is in step2 folder. It also incldes the images that will match the points in ROI and then will return the 2D coordinates.
For step-3, the code for calculating the 3D reconstruction is in step3 folder. It includes
For step-4, the code for calculating the Post processing is in step4 folder.


## Using by command line
For each step, a helpful script is included in .py format. To run the code, open the command line interface and type in the command to run the code. For an instance for step-1, type in the command like "python step1.py". then the interface will ask you for step by step working of the code.


[Track of teamwork](https://trello.com/b/eWc2PCcY/multidic)

[Project timeline](https://www.tiki-toki.com/timeline/entry/1476718/MultiDIC/)

## Reference
[2D-DIC python code](https://github.com/texm/PReDIC)

[muDIC - a toolkit for 2d-DIC](https://mudic.readthedocs.io/en/latest/)

[MultiDIC MATLAB toolbox](https://github.com/MultiDIC/MultiDIC)
