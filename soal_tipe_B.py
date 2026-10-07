"""
PRAKTIKUM DOUBLY LINKED LIST -- TIPE B   (Soal 12 s.d. 22)
=====================================================================
Data awal tipe ini : ['K', 'L', 'M', 'N']
Catatan tipe       : List lebih panjang (4 node), target di tengah.

CARA KERJA
- Setiap nomor soal dikerjakan oleh SATU mahasiswa. Isi NIM & NAMA pada blok
  identitas milik nomor soal Anda, lalu tulis kode pada fungsi soal Anda
  (ganti baris `pass`). Jangan mengubah nama fungsi/parameter dan helper.py.
- Jalankan  python3 soal_tipe_B.py  untuk melihat hasil pengujian otomatis.

STRUKTUR OBJEK (ada di helper.py, tinggal dipakai)
    class Node:
        self.info  -> data node (mis. "K") [atau self.isi]
        self.prev  -> pointer ke node sebelumnya (None jika di ujung kiri)
        self.next  -> pointer ke node sesudahnya  (None jika di ujung kanan)

    class DoublyLinkedList:
        self.first -> pointer ke node paling depan (None jika list kosong) [atau self.head]
        self.last  -> pointer ke node paling belakang (None jika list kosong) [atau self.tail]

- Membuat node baru : P = Node("X")
- Pointer next dan prev HARUS konsisten (diperiksa otomatis dua arah).
"""

from helper import Node, DoublyLinkedList, jalankan_pengujian


# ======================================================================
# SOAL 12 -- Insert Empty Node
# ======================================================================
NIM_12 = "108102530001"
NAMA_12 = "Yeni Trisnawati"

def soal_12_insert_empty(dll, data):
    """
    Sisipkan node berisi "T" ke list yang masih KOSONG.
    Kondisi awal : KOSONG
    Hasil        : T

    PSEUDOCODE:
    P = Node(data)
    dll.first = P
    dll.last = P
    """
    P = Node(data)
    dll.first = P
    dll.last = P


# ======================================================================
# SOAL 13 -- Insert First Node
# ======================================================================
NIM_13 = "108102500035"
NAMA_13 = "MUHAMMAD NABIL ALTHAAF"

def soal_13_insert_first(dll, data):
    """
    Sisipkan node "U" di posisi PALING DEPAN list.
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : U <-> K <-> L <-> M <-> N

    PSEUDOCODE:
    P = Node(data)
    P.next = dll.first
    dll.first.prev = P
    dll.first = P
    """
    P = Node(data)
    P.next = dll.first
    dll.first.prev = P
    dll.first = P # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 14 -- Insert Last Node
# ======================================================================
NIM_14 = "108102500037"
NAMA_14 = "Faatin Jamiilatul Hasanah"

def soal_14_insert_last(dll, data):
    """
    Sisipkan node "V" di posisi PALING BELAKANG list.
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : K <-> L <-> M <-> N <-> V

    PSEUDOCODE:
    P = Node(data)
    P.prev = dll.last
    dll.last.next = P
    dll.last = P
    """
  def soal_14_insert_last(dll, data):
    """Sisipkan node baru di posisi paling belakang list."""
    # 1. Buat node baru
    P = Node(data)  #

    # 2. Jika list masih kosong
    if dll.first is None:
        dll.first = P
        dll.last = P
        return

    # 3. Jika list tidak kosong, sambungkan ke node terakhir (dll.last)
    P.prev = dll.last  #
    dll.last.next = P  #
    dll.last = P  #[cite: 2]
    P = Node(data)
    p.prev = dll.last
    dll.last.next = P
    dll.last = P

# ======================================================================
# SOAL 15 -- Insert After Target Node
# ======================================================================
NIM_15 = "108102500017"
NAMA_15 = "Nathanael Omri Yesurun"

def soal_15_insert_after(dll, node_target, data):
    """
    Sisipkan node "W" tepat SETELAH node_target (node "L").
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : K <-> L <-> W <-> M <-> N

    PSEUDOCODE:
    P = Node(data)
    Q = node_target.next
    P.prev = node_target
    P.next = Q
    node_target.next = P
    Q.prev = P
    """
    

# ======================================================================
# SOAL 16 -- Insert Before Target Node
# ======================================================================
NIM_16 = "108102530013"
NAMA_16 = "M. Albani Mufti Radja T"

def soal_16_insert_before(dll, node_target, data):
    """
    Sisipkan node "Z" tepat SEBELUM node_target (node "M").
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : K <-> L <-> Z <-> M <-> N

    PSEUDOCODE:
    P = Node(data)
    Q = node_target.prev
    P.next = node_target
    P.prev = Q
    node_target.prev = P
    Q.next = P
    """
    pass  # <-- tulis kode Anda di sini
  
    #def soal_16_insert_before(dll, node_target, data):
    P = Node(data)
    Q = node_target.prev
    P.next = node_target
    P.prev = Q
    node_target.prev = P
    if Q is not None:
        Q.next = P
    else:
        dll.head = P  # target adalah head, jadi P jadi head baru
  

# ======================================================================
# SOAL 17 -- Traverse Maju
# ======================================================================
NIM_17 = "ISI_NIM"
NAMA_17 = "ISI_NAMA"

def soal_17_traverse_maju(dll):
    """
    Telusuri list dari first ke last, kembalikan string info node dipisah " <-> ".
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : "K <-> L <-> M <-> N"

    PSEUDOCODE:
    hasil = ""
    P = dll.first
    WHILE P is not None:
        hasil = GABUNG_STRING(hasil, P.info)
        P = P.next
    RETURN hasil
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 18 -- Traverse Mundur
# ======================================================================
NIM_18 = "108102500053"
NAMA_18 = "CHARMALITA AUDRAY PRISCHA SANU"

def soal_18_traverse_mundur(dll):
    """
    Telusuri list dari last ke first, kembalikan string info node dipisah " <-> ".
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : "N <-> M <-> L <-> K"

    PSEUDOCODE:
    hasil = ""
    P = dll.last
    WHILE P is not None:
        hasil = GABUNG_STRING(hasil, P.info)
        P = P.prev
    RETURN hasil
    """
    pass  # <-- tulis kode Anda di sini

def soal_18_traverse_mundur(dll):
    hasil = ""
    P = dll.last

    while P is not None:
        if hasil == "":
            hasil = P.info
        else:
            hasil = hasil + " <-> " + P.info
        P = P.prev

    return hasil
  
# ======================================================================
# SOAL 19 -- Search Target
# ======================================================================
NIM_19 = "108102500058"
NAMA_19 = "Fathya Salsabila"

def soal_19_search(dll, target):
    """
    Cari node berisi "M" dan kembalikan NODE-nya (bukan string). List tidak berubah.
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : node "M"

    PSEUDOCODE:
    P = dll.first
    WHILE P is not None:
        IF P.info == target:
            RETURN P
        P = P.next
    RETURN None
    """
    
 P = dll.first
    WHILE P is not None:
        IF P.info == target:
            RETURN P
        P = P.next
    RETURN None
# ======================================================================
# SOAL 20 -- Delete First Node
# ======================================================================
NIM_20 = "108102500009"
NAMA_20 = "NI MADE SINTIA PRASTINI"

def soal_20_delete_first(dll):
    """
    Hapus node PALING DEPAN dari list.
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : L <-> M <-> N

    PSEUDOCODE:
    dll.first = dll.first.next
    dll.first.prev = None
    """
    dll.first = dll.first.next
    dll.first.prev = None

# ======================================================================
# SOAL 21 -- Delete Last Node
# ======================================================================
NIM_21 = "108102500028"
NAMA_21 = "Nicholas Musa Surya Susanto"

def soal_21_delete_last(dll):
    """
    Hapus node PALING BELAKANG dari list.
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : K <-> L <-> M

    PSEUDOCODE:
    dll.last = dll.last.prev
    dll.last.next = None
    """
    dll.last = dll.last.prev
    dll.last.next = None

# ======================================================================
# SOAL 22 -- Delete Target Node
# ======================================================================
NIM_22 = "108102530008"
NAMA_22 = "Gede Bagus Narindra Utama"

def soal_22_delete_node(dll, node_target):
    """
    Hapus node_target (node "L") dari list.
    Kondisi awal : K <-> L <-> M <-> N
    Hasil        : K <-> M <-> N

    PSEUDOCODE:
    P = node_target.prev
    Q = node_target.next
    P.next = Q
    Q.prev = P
    """
   if node_target is None:
     return
   P = node_target.prev
   Q = node_target.next

   if P is not None:
     P.next = Q
   else:
     dll.first = Q
     
   if Q is not None:
     Q.prev = P
   else:
     dll.last = P


if __name__ == "__main__":
    jalankan_pengujian(12, "Insert Empty Node", NAMA_12, NIM_12, soal_12_insert_empty,
                       [], ('T',), "T", "ubah")
    jalankan_pengujian(13, "Insert First Node", NAMA_13, NIM_13, soal_13_insert_first,
                       ['K', 'L', 'M', 'N'], ('U',), "U <-> K <-> L <-> M <-> N", "ubah")
    jalankan_pengujian(14, "Insert Last Node", NAMA_14, NIM_14, soal_14_insert_last,
                       ['K', 'L', 'M', 'N'], ('V',), "K <-> L <-> M <-> N <-> V", "ubah")
    jalankan_pengujian(15, "Insert After Target Node", NAMA_15, NIM_15, soal_15_insert_after,
                       ['K', 'L', 'M', 'N'], ('L', 'W'), "K <-> L <-> W <-> M <-> N", "ubah")
    jalankan_pengujian(16, "Insert Before Target Node", NAMA_16, NIM_16, soal_16_insert_before,
                       ['K', 'L', 'M', 'N'], ('M', 'Z'), "K <-> L <-> Z <-> M <-> N", "ubah")
    jalankan_pengujian(17, "Traverse Maju", NAMA_17, NIM_17, soal_17_traverse_maju,
                       ['K', 'L', 'M', 'N'], (), "K <-> L <-> M <-> N", "string")
    jalankan_pengujian(18, "Traverse Mundur", NAMA_18, NIM_18, soal_18_traverse_mundur,
                       ['K', 'L', 'M', 'N'], (), "N <-> M <-> L <-> K", "string")
    jalankan_pengujian(19, "Search Target", NAMA_19, NIM_19, soal_19_search,
                       ['K', 'L', 'M', 'N'], ('M',), "M", "node")
    jalankan_pengujian(20, "Delete First Node", NAMA_20, NIM_20, soal_20_delete_first,
                       ['K', 'L', 'M', 'N'], (), "L <-> M <-> N", "ubah")
    jalankan_pengujian(21, "Delete Last Node", NAMA_21, NIM_21, soal_21_delete_last,
                       ['K', 'L', 'M', 'N'], (), "K <-> L <-> M", "ubah")
    jalankan_pengujian(22, "Delete Target Node", NAMA_22, NIM_22, soal_22_delete_node,
                       ['K', 'L', 'M', 'N'], ('L',), "K <-> M <-> N", "ubah")
