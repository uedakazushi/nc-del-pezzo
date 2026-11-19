# 再現手順と検証範囲

2026-11-20（JST） / v0.1

## 組版

リポジトリ直下で実行する。

```bash
latexmk
```

または `make pdf`。主原稿は `papers/nc-del-pezzo.tex`、出力は `build/nc-del-pezzo.pdf`、SyncTeXも同じ場所。`.latexmkrc` はmainを基準に入力と文献の相対パスを解決する。

必要な環境：LuaLaTeX、latexmk、BibTeX、luatexja、luatexja-fontspec、amsmath/amsfonts/amsthm、mathtools、geometry、booktabs、longtable、hyperref、Noto Serif CJK JPおよびNoto Sans CJK JP。TeX Live相当の環境を想定する。TeXは外部PDFや非公開データを読み込まない。

VS Codeでは推奨拡張LaTeX Workshopを入れる。recipeはworkspace rootを作業ディレクトリとして `.latexmkrc` を明示指定する。実質的に同じCLIは次の通り。

```bash
latexmk -norc -r .latexmkrc papers/nc-del-pezzo.tex
```

## 有限計算

```bash
python3 computations/verify_formal_geometry.py
```

Python 3の標準ライブラリのみを使用する。`n=2,...,8` と両次数について、重み付き単項式の独立な計数、monic中心商の基底、簡約Hilbert級数、反標準部分列の第n差分を照合する。次数2の全四添字に対して `P=εQ+ε²R` の二次Plücker係数を記号的に展開し、具体的な障害方向を確認する。

これらは有限範囲の数式確認であり、全Abel変形比較、一般nでの証明、モジュライの代数性、量子化の全高次積を機械的に証明するものではない。

## 検証の状態

- 原稿の主要証明を直接点検した。全Artin比較は引用する一次定理の仮定・射・係数環に照合した。
- 量子化のmonic分裂、QGr係数変更、Abel平坦性、次数スカラーの整合性、初commutatorと形式自己写像による全Artin普遍性を独立に点検した。相対augmentation Ext、形式一般ファイバーの中心、Veroneseの全持上げ、Serre周期からの次数分離の依存関係も点検した。
- 上記Python計算は2026-11-20に実行して全件成功。
- 2026-11-20に上記レシピ相当CLIでLuaLaTeX・BibTeX・latexmkを実行し、26頁のPDFとSyncTeXを生成した。参照・引用の未解決、組版警告、はみ出し、欠落文字はない。全頁のレンダリングを確認し、主要定理・数式・参考文献を目視した。TeXのlabel・citation・inputとMarkdownの内部リンクにも欠落がない。
- 使用したエンジンはLuaHBTeX 1.18.0。必要なluatexjaと和文フォントを備える環境で組版した。VS Code設定の検査とrecipe相当CLIは確認済みだが、VS Code UIのビルド操作とSyncTeXのクリック動作は実行していない。
- 形式証明器は使っていない。包括的な優先権調査、有限非零パラメータでの代数化、全ncモジュライの代数性・成分数の検証は未完了。

## 保存と外部依存

GitHub mainが正本。PDF、ZIP、組版中間物、キャッシュは追跡しない。通常コミット・mainへのpushとhub更新にはGitHubの対象repoへの書込み権限が必要だが、組版・有限計算には認証不要。入力となる他研究の具体的commitと定理は [文献と依存](../research/literature.md) に記載する。
