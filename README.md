# socialblog

0. `git clone git@github.com:charalambospapa/socialblog.git`

1. If you are using a Python 3 version, virtual environment support is included in it, so all you need to do to create one is this:

    `python3 -m venv venv`


    ( If you are using any version of Python older than 3.4 (and that includes the 2.7 release), virtual environments are not supported natively. For those versions of Python, you need to download and install a third-party tool called virtualenv before you can create virtual environments. Once virtualenv is installed, you can create a virtual environment with the following command:  `virtualenv venv` )
    
\
&nbsp;

2. Regardless of the method you used to create it, you should have your virtual environment created. Now you have to tell the system that you want to use it, and you do that by activating it. To activate your brand new virtual environment you use the following command:

    `source venv/bin/activate`

3. bla bla:

    `pip install -r requirements.txt`

4. Finally 
    `flask run`

Open a browser and visit: http://127.0.0.1:5000/
