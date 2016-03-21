import unittest
import sys
if sys.version_info.major == 2:
    import mock    
else:
    from unittest import mock
import json
# from tika import detector
from tika.detector import from_file, from_buffer

class DetectorTest(unittest.TestCase):
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


from tika.language import from_file as lang_from_file
from tika.language import from_buffer as lang_from_buffer
class LanguageTest(unittest.TestCase):
    """
    my setup keeps
    returning 'sk' (Slovenian)
    or 'hu' (Hungarian)!
    as the language from these documents
    check if this is a known bug
    """
    def test_language_pdf(self):
        resp = lang_from_file('tika/tests/arguments/Newton.pdf')
        print(resp)
        self.assertTrue(resp is not None)
        self.assertEqual(len(resp), 2)

    def test_language_de_pdf(self):
        resp = lang_from_file('tika/tests/arguments/Newton_de.pdf')
        print(resp)
        self.assertTrue(resp is not None)
        self.assertEqual(len(resp), 2)

    def test_language_doc(self):
        resp = lang_from_file('tika/tests/arguments/Newton.doc')
        print(resp)
        self.assertTrue(resp is not None)
        self.assertEqual(len(resp), 2)

    def test_language_de_doc(self):
        resp = lang_from_file('tika/tests/arguments/Newton_de.doc')
        print(resp)
        self.assertTrue(resp is not None)
        self.assertEqual(len(resp), 2)

    def test_language_pdf_buf(self):
        with open('tika/tests/arguments/Newton.pdf', 'rb') as f:
            resp = lang_from_buffer(f.read())
            print(resp)
            self.assertTrue(resp is not None)
            self.assertEqual(len(resp), 2)

    def test_language_de_pdf(self):
        with open('tika/tests/arguments/Newton_de.pdf', 'rb') as f:
            resp = lang_from_buffer(f.read())
            print(resp)
            self.assertTrue(resp is not None)
            self.assertEqual(len(resp), 2)

    def test_language_doc(self):
        with open('tika/tests/arguments/Newton.doc', 'rb') as f:
            resp = lang_from_buffer(f.read())
            print(resp)
            self.assertTrue(resp is not None)
            self.assertEqual(len(resp), 2)

    def test_language_de_doc(self):
        with open('tika/tests/arguments/Newton_de.doc', 'rb') as f:
            resp = lang_from_buffer(f.read())
            print(resp)
            self.assertTrue(resp is not None)
            self.assertEqual(len(resp), 2)

if __name__ == '__main__':
    unittest.main()