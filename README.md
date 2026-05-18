This repository contains data and code for analyses in:

Citation: Kupchella, S. C., Kort, A. E., & Phifer-Rixey, M. (2026). Body size and cranial shape differentiation in urban and rural house mice (<em>Mus musculus domesticus</em>). bioRxiv, 2026.05.16.725634. https://doi.org/10.64898/2026.05.16.725634

## DATA
### Stables_Data.xlsx
This file contains all of the supplementary tables listed in the manuscript. Data is provided in tab S1. All columns are labeled inside the file itself, with additional descriptions provided at the bottom of tab S1 where necessary. 

## SCRIPTS
### Analysis_Rscript.Rmd
This script conducts all analyses and generates figures associated with the manuscript. Reads in `Stables_Data.xlsx`. 

### Mirror_Landmarks.py
This script is used to define the midsagittal plane and mirror right-side landmarks across the plane in _3D Sicer_. Script is executed in the _3D Slicer_ python terminal.

### Midsagittal_Plane_Visualization.py
This script simply creates a 2D plane that passes throught the defined MSP for visualization. Script is executed in the _3D Slicer_ python terminal. 

## MESHES
### MHB_096_FNL_MESH.zip
This .zip file contains a cleaned mesh of the reference specimen (MHB096). The unzipped .ply file is read into `Analysis_Rscript.Rmd`

---
Necessary Software
1. R (v4.5.1 (2025-06-13 or above)
2. RStudio (v2025.09.1+401 or above)
