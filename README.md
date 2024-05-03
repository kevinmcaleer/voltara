# Voltara Speaks

## Setup the serial

Run RaspiConfig and set the serial console to off and hardware serial to on:

```bash
sudo raspi-config

> Interfaces > Serial Console = Off
> Hardware Serial = On
> Reboot
```

---

## Set the Baud
Need to set the Serial baud to 19200

```bash
stty -F /dev/serial0 19200
```

---

## Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install the prerequisites

```bash
pip install -r requirements.txt
```
