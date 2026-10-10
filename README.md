# gh600-study
GH-600 学習用のリポジトリです。

## 構成

- `app.py` : 学習用のサンプルコード（`add` 関数）。
- `test_app.py` : `app.py` に対する `unittest` ベースのテスト。
- `docs/task-plan.md` : 課題の進め方（目的・入力・変更対象・禁止事項・検証方法・完了条件）をまとめたタスク計画。
- `docs/answers/template.md` : 演習の回答記入用テンプレート（環境、タスクと受け入れ条件、変更内容、実行結果、コミットSHA、障害有無、自分の言葉での説明など）。

## 使い方

1. `docs/task-plan.md` に沿って対象の脆弱性修正などの課題に取り組む。
2. 作業結果を `docs/answers/template.md` のフォーマットに従って記録する。
3. `python -m unittest test_app.py` でテストを実行し、動作を検証する。
