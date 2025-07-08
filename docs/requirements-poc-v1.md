## mdmerge - PoC要件定義書（個人用簡易版）

### 1. 目的

Markdown管理ツール `mdmerge` の**最小機能の動作検証**（PoC）を行う。主に以下を対象とする：

* Obsidian内のTechディレクトリ配下の**サブディレクトリ一覧表示**

---

### 2. 前提

* 対象環境：Windows + Python 3.12
* ObsidianのTechディレクトリは `C:\Users\ns69a\Documents\Obsidians\tech`
* ClickによるCLI起動
* `emoji.py` に定義された絵文字リスト `EMOJI_LIST` を使用可能

---

### 3. 要件（PoC）

* [x] `scripts/main.py` で `run()` 実行時に対象ディレクトリ一覧を表示
* [x] `.trash`, `.obsidian` は除外

---

### 4. 非要件（PoC時点では無視）

* ❌ `add_space_to_emoji()` の適用（絵文字の見づらさ対策）
* ❌ CLIオプションの対応（引数なしでOK）
* ❌ Markdown統合処理
* ❌ 設定ファイル（`config.yml`）の読み込み
* ❌ テストの整備・CI/CD導入
* ❌ 各ディレクトリ名のリストを加工するための関数 `make_display_text()` を実装
* ❌ （※PoCでは）絵文字のスペース処理 `add_space_to_emoji()` は使わない

---

### 5. 制約・その他

* `make_display_text()` は PoC では単純に `Path.name` を返す処理でよい
* 失敗時に例外を握りつぶさずに出力（Click標準出力に任せる）
* テキスト整形や整列はPoCでは優先しない

---

このように要件を**明示的に「やる／やらない」で区分**すると、PoCの完了ラインがブレず、進行管理がしやすくなります。

必要であれば、このテンプレートを `docs/requirements-poc.md` に保存してGit管理下に置くと良いでしょう。要件の進化に応じてバージョン管理できます。
