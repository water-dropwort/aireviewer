# 概要
生成AIを使ってGitリポジトリの差分をレビューするCLIツール。
最新のコミットとステージされた変更の差分をレビューする。
生成AIはGemini 2.5 Flash-Liteを使用している。

# インストール
## 前提
- pipxがインストールされている。
## インストール手順
1. リポジトリをクローンする。
2. プロジェクトルートに入り、`pipx install .`を実行する。
3. 環境変数に`GEMINI_API_KEY`を設定する。

# 使い方
`review /path/to/git-repository`で実行する。

# 開発
## 開発環境構築手順
1. リポジトリをクローンする。
2. 仮想環境を作成する。`python -m venv .venv`
3. 仮想環境をアクティブにする。`. .venv/bin/activate.fish`
   [NOTE]アクティベートするスクリプトは使用しているシェル環境に合ったものを実行する。
4. 依存パッケージをインストールする。`pip install -r requiremtns.txt`

## 開発中の実行
`python src/aireviewer`で実行する。

