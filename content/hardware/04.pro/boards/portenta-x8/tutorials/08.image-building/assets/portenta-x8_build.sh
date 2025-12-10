# Script to install and build the image for the Arduino Portenta X8
# More info at https://docs.arduino.cc/hardware/portenta-x8
# Script by Massimo Pennazio and Pablo Marquínez (@Arduino)

echo --------------------------------------------------------------------------
echo Starting wrapper script to setup and build an Image and the Flashing tools
echo @arduino Portenta-X8
echo 17 Oct 2023
echo

# Make sure its on the home directory
echo Changing directory to home
cd /dockerVolume

# Git config
echo Git config to example credentials
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

# Initialize the git-repo and pull all the repos
echo Starting git-repo initialization
repo init -u https://github.com/arduino/lmp-manifest.git -m arduino.xml -b release
echo Pulling git-repo files
repo sync

# Build 'lmp-factory-image' image. lmp-partner-arduino-image is now known as lmp-factory-image
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
echo "MFGTOOL_FLASH_IMAGE = \"lmp-factory-image\"" >> conf/local.conf
bitbake mfgtool-files

echo Exit tools folder
cd ..

# Copy files to the deploy folder
todaysDate=$(date +%d-%b-%H_%M)
echo copying files
DEPLOY_FOLDER=/dockerVolume/$todaysDate
mkdir $DEPLOY_FOLDER

cp -L build-lmp-mfgtool/deploy/images/portenta-x8/mfgtool-files-portenta-x8.tar.gz $DEPLOY_FOLDER
cp -L build-lmp-xwayland/deploy/images/portenta-x8/imx-boot-portenta-x8 $DEPLOY_FOLDER
cp -L build-lmp-xwayland/deploy/images/portenta-x8/u-boot-portenta-x8.itb $DEPLOY_FOLDER
cp -L build-lmp-xwayland/deploy/images/portenta-x8/sit-portenta-x8.bin $DEPLOY_FOLDER
cp -L build-lmp-xwayland/deploy/images/portenta-x8/lmp-factory-image-portenta-x8.wic $DEPLOY_FOLDER

cd $DEPLOY_FOLDER
tar xvf mfgtool-files-portenta-x8.tar.gz

echo finished
echo Output folder called $todaysDate
echo
echo Read more at https://docs.arduino.cc/hardware/portenta-x8
