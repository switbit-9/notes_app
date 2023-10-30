# Notes App

This repository contains a Notes App with both backend and frontend components. To set up and run the app, follow the instructions below:

## Backend

1. Create `.env` files:

   - Replace `env-example` with your configuration in both the `backend/` folder and the project's root directory. Ensure that the database variables are the same in both files.

2. Inside the `backend/` folder:

    **Need to run with python version 3.10**

   - Create a Python virtual environment:
     ```
     python3 -m venv .venv
     ```

   - Activate the virtual environment:
     ```
     source .venv/bin/activate
     ```

   - Install the required Python packages:
     ```
     pip3 install -r requirements.txt
     ```

3. Start the server:

   - Navigate to the project directory:
     ```
     cd path/to/notes_app
     ```

   - Launch the Uvicorn server on `localhost` at port `8000` with automatic reloading:
     ```
     uvicorn backend.app.main:app --host localhost --port 8080 --reload
     ```

   - The backend server will be accessible at http://localhost:8080.

   - The database should be available at http://localhost:5432.

## Frontend

Inside the `frontend/` folder:
1. Configure the post to communicate with local server:


2. Install all the required Node.js modules:
npm install

3. Start the Expo development server:
npx expo start

4. To run the app on an iOS simulator, press `i` or to run on web press `w`.

Now, you should have the Notes App up and running with the backend server on http://localhost:8080 and the frontend being developed using Expo. Enjoy using the app!

Feel free to customize the instructions to match your specific project's requirements or provide more details as needed.
