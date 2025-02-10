from project2 import Mod
import unittest


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestMod(unittest.TestCase):

    def setUp(self):
        self.value = 11
        self.modulus = 3

        # Mod objects for comparison tests #
        self.m1 = Mod(15, 5)
        self.m2 = Mod(3, 5)
        self.m3 = Mod(15, 5)
        self.m4 = Mod(10, 5)
        self.m5 = Mod(2, 5)
    

    def test_create_mod(self):
        m1 = Mod(self.value, self.modulus)

        self.assertEqual(m1.modulus, self.modulus)
        self.assertEqual(m1.value, self.value % self.modulus)
    
    def test_create_mod_invalid_values(self):
        with self.assertRaises(TypeError):
            m1 = Mod("hello", self.modulus)
    
        with self.assertRaises(TypeError):
            m1 = Mod(self.value, "hello")

        with self.assertRaises(TypeError):
            m1 = Mod(None, self.modulus)

        with self.assertRaises(TypeError):
            m1 = Mod(self.value, None)
    
    def test_mod_equality(self):
        m1 = Mod(self.value, self.modulus)
        m2 = Mod(self.value, self.modulus)
        m3 = Mod(self.value + 2, self.modulus)
        m4 = Mod(self.value, self.modulus + 1)

        self.assertEqual(m1, m2)
        self.assertNotEqual(m1, m3)
        self.assertNotEqual(m1, m4)
    
    def test_mod_hash(self):
        m1 = Mod(self.value, self.modulus)
        m2 = Mod(self.value, self.modulus)

        self.assertEqual(hash(m1), hash((m1.modulus, m1.value)))
        self.assertEqual(hash(m1), hash(m2))
    
    def test_mod_int(self):
        m1 = Mod(self.value, self.modulus)

        self.assertEqual(int(m1), m1.value)
    
    def test_mod_sum_isum(self):
        m1 = Mod(self.value, self.modulus)
        m2 = Mod(self.value + 2, self.modulus)

        m_sum = m1 + m2
        self.assertEqual(m_sum.value, (m1.value + m2.value) % m1.modulus)
        self.assertEqual(m_sum.modulus, m1.modulus)

        m1 += m2
        self.assertEqual(m1.value, (self.value + m2.value) % self.modulus)
        self.assertEqual(m1.modulus, self.modulus)
    
    def test_mod_sum_isum_int(self):
        m1 = Mod(self.value, self.modulus)

        m_sum = m1 + 5
        self.assertEqual(m_sum.value, (m1.value + 5) % m1.modulus)
        self.assertEqual(m_sum.modulus, m1.modulus)

        m1 += 5
        self.assertEqual(m1.value, (self.value + 5) % self.modulus)
        self.assertEqual(m1.modulus, self.modulus)
    
    def test_mod_sum_isum_invalid_value_error(self):
        m1 = Mod(self.value, self.modulus)
        self.modulus += 2
        m2 = Mod(self.value, self.modulus)

        with self.assertRaises(TypeError):
            m_sum = m1 + m2
        with self.assertRaises(TypeError):
            m_sum = m1 + "hello"
        with self.assertRaises(TypeError):
            m1 += m2
        with self.assertRaises(TypeError):
            m1 += "hello"
    
    def test_mod_subtraction_isub(self):
        m1 = Mod(self.value, self.modulus)
        m2 = Mod(self.value + 2, self.modulus)

        m_sub = m1 - m2
        self.assertEqual(m_sub.value, (m1.value - m2.value) % m1.modulus)
        self.assertEqual(m_sub.modulus, m1.modulus)

        m1 -= m2
        self.assertEqual(m1.value, (self.value - m2.value) % self.modulus)
        self.assertEqual(m1.modulus, self.modulus)

        m_sub = m1 - 5
        self.assertEqual(m_sub.value, (m1.value - 5) % m1.modulus)
        self.assertEqual(m_sub.modulus, m1.modulus)

        old_value = m1.value
        m1 -= 5
        self.assertEqual(m1.value, (old_value - 5) % self.modulus)
        self.assertEqual(m1.modulus, self.modulus)
    
    def test_mod_subtraction_isub_invalid_value_error(self):
        m1 = Mod(self.value, self.modulus)
        self.modulus += 2
        m2 = Mod(self.value, self.modulus)

        with self.assertRaises(TypeError):
            m_sub = m1 - m2
        with self.assertRaises(TypeError):
            m_sub = m1 - "hello"
        with self.assertRaises(TypeError):
            m1 -= m2
        with self.assertRaises(TypeError):
            m1 -= "hello"
    
    
    def test_mod_mul_imul(self):
        m1 = Mod(self.value, self.modulus)
        m2 = Mod(self.value + 2, self.modulus)

        m_mul = m1 * m2
        self.assertEqual(m_mul.value, (m1.value * m2.value) % m1.modulus)
        self.assertEqual(m_mul.modulus, m1.modulus)

        m1 *= m2
        self.assertEqual(m1.value, (self.value * m2.value) % self.modulus)
        self.assertEqual(m1.modulus, self.modulus)

        m_mul = m1 * 5
        self.assertEqual(m_mul.value, (m1.value * 5) % m1.modulus)
        self.assertEqual(m_mul.modulus, m1.modulus)

        old_value = m1.value
        m1 *= 5
        self.assertEqual(m1.value, (old_value * 5) % self.modulus)
        self.assertEqual(m1.modulus, self.modulus)
    
    def test_mod_mul_imul_invalid_value_error(self):
        m1 = Mod(self.value, self.modulus)
        self.modulus += 2
        m2 = Mod(self.value, self.modulus)

        with self.assertRaises(TypeError):
            m_mul = m1 * m2
        with self.assertRaises(TypeError):
            m_mul = m1 * "hello"
        with self.assertRaises(TypeError):
            m1 *= m2
        with self.assertRaises(TypeError):
            m1 *= "hello"
    

    def test_mod_pow_ipow(self):
        m1 = Mod(self.value, self.modulus)
        m2 = Mod(self.value + 2, self.modulus)

        m_pow = m1 ** m2
        self.assertEqual(m_pow.value, (m1.value ** (m2.value % self.modulus)) % m1.modulus)
        self.assertEqual(m_pow.modulus, m1.modulus)

        m1 **= m2
        self.assertEqual(m1.value, (self.value ** (m2.value % self.modulus)) % self.modulus)
        self.assertEqual(m1.modulus, self.modulus)

        m_pow = m1 ** 5
        self.assertEqual(m_pow.value, (m1.value ** (5 % self.modulus)) % m1.modulus)
        self.assertEqual(m_pow.modulus, m1.modulus)

        old_value = m1.value
        m1 **= 5
        self.assertEqual(m1.value, (old_value ** (5 % self.modulus)) % self.modulus)
        self.assertEqual(m1.modulus, self.modulus)
    
    def test_mod_pow_ipow_invalid_value_error(self):
        m1 = Mod(self.value, self.modulus)
        self.modulus += 2
        m2 = Mod(self.value, self.modulus)

        with self.assertRaises(TypeError):
            m_pow = m1 ** m2
        with self.assertRaises(TypeError):
            m_pow = m1 ** "hello"
        with self.assertRaises(TypeError):
            m1 **= m2
        with self.assertRaises(TypeError):
            m1 **= "hello"

    def test_mod_equality(self):
        self.assertEqual(self.m1, self.m3)
        self.assertNotEqual(self.m1, self.m2)

    def test_mod_greater(self):
        self.assertTrue(self.m2 > self.m1)
        self.assertFalse(self.m1 > self.m3)
        self.assertTrue(self.m1 >= self.m3)
        self.assertFalse(self.m1 >= self.m2)
    
    def test_mod_greater_int(self):
        self.assertTrue(self.m2 > 1)
        self.assertFalse(self.m1 > 1)
        self.assertTrue(self.m1 >= 0)
        self.assertFalse(self.m1 >= 3)

    def test_mod_less_than(self):
        self.assertFalse(self.m2 < self.m1)
        self.assertTrue(self.m1 < self.m5)
        self.assertTrue(self.m1 <= self.m3)
        self.assertFalse(self.m2 <= self.m5)
    
    def test_mod_less_than_int(self):
        self.assertFalse(self.m2 < 3)
        self.assertTrue(self.m1 < 3)
        self.assertTrue(self.m1 <= 0)
        self.assertFalse(self.m2 <= 2)


run_tests(TestMod)