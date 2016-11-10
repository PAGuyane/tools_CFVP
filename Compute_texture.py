##Texture extraction=name
##raster=raster
import os
outS= raster.split(os.extsep)[0]
outSFS = out+str('_sfs.tif')
outB3 = out+str('_toasfs3.tif')

outputs_OTBSFSTEXTUREEXTRACTION_1=processing.runalg('otb:sfstextureextraction', raster,4.0,128.0,50.0,100.0,20.0,1.0,5.0,outSFS)

#get band 3 (PSI)
processing.runalg('otb:bandmath', raster,4.0,128.0,50.0,100.0,20.0,1.0,5.0,outSFS)
# superimpose
processing.runalg('otb:superimpose', raster,4.0,128.0,50.0,100.0,20.0,1.0,5.0,outSFS)

# stack TOA and PSI
outputs_GDALOGRMERGE_1=processing.runalg('gdalogr:merge', [ras,outSFSrun],False,False,1,outB3)