class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
    def getNamaPelanggan(self):
        return self._namaPelanggan
    def setNamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru

class WarungMakan:
    DEFAULT_CAPACITY = 5
    def __init__(self): #tidak boleh mengganti / menambah metode init
        self._data = [None] * WarungMakan.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def dequeue(self): #menghapus data paling depan, dan memajukan urutan data yang dibelangkangnya
        if self.is_empty():
            print("Kosong")
        ini = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1)%len(self._data)
        self._size -= 1
        print("\n### Pelanggan",ini.getNamaPelanggan(), "Selesai Membayar ###")
        
        baru = [None] * len(self._data)
        count = 0
        for l in range(len(self._data)):
            if self._data[l] != None:
                baru[count] = self._data[l]
                count += 1
        self._data = baru
        self._front = 0

    def enqueue(self, namaPelanggan): #menambah data ke list
        new = NodePelanggan(namaPelanggan)
        if self._size == len(self._data):
            self.resizeBy3(3+len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = new
        self._size += 1

    def resizeBy3(self,cap): #menambah ukuran queue sebesar 3
        lama = self._data
        self._data = [None]*cap
        dpn = self._front
        for j in range(self._size):
            self._data[j] = lama[dpn]
            dpn = (1+dpn) %len(lama)
        self._front = 0
        print("\n### Melakukan Resize 3###")

    def printAll(self):
        print("\n=== WarungMakan ===")
        for i in range(len(self._data)):
            if self._data[i] != None:
                print(i+1, end=". ")
                print(self._data[i].getNamaPelanggan())
            else:
                print(i+1,end=". ")
                print("Kosong")


# test case program
wm = WarungMakan()
wm.enqueue("Pelanggan A")
wm.enqueue("Pelanggan B")
wm.enqueue("Pelanggan C")
wm.enqueue("Pelanggan D")
wm.enqueue("Pelanggan E")
wm.printAll()
wm.enqueue("Pelanggan F")
wm.enqueue("Pelanggan G")
wm.printAll()
wm.dequeue()
wm.dequeue()
wm.dequeue()
wm.printAll()