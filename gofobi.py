import streamlit as st

st.title("週間ごほうびアプリ")

# サイドバーで家族メンバーを選択
kazoku = st.sidebar.selectbox("家族を選択", ["父", "母", "長男", "次男"])

# チェックボックスの表示とポイントの設定
tasks = {
    "父": [
        ("休日子どもと野球する", 2),
        ("洗車する", 2),
        ("平日のコンビニスイーツを我慢する", 2),
        ("資格の勉強をする", 2),
        ("駅まで歩く", 2)
    ],
    "母": [
        ("庭の草引きをする", 2),
        ("水回りの掃除をする", 2),
        ("玄関の掃除をする", 2),
        ("靴を洗う", 2),
        ("本を１冊以上読む", 2)
    ],
    "長男": [
        ("算盤教室に週４回行く", 2),
        ("スイミングに行く", 2),
        ("ゲームの時間を守る", 2),
        ("週末はこどもチャレンジをする", 2),
        ("弟を叩かない", 2)
    ],
    "次男": [
        ("スイミングに行く", 2),
        ("ゲームの時間を守る", 2),
        ("週末はこどもチャレンジをする", 2),
        ("おもちゃを片付ける", 2),
        ("学校の用意を一人でする", 2)
    ]
}

# 選択された家族メンバーのチェックボックスを表示
selected_tasks = tasks[kazoku]
total_checked = 0

for task, points in selected_tasks:
    if st.checkbox(task):
        total_checked += points

st.write("<各2点>")

#合計を表示する
st.write(f"合計点: {total_checked}")

#満点ならごほうび画像を表示する
images = {
  "父": "massage.png",
  "母": "cake.png",
  "長男": "game.png",
  "次男": "gatyapon.png"
}

if total_checked==10:
  st.markdown("## 満点！！ごほうびゲット！！")
  image = images[kazoku]
  st.image(image)