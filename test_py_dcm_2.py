###  
import os
import pydicom

#Input dir
dcm_dir = "C:/Users/chi.zhang/Downloads/W584_9166-000058941/W584_9166_DICOM_Image_copy"

spacing_list = []
error_files = []
fileNames = os.listdir(dcm_dir)

z_dims = []

for i in range(len(fileNames)-1):
  filename0 = fileNames[i]
  filename1 = fileNames[i+1]
  if filename0.endswith(".dcm"):
    file_path0 = os.path.join(dcm_dir, filename0)
    file_path1 = os.path.join(dcm_dir, filename1)
    # Read the DICOM file
    ds0 = pydicom.dcmread(file_path0)
    ds1 = pydicom.dcmread(file_path1)
    
    if i!=5 and i!=105 and i!=205:
      ds1.ImagePositionPatient[2] = ds0.ImagePositionPatient[2] - 0.6
    elif i == 5:
      ds1.ImagePositionPatient[2] = ds0.ImagePositionPatient[2] + 61.299999999999955
    elif i ==105:
      ds1.ImagePositionPatient[2] = ds0.ImagePositionPatient[2] + 116.10000000000002
    elif i == 205:
      ds1.ImagePositionPatient[2] = ds0.ImagePositionPatient[2] + 116.10000000000002
    
    spacing = ds0.ImagePositionPatient[2] - ds1.ImagePositionPatient[2]
    spacing_list.append(spacing)
      
    ds0.save_as(os.path.join(dcm_dir, filename0))
    ds1.save_as(os.path.join(dcm_dir, filename1))

    z_dims.append(ds0.ImagePositionPatient[2])
