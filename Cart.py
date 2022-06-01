
from this import d


class Cart:
    
    cart = {}

    def __init__(self) -> None:
        self.cart = {}

    @classmethod
    def tambah_product(cls, nama_product, jumlah):
        key_product = nama_product.lower().replace(' ', '_')
        if not cls.cart.get(key_product):
            cls.cart[key_product] = {
                'nama': nama_product,
                'jumlah': jumlah
            }
        else:
            cls.cart[key_product]['jumlah'] += jumlah

    @classmethod
    def hapus_product(cls, kode_product):

        key_product = kode_product.lower().replace(' ', '_')
        try:
            del cls.cart[key_product]
        except Exception as e:
            print ('Product yg ingin dihapus tidak ada')

    
    @classmethod
    def tampilkan_cart(cls):
        for item in cls.cart:
            print (cls.cart.get(item))
    
    @classmethod
    def get_cart(cls):
        return cls.cart['pisang_hijau']


if __name__ == '__main__':
    cart_obj = Cart()
    cart_obj.tambah_product('Pisang Hijau', 2)
    cart_obj.tambah_product('Apel Merah', 1)
    cart_obj.tambah_product('Apel Merah', 2)
    cart_obj.tambah_product('Apel Merah', 4)
    cart_obj.hapus_product('Pisang Hijau', 1)
    cart_obj.hapus_product('Pisang Hijau', 2)
    cart_obj.tampilkan_cart()



