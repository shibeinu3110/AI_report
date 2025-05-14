# AI_report
# Structure
```bash
├── .gitignore
├── README.md
├── backup.py
├── lib-bot.py
├── requirements.txt
└── Connect4-MCTS/
    ├── __pycache__/
    ├── README.md
    ├── app.py
    ├── connect4.py
    ├── mcts.py
    ├── requirements.txt
    ├── run.py
    ├── run_ver2.py
```
#
🔹 lib-bot.py
Chứa code của bot Connect4 sử dụng thư viện PySpiel của DeepMind.

Áp dụng thuật toán MCTS được hỗ trợ bởi PySpiel để đưa ra nước đi tối ưu.

🔹 backup.py
Triển khai thuật toán Minimax kết hợp với Alpha-Beta Pruning để tăng hiệu suất.

Có thể dùng như phương án dự phòng hoặc để so sánh hiệu suất với MCTS.

## Connect4-MCTS/
🔸 mcts.py
Chứa logic triển khai thuật toán Monte Carlo Tree Search thuần (không dùng thư viện ngoài).

Bao gồm các bước: selection, expansion, simulation và backpropagation.

🔸 connect4.py
Quản lý logic game Connect4: khởi tạo bảng, kiểm tra trạng thái thắng/thua/hòa, và hợp lệ của nước đi.

🔸 run.py & run_ver2.py
Dùng để chơi thử local và test bot.

Hữu ích để debug và điều chỉnh chiến thuật trước khi đưa lên server.

🔸 app.py
Dùng để triển khai bot trên server.

Nhận input từ server (thông tin trạng thái game), xử lý đầu vào, và đưa ra nước đi tối ưu dựa trên thuật toán MCTS.

🔸 requirements.txt
Danh sách các thư viện cần thiết cho phần MCTS nội bộ.

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


