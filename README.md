# TASK MANAGEMENT SYSTEM

This is a robust RESTful API for task management system, built with Django and DRF (Django Rest Framework). Uses custom JWT authentication, Role Based Access Control (RBAC), nested resource management for comments and status endpoints and other costom endpoints.

## Tech Stacks
- **Framework:** Django and DRF (Django REST Framework)
- **Authentication and Authorization:** Simplejwt (JSON Web Token)
- **Database:** SQLite
- **Python:** version 3.10+

## Features
* **Custom user management** uses `get_user_model()` to access and use custom user model.
* **Authentication and Authorization** uses simple jwt for secured `(/tasks_api/auth/register)` registration and  `(/tasks_api/auth/login)` login.
* **Role Based Access Control**
    *  `(/tasks_api/auth/users)` used to see all registered users and accessed only by admin.
    *  `(/tasks_api/auth/users/me)` use to read/update current user profile accessed by any authenticated users.
    *  `(/tasks_api/tasks)` authenticated user can access this endpoint to see assigned tasks for them or to create and assign tasks for other users. 

## Setup and installation
**Prerequsites**
* python 3.10+
* Git

### Clone repository
``` bash
git clone https://github.com/Amlakyalew/TaskManagementSystem.git
cd TaskManagementSystem
```
## Main endpoints

```
METHOD       ENDPOINT                                DESCRIPTION                                                   AUTH & PERMISSIONS
POST         /tasks_api/auth/register/               Register new user account                                     Public
POST         /tasks_api/auth/login/                  Authenticate and obtain JWT access/refresh                    Public
POST         /tasks_api/auth/refresh/                Refresh access token                                          Public
GET          /tasks_api/auth/users/                  List all registered users                                     IsAdminUser
GET/PUT      /tasks_api/auth/users/me/               Retrieve or update current user profile                       IsAuthenticated
GET/POST     /tasks_api/tasks/                       List tasks (with filters) or create task                      IsAuthenticated
GET          /tasks_api/tasks/{id}/                  Retrieve task detailed view                                   IsAuthenticated
PUT/DELETE   /tasks_api/tasks/{id}/                  Update task details or remove task                            Creator or Admin
PATCH        /tasks_api/tasks/{id}/status/           Update task status (Pending → Progress → Done)                Assignee Only
GET/POST     /tasks_api/tasks/{id}/comments/         List task comments or post a comment                          IsAuthenticated
PUT/DELETE   /tasks_api/tasks/{id}/comments/{id}/    Edit or delete comment                                        Comment Owner
