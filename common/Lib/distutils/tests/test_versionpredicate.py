# Embedded file name: scripts/common/Lib/distutils/tests/test_versionpredicate.py
import distutils.versionpredicate
import doctest
from test.test_support import run_unittest

def test_suite():
    return doctest.DocTestSuite(distutils.versionpredicate)


if __name__ == '__main__':
    run_unittest(test_suite())