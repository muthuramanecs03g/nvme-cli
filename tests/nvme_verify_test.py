# SPDX-License-Identifier: GPL-2.0-only
#
# This file is part of nvme-cli
#
# Copyright (c) 2022 Samsung Electronics Co., Ltd. All Rights Reserved.
#
# Author: Arunpandian J <apj.arun@samsung.com>

"""
NVMe Verify Testcase:-

    1. Issue verify command on set of block; shall pass.

"""

from nose.tools import assert_equal
from nvme_test import TestNVMe


class TestNVMeVerify(TestNVMe):

    """
    Represents NVMe Verify testcase.
        - Attributes:
              - start_block : starting block of to verify operation.
              - test_log_dir : directory for logs, temp files.
    """

    def __init__(self):
        """ Pre Section for TestNVMeVerify """
        TestNVMe.__init__(self)
        self.start_block = 0
        self.block_count = 0
        self.namespace = 1
        self.setup_log_dir(self.__class__.__name__)

    def __del__(self):
        """ Post Section for TestNVMeVerify """
        TestNVMe.__del__(self)

    def verify(self):
        """ Wrapper for nvme verify
            - Args:
                - None
            - Returns:
                - return code for nvme verify command.
        """
        verify_cmd = "nvme verify " + self.ctrl + \
                     " --namespace-id=" + str(self.namespace) + \
                     " --start-block=" + str(self.start_block) + \
                     " --block-count=" + str(self.block_count)
        return self.exec_cmd(verify_cmd)

    def test_verify(self):
        """ Testcase main """
        assert_equal(self.verify(), 0)
