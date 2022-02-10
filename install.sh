cd ~/Desktop
git clone https://github.com/AviationSFO/lifesimpack
cd lifesimpack
python3 -m pip install --upgrade build
python3 -m build
echo "Your python version is:"
python3 --version
echo "WARNING!"
echo "If the version above is NOT 3.6 or later, the life sim module will not work, please consider upgrading to a compatible version."