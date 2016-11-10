##ecw=name
##ecwFolder=folder

import os
for ecw in os.listdir(ecwFolder):
    if ecw.endswith(".ecw"):
        outTif = os.path.splitext(ecw)[0]+str('.tif')
        #processing.runalg('gdalogr:translate', ecw,100.0,False,'-9999',1,'EPSG:32622',None,False,5,4,75.0,6.0,1.0,False,1,False,None,outTif)
        outputs_GDALOGRTRANSLATE_1=processing.runalg('gdalogr:translate', ecw,100.0,True,'-9999',1,'EPSG:32622',None,False,5,4,75.0,6.0,1.0,False,2,False,None,outTif)