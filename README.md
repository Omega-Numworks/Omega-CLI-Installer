<p align="center"><img src="https://github.com/Omega-Numworks/Omega-Design/blob/master/Omega-CLI-Installer.png" /></p>

<p align="center">
  <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="License: CC BY-NC-SA 4.0" src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg?logo=creative%20commons&style=for-the-badge" /></a>
  <a href="https://github.com/Omega-Numworks/Omega-CLI-Installer/issues"><img alt="Issues" src="https://img.shields.io/github/issues/Omega-Numworks/Omega-CLI-Installer.svg?logo=git&style=for-the-badge" /></a>
</p>

## About

This installer is made to install easily [Omega](https://github.com/Omega-Numworks/Omega). It also allows you to choose the apps and languages you want to install. This CLI is an `ALPHA` release. Errors are not handled correctly.

## Install Omega

First of all, follow **step 1** [here](https://www.numworks.com/resources/engineering/software/build/). Then, you have two choices:

* **Install from `pip`**
```
sudo pip install omega-cli
sudo omega-cli
```

* **Install from source**
```
git clone https://github.com/Omega-Numworks/Omega-CLI-Installer.git
cd Omega-CLI-Installer/omega-cli
pip install click, PyInquirer
sudo python installer.py
```

...and follow the steps in your terminal!

![Screenshot](https://github.com/Omega-Numworks/Omega-Design/blob/master/screenshots/cli.png)
