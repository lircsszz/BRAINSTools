# -*- coding: utf8 -*- 
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec, File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath
import os


class DWIConvertInputSpec(CommandLineInputSpec):
    conversionMode = traits.Enum("DicomToNrrd", "DicomToFSL", "NrrdToFSL", "FSLToNrrd", desc="Determine which conversion to performn", argstr="--conversionMode %s")
    inputVolume = File(desc="Input DWI volume -- not used for DicomToNrrd.", exists=True, argstr="--inputVolume %s")
    outputVolume = traits.Either(traits.Bool, File(), hash_files=False, desc="Output filename (.nhdr or .nrrd)", argstr="--outputVolume %s")
    fMRI = traits.Bool(desc="Output a NRRD file, but no Gradients", argstr="--fMRI ")
    inputDicomDirectory = Directory(desc="Directory holding Dicom series", exists=True, argstr="--inputDicomDirectory %s")
    outputDirectory = traits.Either(traits.Bool, Directory(), hash_files=False, desc="Directory holding the output NRRD format", argstr="--outputDirectory %s")
    gradientVectorFile = traits.Either(traits.Bool, File(), hash_files=False, desc="Text file giving gradient vectors", argstr="--gradientVectorFile %s")
    smallGradientThreshold = traits.Float(desc="If a gradient magnitude is greater than 0 and less than smallGradientThreshold, then DWIConvert will display an error message and quit, unless the useBMatrixGradientDirections option is set.", argstr="--smallGradientThreshold %f")
    writeProtocolGradientsFile = traits.Bool(desc="Write the protocol gradients to a file suffixed by \'.txt\' as they were specified in the procol by multiplying each diffusion gradient direction by the measurement frame.  This file is for debugging purposes only, the format is not fixed, and will likely change as debugging of new dicom formats is necessary.", argstr="--writeProtocolGradientsFile ")
    useIdentityMeaseurementFrame = traits.Bool(desc="Adjust all the gradients so that the measurement frame is an identity matrix.", argstr="--useIdentityMeaseurementFrame ")
    useBMatrixGradientDirections = traits.Bool(desc="Fill the nhdr header with the gradient directions and bvalues computed out of the BMatrix. Only changes behavior for Siemens data.  In some cases the standard public gradients are not properly computed.  The gradients can emperically computed from the private BMatrix fields.  In some cases the private BMatrix is consistent with the public grandients, but not in all cases, when it exists BMatrix is usually most robust.", argstr="--useBMatrixGradientDirections ")
    inputBValues = File(desc="B Values text file", exists=True, argstr="--inputBValues %s")
    inputBVectors = File(desc="B Vector text file", exists=True, argstr="--inputBVectors %s")
    outputBValues = traits.Either(traits.Bool, File(), hash_files=False, desc="B Values text file", argstr="--outputBValues %s")
    outputBVectors = traits.Either(traits.Bool, File(), hash_files=False, desc="B Vector text file", argstr="--outputBVectors %s")


class DWIConvertOutputSpec(TraitedSpec):
    outputVolume = File(desc="Output filename (.nhdr or .nrrd)", exists=True)
    outputDirectory = Directory(desc="Directory holding the output NRRD format", exists=True)
    gradientVectorFile = File(desc="Text file giving gradient vectors", exists=True)
    outputBValues = File(desc="B Values text file", exists=True)
    outputBVectors = File(desc="B Vector text file", exists=True)


class DWIConvert(SEMLikeCommandLine):
    """title: DWIConverter

category: Diffusion.Diffusion Data Conversion

description: Converts diffusion weighted MR images in dicom series into Nrrd format for analysis in Slicer. This program has been tested on only a limited subset of DTI dicom formats available from Siemens, GE, and Phillips scanners. Work in progress to support dicom multi-frame data. The program parses dicom header to extract necessary information about measurement frame, diffusion weighting directions, b-values, etc, and write out a nrrd image. For non-diffusion weighted dicom images, it loads in an entire dicom series and writes out a single dicom volume in a .nhdr/.raw pair.

version: Version 1.0

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/DWIConverter

license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt

contributor: Vince Magnotta (UIowa), Hans Johnson (UIowa), Joy Matsui (UIowa), Kent Williams (UIowa), Mark Scully (Uiowa), Xiaodong Tao (GE)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.  Additional support for DTI data produced on Philips scanners was contributed by Vincent Magnotta and Hans Johnson at the University of Iowa.

"""

    input_spec = DWIConvertInputSpec
    output_spec = DWIConvertOutputSpec
    _cmd = " DWIConvert "
    _outputs_filenames = {'outputVolume':'outputVolume.nii','outputBVectors':'outputBVectors','outputBValues':'outputBValues','gradientVectorFile':'gradientVectorFile','outputDirectory':'outputDirectory'}
