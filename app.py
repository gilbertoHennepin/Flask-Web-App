from flask import Flask, render_template, request  # NOT the same as requests 
from github_api import get_github_user_info

app = Flask(__name__)

@app.route('/') # home page
def homepage():
    return render_template('index.html')

@app.route('/get_user')
def get_user():
    #get user info from github api and displaay on new page
    print('form data is', request.args)  # for GET requests, use request.args is a dictionary
    username = request.args.get('username') # safer, retursn none if no username

    user_info, error_message = get_github_user_info(username) # dictionary of user info
    if error_message:
        return render_template('error.html', error_message=error_message)
    else:
        return render_template('github.html', user=user_info)

    return render_template('github.html', user)


if __name__ == '__main__':
    app.run()