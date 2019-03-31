# xfinitywifi-freeinternet
This isn't anywhere near done but the script will change your mac address if you edit wifid to equal the name of your wifi adapter which you can find a number of ways like typing ifconfig on a mac or linux machine.
-----
Automatically change mac address before free hour is up, auto-fill required forms on sign up page.

Xfinitywifi's are all over the place. They give you a free hour of internet (per month) if you sign up, but if you change the MAC address of your wifi adapter, it will think its a new machine and you can get another hour.

To automate this whole thing every hour would require a program to change the mac before the hour is up, then wait for the webpage to pop up, then auto-fill the forms with somewhat random data, then automate sending the form, closing the window, then waiting for that hour to be up, repeat.

