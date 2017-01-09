#!/usr/bin/env python

import unittest, my_path


class ProductTestCase(unittest.TestCase):
    def testIntegers(self):
        for x in xrange(-10, 10):
            for y in xrange(-10, 10):
                p = my_path.product(x, y)
                self.failUnless(p == x * y, 'Integer multiplication failed')

    def testFloats(self):
        for x in xrange(-2, 2):
            for y in xrange(-2, 2):
                x = x / 10.0
                y = y / 10.0
                p = my_path.product(x, y)
                print "x = {}, y = {}, p = {}".format(x, y, p)
            self.failUnless(p == x * y, 'Float multiplication failed')


if __name__ == "__main__":
    unittest.main()
