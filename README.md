# HW 0

* *Assigned: TBA**
* *Due: TBA (just before class)*


The goal of this assignment is for you to set up Microsoft Azure.

Many of the assignments in this class will use Microsoft's cloud computing
infrastructure.  Using a cloud service like Microsoft (or Amazon, etc) makes it easy to
share data sets, and quickly run any number of virtual machines that are
identical for all students in the class.  We have credits from Azure,
which we will use for this class (in this homework, we will use a free
"micro" instance.)


<span style="color:#ff5511">**Caution: allocating and running services (e.g., virtual machines) on any cloud provider
  costs money.  It can be _very_ easy to spend more than you anticipated by leaving your services
  running.  Make it a habit to stop your services when not in use.  If you run out of credits,
  there's not much we (the staff) can do.**</span>

## Sign up and setup the OS

**Signup**: 

[register for an account](TBA)

You should not expect to provide credit card information.
Once the class registration has settled down, we can provide you with information to use the class's Azure credits.


**Launch an instance**

1. Go to [https://manage.windowsazure.com/](https://manage.windowsazure.com)
2. Click "NEW" in the bottom left of the screen
3. Click "Compute", then "Virtual Machine", then "Quick Create"
4. In DNS Name, provide a name for your new machine/website
5. In Image, pick **Ubuntu Server 14.04 LTS**
6. In Size, pick **D1 (1 core, 3.5 GB Memory)**
7. Pick a username and password and remember them
8. In Region, you can optionally pick East US or East US 2.  It will allocate your machine in a data center on the East Coast, so latency to the VM should be faster.
9. Click "Create Virtual Machine" and wait a couple minutes for it to launch.
1. Click on "Virtual Machines" in the main left panel to see your VMs
2. Once the VM has started, click on it, then click on the "Dashboard" tab
3. You should see your machine's DNS Name as <name you picked>.cloudapp.net.  **this is your public address**


**SSH to Your Instance**

Using a terminal program (e.g, MacOS Terminal, or an xterm on Athena, or a Cygwin terminal under windows), type:

    ssh <username>@<vm name>.cloudapp.net

It will ask for your password, once you enter you should see something like:

    Welcome to Ubuntu 14.04.3 LTS (GNU/Linux 3.19.0-25-generic x86_64)

    * Documentation:  https://help.ubuntu.com/

    System information as of Wed Aug 19 04:28:23 UTC 2015

    System load:  0.27              Processes:           107
    Usage of /:   4.1% of 28.80GB   Users logged in:     0
    Memory usage: 4%                IP address for eth0: 10.0.0.4
    Swap usage:   0%

    Graph this data and manage this system at:
    https://landscape.canonical.com/

    Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud


    Last login: Wed Aug 19 04:28:23 2015 from columbia.edu
    eugenewu@ewutest:~$

**Setup the OS**

Ensure the following packages are available using the Ubuntu package management tool _apt-get_.  

To install a package, type:

    sudo apt-get install <packagename1 packagename2 ...>

Make sure you have the following packages:

* python2.7
* postgresql-9.3
* postgresql-client-9.3
* postgresql-server-dev-9.3
* libpq-dev
* python-dev
* sqlite3
* git


**Setup Python**: 

Python uses its own package manager to install/update/remove packages.  In general, the following installs python packages:

    pip install <packagename>
    
Typically the package manager will require `sudo` and install the packages in a global folder that affects everyone using your machine.  This is bad hygiene because different python applications may use different versions of packages and it's easy to step on each other's toes.  

We will use `virtualenv` to create virtual environments that contain their own copies of `python` and packages.  When we work in a virtual environment, pip will install packages local to the environment rather than globbaly.  You can read [a detailed tutorial](http://docs.python-guide.org/en/latest/dev/virtualenvs/).
    
Lets setup your environment

1. Install `virtualenv` and convenience libraries in `virtualenvwrapper` (this is the one time you should install globally)

        sudo pip install virtualenv virtualenvwrapper
2. add the wrapper commands (you may add this line in ~/.bashrc so it runs when you create a bash shell)

        source /usr/local/bin/virtualenvwrapper.sh
3. create a new environment (will create a folder `test/` in `~/.virtualenvs/`)

        mkvirtualenv test
4. switch (activate) an environment by using `workon`

        workon test
        
5. switch out of an environment:
        
        deactivate


Now let's install a set of useful packages into your environment:
   
1. Activate your environment (see above)
2. install the following packages using `pip` (see above)
    * flask
    * psycopg2
    * sqlalchemy
    * click
3. Deactivate and you're done
      
  


**Checkout the class repository**

The class is organized a repositories under the organization 4111: http://www.github.com/w4111.  
Each assignment is managed as a separate repository. 
As the course progresses, more repositories will be made available. 
Copying a repository to your local machine is called "cloning a repository".  
Clone this homework using `git`:

    git clone https://github.com/w4111/hw0
    

## Test that things worked

Let's make sure you have access to Python, sqlite3, and the git repository.

**Python**

Type `python` and ensure that you see the following like (the Python version may be slightly different 2.7.X):

    Python 2.7.4 (default, Apr 19 2013, 18:28:01) 
    [GCC 4.7.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

Then try importing some modules from the packages we installed

    >>> import flask
    >>> import psycopg2
    >>> import sqlalchemy
    >>> import click

If that worked, push `ctrl+d` to exit the prompt.

**sqlite3**

SQLite is an "embedded" SQL database (it doesn't depend on a dedicated server process;  instead the client just manipulated a stored
datbase file directly.)

To ensure it is installed, type `sqlite3` and verify that you see the following:

    SQLite version 3.7.15.2 2013-01-09 11:53:05
    Enter ".help" for instructions
    Enter SQL statements terminated with a ";"
    sqlite>

If you do, push `ctrl+d` to exit the prompt.

**PostgreSQL**

We will use the PostgreSQL DBMS in this class.  Check that the client program works:

    psql --version

If it prints something like the following then it works
   
    psql (PostgreSQL) 9.3.9
    


**git repository**

Type `cat hw0/README.md` 

You should see the instructions for this hw fly by.


    

**(Optional) PostgreSQL using Amazon RDS**

PostgreSQL is an open source standalone database server (a DBMS!)  
Amazon provides a **cloud database service** that makes it easy to 
start and access a PostgreSQL (or MySQL, etc) database without the hassle
of installation.  If you have an Amazon AWS account or a trial account, you can setup your own database on Amazon.  **This is compeletly optional because Amazon asks for your credit card information**

Set it up by logging into your [aws.amazon.com](http://aws.amazon.com) account and following
[**the instructions**](./rdssetup.pdf).  

If you can run `psql` and access your RDS database, then push `ctrl+d` to exit the `psql` prompt.


**Handing in your work**:

To complete this lab, download the "zoo.json" file from Amazon into your "micro" instance, by typing:

    wget https://raw.githubusercontent.com/w4111/hw0/master/iowa-liquor-sample.csv

Write a python script tthat reads the file and computes the number of records 
(in this dataset, each line is a record) that contain the exact phrase "single malt scotch" (ignoring case).
Ignore upper and lower casing, so "Single Malt Scotch", and "SINGLE Malt Scotch" all match, whereas
"Single's Malty Scootch" does not.

You should create a text (.txt) file with the following format:

    <YOURNAME>
    <Student UNI>
    <# of single malt scotch records>
    <your python program>

For example:

    Eugene Wu
    ew2493
    9
    import sys
    num_whiskies = 0
    num_whiskies += 9
    print num_whiskies

Upload it to the [coureworks website](http://courseworks.columbia.edu/) as the "hw0" assignment.

Now you're almost done!  Go read the assigned paper(s) for today.

You can always feel free to send us questions on Piazza!




## Stop your virtual machine

While the free tier should get you through the class, it's very easy to accidentally use up all of your credits.
To conserve your hours (and avoid wasting energy), make sure to turn off your machine **whenever you are not using it**. 

1. Go to the [Azure Console](https://manage.windowsazure.com/).
1. In the left panel, click on "Virtual Machines"
2. Select your VM
3. Click "Shut Down" in the menu at the bottom of the screen
4. To resume the VM,  click "Start" in the menu
5. Before doing future assignments, you'll have to follow these instructions and choose "Start" to restart your instance.  Note that Shutting down and Starting the instance will potentially change the "Public DNS" value for that instance, however the URL <name>.cloudapp.net will stay the same.

