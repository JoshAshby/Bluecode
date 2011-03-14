#!/usr/bin/python
#JoshAshby 2011
#joshuaashby@joshashby.com
#http://joshashby.com

import httplib, urllib
import sys
import android

droid = android.Android()
droid.toggleBluetoothState(True)
droid.bluetoothMakeDiscoverable()
droid.bluetoothAccept()

while True:
   (id, result, error) = droid.scanBarcode()
   query = str(result['extras']['SCAN_RESULT'])
   droid.bluetoothWrite(query)
