import unittest
from unittest.mock import Mock
import Cart as TestCase


class TestCartLibrary(unittest.TestCase):

    def setUp(self):
        self.cart = {}

    def tearDown(self) :
        TestCase.Cart.cart = {}
    
    def test_total_cart_single(self):
        """single adding"""
        cart_obj = TestCase.Cart()
        cart_obj.tambah_product('Pisang Hijau', 2)
        expected = 2
        actual_result = TestCase.Cart.cart.get('pisang_hijau').get('jumlah')
        self.assertEqual(expected, actual_result)
    
    def test_total_cart_multi(self):
        """multi adding 1 jenis product"""
        cart_obj = TestCase.Cart()
        for jumlah in ([2, 5]):
            cart_obj.tambah_product('Pisang Hijau', jumlah)
            
        expected = 7
        actual_result = TestCase.Cart.cart.get('pisang_hijau').get('jumlah')
        self.assertEqual(expected, actual_result)
    
    def test_total_multi_product(self):
        """multi products"""
        
        products = [
            {'nama': 'Pisang Hijau', 'jumlah': 2},
            {'nama': 'Apel Merah', 'jumlah': 5}
        ]

        cart_obj = TestCase.Cart()
        for product in products:
            cart_obj.tambah_product(product['nama'], product['jumlah'])

        expected_pisang = 2
        expected_apel = 5
        actual_result_pisang = TestCase.Cart.cart.get('pisang_hijau').get('jumlah')
        actual_result_apel = TestCase.Cart.cart.get('apel_merah').get('jumlah')
        self.assertEqual(expected_pisang, actual_result_pisang)
        self.assertEqual(expected_apel, actual_result_apel)

    def test_hapus_product(self):

        TestCase.Cart.cart['pisang_hijau'] = {'nama': 'Pisang Hijau', 'jumlah': 5}
        test_cart_obj = TestCase.Cart()
        test_cart_obj.hapus_product('Pisang Hijau')
        self.assertEqual(None, TestCase.Cart.cart.get('pisang_hijau'))
        

if __name__ == '__main__':
    unittest.main()