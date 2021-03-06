import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging

#
# SlicerMorphSampleData
#

class SlicerMorphSampleData(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "SlicerMorph Sample Data"
    self.parent.categories = ["SlicerMorph"]
    self.parent.dependencies = ["SampleData"]
    self.parent.contributors = ["Murat Maga & Sara Rolfe"]
    self.parent.helpText = """This module adds sample data for SlicerMorph into the SampleData module"""
    self.parent.acknowledgementText = """
This work was was funded
"""

    # don't show this module - additional data will be shown in SampleData module
    parent.hidden = True

    # Add data sets to SampleData module
    iconsPath = os.path.join(os.path.dirname(self.parent.path), 'Resources/Icons')
    import SampleData
    SampleData.SampleDataLogic.registerCustomSampleDataSource(
      sampleName='Gorilla Skull Landmarks Only',
      category='SlicerMorph',
      uris='https://github.com/SlicerMorph/SampleData/blob/master/Gorilla_Skull_LMs.zip?raw=true',
      loadFiles=True,
      fileNames='Gorilla_Skull_LMs.zip',
      thumbnailFileName=os.path.join(iconsPath, 'pointcloud.png'),
      loadFileType='ZipFile',
)
    SampleData.SampleDataLogic.registerCustomSampleDataSource(
      sampleName='Gorilla Skull Reference Model',
      category='SlicerMorph',
      uris=['https://github.com/SlicerMorph/SampleData/blob/master/Gor_template_low_res.vtk?raw=true','https://raw.githubusercontent.com/SlicerMorph/SampleData/master/Gorilla_template_LM1.fcsv?raw=true'],
      loadFiles=[True, True],
      fileNames=['Gor_template_low_res.vtk', 'Gorilla_template_LM1.fcsv'],
      nodeNames=['Gor_template_low_res', 'Gorilla_template_LM1'],
      thumbnailFileName=os.path.join(iconsPath, 'gorilla3D.png'),
      loadFileType=['ModelFile', 'MarkupsFiducials'],
)
    SampleData.SampleDataLogic.registerCustomSampleDataSource(
      sampleName='Mouse Skull Landmarks Only',
      category='SlicerMorph',
      uris='https://github.com/SlicerMorph/SampleData/blob/master/mouse_skull_LMs.zip?raw=true',
      loadFiles=True,
      fileNames='mouse_skull_LMs.zip',
      thumbnailFileName=os.path.join(iconsPath, 'pointcloud.png'),
      loadFileType='ZipFile',
)
    SampleData.SampleDataLogic.registerCustomSampleDataSource(
      sampleName='Mouse Skull Reference Model',
      category='SlicerMorph',
      uris=['https://github.com/SlicerMorph/SampleData/blob/master/4074_skull.vtk?raw=true', 'https://raw.githubusercontent.com/SlicerMorph/SampleData/master/4074_S_lm1.fcsv?raw=true'],
      loadFiles=[True, True],
      fileNames=['4074_skull.vtk','4074_S_lm1.fcsv'],
      nodeNames=['4074_skull', '4074_S_lm1'],
      thumbnailFileName=os.path.join(iconsPath, 'mouse3D.png'),
      loadFileType=['ModelFile','MarkupsFiducials'],
)
    SampleData.SampleDataLogic.registerCustomSampleDataSource(
      sampleName='Bruker/Sykscan mCT Recon sample',
      category='SlicerMorph',
      uris='https://github.com/SlicerMorph/SampleData/blob/master/sample_Skyscan_mCT_reconstruction.zip?raw=true',
      loadFiles=False,
      fileNames='sample_Skyscan_mCT_reconstruction.zip',
      #thumbnailFileName=os.path.join(iconsPath, 'CTPCardio.png'),
      loadFileType='zip',
)
