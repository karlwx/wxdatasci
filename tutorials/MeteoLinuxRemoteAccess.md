# Meteo Linux - Remote Access
Follow these steps to be able to access the meteo linux system remotely - no need to be in Walker!

1. Download and install the Cisco AnyConnect VPN Client: https://pennstate.service-now.com/sp/help.psu.edu?id=kb_article_view&sysparm_article=KB0011711

2. Connect to the VPN - you will not be able to access the meteo linux until you start the VPN connection.

3. Using the terminal (Mac, Linux) or MobaXTerm (or similar, Windows) you can log in via ssh: ```ssh <xyz1234>@<server>.met.psu.edu```  
You can use the X flag to enable X-11 forwarding, which will enable you to use GUI programs such as Gedit, Spyder, Matlab, etc. Note that these may run slowly, especially if your internet connection is poor.  
Example login: ```ssh -X kps5442@ulteosrv2.met.psu.edu```