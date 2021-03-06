import unittest

from base import SD_VM_Local_Test


class SD_SVS_Disp_Tests(SD_VM_Local_Test):
    def setUp(self):
        self.vm_name = "sd-svs-disp"
        super(SD_SVS_Disp_Tests, self).setUp()

    def test_sd_svs_disp_config_package_installed(self):
        pkg = "securedrop-workstation-svs-disp"
        self.assertTrue(self._package_is_installed(pkg))

    def test_sd_svs_disp_evince_installed(self):
        pkg = "evince"
        self.assertTrue(self._package_is_installed(pkg))

    def test_sd_svs_disp_libreoffice_installed(self):
        self.assertTrue(self._package_is_installed("libreoffice"))


def load_tests(loader, tests, pattern):
    suite = unittest.TestLoader().loadTestsFromTestCase(SD_SVS_Disp_Tests)
    return suite
