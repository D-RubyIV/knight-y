# Dự Án Knight-Y

## Tổng Quan
Knight-Y là một ứng dụng desktop được xây dựng bằng PySide6 (Qt) cung cấp khả năng tương tác tự động với YouTube. Ứng dụng có giao diện người dùng hiện đại không viền với các phiên bản trình duyệt Chrome được nhúng để thực hiện nhiều thao tác cùng lúc.

## Tính Năng
- Thiết kế cửa sổ không viền với các điều khiển tùy chỉnh
- Nhiều phiên bản trình duyệt Chrome được nhúng
- Khả năng tương tác tự động với YouTube
- Hồ sơ người dùng riêng cho mỗi phiên bản trình duyệt
- Chức năng kéo thả và thay đổi kích thước cửa sổ
- Duy trì phiên làm việc của trình duyệt

## Cấu Trúc Dự Án
```
knight-y/
├── automation/     # Các module tự động hóa
├── common/         # Tiện ích và mã nguồn dùng chung
├── config/         # Các file cấu hình
├── data/          # Dữ liệu và hồ sơ người dùng
├── embed/         # Tiện ích nhúng trình duyệt
├── equipment/     # Thiết bị và mô hình cốt lõi
├── logger/        # Chức năng ghi log
├── puzzle/        # Module giải quyết puzzle YouTube
├── repository/    # Lớp lưu trữ dữ liệu
├── resources/     # Tài nguyên và tài sản giao diện
├── runnable/      # Các script thực thi
├── service/       # Các thành phần lớp dịch vụ
├── utils/         # Các hàm tiện ích
├── main.py        # Điểm khởi đầu ứng dụng
└── run.bat        # File batch Windows để chạy ứng dụng
```

## Yêu Cầu Hệ Thống
- Python 3.x
- PySide6
- Trình duyệt Chrome
- ChromeDriver
- Hệ điều hành Windows (do phụ thuộc vào win32gui)

## Cài Đặt
1. Clone repository
2. Cài đặt các gói Python cần thiết:
   ```bash
   pip install PySide6 pywin32
   ```
3. Đảm bảo đã cài đặt trình duyệt Chrome
4. Đặt file chromedriver.exe vào thư mục gốc của dự án

## Cấu Hình
Ứng dụng sử dụng các file cấu hình nằm trong thư mục `config/`. Các cài đặt chính bao gồm:
- Số lượng worker
- Đường dẫn trình duyệt Chrome
- Thư mục dữ liệu người dùng
- Cấu hình cổng

## Cách Sử Dụng
1. Chạy ứng dụng bằng `run.bat` hoặc trực tiếp qua Python:
   ```bash
   python main.py
   ```
2. Ứng dụng sẽ khởi động với nhiều phiên bản Chrome được nhúng
3. Sử dụng các điều khiển giao diện để tương tác với các trình duyệt được nhúng
4. Mỗi phiên bản trình duyệt duy trì hồ sơ và phiên làm việc riêng

## Tích Hợp Trình Duyệt
- Ứng dụng nhúng các phiên bản trình duyệt Chrome vào các khung Qt
- Mỗi phiên bản chạy trên một cổng debug riêng biệt
- Cửa sổ trình duyệt tự động thay đổi kích thước để vừa với khung chứa
- Duy trì hồ sơ người dùng tùy chỉnh cho mỗi phiên bản

## Phát Triển
### Các Thành Phần Chính
- Lớp `Application`: Quản lý cửa sổ chính và giao diện người dùng
- `YoutubePuzzle`: Tự động hóa tương tác với YouTube
- `PortFinder`: Quản lý cổng cho các phiên bản trình duyệt
- `BaseModel`: Định nghĩa mô hình cơ sở dữ liệu

### Thêm Tính Năng Mới
1. Tạo module mới trong thư mục phù hợp
2. Cập nhật cấu hình nếu cần
3. Tích hợp với ứng dụng chính thông qua giao diện

## Ghi Log
- Log ứng dụng được lưu trong `app.log`
- Cấu hình ghi log có thể tìm thấy trong thư mục `logger/`

## Cơ Sở Dữ Liệu
- Sử dụng cơ sở dữ liệu SQLite (`database.db`) để lưu trữ dữ liệu
- Các mô hình được định nghĩa trong thư mục `equipment/`

## Đóng Góp
1. Fork repository
2. Tạo nhánh tính năng
3. Commit các thay đổi
4. Push lên nhánh
5. Tạo Pull Request

