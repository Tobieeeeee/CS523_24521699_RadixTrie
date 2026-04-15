import os
from main.radix_trie import TuDien 

def doc_du_lieu_tu_file(filepath, tu_dien):
    if not os.path.exists(filepath):
        print(f"[*] Không tìm thấy file {filepath}. Bắt đầu với từ điển trống.")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('|')
            if len(parts) == 2:
                word, meaning = parts[0].strip(), parts[1].strip()
                tu_dien.them_tu(word, meaning)
    print("[*] Đã tải dữ liệu từ điển thành công!")

def hien_thi_menu():
    print("\n" + "="*30)
    print("   TỪ ĐIỂN ANH - VIỆT (RADIX-TRIE)   ")
    print("="*30)
    print("1. Tìm nghĩa của từ")
    print("2. Thêm một mục từ mới")
    print("3. Xóa một mục từ")
    print("4. Thoát ứng dụng")
    print("="*30)

def chay_ung_dung():
    tu_dien = TuDien()
    filepath = os.path.join('data', 'tu_vung.txt')
    
    doc_du_lieu_tu_file(filepath, tu_dien)
    
    while True:
        hien_thi_menu()
        lua_chon = input("Nhập lựa chọn của bạn (1-4): ")
        
        if lua_chon == '1':
            word = input("Nhập từ cần tìm: ").lower()
            ket_qua = tu_dien.tim_nghia(word)
            if ket_qua:
                print(f"-> Nghĩa của từ '{word}': {ket_qua}")
            else:
                print(f"-> Không tìm thấy từ '{word}' trong từ điển.")
                
        elif lua_chon == '2':
            word = input("Nhập từ tiếng Anh: ").lower()
            meaning = input("Nhập nghĩa tiếng Việt: ")
            tu_dien.them_tu(word, meaning)
            print(f"-> Đã thêm thành công '{word}': {meaning}")
            
            # TỰ ĐỘNG IN CÂY SAU KHI THÊM
            print("\n[+] CẤU TRÚC CÂY SAU KHI THÊM:")
            tu_dien.in_cay()
            
        elif lua_chon == '3':
            word = input("Nhập từ cần xóa: ").lower()
            if tu_dien.tim_nghia(word):
                tu_dien.xoa_tu(word)
                print(f"-> Đã xóa thành công mục từ '{word}'.")
                
                # TỰ ĐỘNG IN CÂY SAU KHI XÓA
                print("\n[-] CẤU TRÚC CÂY SAU KHI XÓA:")
                tu_dien.in_cay()
            else:
                print(f"-> Từ '{word}' không tồn tại để xóa.")
                
        elif lua_chon == '4':
            print("Đã thoát ứng dụng. Tạm biệt!")
            break
            
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại!")

if __name__ == "__main__":
    chay_ung_dung()