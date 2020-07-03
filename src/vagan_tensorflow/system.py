# Authors:
# Christian F. Baumgartner (c.f.baumgartner@gmail.com)
# Modified by Ricardo Bigolin Lanfredi 
# Last modified: 2020-07-01

import os
import socket
import logging
from . import adni_experiment
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

### SET THESE PATHS MANUALLY #####################################################
# Full paths are required because otherwise the code will not know where to look
# when it is executed on one of the clusters.

at_biwi = False  # Are you running this code from the ETH Computer Vision Lab (Biwi)?

project_root = adni_experiment.project_root
local_hostnames = ['bmicdl03']  # used to check if on cluster or not

##################################################################################

log_root = project_root

def setup_GPU_environment():

    if at_biwi:

        hostname = socket.gethostname()
        print('Running on %s' % hostname)
        if not hostname in local_hostnames:
            logging.info('Setting CUDA_VISIBLE_DEVICES variable...')

            # This command is multi GPU compatible:
            os.environ["CUDA_VISIBLE_DEVICES"] = ','.join(os.environ["SGE_GPU"].split('\n'))
            logging.info('SGE_GPU is %s' % os.environ['SGE_GPU'])
            logging.info('CUDA_VISIBLE_DEVICES is %s' % os.environ['CUDA_VISIBLE_DEVICES'])

    else:
        logging.warning('!! No GPU setup defined. Perhaps you need to set CUDA_VISIBLE_DEVICES etc...?')