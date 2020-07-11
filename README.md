# Paper-Summary
An app designed to record the summary of papers I read.

## How to use the app?
- First run the `flask-service`. For Windows Powershell, use the following:
    - ```$env:FLASK_ENV="development"```
    - ```$env:FLASK_APP="main.py"```
    - ```flask run```
- Add your papers in the `./app/Papers` folder.
- Goto `http://localhost:5000` and you will see a two column table showing papers with and without exisiting summary.

<!-- ## TODO -->