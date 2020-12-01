## Team Number \27 - \IVOTE

The participants are required to fork this repository and create a public Github repository under their own username (Single repository per team). *Clone the repo on your local system and build on top of that*

The following created sections in this README.md need to be duly filled, highlighting the denoted points for the solution/implementation. 

**Please feel free to create further sub-sections in this markdown.** The idea is to understand all the particulars of your solution in a singular document.

### Project Overview

Problem: To implement an online Election Management System to conduct the college council elections ensuring the anonymity of the voter to the admin.

Solution: A full-stack secure application (I-VOTED) for conduction of council election has been implemented and deployed and it can be accessed here: <LINK FOR THE DEMO>

### Solution Description

The application is made in Python using the django framework. The application architechture is robust and contains all the necessary security features given in the problem statement.No information of the voters is being stored in the database thus ensuring complete anonymity of the voters. It consists of four views, three of which are i.e.- Election-Admin, Candidate and Voter. Apart from these, there is a fourth view which allows the application to be controlled by a Super-Admin who will possess the necessary rights to create and modify the election-admin. The implementation of super-admin gives the required flexibility to the application without compromising its security. Hence the app is fully scalable and can be modified easily to implement an election management system for any other scenario. The architecture design and other technical details are as follows.

#### Architecture Diagram

<img src="https://github.com/harshvardhan-anand/Adrishta-Hackathon-Template/blob/master/Application%20Code/DataFlow.png">

#### Technical Description

An overview of:
* Technologies Used - Django, JavaScript, HTML, CSS

* Setup/Installations - 
-- To install Django<br>
1. Install Python
2. pip install django

* Instructions to run the submitted code - python manage.py runserver

### Screenshots
Affix the relevant screenshots of the developed project here.

### Team Members
List of team member names and email IDs with their contributions.
|Member Name|Email|Contribution|
|-----------|-----|------------|
|Member 1|mem1@example.com|Backend Architecture|
|Member 2|mem2@example.com|Frontend Designing|
|Member 3|mem3@example.com|frontend Designing|

### References
Affix links to the online tools/repositories/blogs etc., which helped you along the development of the project
