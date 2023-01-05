class Node:
    def __init__(self, data, priority) -> None:
        self._data = data
        self._priority = priority
        self._next = None
        self._prev = None

class PQSTugas:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def isEmpty(self) -> bool:
        if self._size == 0:
            return True
        else:
            return False
        
    def printAll(self) -> None:
        if self.isEmpty() == True:
            print("Tidak ada tugas")
        else:
            print("\n### Prioritas Tugas ###")
            while self._head != None:
                print("[",self._head._priority,"] :",self._head._data, end='')
                self._head = self._head._next
            print()

    def _addHead(self, newNode) -> None:
        tambah = newNode
        if self.isEmpty():
            self._head = tambah
            self._tail = tambah

    def _addTail(self, newNode) -> None:
        pass
    def _addMiddle(self, newNode) -> None:
        #isi kode anda
        pass
    def add(self, data, priority) -> None:
        new = Node(data,priority)
        if self.isEmpty():
            self._head = new
            self._tail = new
        elif self._size == 1:
            if self._head._priority > priority:
                new._next = self._head
                new = self._head._prev
                self._head = new
            else:
                self._head._next = new
                new._prev = self._head
                self._tail = new
        
        else:
            if self._head._priority > priority:
                new._next = self._head
                self._head._prev = new
                self._head = new
            elif self._tail._priority <= priority:
                self._tail._next = new
                new._prev = self._tail
                self._tail = new
            else:
                bantu = self._head
                while bantu._priority < priority:
                    bantu = bantu._next
                bantu2 = bantu._prev
                new._next = bantu
                bantu._prev = new
                bantu2._next = new
                new._prev = bantu2
        self._size = self._size +1
    def remove(self) -> None:
        if self.isEmpty() == False:
            hapus = self._head
            if self._size == 1:
                self._head = None
            else:
                self._head = self._head._next
                self._head._prev = None
            del hapus
            self._size -= 1

    def removePriority(self, priority) -> None:
        lis = []
        for i in range(len(self._data)):
            if self._data[i][1] == priority:
                del self._data[i][1]
        for j in range (len(self._data)):
            if len(self._data[j]) == 1:
                pass
            else:
                lis.append(self._data[j])
        self._data = lis
        self._size -= 1

if __name__ == "__main__":
    tugasKu = PQSTugas()
    tugasKu.add("StrukDat",1)
    tugasKu.printAll()
    tugasKu.add("Menyapu", 5)
    tugasKu.add("Cuci Baju", 4)
    tugasKu.add("Beli Alat Tulis", 3)
    tugasKu.add("Cuci Sepatu", 4)
    tugasKu.printAll()
    tugasKu.remove()
    tugasKu.printAll()
    tugasKu.removePriority(2)
    tugasKu.removePriority(4)
    tugasKu.printtAll()