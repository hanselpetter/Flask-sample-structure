# Create a project environment for the Flask tutorial
 
 In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Create Environment command to create a virtual environment in your workspace. Select venv and then the Python environment you want to use to create it.
 
![image](https://github.com/hanselpetter/Flask-sample-structure/assets/141368939/eb80a4f8-7b09-462c-a65c-ad49c4f7e97b)
 
 # Run a minimal Flask app
1. Install Flask in the virtual environment by running the following command in the VS Code Terminal(Ctrl+Shift+`):
 
   `python -m pip install flask`
 
2. If you want to run the development server on a different IP address or port, use the host and port command-line arguments, as with --host=0.0.0.0 --port=80.
 
3. Application Discovery
 The flask command is installed by Flask, not your application; it must be told where to find your application in order to use it. The FLASK_APP environment variable is used to specify how to load the application.
 
    Unix Bash (Linux, Mac, etc.):
   ` $ export FLASK_APP=hello`
    `$ flask run`
    
    Windows CMD:
    `> set FLASK_APP=hello`
    `> flask run`
    
    Windows PowerShell:
    `> $env:FLASK_APP = "hello"`
    `> flask run`

# Python Version Manage
# Install pyenv for python version manage
`pip install pyenv-win`
`pip install pyenv-win --target %USERPROFILE%\\.pyenv`
`pyenv install --list`


#Power Shell
The easiest way to install pyenv-win is to run the following installation command in a PowerShell terminal:

Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"


#pyenv-win commands
   commands     List all available pyenv commands
   local        Set or show the local application-specific Python version
   global       Set or show the global Python version
   shell        Set or show the shell-specific Python version
   install      Install 1 or more versions of Python 
   uninstall    Uninstall 1 or more versions of Python
   update       Update the cached version DB
   rehash       Rehash pyenv shims (run this after switching Python versions)
   vname        Show the current Python version
   version      Show the current Python version and its origin
   version-name Show the current Python version
   versions     List all Python versions available to pyenv
   exec         Runs an executable by first preparing PATH so that the selected Python
   which        Display the full path to an executable
   whence       List all Python versions that contain the given executable

#virtual environment creating

pip install virtualenv-pyenv
virtualenv -p 3.9.13 venv

https://www.freecodecamp.org/news/manage-multiple-python-versions-and-virtual-environments-venv-pyenv-pyvenv-a29fb00c296f/