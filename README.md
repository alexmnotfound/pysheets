# Google Sheets API Integration with Python

## Purpose
This repository will provide an easy-to-use interface for interacting with Google Sheets using Python code. It will be useful for individuals and businesses that need to automate data processing and analysis tasks in Google Sheets.

---

This Python repository will use the Google Sheets API to read and write data to a specific Google Sheet. The repository will require the user to authenticate their Google account and authorize the application to access their Google Sheets. Once authorized, the Python code will use the Google Sheets API to establish a connection to the specified Google Sheet and read or write data.

The repository will contain functions that allow users to read, write, update, and delete data from specific sheets and ranges within a Google Sheet. Users can specify the sheet and range of cells they want to interact with, and the Python code will handle the rest.

---


## Google Authorization Process

1. Enable the Google Sheets API and appropriate scopes for the application:
   - Go to the Google Cloud Console at https://console.cloud.google.com/w
   - Create a new project or select an existing one.
   - Navigate to APIs and Services, then to the "API Library" tab and search for "Google Sheets API". Click "Enable".
   - Navigate to APIs and Services, then to the "Credentials" tab and click "Create credentials" -> "Service account key".
   - Enter a name for the service account, choose "JSON" as the key type, and click "Create".
   - Save the resulting JSON file in `./credentials` and rename it into `creds.json` secure location.


## How to run it
I personally recommend it to run it in a virtual environment, as follows:
1. Open a command prompt or terminal window.
2. Navigate to the directory where you want to create the virtual environment. You can use the `cd` command to change directories.
3. Enter the following command to create a new virtual environment: `python3 -m venv myenv`, replacing "myenv" with the name you want to give to your virtual environment.
4. Activate the virtual environment by entering the following command (Linux environments): `source myenv/bin/activate`
5. Once the virtual environment is activated, you can install Python packages using `pip` as usual. For example, to install the all the packages, 
you can enter the following command: `pip3 install -r requirements.txt`
6. Assuming you're on the project's folder, now you can run `python3 main.py`
7. When you're done using the virtual environment, you can deactivate it by entering the following command: `deactivate`


### References
- [Google Sheets API Python Quickstart](https://developers.google.com/sheets/api/quickstart/python#step_3_set_up_the_sample)