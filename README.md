# Create a project environment for the Flask tutorial
 
1. In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Create Environment command to create a virtual environment in your workspace. Select venv and then the Python environment you want to use to create it.
 
![image](https://github.com/hanselpetter/Flask-sample-structure/assets/141368939/eb80a4f8-7b09-462c-a65c-ad49c4f7e97b)
 
 
2. Install Flask in the virtual environment by running the following command in the VS Code Terminal(Ctrl+Shift+`):
 
 `python -m pip install flask`
 
3. If you want to run the development server on a different IP address or port, use the host and port command-line arguments, as with --host=0.0.0.0 --port=80.
 
4. Application Discovery
 The flask command is installed by Flask, not your application; it must be told where to find your application in order to use it. The FLASK_APP environment variable is used to specify how to load the application.
 
 Unix Bash (Linux, Mac, etc.):
 $ export FLASK_APP=hello
 $ flask run
 
 Windows CMD:
 > set FLASK_APP=hello
 > flask run
 
 Windows PowerShell:
 > $env:FLASK_APP = "hello"
 > flask run
