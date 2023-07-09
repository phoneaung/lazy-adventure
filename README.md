# Recruitment Management System
#### Video Demo:  <https://youtu.be/gSCvTgQN3Qw>
#### Description:
A recruitment management system is web-based application developed using Python, Django and Boostrap. It is a platform for managing and organizing candidates for a company or organization. The system allows users to create, edit, remove candidates, track their status and information. 

#### Key features
- User Authentication: The system includes user authentication functionality to ensure secure access to the application.
- Candidate Management: Users can add new candidates to the system, providing details such as name, description, status, contact information, and profile picture.
- Candidate Search: The system offers a search function to easily find candidates based on their names.
- Candidate Profile: Users can view detailed information about each candidate, including their profile picture, status, contact details, and comment history.
- Edit and Delete Candidates: Users can edit and update candidate information as needed, including changing their status, updating contact details, or modifying their profile picture.
- Commenting System: The system provides a comment section where users can add comments about a candidate, including the commenter's name and the date of the comment.
- Resume Upload: Candidates can upload their resumes, which can be downloaded by users for further review.
- Download Resume: Users can download the resumes attached to candidates' profiles for offline viewing and evaluation.

#### Getting started
- Clone the repository: git clone <repository-url>
- Navigate to the project directory: cd recruitment-management-system
- Create a virtual environment: python -m venv venv
- Activate the virtual environment:
    - For Windows: venv\Scripts\activate
    - For macOS/Linux: source venv/bin/activate
- Install the dependencies: pip install -r requirements.txt
- Run database migrations: python manage.py migrate
- Start the development server: python manage.py runserver
- Access the application in your web browser at http://localhost:8000

#### Functions
#### Apps
I have created into core, userprofile, dashboard and candidate apps. Core will contains index and about page. Userprofile contains signup. Dashboard will show list of candidates that has been added by recruiters. Candidate includes candidate and comment database models. 
##### Log in, Sign up and Log out
For authentication, I use Django's built in auth library to authenticate users logins. For sign up, I use Django's built in UserCreationForm to let users create an account. Same goes for log out function.
##### Candidate list
For showing lists of candidates created, I filter the Candidate model and return them in html templates by looping. 
##### Search
For searching candidates, if user's input(query) is equals to 'name__icontains' of candidates, show the list of candidates
##### Candidate details
When clicking a specific candidate, it will go to that candidate's details page. 
##### Add candidate
I created a AddCandidateForm in forms.py to let users add candidates. If request.method is equals to POST, plug in the user's inputs such as files and text. If form is valid, I save it in candidate variable and set commit is equals to false and set candidate.created_by is current user and candidate.last_modified_by is current user. Then we can save the candidate object. Show a message saying candidate has been successfully created and return to candidate list page. Else, show the create new candidate page. For image field, if user does not upload any image, it will automatically set the default image as profile image. In forms, I have also set multiple is false in image field which makes user only upload one file at a time. Same goes for resume. 
##### Edit candidate
For editing, I get the candidate first and then if the request method is post, AddCandidateForm will show with instance equals to candidate that we are editing. It prevents from creating a new candidate instead of editing. I also added a clear button for image field and resume field to let users delete their image or resume. For image, if user does not choose any image or removed an existing one, it will automatically set the default image that I have set. 
##### Delete candidate
I use delete function and then save the candidate. Show a message to let users know that they have deleted that candidate.
##### Comment
I first created the Comment database model and AddCommentForm in forms with comment field. First if the request method is post, AddCommentForm will appear, if form is valid, query the comment from html form and let users comment. Save comment. Show a message to let users know that they have added a comment. 
##### Dashboard
In dashboard, candidates that have been added by users will appear in a chronological order.
##### Media
Any media uploaded by users will be saved in media folder which will contains images folder and resume folder. I use python pillow for handling image files.
