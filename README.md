# AI_report
# Structure
```bash
├── .gitignore
├── README.md
├── backup.py                           # Minimax + Alpha-Beta Pruning bot (dự phòng/so sánh)
├── lib-bot.py                          # Bot Connect4 dùng thư viện PySpiel của DeepMind với MCTS
├── requirements.txt                    # Thư viện cần thiết cho toàn bộ dự án
└── Connect4-MCTS/                      # Thư mục chính chứa code MCTS thuần và ứng dụng server
    ├── pycache/
    ├── README.md
    ├── app.py                          # Triển khai bot trên server
    ├── connect4.py                     # Logic game Connect4: bảng, trạng thái, kiểm tra hợp lệ
    ├── mcts.py                         # Thuật toán Monte Carlo Tree Search thuần
    ├── requirements.txt                # Thư viện cần thiết cho phần MCTS nội bộ
    ├── run.py                          # Chạy thử bot local, debug chiến thuật
    ├── run_ver2.py                     # Phiên bản chạy thử khác
```

## Mô tả chi tiết

### lib-bot.py
- Triển khai bot Connect4 sử dụng thư viện [PySpiel](https://github.com/deepmind/open_spiel) của DeepMind.
- Sử dụng thuật toán MCTS có sẵn trong PySpiel để chọn nước đi tối ưu.

### backup.py
- Triển khai thuật toán Minimax kết hợp Alpha-Beta Pruning để cải thiện hiệu suất tìm kiếm.
- Có thể dùng làm giải pháp dự phòng hoặc để so sánh với MCTS.

### Connect4-MCTS/mcts.py
- Cài đặt thuật toán Monte Carlo Tree Search thuần không phụ thuộc thư viện ngoài.
- Bao gồm đầy đủ 4 bước: selection, expansion, simulation, backpropagation.

### Connect4-MCTS/connect4.py
- Xử lý logic game Connect4:
  - Khởi tạo bảng game.
  - Kiểm tra trạng thái thắng/thua/hòa.
  - Kiểm tra tính hợp lệ của nước đi.

### Connect4-MCTS/run.py & run_ver2.py
- Chạy thử bot local.
- Hỗ trợ debug, thử nghiệm và tinh chỉnh chiến thuật.

### Connect4-MCTS/app.py
- Triển khai bot trên server.
- Nhận trạng thái game từ server, xử lý và trả về nước đi tốt nhất dựa trên MCTS.

---

# Implementation

## Setup
```bash
pip install -r requirements.txt
```

## Local test
```bash
cd Connect4-MCTS
python run.py
# hoặc
python run_ver2.py
```

## Deploy server
```bash
cd Connect4-MCTS
python app.py
```

## Backup and library bot
```bash
python lib-bot.py
# hoặc
python backup.py
```


