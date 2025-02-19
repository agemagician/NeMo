# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from nemo.collections.asr.parts.numba.numba_utils import (
    NUMBA_INSTALLATION_MESSAGE,
    numba_cuda_is_supported,
    skip_numba_cuda_test_if_unsupported,
)
from nemo.collections.asr.parts.numba.rnnt_loss.rnnt_pytorch import RNNTLossNumba

# Prevent Numba CUDA logs from showing at info level
cuda_logger = logging.getLogger('numba.cuda.cudadrv.driver')
cuda_logger.setLevel(logging.ERROR)  # only show error

__NUMBA_MINIMUM_VERSION__ = "0.53.0"
