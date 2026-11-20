# 研究作業指示 — 次数1・2の非可換del Pezzo多様体

2026-11-20（JST） / v0.3

## 入口と対象

研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。該当項目を確認し、本repoでは最初に `00_research_plan.md`、続いて `research/research_notes.md` と主原稿 `papers/nc-del-pezzo.tex`、`docs/reproduction.md` を読む。GitHub `uedakazushi/nc-del-pezzo` のmainを正本とする。

中心目標は、次数1・2の非可換del Pezzo n-foldを一般の n≥2 で扱い、構造対象Oだけを標識したモジュライ、Poissonモジュライとの比較、既約成分の構造を研究することである。基本偏極・豊富列・通常の次数付き表示は存在条件と選択データを区別し、射には全てのO保存完全Abel同値を入れる。

`poisson-del-pezzo` の相対Jacobi錐と `nc-cubic-threefold-moduli` のO-marked Abel圏の枠組みを具体的な入力とする。輸入する結果は定理番号・ラベル・仮定・確認したcommitを記載する。関連repoの本文をここへ重複して移さず、必要な結果・証明・障害を本研究の論理に統合する。

## 数学的な区別

1. 全Abel Artin変形の同型類、framed 1群oid、未切断2群oid、大域的なfppf stack化、有限型代数スタックを区別する。形式環の既約性だけで全NCモジュライの成分数を決めない。
2. 固定Poisson構造の形式量子化、同変な相対量子化、有限パラメータでの代数化、全NC変形の被覆は別の主張である。形式級数にパラメータ1を代入しない。
3. 次数1の生成重みは (1^n,2,3)、関係次数6。次数2は (1^(n+1),2)、関係次数4。次数一生成を仮定しない。非零rank2構造の中心的な一次Casimirは両次数とも n−1 個である。
4. AS-Gorenstein index n−1 だけから、無捩れなSerre式や通常の反標準Veroneseを結論しない。Nakayama自己同型、相対基底線束、反標準列自体の豊富性とsection復元を確認する。
5. 定理の仮定・依存・証明箇所を明記し、証明済み・追加仮定付き・未証明・計算的観察を分ける。原稿の証明、今回の点検、実行した計算、形式証明、新規性確認は別の状態である。誤りは依存する主張・要約・方針・hubにも反映する。
6. 主張の優先権を推測しない。公表用原稿では一次資料の適用条件を確認し、既知の変形・量子化・復元定理と本研究固有の帰結を区別する。

## 現行研究一式と保存許可

研究方針・研究ノート・公表用論文を中心とし、有効な知識と再現に必要な最小限のソース・入力・コード・書誌を保持する。日誌・過去の会話・旧原稿・旧bundle・バックアップ・作業ログ・大量の外部PDFを蓄積しない。価値ある証明を軽量化のために削除しない。主要文書は日付と版を付け、現在の内容へ置き換える。

主原稿は必ず本文を持つ `papers/nc-del-pezzo.tex` とし、日本語LuaLaTeXで書く。分割稿は `papers/sections/`。独立論文には内容を表す名前を付け、役割をREADMEと方針に記載する。著者欄は空欄にする。

通常コミットとmainへのpushは承諾を求めず実行する。15〜30分を目安に区切りのよいところで保存し、remote SHAと内容を照合する。他の作業者の変更を保持する。force push、履歴改変、GitHub Actionsの追加・起動は行わない。PDF・ZIP・中間物・キャッシュはGitで追跡しない。GitHub保存後はLibraryへの定常的二重保存を行わず、pushできない場合の緊急保存または明示的な依頼に限る。既存Libraryファイルを無断で削除しない。

## 組版と検証

research-hubの `papers/paper-template.tex`、`papers/README.md`、`.latexmkrc`、`.vscode/settings.json`、`.vscode/extensions.json` を参考にする。ルートの `latexmk` または `make pdf` で `build/nc-del-pezzo.pdf` と同じ場所のSyncTeXを生成する。主稿改名時はinput・文献・分割ソースのroot指定・README・方針・設定を揃える。

保存前に必要ファイル・ローカル参照・TeXの参照と引用・必要範囲の計算・組版を確認する。VS Code UI操作とCLIのレシピ相当実行は区別する。未実施・失敗・依存環境の制約を `docs/reproduction.md` に正確に記す。

## research-hubの更新義務

研究の区切りには、まず本repoの原稿・ノート・方針・READMEを整理して保存し、その結果に基づいてhubの該当項目を更新する。主要到達点、確実性、未解決の核心、次の一手、依存関係、正本・再開先、実際の資料確認日を反映する。詳細todo・証明・履歴はhubに重複させない。実質的変更がなければ日付だけを更新しない。

保存直前にhubの最新内容を読み、他研究と並行変更を保持して通常コミットでmainへ反映する。本repoの保存とhub更新の成否を別々に確認する。hubを更新できなくても研究成果を保存し、未反映項目と理由を報告する。
