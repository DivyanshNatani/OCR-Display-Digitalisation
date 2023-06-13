Welcome to OCR Display Digitalisation repository.

This is my B.Tech project done under Prof. Mani Bhushan, Department of Chemical Engineering, IIT Bombay

### Aim of the project

This projects aims to completely digitalise the currently man-handelled displays (where the recording of data is done manually and stored physically) at various Chemical Industries using techniques of Computer Vision. 

Detailed [report](Report.pdf) and [presentation](Presentation.pdf) have been added for more details.

### Workflow

This project involves three part - 
- Taking image from camera to system
-- A working IP Camera is required and should be connected to same wifi network as the processing system
-- IP camera provides local API links to access image from live video stream captured by camera
-- A python file is used to request this API and retrieve image(and saves it for data saving purpose)
- Processing image to identify and retrieve data
-- This is the Computer Vision part where the image file is used to retrieve instrument reading and returning a numerical data
- Store data in database
-- The data retrieved is sent to database via API service and further retriving information and trends from this data can be done at this level. For this project, we have chosen Django framework with SQLite database for information storage

### File Discription

Initially the repositary is devided into two folders
- DBMS
It contains all Django related files and database files
- Seven-seg
This folder contains all image processing trial notebook files
- Python Server
This folder contains file pertaining to Part 1 and 2 of the project (Details of file inside)