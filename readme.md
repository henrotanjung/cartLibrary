Task:

Data Structure - Shopping Cart
Buat sebuah Software Library Shopping Cart yang harus memilik fungsi:

void tambahProduk(string kodeProduk, int kuantitas)
Menambahkan produk dengan kuantitas yang ditentukan.
Apabila produk sudah ada di dalam Cart, tambahkan kuantitasnya.
void hapusProduk(string kodeProduk)
Menghapus produk dari Cart.
void tampilkanCart()
Menampilkan isi Cart dengan format {kodeProduk} ({kuantitas})
Buatlah class Cart berikut feature code dan unit testnya.

Sebagai contoh gunakan skenario di bawah:

Cart keranjang = new Cart();

keranjang.tambahProduk("Pisang Hijau", 2);

keranjang.tambahProduk("Semangka Kuning", 3);

keranjang.tambahProduk("Apel Merah", 1);
keranjang.tambahProduk("Apel Merah", 4);
keranjang.tambahProduk("Apel Merah", 2);

keranjang.hapusProduk("Semangka Kuning");

keranjang.hapusProduk("Semangka Merah");

keranjang.tampilkanCart();
Output:

Pisang Hijau (2)
Apel Merah (7)


#@classmethod
    # def hapus_product(cls, nama_product, jumlah):

    #     key_product = nama_product.lower().replace(' ', '_')
    #     if cls.cart.get(key_product):
    #         cls.cart[key_product]['jumlah'] -= jumlah
    #         product_in_cart = cls.cart[key_product]['jumlah'] - jumlah
    #         if product_in_cart < 0:
    #             cls.cart[key_product]['jumlah'] = 0
