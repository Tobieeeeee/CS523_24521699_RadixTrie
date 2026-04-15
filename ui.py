import os
import tkinter as tk
from tkinter import messagebox, simpledialog

# Import core logic từ thư mục của bạn
from main.radix_trie import TuDien

class TuDienApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Từ Điển Anh - Việt (Radix-Trie)")
        # Tăng chiều cao cửa sổ lên để lấy chỗ đặt bảng đen
        self.root.geometry("500x650") 
        self.root.eval('tk::PlaceWindow . center')

        self.tu_dien = TuDien()
        self.load_du_lieu()

        self.tao_giao_dien()
        
        # Tự động vẽ cây lần đầu sau khi load dữ liệu
        self.ve_cay_len_bang_den("CẤU TRÚC CÂY HIỆN TẠI")

    def load_du_lieu(self):
        filepath = os.path.join('data', 'tu_vung.txt')
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split('|')
                    if len(parts) == 2:
                        self.tu_dien.them_tu(parts[0].strip(), parts[1].strip())

    def tao_giao_dien(self):
        # Frame chứa các nút bấm (Phần trên)
        frame_top = tk.Frame(self.root)
        frame_top.pack(pady=10)

        lbl_title = tk.Label(frame_top, text="TỪ ĐIỂN RADIX-TRIE", font=("Arial", 16, "bold"))
        lbl_title.pack(pady=10)

        # Xếp các nút theo hàng ngang cho gọn
        btn_tim = tk.Button(frame_top, text=" Tìm Từ", font=("Arial", 11), width=12, command=self.popup_tim_tu)
        btn_tim.pack(side=tk.LEFT, padx=5)

        btn_them = tk.Button(frame_top, text=" Thêm Từ", font=("Arial", 11), width=12, command=self.popup_them_tu)
        btn_them.pack(side=tk.LEFT, padx=5)

        btn_xoa = tk.Button(frame_top, text=" Xóa Từ", font=("Arial", 11), width=12, command=self.popup_xoa_tu)
        btn_xoa.pack(side=tk.LEFT, padx=5)

        # Chèn Bảng Đen (Phần dưới)
        lbl_bang = tk.Label(self.root, text="BẢNG MÔ PHỎNG SỰ THAY ĐỔI DỮ LIỆU", font=("Arial", 10, "bold"), fg="blue")
        lbl_bang.pack(pady=(10, 0))

        # Text Widget làm bảng đen
        self.txt_bang_den = tk.Text(self.root, bg="black", fg="#00FF00", font=("Consolas", 11), wrap=tk.NONE)
        self.txt_bang_den.pack(padx=15, pady=5, fill=tk.BOTH, expand=True)

    def ve_cay_len_bang_den(self, tieu_de):
        """Hàm duyệt cây Radix-Trie và in text lên bảng đen"""
        self.txt_bang_den.config(state=tk.NORMAL) # Mở khóa để viết chữ vào
        self.txt_bang_den.delete(1.0, tk.END)     # Xóa nội dung cũ
        self.txt_bang_den.insert(tk.END, f"=== {tieu_de} ===\n\n")

        def duyet_cay(node, prefix="", is_last=True):
            if node == self.tu_dien.root:
                self.txt_bang_den.insert(tk.END, "GỐC (Root)\n")
                
            children_items = list(node.children.items())
            for i, (char, child_node) in enumerate(children_items):
                last_item = (i == len(children_items) - 1)
                connector = "└── " if last_item else "├── "
                
                # Đánh dấu node có nghĩa
                end_mark = f" ---> ({child_node.meaning})" if child_node.is_end_of_word else ""
                
                # Ghi 1 dòng lên bảng đen
                line = f"{prefix}{connector}[{child_node.key}]{end_mark}\n"
                self.txt_bang_den.insert(tk.END, line)
                
                # Duyệt tiếp nhánh con
                new_prefix = prefix + ("    " if last_item else "│   ")
                duyet_cay(child_node, new_prefix, last_item)

        # Bắt đầu duyệt từ Root
        duyet_cay(self.tu_dien.root)
        
        self.txt_bang_den.config(state=tk.DISABLED) # Khóa lại (Read-only)

    # --- CÁC HÀM XỬ LÝ POPUP ---

    def popup_tim_tu(self):
        word = simpledialog.askstring("Tìm từ", "Nhập từ (Tiếng Anh):", parent=self.root)
        if word:
            word = word.lower().strip()
            ket_qua = self.tu_dien.tim_nghia(word)
            if ket_qua:
                messagebox.showinfo("Kết quả", f"Nghĩa của '{word}' là:\n\n{ket_qua}")
            else:
                messagebox.showwarning("Không tìm thấy", f"Từ '{word}' chưa có trong từ điển.")

    def popup_them_tu(self):
        word = simpledialog.askstring("Thêm từ mới", "Nhập từ tiếng Anh:", parent=self.root)
        if word:
            meaning = simpledialog.askstring("Thêm từ mới", f"Nhập nghĩa tiếng Việt của từ '{word}':", parent=self.root)
            if meaning:
                self.tu_dien.them_tu(word.lower().strip(), meaning.strip())                
                # CẬP NHẬT LẠI BẢNG ĐEN
                self.ve_cay_len_bang_den(f"CẤU TRÚC SAU KHI THÊM '{word.upper()}'")

    def popup_xoa_tu(self):
        word = simpledialog.askstring("Xóa từ", "Nhập từ cần xóa:", parent=self.root)
        if word:
            word = word.lower().strip()
            if self.tu_dien.tim_nghia(word):
                self.tu_dien.xoa_tu(word)
                
                # CẬP NHẬT LẠI BẢNG ĐEN
                self.ve_cay_len_bang_den(f"CẤU TRÚC SAU KHI XÓA '{word.upper()}'")
            else:
                messagebox.showerror("Lỗi", f"Không thể xóa. Từ '{word}' không tồn tại!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TuDienApp(root)
    root.mainloop()