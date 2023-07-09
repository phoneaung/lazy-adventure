# Recruitment Management System
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
- Clone the repository: git clone <https://github.com/phoneaung/rms>
- Navigate to the project directory: cd recruitment-management-system
- Create a virtual environment: python -m venv venv
- Activate the virtual environment:
    - For Windows: venv\Scripts\activate
    - For macOS/Linux: source venv/bin/activate
- Install the dependencies: pip install -r requirements.txt
- Run database migrations: python manage.py migrate
- Start the development server: python manage.py runserver
- Access the application in your web browser at http://localhost:8000
