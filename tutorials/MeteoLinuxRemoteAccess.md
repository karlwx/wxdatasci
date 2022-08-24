# Meteo Linux - Remote Access
Follow these steps to be able to access the meteo linux system remotely - no need to be in Walker!

1. Download and install the GlobalProtect VPN client following the directions in [this Penn State Knowledge Base article](https://pennstate.service-now.com/sp?id=kb_article_view&sysparm_article=KB0013431&sys_kb_id=6b8c36a147c591d016c93525d36d43f9&spa=1)

2. Connect to the VPN - you will not be able to access the meteo linux until you start the VPN connection.

3. Using the terminal (Mac, Linux) or MobaXTerm (or similar, Windows) you can log in via ssh: ```ssh <xyz1234>@<server>.met.psu.edu```  
You can use the X flag to enable X-11 forwarding, which will enable you to use GUI programs such as Gedit, Spyder, Matlab, etc. Note that these may run slowly, especially if your internet connection is poor.  
Example login: ```ssh -X kps5442@ulteosrv2.met.psu.edu```
    - ssh programs on Windows are available from:
      -  [MobaXTerm](https://mobaxterm.mobatek.net/): Integrated X server and SFTP browser.  Provides local terminal as well
      -  [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/) and XMing: Separate ssh and graphical display programs
      -  [Cygwin/X](https://x.cygwin.com/): Local terminal with [ssh](https://cygwin.com/packages/summary/openssh.html) and [X server](https://cygwin.com/packages/summary/xinit.html) programs.  I start X with `startxwin` in one window, then open another, tell programs where to find X with `export DISPLAY=:0.0`, and ssh from there
      -  [WinSCP](https://winscp.net/eng/index.php): Not an ssh client, just `scp`/`sftp`: provides a graphical interface to transfer files to/from servers
      -  Windows Subsystem for Linux (available for Windows 10+ from Windows Store): provides Linux distributions within Windows (open a Linux shell then follow the Linux directions)
    - Mac directions are available [as a Penn State Knowledge Base article](https://pennstate.service-now.com/sp?id=kb_article&sysparm_article=KB0010323&sys_kb_id=aab6f5dcdbc134507fb5266e13961961&spa=1)
      - A Terminal application is available in the `Finder -> Applications -> Utilities -> Terminal` menu
      - [XQuartz](https://www.xquartz.org/) provides an X server to translate graphical applications from Linux (on the far side of `ssh`) to something MacOS understands (and can put on your screen).
