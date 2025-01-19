# command-center
Back-end for "TBD"

## DISCLOSURE

All commands displayed here for terminal are based on ***windows git bash*** version.
Use the internet to find the version of it for your terminal/OS setup.

## Start (prerequisites)

1. Get latest stable python.
    * https://www.python.org/
2. Create virual environment locally at the from the project root level
    * `py -m venv .venv`
3. install all dependacies from requirements.txt
    * `pip install -r requirements.txt`

### To update new requirements

Each time there is an alteration to project packages (new/update/remove) be sure to update the <u>**_requirements.txt_**</u> file for future devs to be able to work on latest version as well.
* `pip freeze > requirements.txt`

### Local

To run build locally for testing purposes simply run the <u>**_api.py_**</u> file.
* `py api.py`