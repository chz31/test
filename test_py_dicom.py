import os
import pydicom

dicom_dir = "C:/Users/chi.zhang/Downloads/morphosource_media-2024-04-19-11_33_51/Media 000058941 - Element Unspecified CTImageSeries Etc/W584_9166-000058941/W584_9166_DICOM_Image"
new_pixel_spacing = [0.292969, 0.292969]
new_slice_thickness = 0.6

for filename in os.listdir(dicom_dir):
  if filename.endswith(".dcm"):
    file_path = os.path.join(dicom_dir, filename)
    # Read the DICOM file
    ds = pydicom.dcmread(file_path)
    
    # Update pixel spacing and slice thickness
    ds.PixelSpacing = new_pixel_spacing
    ds.SliceThickness = new_slice_thickness
    
    ds.save_as(file_path)

