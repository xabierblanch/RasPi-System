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



## Tested with:
- [x] RPi Zero W + WittyPi3
- [x] RPi 3 Model B + WittyPi3
- [x] RPi 4 Model B + WittyPi3
- [ ] RPi Zero W + WittyPi4
- [ ] RPi 3 Model B + WittyPi4
- [ ] RPi 4 Model B + WittyPi4
