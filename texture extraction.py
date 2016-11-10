##Texture extraction=name
##raster=raster
import os
out = raster.split(os.extsep)[0]
outSFS = out+str('_sfs.tif')
outB3 = out+str('_toasfs3.tif')

if not os.path.isfile(outSFS):
    SFS=processing.runalg('otb:sfstextureextraction', raster,1.0,128.0,30.0,100.0,20.0,1.0,5.0,outSFS)
    
# Extract band 3
print('Extract band 3')
SFSB3=processing.runalg('otb:bandmath', [outSFS],128.0,'im1b3',None)
# sup impose
print('Superimpose band 3 with raster')
SuperImposeB3=processing.runalg('otb:superimposesensor', raster,SFSB3['-out'],0.0,4.0,1,1,2.0,128.0,None)

# stack TOA and PSI
print('Stack')
StackImage=processing.runalg('gdalogr:merge', [raster,SuperImposeB3['-out']],False,False,1,outB3)