
### Sarah McLaughlin
### Assignment 2: Requirements Analysis


## Different Types of Users of the software system and the Activities they will perform:

## ADMIN users: Professors, some TAs
	(Manage course and structure)

	# Create assignments/quizzes/tests/etc.
		# Constraints:
		- Formatted questions for tests/quizzes/etc.
			- In class or online? 
				- On Canvas platform?
				- Link somewhere else?
		- Solutions/answers provided or not
		- Additional links/resource links
		- Able to store different file types through upload
			- PDF, DOC, PPT, EXCEL, text, etc. 
		- Grade calculations
			- Amount/percent worth
		- Store all past and upcoming information/assignments
		- Create calendar events
			- Due dates, exams, etc.
		- Storage necessary that can hold different types of files

	# Edit assignments/quizzes/tests/etc.
		- Due date, document, location of assignment, syllabus, links, etc.
		
		# Constraints:
		- Altering calendar dates and events
		- Change where a document or file is stored 
		- Edit visable text on the form itself
		- No ability to alter HTML/CSS code and backend code
		- Editing hardware able to make changes

	# Delete assignments/quizzes/tests/etc.
		# Constraints:
		- Removed from database or just marked as inactive
		- Deletions of entire course or files
		- Removal of events or files

	# Grade assignments/quizzes/tests/etc.
		# Constraints:
		- Mark grades for each student
		- Stored and viewable for all the specific student and ITIL users
		- Calculations of grades done 
		- Grade saved within 

	# Submit final grade for course
		# Constraints:
		- Must be instructor/professor, NOT any others
		- Cannot be changed or edited
		- Tied to main college database and student GPA/grades

	# Edit layout
		# Constraints:
		- Can make minor changes and alterations
		- No changes in functions or actions
		- Only label and organizational changes possible

	# Send emails/messages to all/specific student(s)
		# Constraints:
		- Mass email or message that can be sent to students 
			- Both on Canvas and email
		- Can send alerts and messages
		- Responds to all responses if sent
		

## ITIL users: TAs, Faculty
	(Receives the activities/assignments)

	# Grade assignments
		# Constraints:
		- Insert or update and grade for any test or assignment
		- CANNOT change actual letter grade or calculated grade
		- Grades are calculated and saved 
		- Able to be viewed by all ADMIN and ITIL users, or if the specific student
		- Grades are stored and calculated by the platform 

	# View student submissions
		# Constraints:
		- Can only view student submissions inside their specific class and section
		- Only view, not alter submissions
		- Can view the file, link, quiz, etc.
		- VIEW only of students' submissions and comments added 
		- Submissions that are currently in the database

	# Change grades
		# Constraints:
		- Can change grades already input
		- Cannot change after a specified time period
		- Notify students of change or addition of grade
		- Inserted into grade and calculations/overall grade is altered
		- Can alter the data held on the platform's database

	# Send class/group messages and alerts
		# Constraints:
		- Send messages and alerts inside of Canvas
		- No mass messages through University email
			- Unless notfiications about alerts/messages in Canvas are enabled
		- Posted to each viewers messages/alerts


# End users: Undergraduate/Graduate Students

	# View assignments
		# Constraints: 
		- Can only view the documents and assignments posted by ADMIN or ITIL users
		- Can only view anything on the site once it has been published
		- Can see past and upcoming assignments (if published on the form)
		- CANNOT change or alter anything

	# Submit and re-submit assignments
		# Constraints:
		- Able to submit 
		- Able to upload
		- Limited types of uploads for submission
		- Can see past submissions
		- Stored in database for future reference

	# Message/leave comments to Professors, TAs, Faculty, etc.
		# Constraints:
		- Messages can be viewed by all ADMIN and ITIL
		- Public discussion messages can be seen by all users
		- Each message stored in database so that past messages can be accessed


## System Constraints - Hardware and necessary components:

	# Protected database
	# Protected server
	# SLA rules regarding users and their access
	# Encryption of personal information
	# Strong database architechture
	# User friendly format and platform
