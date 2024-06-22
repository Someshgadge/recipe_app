# Recipe App

## Features
- User registration and login
- Create, edit, delete recipes
- Search recipes by title or ingredients
- Pagination for listing recipes

## Setup Instructions
1. Clone the repository
2. Create a virtual environment and install dependencies
3. Set up the database
4. Run the application

## Endpoints
- `/register`: Register a new user
- `/login`: Login for existing users
- `/logout`: Logout the current user
- `/`: Home page listing user recipes
- `/recipe/new`: Create a new recipe
- `/recipe/<int:recipe_id>/edit`: Edit an existing recipe
- `/recipe/<int:recipe_id>/delete`: Delete a recipe
