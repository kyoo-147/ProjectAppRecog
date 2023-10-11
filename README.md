# Hệ thống giao diện nhận diện tích hợp lấy dữ liệu, train, nhận diện trên một giao diện
----Phát Triển: Bùi Minh Cường - NaVin Tech-----

- Hệ thống hoạt động dựa trên nguyên tắc giao diện minh họa cho một ứng dụng
có thể lấy dữ liệu data của người dùng, đào tạo mô hình, và nhận diện được 
cá nhân đó, độ chính xác giao động từ 75% - 92%. Hoạt động dựa trên mô hình 
OpenVINO được phát triển bởi Intel. Hệ thống cho thấy tiềm năng có thể liên 
và chạy được trên các thiết bị máy tính nhúng Jetson Nano, Raspberry,...
- Chương trình đã được đưa vào thực nghiệm và đã hoạt động thành công.
- Model xử dụng 3 mô hình để xây dựng một quy trình có thể phát hiện khuôn 
mặt trên video, các điểm đặc biệt(landmarks) và nhận dạng người bằng cơ sở 
dữ liệu khuôn mặt được cung cấp

+ các mô hình được sử dụng: 
* `face-detection-retail-0004` và `face-detection-adas-0001`, dùng để phát 
hiện khuôn mặt và dự đoán các bounding boxes
* `landmarks-regression-retail-0009`, dự đoán các điểm chính trên khuôn mặt
* `face-reidentification-retail-0095`, `Sphereface`, `facenet-20180408-102900` hoặc `face-recognition-resnet100-arcface-onnx` để nhận dạng cá nhân

## How it works
## Cách chương trình hoạt động

- Ứng dụng được gọi từ dòng lệnh. Nó đọc đầu vào được chỉ định
luồng video theo từng khung hình, có thể là thiết bị máy ảnh hoặc tệp video,
và thực hiện phân tích độc lập từng khung hình. Để đưa ra dự đoán
ứng dụng triển khai 3 mô hình trên các thiết bị được chỉ định bằng OpenVINO
thư viện và chạy chúng theo cách không đồng bộ. Một khung đầu vào được xử lý bởi
mô hình phát hiện khuôn mặt để dự đoán các hộp giới hạn khuôn mặt. Sau đó, đối mặt với các điểm chính
được dự đoán bởi mô hình tương ứng. Bước cuối cùng trong xử lý khung
được thực hiện bởi mô hình nhận dạng khuôn mặt, sử dụng các điểm chính được tìm thấy
để căn chỉnh các khuôn mặt và bộ sưu tập khuôn mặt để khớp với các khuôn mặt được tìm thấy trên video
khung với những cái trong bộ sưu tập. Sau đó, kết quả xử lý được
được trực quan hóa và hiển thị trên màn hình hoặc được ghi vào tệp đầu ra.


## Những chuẩn bị cho việc chạy chương trình

- Các mô hình đã được tải sẵn về trong chương trình, bạn có thể tìm thấy các phiên bản của chúng tại
thư mục intel/ hoặc public/
- hoặc có thể dùng lệnh sau để cài đặt các mô hình cho chương trinh:

  cài đặt mô hình:

```sh
omz_downloader --list models.lst
```

  chuyển đổi mô hình:

```sh
omz_converter --list models.lst
```

### Mô hình được hỗ trợ

* face-detection-adas-0001
* face-detection-retail-0004
* face-recognition-resnet100-arcface-onnx
* face-reidentification-retail-0095
* facenet-20180408-102900
* landmarks-regression-retail-0009
* Sphereface

### Cách để chạy chương trình

---- các bước tiền xử lí đã được tôi seup đầy đủ và hoàn tất

---- đầu tiên, hãy đảm bảo rằng bạn đã cài đặt tất cả các thư viện cần thiết
để bắt đầu chạy chương trình:
          \\ pip install -r requirements.txt \\
---- và hãy đảm bảo rằng phiên bản python của bạn là thích hợp để cài đặt các thư 
viện, \\ đề xuất của tôi là bạn hãy sử dụng phiên bản python 3.8.3 để giẩm thiểu 
xung đột giữa các phiên bản \\

---- cuối cùng bạn chỉ cần tìm đến tệp có tên \\ train.exe \\ để chạy chương trình
---- tuy nhiên tài nguyên git là có hạn, nên tôi buộc phải xóa tệp tin exe
---- bạn có thể chạy chương trình bằng cách sử dụng file train.py

    + ( hãy đảm bảo rằng bạn đã kích hoạt âm thanh để có trải nghiệm tốt nhất)
    + đầu tiên hãy nhâp id của bạn với số thứ tụ
    + tiếp đến là tên của bạn, lưu ý phải là một kí tự không dấu và không khoảng cách
    + sau khi đã xong bạn hãy click vào nút lấy dữ liệu, chương trình sẽ hướng dẫn bạn
    + tiếp đến hãy click vào bút Huấn Luyện Mô Hình để chương trinh xử lí
    + sau cùng, khi tất cả mọi thứ đã hoàn thành bạn hãy click vào nút Nhận Diện
    + chương trình sẽ hoạt động

## Các đối số bạn có thể thay đổi 

Chạy ứng dụng có hoặc không có tùy chọn `-h`
mọi đối số đều mang lại thông báo sau:

```
cách sử dụng: face_recognition_demo.py [-h] -i INPUT [--loop] [-o OUTPUT] [-limit OUTPUT_LIMIT] [--output_resolution OUTPUT_RESOLUTION] [--no_show] [--crop_size CROP_SIZE CROP_SIZE] [--match_algo { HUNGARIAN,MIN_DIST}] [-u UTILIZATION_MONITORS]
                                 [-fg FG] [--run_detector] [--allow_grow] -m_fd M_FD -m_lm M_LM -m_reid M_REID [--fd_input_size FD_INPUT_SIZE FD_INPUT_SIZE] [-d_fd {CPU,GPU,HETERO}] [-d_lm {CPU,GPU, HETERO}] [-d_reid {CPU,GPU,HETERO}] [-v]
                                 [-t_fd [0..1]] [-t_id [0..1]] [-exp_r_fd SỐ]

đối số tùy chọn:
   -h, --help hiển thị thông báo trợ giúp này và thoát

Tổng quan:
   -i ĐẦU VÀO, --input ĐẦU VÀO
                         Yêu cầu. Một đầu vào để xử lý. Đầu vào phải là một hình ảnh, một thư mục hình ảnh, tệp video hoặc id máy ảnh.
   --loop Tùy chọn. Cho phép đọc đầu vào trong một vòng lặp.
   -o ĐẦU RA, --đầu ra ĐẦU RA
                         Không bắt buộc. Tên của (các) tệp đầu ra để lưu.
   -giới hạn OUTPUT_LIMIT, --output_limit OUTPUT_LIMIT
                         Không bắt buộc. Số lượng khung để lưu trữ trong đầu ra. Nếu 0 được đặt, tất cả các khung được lưu trữ.
   --output_resolution OUTPUT_RESOLUTION
                         Không bắt buộc. Chỉ định độ phân giải cửa sổ đầu ra tối đa ở định dạng (chiều rộng x chiều cao). Ví dụ: 1280x720. Kích thước khung đầu vào được sử dụng theo mặc định.
   --no_show Tùy chọn. Không hiển thị đầu ra.
   --crop_size CROP_SIZE CROP_SIZE
                         Không bắt buộc. Cắt luồng đầu vào thành độ phân giải này.
   --match_algo {HUNGARIAN,MIN_DIST}
                         Không bắt buộc. Thuật toán so khớp khuôn mặt. Mặc định: HUNGARIAN.
   -u UTILIZATION_MONITORS, --utilization_monitor UTILIZATION_MONITORS
                         Không bắt buộc. Danh sách các màn hình để hiển thị ban đầu.

Cơ sở dữ liệu khuôn mặt:
   -fg FG Tùy chọn. Đường dẫn đến thư mục hình ảnh khuôn mặt.
   --run_detector Tùy chọn. Sử dụng mô hình Nhận diện khuôn mặt để tìm khuôn mặt trên hình ảnh khuôn mặt, nếu không thì sử dụng hình ảnh đầy đủ.
   --allow_grow Tùy chọn. Cho phép phát triển bộ sưu tập khuôn mặt và đổ vào đĩa. Chỉ khả dụng nếu tùy chọn --no_show bị tắt.

Mô hình:
   -m_fd M_FD Bắt buộc. Đường dẫn đến tệp .xml có mô hình Nhận diện khuôn mặt.
   -m_lm M_LM Bắt buộc. Đường dẫn đến tệp .xml với mô hình Phát hiện dấu mốc trên khuôn mặt.
   -m_reid M_REID Bắt buộc. Đường dẫn đến tệp .xml có mô hình Nhận dạng lại khuôn mặt.
   --fd_input_size FD_INPUT_SIZE FD_INPUT_SIZE
                         Không bắt buộc. Chỉ định kích thước đầu vào của mô hình phát hiện để định hình lại. Ví dụ: 500 700.

Tùy chọn suy luận:
   -d_fd {CPU,GPU,HETERO}
                         Không bắt buộc. Thiết bị đích cho mô hình Nhận diện khuôn mặt. Giá trị mặc định là CPU.
   -d_lm {CPU,GPU,HETERO}
                         Không bắt buộc. Thiết bị mục tiêu cho mô hình Phát hiện dấu mốc trên khuôn mặt. Giá trị mặc định là CPU.
   -d_reid {CPU,GPU,HETERO}
                         Không bắt buộc. Thiết bị mục tiêu cho mô hình Nhận dạng lại khuôn mặt. Giá trị mặc định là CPU.
   -v, --verbose Tùy chọn. Hãy dài dòng hơn.
   -t_fd [0..1] Tùy chọn. Ngưỡng xác suất để phát hiện khuôn mặt.
   -t_id [0..1] Tùy chọn. Ngưỡng khoảng cách cosine giữa hai vectơ để nhận dạng khuôn mặt.
   -exp_r_fd SỐ Tùy chọn. Tỷ lệ chia tỷ lệ cho các hộp được chuyển sang nhận dạng khuôn mặt.
```

--- lưu ý rằng các đối số đã được cài đặt sẵn trong file \\ face_recognition_demo.py \\
      hãy chỉnh sử tại file đó.



>**LƯU Ý**: Nếu bạn cung cấp một hình ảnh duy nhất làm đầu vào, bản trình diễn sẽ xử lý và hiển thị hình ảnh đó một cách nhanh chóng, sau đó thoát ra. Để liên tục trực quan hóa các kết quả suy luận trên màn hình, hãy áp dụng tùy chọn `loop`, cho phép xử lý một hình ảnh duy nhất trong một vòng lặp.

* **FPS**: tốc độ xử lý khung hình video trung bình (khung hình trên giây).
* **Độ trễ**: thời gian trung bình cần thiết để xử lý một khung hình (từ khi đọc khung hình đến hiển thị kết quả).
Bạn có thể sử dụng cả hai chỉ số này để đo lường hiệu suất cấp ứng dụng.

##  Liên hệ với tôi:
upwork: ``` https://www.upwork.com/freelancers/~011ca77d21dc10889d  ```

facebook: ``` https://www.facebook.com/mcng.2806/ ```

fiver: ``` https://www.fiverr.com/macdaiqua147?up_rollout=true ```

github: ``` https://github.com/kyoo-147 ```

twitter: ``` https://twitter.com/mih_cuog ```

gmail: ``` ngoctuanvinh1332@gmail.com ```

gmail: ``` baemyungkang2806@gmail.com ```

youtube: ``` https://www.youtube.com/@kyoodavision1332 ```

linkedin: ``` https://www.linkedin.com/in/minh-cuong-bui/ ```

dribble: ``` https://dribbble.com/macdaiqua147 ```

instagram: ``` https://www.instagram.com/1332_kyojunehieight/ ```

zalo: ``` https://zalo.me/0365646109 ```# ProjectAppRecognition
