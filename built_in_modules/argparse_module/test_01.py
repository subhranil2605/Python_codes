import unittest
import ap_01


class TestName(unittest.TestCase):

    def test_name(self):
        self.assertEqual(ap_01.full_name(first='Subhranil', middle='Kumar', last='Sarkar'), "Subhranil Kumar Sarkar")
        self.assertEqual(ap_01.full_name(first='subhranil', middle='kumar', last='sarkar'), "Subhranil Kumar Sarkar")
        self.assertEqual(ap_01.full_name(first='Subhranil', last='Sarkar'), "Subhranil Sarkar")
        self.assertEqual(ap_01.full_name(first='subhranil', last='sarkar'), "Subhranil Sarkar")
        self.assertEqual(ap_01.full_name('subhranil', 'sarkar'), "Subhranil Sarkar")
        self.assertEqual(ap_01.full_name('subhranil', 'sarkar', 'kumar'), "Subhranil Kumar Sarkar")
        
        with self.assertRaises(TypeError):
            ap_01.full_name()
            ap_01.full_name('subhranil')



if __name__ == "__main__":
    unittest.main()
