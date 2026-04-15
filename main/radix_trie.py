# Bai tap cau truc du lieu - Radix Trie
# sinh vien thuc hien: ...

class Node:
    def __init__(self, key=""):
        self.key = key
        self.children = {}
        self.is_end = False  # danh dau ket thuc tu
        self.nghia = None    # luu nghia cua tu


class TuDien:
    def __init__(self):
        self.root = Node()
        self.so_tu = 0  # dem so luong tu

    # ham tinh do dai phan chung giua 2 chuoi
    def _common_prefix(self, s1, s2):
        i = 0
        while i < len(s1) and i < len(s2):
            if s1[i] != s2[i]:
                break
            i += 1
        return i

    # them tu vao tu dien
    def them_tu(self, word, nghia):
        node = self.root
        i = 0

        while i < len(word):
            c = word[i]

            # neu ky tu nay chua co trong children thi tao node moi
            if c not in node.children:
                new_node = Node(word[i:])
                new_node.is_end = True
                new_node.nghia = nghia
                node.children[c] = new_node
                self.so_tu += 1
                return True

            child = node.children[c]
            cl = self._common_prefix(word[i:], child.key)

            if cl == len(child.key):
                # di tiep xuong
                node = child
                i += cl
            else:
                # phai tach node ra (split)
                # tao node chua phan con lai cua child cu
                split = Node(child.key[cl:])
                split.children = child.children
                split.is_end = child.is_end
                split.nghia = child.nghia

                # cap nhat child hien tai
                child.key = child.key[:cl]
                child.children = {split.key[0]: split}
                child.is_end = False
                child.nghia = None

                rem = word[i + cl:]
                if rem:
                    # them node moi cho phan con lai cua word
                    leaf = Node(rem)
                    leaf.is_end = True
                    leaf.nghia = nghia
                    child.children[rem[0]] = leaf
                else:
                    child.is_end = True
                    child.nghia = nghia

                self.so_tu += 1
                return True

        # truong hop word da ton tai roi
        is_new = not node.is_end
        node.is_end = True
        node.nghia = nghia
        if is_new:
            self.so_tu += 1
        return is_new

    # tim nghia cua tu
    def tim_nghia(self, word):
        node = self.root
        i = 0

        while i < len(word):
            c = word[i]
            if c not in node.children:
                return None  # khong tim thay

            child = node.children[c]
            cl = self._common_prefix(word[i:], child.key)

            if cl != len(child.key):
                return None

            node = child
            i += cl

        if node.is_end:
            return node.nghia
        return None

    # xoa tu khoi tu dien
    def xoa_tu(self, word):
        da_tim_thay = [False]

        def _xoa(node, con_lai):
            if con_lai == "":
                if not node.is_end:
                    return False  # tu nay ko ton tai
                node.is_end = False
                node.nghia = None
                da_tim_thay[0] = True
                # neu ko co con thi xoa node nay luon
                return len(node.children) == 0

            c = con_lai[0]
            if c not in node.children:
                return False

            child = node.children[c]
            cl = self._common_prefix(con_lai, child.key)

            if cl != len(child.key):
                return False

            nen_xoa = _xoa(child, con_lai[cl:])

            if nen_xoa:
                del node.children[c]

            # merge neu chi con 1 con va node nay khong phai ket thuc tu
            if len(node.children) == 1 and not node.is_end and node is not self.root:
                k = next(iter(node.children))
                only_child = node.children[k]
                node.key += only_child.key
                node.is_end = only_child.is_end
                node.nghia = only_child.nghia
                node.children = only_child.children
                return False

            return len(node.children) == 0 and not node.is_end

        _xoa(self.root, word)

        if da_tim_thay[0]:
            self.so_tu -= 1
        return da_tim_thay[0]

    def __contains__(self, word):
        return self.tim_nghia(word) is not None

    def __len__(self):
        return self.so_tu

    # lay tat ca cac tu bat dau bang prefix
    def tim_theo_prefix(self, prefix=""):
        ket_qua = []

        node = self.root
        i = 0
        while i < len(prefix):
            c = prefix[i]
            if c not in node.children:
                return ket_qua
            child = node.children[c]
            cl = self._common_prefix(prefix[i:], child.key)
            if cl < len(child.key) and i + cl < len(prefix):
                return ket_qua
            node = child
            i += cl

        # dfs de lay het cac tu
        def dfs(n, cur):
            if n.is_end:
                ket_qua.append((cur, n.nghia))
            for child in n.children.values():
                dfs(child, cur + child.key)

        dfs(node, prefix)
        return ket_qua

    # in cay ra man hinh de kiem tra
    def in_cay(self, node=None, prefix=""):
        if node is None:
            node = self.root
            print(f"Root -- co {self.so_tu} tu")

        ds = list(node.children.items())
        for i, (_, child) in enumerate(ds):
            last = (i == len(ds) - 1)
            connector = "L-- " if last else "|-- "
            dau = f" -> {child.nghia}" if child.is_end else ""
            print(f"{prefix}{connector}[{child.key}]{dau}")
            self.in_cay(child, prefix + ("    " if last else "|   "))