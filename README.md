# Week 11 Homework — N-back Dashboard (Starter)

> 把這份資料夾複製到自己的 GitHub repo，把 `TODO` 區塊填完整即可。

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

App 開在 <http://localhost:8501>。

## Files

```
.
├── app.py                          ← 你要改的檔案（含 5 個 TODO）
├── data/
│   └── nback_working_memory.csv    ← 不要改動
├── requirements.txt
└── README.md                        ← 改成你自己的 README
```

## What to do

完整作業說明見 `week-11-homework.md`（在 homeworks/week11 根目錄）。
最低要求：完成 TODO 1–5 + 部署到 Streamlit Cloud。

## Submission

繳交：

1. GitHub repo URL（public）
2. Streamlit Cloud URL
3. 一張 dashboard 截圖

## Reflection
本資料集儀表為使用 n-back 作業測量在不同情境下的準確率作為工作記憶操作能力表現之結果，可以「Age」、「Sex」、「Condition」等條件進行資料篩選，適合好奇在年齡或性別變項下之工作記憶操作能力之觀眾。惟注意本資料結果僅供參考，無法普遍推論至一般大眾。