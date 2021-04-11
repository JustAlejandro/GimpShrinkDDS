# GimpShrinkDDS
Simple copy-paste command for Gimp to shrink all DDS textures in a directory that exceed 5MB and 1024x1024

## Execution
Open Gimp->Filters->Python-Fu->Console

Paste the .py file contents into console

Call `processFiles("C:\\TextureDir")` replacing with whatever directory it should start at

## Warnings
This is something I just tossed together, so best to back up the full resolution textures first, since this will overwrite them.

If you need to make changes go to Gimp->Help->Procedure Browser, for function signatures/parameters.
This isn't set up as a filter/tool since I only needed it once, but feel free to do whatever you like with the code.
