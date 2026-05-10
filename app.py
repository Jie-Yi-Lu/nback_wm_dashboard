"""Week 11 Homework — N-back Working Memory Dashboard (STARTER).

Run locally:
    pip install -r requirements.txt
    streamlit run app.py

完成順序見 week-11-homework.md 的 Step-by-Step Checklist。
共 5 個 TODO 區塊（1～5），加上部署到 Streamlit Cloud。
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# -----------------------------------------------------------
# Page config — 第一個 streamlit 呼叫必須是這個
# -----------------------------------------------------------
st.set_page_config(
    page_title="N-back Working Memory Dashboard",
    layout="wide",
)

DATA_PATH = Path(__file__).parent / "data" / "nback_working_memory.csv"


# ===========================================================
# TODO 1 — 資料載入 + 錯誤處理  (10 pts)
# ===========================================================
# 提示：
#   1. 用 pd.read_csv(DATA_PATH) 載入資料
#   2. 若檔案不存在，用 st.error + st.stop 通知使用者
# -----------------------------------------------------------

# TODO 1.a: 用 st.error(...) 顯示「找不到資料檔」並 st.stop()
if not DATA_PATH.exists():
    st.error(f"找不到資料檔案：data/nback_working_memory.csv，請確認檔案路徑是否正確。")
    st.stop()

# TODO 1.b: 把下面這行改成 pd.read_csv(DATA_PATH)
df_all = pd.read_csv(DATA_PATH)


# ===========================================================
# Page header
# ===========================================================
st.title("🧠 N-back Working Memory Dashboard")
st.write(
    "Interactive visualization of a synthetic N-back working memory study "
    "(n=200, conditions: 1-back / 2-back / 3-back). 用左側 sidebar 篩選資料。"
)


# ===========================================================
# TODO 2 — Sidebar widgets  (15 pts)
# ===========================================================
# 在 with st.sidebar: 區塊內加入：
#   - age range slider          → age_min, age_max = st.slider(...)
#   - sex multiselect           → sex_choices = st.multiselect(...)
#   - condition selectbox 或 multiselect
# -----------------------------------------------------------
with st.sidebar:
    st.header("🔬 Filters")

    # TODO 2.a: age slider，min=18, max=75，預設 (18, 75)
    age_min, age_max = st.slider("Age", 18, 75, (18, 75))

    # TODO 2.b: sex multiselect，options=["F","M"]，預設兩者
    sex_choices = st.multiselect("Sex", options=["F", "M"], default=["F", "M"])

    # TODO 2.c: condition selectbox 或 multiselect
    selected_conds = st.multiselect("Condition", options=["1-back", "2-back", "3-back"], default=["1-back", "2-back", "3-back"])

    st.markdown("---")
    st.caption("HW Week 11 · NS5116 Spring 2026")


# Apply filters
mask = (
    df_all["age"].between(age_min, age_max)
    & df_all["sex"].isin(sex_choices)
    & df_all["condition"].isin(selected_conds)
)
df = df_all[mask].copy()


n_subj = df["participant_id"].nunique()

if df.empty:
    st.warning("沒有資料符合目前的篩選條件，請放寬篩選條件。")
    st.stop()
elif n_subj < 20:
    st.warning(f"⚠️ 篩選後僅 N={n_subj} 位受試者，請謹慎解讀資料結果。")
else:
    st.info(f"經篩選後，已載入 {n_subj} 位受試者資料。")

# ===========================================================
# TODO 3 — 三個 metric  (10 pts)
# ===========================================================
# 用 st.columns(3) 並排顯示：
#   1. 篩選後 row 數 (或 unique participant 數)
#   2. 平均 accuracy（小數兩位）
#   3. 平均 RT（整數 ms）
# -----------------------------------------------------------

# TODO 3.a: 用 st.columns(3) 拿到 c1, c2, c3
# TODO 3.b: c1.metric("Rows", ...) etc.

st.write("**TODO 3:** 在這裡加入 3 個 metric (st.columns(3) + 3 個 .metric)")
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Participants", df["participant_id"].nunique())

with c2:
    st.metric("Mean Accuracy", f"{df['accuracy'].mean():.2f}")

with c3:
    st.metric("Mean RT (ms)", f"{df['mean_rt_ms'].mean():.0f}")


st.markdown("---")


# ===========================================================
# TODO 4 — 一張 chart  (15 pts)
# ===========================================================
# 用 matplotlib 畫一張圖，例如：
#   - scatter: x=age, y=accuracy, color by condition
#   - 或 bar: group × condition 的平均 accuracy
# 記得：xlabel / ylabel / title / legend，最後 st.pyplot(fig)
# -----------------------------------------------------------

st.subheader("Performance by age and condition")

# TODO 4: 畫一張 matplotlib 圖
# 範例骨架：
#   fig, ax = plt.subplots(figsize=(8, 4.5))
#   for cond in selected_conds:
#       sub = df[df["condition"] == cond]
#       ax.scatter(sub["age"], sub["accuracy"], label=cond, alpha=0.6)
#   ax.set_xlabel("...")
#   ax.set_ylabel("...")
#   ax.legend()
#   st.pyplot(fig)

# st.info("TODO 4: 在這裡放你的 matplotlib chart")
fig, ax = plt.subplots(figsize=(8, 4.5))
for cond in selected_conds:
    sub = df[df["condition"] == cond]
    ax.scatter(sub["age"], sub["accuracy"], label=cond, alpha=0.6)
ax.set_xlabel("age")
ax.set_ylabel("Accuracy")
ax.set_title("N-back performance by age and condition")
ax.legend()
st.pyplot(fig)


# ===========================================================
# TODO 5 — Dataframe + download button  (10 pts)
# ===========================================================
# - st.dataframe(df) 顯示篩選後資料
# - st.download_button(...) 讓使用者下載 CSV
# -----------------------------------------------------------

st.subheader("Filtered data")
# TODO 5.a: st.dataframe(df, use_container_width=True)

# TODO 5.b: st.download_button(
#     label="⬇️ Download CSV",
#     data=df.to_csv(index=False).encode("utf-8"),
#     file_name="nback_filtered.csv",
#     mime="text/csv",
# )

# st.write("**TODO 5:** 在這裡放 st.dataframe + st.download_button")
st.dataframe(df, use_container_width=True)
st.download_button(
    label="⬇️ Download CSV",
    data=df.to_csv(index=False).encode("utf-8"),
    file_name="nback_filtered.csv",
    mime="text/csv",
)

# ===========================================================
# Optional bonuses — 如果有時間
# ===========================================================
# Bonus A: 在資料載入與篩選後加 st.success / .warning / .info
st.success(f"經篩選後，已載入 {n_subj} 位受試者資料。")    #  .warning / .info 等 code 請見 TODO 2

# Bonus B: 用 st.tabs([...]) 把 chart / dataframe 分頁
tab1, tab2, tab3 = st.tabs(["📊 Overview", "📈 By Condition", "🗃️ Raw Data"])

with tab1:
    # TODO 3 的三個 metric
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Participants", df["participant_id"].nunique())
    with col2:
        st.metric("Mean Accuracy", f"{df['accuracy'].mean():.2f}")
    with col3:
        st.metric("Mean RT (ms)", f"{df['mean_rt_ms'].mean():.0f}")

with tab2:
    # TODO 4 的 scatter plot
    st.subheader("Performance by age and condition")
    fig, ax = plt.subplots(figsize=(8, 4.5))
    for cond in selected_conds:
        sub = df[df["condition"] == cond]
        ax.scatter(sub["age"], sub["accuracy"], label=cond, alpha=0.6)
    ax.set_xlabel("Age")
    ax.set_ylabel("Accuracy")
    ax.set_title("N-back performance by age and condition")
    ax.legend()
    st.pyplot(fig)

with tab3:
    # TODO 5 的 dataframe + download
    st.subheader("Filtered data")
    st.dataframe(df, use_container_width=True)
    st.download_button(
        label="⬇️ Download CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="nback_filtered.csv",
        mime="text/csv",
        key="download_btn"
    )

# Bonus C: 在 README 寫一段 100 字 reflection
## 已寫於 README.md
