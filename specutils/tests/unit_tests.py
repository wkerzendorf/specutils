#Testing simple slicing
import numpy as np
from specutils import spectrum1d
np.random.seed(20000101)
disp = np.arange(6000, 9000, 1)
flux = np.random.random(3000)

def test_slice():
    test_spectrum = spectrum1d.Spectrum1D(flux, dispersion=disp, copy=True)
    disp_start, disp_stop = np.random.uniform(6000, 9000, 2)
    idx_start, idx_stop = disp.searchsorted([disp_start, disp_stop])
    
    assert all(flux[idx_start:idx_stop] == test_spectrum.slice(idx_start, idx_stop, units='index').flux)
    assert all(flux[idx_start:idx_stop] == test_spectrum.slice(disp_start, disp_stop, units='dispersion').flux)
    

def test_add_spectrum():
    test_spectrum1 = spectrum1d.Spectrum1D(flux, dispersion=disp, copy=True)
    test_spectrum2 = spectrum1d.Spectrum1D(flux, dispersion=disp, copy=True)
    
    add_spectrum = test_spectrum1 + test_spectrum2
    assert all(disp == add_spectrum.dispersion)
    assert all((2*flux) == add_spectrum.flux)

def test_add_constant():
    rand_const = np.random.random()
    test_spectrum = spectrum1d.Spectrum1D(flux, dispersion=disp, copy=True)
    add_spectrum = test_spectrum + rand_const
    
    assert all((flux + rand_const) == add_spectrum.flux)
    assert all(disp == add_spectrum.dispersion)
