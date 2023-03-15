# Low-cost time-lapse camera monitoring (light version)

*this code only store the images into the USB drive*

## Main code

[main.py](main.py) -> code in charge to capture the images

*Copy in:*
```
/home/pi/
```

## RPi configuration

[fstab](fstab) -> file that mount automatically the USB drive

*Copy in:*
```
/etc/
```

## WittyPi files

[afterStartup.sh](afterStartup.sh) -> execute main.py after WittyPi boot

[daemon.sh](daemon.sh) -> Modifications to optimize the boot.

*Copy in:*
```
/home/pi/WittyPi
```

## Installation steps:

- [x] Install RPi OS -> [Raspberry Pi OS Lite (Legacy)](https://downloads.raspberrypi.org/raspios_oldstable_lite_armhf/images/raspios_oldstable_lite_armhf-2022-09-26/2022-09-22-raspios-buster-armhf-lite.img.xz)
- [X] Install WittyPi software -> [WittyPi](https://www.uugear.com/product/witty-pi-3-realtime-clock-and-power-management-for-raspberry-pi/)
- [X] Assembling the WittyPi and Camera to the RPi
- [X] Create the mount folder (called USB):
- [X] Install PyCamera library (sudo apt-get install python-picamera python3-picamera) -> [PiCamera](https://picamera.readthedocs.io/en/release-1.13/install.html)

```
sudo mkdir /media/usb
```
- [x] Copy the files of this repository
- [x] Activate the camera using [+info](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/):
```
sudo raspi-config
```

## Tested with:
- [x] RPi Zero W + WittyPi3
- [x] RPi 3 Model B + WittyPi3
- [x] RPi 4 Model B + WittyPi3
- [ ] RPi Zero W + WittyPi4
- [ ] RPi 3 Model B + WittyPi4
- [ ] RPi 4 Model B + WittyPi4
