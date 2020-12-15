sudo pip3 uninstall enable -y
pushd enable 
rm -rf build
python3 setup.py build
sudo python3 setup.py install
if [ $? -ne 0 ]; then
	exit $?
fi
popd
