import unittest
import sys
if sys.version_info.major == 2:
    import mock    
else:
    from unittest import mock
import json
# from tika import detector
from tika.detector import from_file, from_buffer

class BasicTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1+1, 2)

    def test_detect_pdf(self):
        resp = from_file('tika/tests/arguments/Newton.pdf')
        self.assertEqual(resp, 'application/pdf')

    def test_detect_doc(self):
        resp = from_file('tika/tests/arguments/Newton.doc')
        self.assertEqual(resp, 'application/msword')

    def test_detect_pdf_buffer(self):
        with open('tika/tests/arguments/Newton.pdf', 'rb') as f:
            resp = from_buffer(f.read())
            self.assertEqual(resp, 'application/pdf')

    def test_detect_doc_buffer(self):
        with open('tika/tests/arguments/Newton.doc', 'rb') as f:
            resp = from_buffer(f.read())
            self.assertEqual(resp, 'application/msword')


if __name__ == '__main__':
    unittest.main()