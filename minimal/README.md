## minimal

This sample application is the absolute minimal example of how to use Dashboard Engine. This app contains only a DashboardCanvas component, connected to a single hardcoded sample data frame. Users of this app can configure the canvas how they like, but their changes are not visible to any other user, and are lost when the user closes the tab/window or navigates away.

## Running Locally

This app is ready to be run (and modified and re-run!) locally by following these steps:

* Open a terminal shell in the directory containing this README
* Copy the code to a new working directory: `cp -r . ../my-sample-copy` and then change directory to the copy with `cd ../my-sample-copy` (so that you can make changes and experiment with this app without losing the original sample app code)
* Create and activate a local Python environment using your tool of choice e.g. `virtualenv env && source env/bin/activate` (or use `conda` or equivalent)
  * On Windows, using PowerShell, this command should be e.g. `python3 -m virtualenv env; . .\venv\Scripts\activate`
* Install the dependencies with `pip install -r requirements.txt`
* Run the app with `python app.py`

## Running on Dash Enterprise

This app is ready to be deployed (and modified and redeployed!) to your Dash Enterprise server by following these steps:

* Open a terminal shell in the directory containing this README
* Make a copy of this directory with `cp -r . ../my-sample-copy` and then change directory to the copy with `cd ../my-sample-copy` (so that you can make changes and experiment with this app *without losing the original sample app code)
* Initialize a new git repository with `git init` and commit the contents using `git commit -am “initial commit”
* Initialize an app using the Dash Enterprise App Manager user interface, and copy the “Push URL”
* Add the Push URL as a remote in your terminal with `git remote add plotly <Push URL>`
* Push your app with `git push plotly master`
* You can now either modify and iterate on this app locally, or by initializing a Dash Enterprise Workspace if your version of Dash Enterprise supports this
