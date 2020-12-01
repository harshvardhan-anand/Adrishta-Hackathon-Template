## Team Number 27 - IVOTED

The participants are required to fork this repository and create a public Github repository under their own username (Single repository per team). *Clone the repo on your local system and build on top of that*

The following created sections in this README.md need to be duly filled, highlighting the denoted points for the solution/implementation. 

**Please feel free to create further sub-sections in this markdown.** The idea is to understand all the particulars of your solution in a singular document.

### Project Overview

Problem: To implement an online Election Management System to conduct the college council elections ensuring the anonymity of the voter to the admin.

Solution: A full-stack secure application (I-VOTED) for conduction of council election has been **implemented and deployed** and it can be accessed here: <a href="harshvardhanpy.pythonanywhere.com">harshvardhanpy.pythonanywhere.com</a>

 - User Access = jinen@smit.smu.edu.in (psw - munnamunna)
 - Election Admin = admin@smit.smu.edu.in (psw - smitsmit) 

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
<img src="https://github.com/harshvardhan-anand/Adrishta-Hackathon-Template/blob/master/Application%20Code/resources/WhatsApp%20Image%202020-12-01%20at%2010.28.09%20PM.jpeg">
<img src='https://github.com/harshvardhan-anand/Adrishta-Hackathon-Template/blob/master/Application%20Code/resources/WhatsApp%20Image%202020-12-01%20at%2010.28.21%20PM.jpeg'>
<img src="https://github.com/harshvardhan-anand/Adrishta-Hackathon-Template/blob/master/Application%20Code/resources/WhatsApp%20Image%202020-12-01%20at%2010.28.29%20PM.jpeg">
<img src="https://github.com/harshvardhan-anand/Adrishta-Hackathon-Template/blob/master/Application%20Code/resources/WhatsApp%20Image%202020-12-01%20at%2011.01.19%20PM.jpeg"
<img src="https://github.com/harshvardhan-anand/Adrishta-Hackathon-Template/blob/master/Application%20Code/resources/WhatsApp%20Image%202020-12-01%20at%2011.01.19%20PM.jpeg">
<img src="https://github.com/harshvardhan-anand/Adrishta-Hackathon-Template/blob/master/Application%20Code/resources/WhatsApp%20Image%202020-12-01%20at%2011.01.20%20PM.jpeg">
<img src="https://github.com/harshvardhan-anand/Adrishta-Hackathon-Template/blob/master/Application%20Code/resources/WhatsApp%20Image%202020-12-01%20at%2011.01.22%20PM%20(1).jpeg">
<img src="https://github.com/harshvardhan-anand/Adrishta-Hackathon-Template/blob/master/Application%20Code/resources/WhatsApp%20Image%202020-12-01%20at%2011.01.22%20PM.jpeg">
<img src="https://github.com/harshvardhan-anand/Adrishta-Hackathon-Template/blob/master/Application%20Code/resources/WhatsApp%20Image%202020-12-01%20at%2011.25.51%20PM.jpeg">
<img src="https://github.com/harshvardhan-anand/Adrishta-Hackathon-Template/blob/master/Application%20Code/resources/WhatsApp%20Image%202020-12-01%20at%2011.27.50%20PM.jpeg">
<img src="https://github.com/harshvardhan-anand/Adrishta-Hackathon-Template/blob/master/Application%20Code/resources/WhatsApp%20Image%202020-12-01%20at%2011.28.23%20PM.jpeg">
<img src="https://github.com/harshvardhan-anand/Adrishta-Hackathon-Template/blob/master/Application%20Code/resources/WhatsApp%20Image%202020-12-01%20at%2011.28.34%20PM.jpeg">

### Team Members
List of team member names and email IDs with their contributions.
|Member Name|Email|Contribution|
|-----------|-----|------------|
|Member 1|hharshvardhanaanand@gmail.com|Backend Architecture|
|Member 2|richaverma6561@gmail.com|Frontend Designing|
|Member 3|jinenmodi810@gmail.com|frontend Designing|

### References
Online tools used - StackOverflow, django.com, bootstrap.com, quora.com
