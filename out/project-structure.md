# プロジェクト構成

## ディレクトリ構造

```
mdmerge/
├── README.md                   # プロジェクトのメイン説明ファイル
├── __init__.py                # モジュール初期化ファイル
├── cli/                       # CLI関連モジュール（今後実装予定）
│   └── __init__.py
├── config/                    # 設定ファイル関連（今後実装予定）
│   └── config.yml
├── const/                     # 定数定義モジュール
│   ├── __init__.py
│   └── emoji.py              # 絵文字定数リスト
├── docs/                      # ドキュメント
│   └── project-structure.md  # このファイル
├── scripts/                   # メインスクリプト
│   ├── __init__.py
│   └── main.py               # メインロジック
└── tests/                     # テストファイル
    ├── __init__.py
    ├── emoji_mock.py          # テスト用モックデータ
    └── test_add_space_to_emoji.py  # 絵文字スペース追加機能のテスト
```

## ファイル詳細

### ルートディレクトリ
- `README.md`: プロジェクトの概要と使用方法
- `__init__.py`: Pythonモジュール初期化ファイル

### `cli/` - CLIインターフェース（今後実装予定）
- `__init__.py`: CLIモジュール初期化ファイル
- **実装予定**: コマンドライン引数の処理、ユーザーインターフェース

### `config/` - 設定管理（今後実装予定）
- `config.yml`: アプリケーション設定ファイル（YAML形式）
- **実装予定**: 設定の読み込み、バリデーション機能

### `const/` - 定数定義
- `__init__.py`: 定数モジュール初期化ファイル
- `emoji.py`: 絵文字定数リスト
  - `EMOJI_LIST`: 利用可能な絵文字のリスト定義

### `docs/` - ドキュメント
- `project-structure.md`: このファイル（プロジェクト構成説明）

### `scripts/` - メインスクリプト
- `__init__.py`: スクリプトモジュール初期化ファイル
- `main.py`: メインアプリケーションロジック
  - `run()`: メイン実行関数（Click CLIコマンド）
  - `dir_search()`: ディレクトリ検索機能
  - `make_display_text()`: ディレクトリ名表示変換機能
  - `add_space_to_emoji()`: 絵文字スペース追加機能

### `tests/` - テストファイル
- `__init__.py`: テストモジュール初期化ファイル
- `emoji_mock.py`: テスト用モックデータ
- `test_add_space_to_emoji.py`: 絵文字スペース追加機能のテスト
  - `sample_dirnames()`: テスト用サンプルデータ
  - `test_add_space_to_emoji()`: 絵文字スペース追加のテスト関数

## 参考情報

- Obsidianディレクトリ: `C:\Users\ns69a\Documents\Obsidians\tech`
