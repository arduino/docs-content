# Script to install and build the image for the Arduino Portenta X8
# More info at https://docs.arduino.cc/hardware/portenta-x8
# Script by Massimo Pennazio and Pablo Marquínez (@Arduino)

# Git-repo tool installation
echo installing git-repo
mkdir -p ~/.bin
PATH="${HOME}/.bin:${PATH}"
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/.bin/repo
chmod a+rx ~/.bin/repo

# Initialize the git-repo and pull all the repos
echo Starting git-repo initialization
repo init -u https://github.com/arduino/lmp-manifest.git -m arduino.xml -b release
echo Pulling git-repo files
repo sync

# Build 'lmp-partner-arduino-image' image
echo Building Portenta-X8 image
DISTRO=lmp-xwayland MACHINE=portenta-x8 . setup-environment
echo "ACCEPT_FSL_EULA = \"1\"" >> conf/local.conf
bitbake lmp-partner-arduino-image

echo Exit X8 folder
cd ..

# Build flashing tools
echo Building tools
DISTRO=lmp-mfgtool MACHINE=portenta-x8 . setup-environment
echo "ACCEPT_FSL_EULA = \"1\"" >> conf/local.conf
echo "MFGTOOL_FLASH_IMAGE = \"lmp-partner-arduino-image\"" >> conf/local.conf
bitbake mfgtool-files

echo Exit tools folder
cd ..

# Copy files to the deploy folder
echo copying files
mkdir deploy
DEPLOY_FOLDER=./deploy

cp -L build-lmp-mfgtool/deploy/images/portenta-x8/mfgtool-files-portenta-x8.tar.gz $DEPLOY_FOLDER
cp -L build-lmp-xwayland/deploy/images/portenta-x8/imx-boot-portenta-x8 $DEPLOY_FOLDER
cp -L build-lmp-xwayland/deploy/images/portenta-x8/u-boot-portenta-x8.itb $DEPLOY_FOLDER
cp -L build-lmp-xwayland/deploy/images/portenta-x8/sit-portenta-x8.bin $DEPLOY_FOLDER
cp -L build-lmp-xwayland/deploy/images/portenta-x8/lmp-image-portenta-x8.wic $DEPLOY_FOLDER
cd $DEPLOY_FOLDER

tar xvf mfgtool-files-portenta-x8.tar.gz

echo finished
echo
echo Read more at https://docs.arduino.cc/hardware/portenta-x8
