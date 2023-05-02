import matplotlib.pyplot as plt
import pandas as pd
import webbrowser
df = pd.read_csv('data_coordinate\\sample_coordinate.csv', header=None)  # 1行目をヘッダーとして読み込まない
for i in range(1, 4, 1):
    s = df[df.columns[i]]
    Title=s[0]
    df1=pd.DataFrame(s).drop(0)
    # # 座標データを取得
    x = df1.iloc[::2, 0]  # 偶数行のデータをx座標として取得
    y = df1.iloc[1::2, 0]  # 奇数行のデータをy座標として取得
    x=x.astype(float)
    y=y.astype(float)
    fig_1, ax=plt.subplots(figsize=(6, 6))
    ax.plot(x, y, color="blue", lw=0, ls='-', marker='o', markersize=6.5)
    ax.set_xlim([-35, 35])
    ax.set_ylim([-120, 0])
    ax.set_xlabel('x coordinate [mm]', fontsize=11)  # X軸のラベルを設定
    ax.set_ylabel('y coordinate [mm]', fontsize=11)  # Y軸のラベルを設定
    plt.title(Title, fontsize=12)  # グラフのタイトルを設定
    ax.grid(ls=':')  # グリッドを表示
    PngFile='data_coordinate\\'+Title+'.png'
    PdfFile='data_coordinate\\'+Title+'.pdf'
    fig_1.subplots_adjust(left=0.12, right=0.97, bottom=0.08, top=0.92)
    fig_1.savefig(PngFile, facecolor='white')
    fig_1.savefig(PdfFile, facecolor='white')
    webbrowser.open_new(PngFile)
    webbrowser.open_new(PdfFile)