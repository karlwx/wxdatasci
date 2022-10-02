# Jupyter Lab Demo
Meteo 473 - Spring 2022

### Using Jupyter Lab with Meteo Linux - Instructions for first time users

We'll use MobaXTerm in order to connect to the meteo servers via ssh.  
1. Open a terminal window in MobaXTerm and into your meteo server of choice. For this example, we'll use ulteosrv2:  
`ssh <username>@ulteosrv2.met.psu.edu`  

In order to create and manage anaconda environments, we need to change our shell to bash and configure anaconda.  
1. First, copy the bash configuration file located in the demo folder to your home directory:  
`cp /home/meteo/kps5442/jupyter-demo/.bashrc ~`  
2. Next, change the shell to bash:  
`bash`  
You should notice that your command prompt looks a bit different.  
3. Load the anaconda module:  
`module load python/3.8.3_anaconda`  
4. Now, initialize anaconda (so you won't have to re-load the module every time you log in):  
`conda init`  
Close and re-open your terminal (ctrl+D, then type `bash` again).  

Next, we'll create an anaconda environment to install jupyter lab in. This will also enable you to install any python packages or command line utilities you need (without administrator priviliges!).  
1. Create a new anaconda environment called jupytertest:  
`conda create --name jupytertest`  
2. Activate the environment:  
`conda activate jupytertest`  
3. Install jupyter lab:  
`conda install -c conda-forge jupyterlab`  
4. You can install additional packages using the same syntax. We'll be using metpy for the notebook demo, so install it now:  
`conda install -c conda-forge metpy`  

Finally, just a couple of more configuration steps before using Jupyter Lab:  
1. Create the necessary configuration files:  
`jupyter lab --generate-config`  
2. Set a password (Note: this is NOT tied to your PSU account):  
`jupyter lab password`  

Now, we're finally ready to use Jupyter Lab!  
1. Start jupyter lab on the meteo server. Before doing so, make sure you're in the directory you want to work out of:
`jupyter lab --no-browser`  
By default, Jupyter Lab tries to open in a browser window on the machine it's running on. Since we want to interact with it on our local computer (not the Meteo server where it is running), we use the `--no-browser` option to suppress that behavior.  
2. Take note of the port number jupyter is using. Often, this will be port 8888, but this is not always the case. For example:  
`[I 2022-03-31 15:44:44.677 ServerApp] Jupyter Server 1.11.1 is running at:
[I 2022-03-31 15:44:44.677 ServerApp] http://localhost:8888/lab`  
3. In a new terminal window on MobaXTerm, establish the connection to the running jupyter lab server:  
`ssh -L 8888:localhost:8888 <username>@ulteosrv2.met.psu.edu`  
If the port number was not 8888, replace the correct port number in the above command.  
4. Finally, visit http://localhost:8888/ in a web browser on your computer, enter your password when prompted, and you should be able to use Jupyter Lab!  

##### Complete the in-class demo!

### Using Jupyter Lab with Meteo Linux - Instructions for returning users
If you'd like to use Jupyter Lab in the future, the set-up process will be much simpler now that you've completed the configuration steps. Follow the steps below to start connect to your jupyter lab server:  
1. Connect to the meteo server via ssh:  
`ssh <username>@<server>.met.psu.edu`  
2. Change your shell to bash:  
`bash`  
3. Activate your anaconda environment:  
`conda activate <envname>`  
Note: you can create new anaconda environments using the same process used above.  
4. Start jupyter lab server:  
`jupyter lab --no-browser`  
Don't forget to note the port number (usually 8888, but not always).  
5. Connect to the server. In a new MobaXTerm terminal window:  
`ssh -L <port>:localhost:<port> <username>@<server>.met.psu.edu`  
6. Visit http://localhost:8888/ in your web browser to interact with Jupyter Lab!  

### Tips and Tricks
You can use Jupyter Lab to edit and run your code from anywhere. If you're not on campus but want to work, you'll need to be connected to the GlobalProtect VPN in order to do so. Instructions for using the VPN can be found here: https://pennstate.service-now.com/kb?id=kb_article_view&sysparm_article=KB0013431  