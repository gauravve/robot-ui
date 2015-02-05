# Robot Framework UI #

# Web UI for Robot Framework #

* Robot Framework UI aims to be a central hub a Robot Framework Hub which can then be used as a dashboard for all robot framework test runs.

* Short and long term goals with this project are :
	1. Ability to be able to store data for test reporting we will have to have information about every time a suite or a test case is run somewhere that needs to be tracked. 
	2. Ability to Edit test cases on WEB-UI
	3. Ability to connect to Git for just reading information. Hopefully then version control test cases using the UI.
	4. Ability to connect to JIRA helping testers and BAs to write better acceptance criteria and which can be automated with little or no effort
	4. Have a project and application level authorisation and authentication mechanism

* Data Model 
	1. 	Using DBBot at this stage. https://github.com/robotframework/DbBot
	2. 	Currently exposing REST API for all DBBot objects using Django REST Framework. 
	3. 	Project and Application object have been added to the DBBot model to provide an Authorization layer at a project and application level.  



## Setup ##

1. Clone the repository

		git clone https://gauravve@bitbucket.org/gauravve/robot-ui.git

1. Clean Database (optional if setting up first time)
	
		cd robot-ui
		python manage.py sqlclear robothub | python manage.py dbshell

	
3. Populate Database (sample file).

		python dbbot/run.py -b robothub.db -v -a robothub dbbot/testdata/multiple/test_output.xml -k
	

4. Install dependencies

		pip install -r requirements.txt

5. Run WSGI server (ip_address is optional)

		python manage.py runserver [ip_address]
		

### Test ###

3. API link

		http://localhost:8000/api	
		
4. API Documentation using Swagger

		http://localhost:8000/docs
		
Automated tests to be setup later
				

### Screenshots ###

1. API Root  
![](https://bytebucket.org/gauravve/robot-ui/raw/9893bc42e9ffcad524f634ed2ee241b4c06638b4/doc/Api_root.jpg)

2. Swagger Documentation   

![](https://bytebucket.org/gauravve/robot-ui/raw/9893bc42e9ffcad524f634ed2ee241b4c06638b4/doc/Swagger_UI.jpg)

### Database Model ###

![](https://bytebucket.org/gauravve/robot-ui/raw/be523947b0efb96e4be879ee14efecee690be779/doc/database_model.png)


### Authentication and Authorization ###

This feature is not implemented yet. Planning on using 

1. For Authorization : http://www.django-rest-framework.org/api-guide/authentication/
2. For Authentication : http://www.django-rest-framework.org/api-guide/permissions/
