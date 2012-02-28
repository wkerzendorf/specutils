#module with convenience functions
from specutils import specwcs
from specutils.spectrum1d import Spectrum1D

import numpy as np

def array2spectrum1d(disp, flux, disp_units=None, flux_units=None):
    #reading from an array
    new_wcs = specwcs.LookUpWCS(disp, dispt_units=disp_units)
    return Spectrum1D(flux, wcs=new_wcs, units=flux_units)
    
def ascii2spectrum1d(fname, disp_units=None, flux_units=None, dtype=float, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None):
    spec_data = np.loadtxt(fname, dtype=dtype, comments=comments, delimiter=delimiter, converters=converters, skiprows=skiprows, usecols=usecols)
    disp = spec_data[:,0]
    flux = spec_data[:,1]
    return array2spectrum1d(disp, flux, disp_units=disp_units, flux_units=flux_units)