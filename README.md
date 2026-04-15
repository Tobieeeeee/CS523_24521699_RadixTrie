# Ứng Dụng Từ Điển Anh - Việt (Radix-Trie)

Đây là đồ án môn học xây dựng một ứng dụng từ điển tiếng Anh bằng Python, sử dụng cấu trúc dữ liệu **Radix-Trie** (Patricia Trie) làm chỉ mục để tối ưu hóa bộ nhớ và tốc độ tra cứu.

## Tính năng nổi bật

* **Tra cứu siêu tốc:** Tìm kiếm nghĩa của từ với độ phức tạp O(k) (trong đó k là độ dài của từ).
* **Tối ưu bộ nhớ (Nén nhánh):** Các chuỗi ký tự có chung tiền tố (common prefix) được gộp lại, các node không rẽ nhánh được nén thành một chuỗi duy nhất để tiết kiệm không gian lưu trữ so với Trie thông thường.
* **Tự động tối ưu cây (Merge):** Khi một mục từ bị xóa, hệ thống sẽ tự động dò tìm và gộp các node rẽ nhánh thừa lại với nhau để duy trì cấu trúc nén gọn gàng nhất.
* **Trực quan hóa dữ liệu (Live Visualization):** Tích hợp "bảng đen" theo dõi cấu trúc cây. Mỗi thao tác Thêm/Xóa từ đều sẽ lập tức vẽ lại sơ đồ Radix-Trie ra màn hình để minh họa sự thay đổi của dữ liệu theo thời gian thực.

## Cấu trúc dự án

```text
do_an_tu_dien/
│
├── data/
│   └── tu_vung.txt          # File cơ sở dữ liệu lưu trữ các mục từ và nghĩa
│
├── core/
│   ├── __init__.py          
│   └── radix_trie.py        # Chứa logic thuật toán cốt lõi (RadixNode, Thêm, Xóa, Tìm)
│
├── main.py                  # Kịch bản chạy ứng dụng trên giao diện Console (CLI)
├── app_gui.py               # Kịch bản chạy ứng dụng với giao diện đồ họa (Tkinter)
└── README.md                # Tài liệu giới thiệu dự án
```

## Cài đặt và Sử dụng

### 1. Yêu cầu hệ thống
* Trình thông dịch: **Python 3.x**
* Không yêu cầu cài đặt thêm bất kỳ thư viện bên ngoài (third-party) nào. Ứng dụng sử dụng hoàn toàn thư viện chuẩn của Python (`tkinter`, `os`).

### 2. Cách chạy ứng dụng

Mở Terminal / Command Prompt, di chuyển đến thư mục chứa dự án và chọn 1 trong 2 chế độ chạy:

**Cách 1: Chạy với giao diện đồ họa (Khuyên dùng)**
Giao diện cửa sổ trực quan, có popup nhập liệu và bảng đen mô phỏng cây.
```bash
python app_gui.py
```

**Cách 2: Chạy với giao diện dòng lệnh (Console)**
Giao diện text-based truyền thống.
```bash
python main.py
```

## ⚙️ Các thao tác hỗ trợ
1. **Tìm kiếm mục từ:** Trả về nghĩa tiếng Việt của từ khóa tiếng Anh nếu tồn tại.
2. **Thêm mục từ:** Chèn một từ mới. Thuật toán sẽ tự động tách node (split) nếu phát hiện tiền tố chung với các từ đã có.
3. **Xóa mục từ:** Gỡ bỏ từ khỏi hệ thống. Thực hiện gộp nhánh (merge) nếu cấu trúc cây tạo ra các node đơn không cần thiết sau khi xóa.

Nguyễn Văn Quốc Thịnh - 24521699
