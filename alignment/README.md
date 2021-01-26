# Setting alignment
## Initial setting
1. Install requirement <br>
This requirement is used for Raspberry Pi and Python3
```
$ sudo apt install python3 python3-dev python3-pip python3-opencv
$ pip3 install matplotlib
$ pip3 install pyqt5
```

2. Clone package <br>
```
$ git clone https://github.com/DuyNamUET/alignment.git
```

3. Autorun Script setup on Raspberry Pi <br>
Now we need to tell the operating system to run the script for the Pi user. In the command prompt or in a terminal window type :
```
$ sudo nano /etc/profile
```
Scroll to the bottom and add the following line :
```
$ sudo python3 /home/pi/alignment/testAlign.py
```
where ```/home/pi/alignment/testAlign.py``` is the path to your script. Type ```Ctrl+X``` to exit, then ```Y``` to save followed by ```Enter``` twice.<br>

4. Reboot and Test <br>
To test if this has worked reboot your Pi using :
```
$ sudo reboot
```
## Hardware config


## Setting with new dataset
1. Collect the data (using ```capture.py```) <br>
```
$ cd ../alignment
$ python3 capture.py
```
* Correct images: capture 5 images that have corrected camera on zig base. They will have a name is from ```0.png``` to ```4.png```.
* Incorrect images: capture 3 or 5 images in each incorrect cases. Their names will start from ```5.png```.

2. Move images to each folder <br>
Above, we have 5 correct images and incorrect images. Move correct images to folder ```images/ok``` and move incorrect images to folder ```images/notok```.

3. Get mask and get data <br>
Uncomment all code lines in ```testAlign.py```
``` python
### WARNING: Get data ###
get_mask('images/ok/0.png')
get_mean_corrected('images/ok')

# get_mask_with_fix_size('cam/ok/7.jpg')
# get_mask_with_all_imgs('cam/ok')
# get_mask_with_all_imgs('cam/notok')
```
4. Run
