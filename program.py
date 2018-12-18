nama=input("masukan nama barang = ")
x=int(input("masukan harga banrang = "))
jb=int(input("masukan jumlah barang = "))
total=x*jb
print("total harga",nama,"anda adalah Rp.",total)
pem=int(input("masukan pembayaran = "))
hu=total-pem
if (pem>total):
	print("jumlah kembalian anda adalah Rp.",pem-total)
else:
	print:("anda memiliki hutang Rp.",hu)
