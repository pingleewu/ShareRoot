
# swig -version == 3.0.12

# Use wxPython or QT4
sudo pip3 show wxpython
if [ $? -ne 0 ]; then
	exit $?
fi

sudo pip3 uninstall traits -y
pushd traits
rm -rf build
python3 setup.py build
sudo python3 setup.py install 
if [ $? -ne 0 ]; then
        exit $?
fi
popd

sudo pip3 uninstall pyface
pushd pyface 
rm -rf build
python3 setup.py build
sudo python3 setup.py install 
if [ $? -ne 0 ]; then
	exit $?
fi
popd


sudo pip3 uninstall traitsui
pushd traitsui 
rm -rf build
python3 setup.py build
sudo python3 setup.py install 
if [ $? -ne 0 ]; then
	exit $?
fi
popd

sudo pip3 uninstall enable
pushd enable 
rm -rf build
python3 setup.py build
sudo python3 setup.py install 
if [ $? -ne 0 ]; then
	exit $?
fi
popd

sudo pip3 uninstall chaco
pushd chaco 
rm -rf build
python3 setup.py build
sudo python3 setup.py install 
if [ $? -ne 0 ]; then
	exit $?
fi
popd

echo "Done success"

