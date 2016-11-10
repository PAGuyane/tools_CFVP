##raster=raster
##outSFS=output raster
import os
import subprocess
#from PyQt4.QtCore import *
#from PyQt4.QtGui import *
#from qgis.core import *


outSFS=raster.split(os.extsep)[0]
outSFS=outSFS+str('_sfs.tif')