## multi_dashboard

This sample application shows how to use Dashboard Engine in conjunction with Snapshot Engine to allow users not only to create and edit their own dashboards, but persist them on the server for later retrieval by themselves and other users. This app also shows the functioning of the connection_params mechanism for an instance of the dashboard engine to potentially connect to multiple data sources, as configured outside the canvas. This app does not implement any kind of access control for dashboards, but could be used as a base from which to add these features.

## Running Locally

This app is ready to be run (and modified and re-run!) locally by following these steps:

* Open a terminal shell in the directory containing this README
* Copy the code to a new working directory: `cp -r . ../my-sample-copy` and then change directory to the copy with `cd ../my-sample-copy` (so that you can make changes and experiment with this app without losing the original sample app code)
* Create and activate a local Python environment using your tool of choice e.g. `virtualenv env && source env/bin/activate` (or use `conda` or equivalent)
  * On Windows, using PowerShell, this command should be e.g. `python3 -m virtualenv env; . .\venv\Scripts\activate`
* Install the dependencies with `pip install -r requirements.txt`
* Run the app with `python app.py`
  * This app will automatically create an SQLite database to locally store snapshots, at a location provided by the DATABASE_URL environment variable. By default, this location is in memory (`'sqlite:///:memory:'`). As such, saved dashboards will NOT be available once the Python process stops running.

## Running on Dash Enterprise

This app is ready to be deployed (and modified and redeployed!) to your Dash Enterprise server by following these steps:

* Open a terminal shell in the directory containing this README
* Make a copy of this directory with `cp -r . ../my-sample-copy` and then change directory to the copy with `cd ../my-sample-copy` (so that you can make changes and experiment with this app *without losing the original sample app code)
* Initialize a new git repository with `git init` and commit the contents using `git commit -am “initial commit”
* Initialize an app using the Dash Enterprise App Manager user interface, and copy the “Push URL”
  * when initializing this app, you will need to create and link a Postgres database for snapshots to be stored
* Add the Push URL as a remote in your terminal with `git remote add plotly <Push URL>`
* Push your app with `git push plotly master`
* You can now either modify and iterate on this app locally, or by initializing a Dash Enterprise Workspace if your version of Dash Enterprise supports this
