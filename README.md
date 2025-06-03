# 📝 MemoMemo

Gitを学習している最中なので、Git学習前に作ったメモアプリをGitでちゃんと見せられる形に整えてみました。
AIさんと一緒に開発しました。マジで大変だった…

AIを活用したメモ管理アプリケーション。メモの作成、管理、検索を簡単に行えます。

## ✨ 主な機能

- メモの作成と管理
- AIによる自動タグ生成
- タグによるメモの分類と検索（実装予定）
- 直感的なユーザーインターフェース
- データの永続化

## 🚀 セットアップ

### 必要条件

- Python 3.8以上
- pip（Pythonパッケージマネージャー）

### インストール

1. リポジトリのクローン
```bash
git clone https://github.com/An-Ste/MemoMemo.git
cd MemoMemo
```

2. 必要なパッケージのインストール
```bash
pip install -r requirements.txt
```

3. 環境変数の設定
プロジェクトのルートディレクトリに`.env`ファイルを作成し、以下の内容を設定：

今回利用した Groqモデル：gemma2-9b-it

後は…
API_KEY, API_URL

### 起動方法

1. FastAPIサーバーの起動
```bash
uvicorn App.api.fast_api:app --reload
```

2. Streamlitアプリの起動（別のターミナルで）
```bash
streamlit run App/app.py
```

## 💻 使用方法

1. **メモの作成**
   - タイトルと内容を入力
   - AIが自動的にタグを生成
   - 「メモを保存」ボタンで保存

2. **メモの管理**
   - メモ一覧で全てのメモを確認
   - メモの削除が可能
   - タグによる検索（なぜか出来なくなったので今後追加）

3. **タグの管理**
   - タグの作成と削除
   - タグによるメモの分類

## 🛠️ 技術スタック

- **フロントエンド**: Streamlit
- **バックエンド**: FastAPI
- **データベース**: SQLite
- **AI**: Groq API
- **その他**: Python, Pydantic

## 📁 プロジェクト構造

```
MemoMemo/
├── App/
│   ├── api/
│   │   ├── fast_api.py
│   │   └── groq_res.py
│   ├── data/
│   │   ├── memo_class.py
│   │   └── tag_list.py
│   ├── utils/
│   │   └── load_env.py
│   └── app.py
├── .env
├── .gitignore
└── README.md
```


## 👥 作者

あなたの名前 - [@An-Ste](https://github.com/An-Ste)





