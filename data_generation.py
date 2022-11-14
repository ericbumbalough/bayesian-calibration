import numpy as np

CONST_K = 2 # 2 for convention in metrology of tolerance limit = 2 * sigma (~95%). 1 for tolerance limit = sigma (~68%)

def gen_device(cycles = 10, thresh = CONST_K,
                init_mean = 0, init_sd = CONST_K/25,
                drift_mean = CONST_K/10, drift_sd = CONST_K/10):
    '''
    generate an 1darray of simulated calibration results

    algorithm: start normally distributed with N(init_mean, init_sd)
    each cycle, add a normally distributed drift N(drift_mean, drift_sd)
    if absolute value exceeds thresh value, then reset to normally distibuted N(init_mean, init_sd)
    '''


    # TODO
        # handle more advance decision rules
        # speed up with vectorization? premature
        # make an iterator version? premature probably not necessary
        # parallelize? premature
        # round them to simulate real accuracy? premature

    rng = np.random.default_rng()

    output = np.empty(cycles)

    # initials
    output[0] = rng.normal(loc=init_mean, scale=init_sd)

    for i in range(1, cycles):
        #next cycle
        output[i] = output[i-1] + rng.normal(loc=drift_mean, scale=drift_sd)
        if abs(output[i]) > thresh: 
            #needs recalibration
            output[i] = rng.normal(loc=init_mean, scale=init_sd)

    return output