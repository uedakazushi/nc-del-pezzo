# 再現手順と検証範囲

2026-11-20（JST） / v0.4

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
make verify
# 個別には
python3 computations/verify_formal_geometry.py
python3 computations/verify_finite_families.py
python3 computations/verify_cubic_top.py
```

Python 3の標準ライブラリのみを使用する。`n=2,...,8` と両次数について、重み付き単項式の独立な計数、monic中心商の基底、簡約Hilbert級数、反標準部分列の第n差分を照合する。次数2の全四添字に対して `P=εQ+ε²R` の二次Plücker係数を記号的に展開し、具体的な障害方向を確認する。さらに二次標準Plücker単項式を独立に数え、符号粗商の接空間次元の閉公式と照合し、両次数の特異性を確認する。

さらに `verify_finite_families.py` は、有理数係数の多項式環 `Q[h,p1,...,p5,q1,q2,q3]` 上で唯一のPBW overlapと明示的Casimirの三つの交換子を厳密に簡約する。係数やhの数値特殊化、h進有限jetによる検査ではなく、全係数の多項式恒等式を確認する。次数2のp5=0特殊化、両次数の内部斉次性、補助重みによる停止性、中心補正項がmonic二次項を保つことも照合する。定数項p0,q0は中心性に影響しないため計算から省いている。

`verify_cubic_top.py` は `Q[a,b,c,alpha,beta,t]`、t=h²、上の自由代数で、四次Sklyanin中心元の九項交換子証明書を両生成元について確認する。type-Aパラメータ置換、zの消去関係、C0恒等式、多項式として正規化した中心元のh=0極限も照合する。SymPyなど追加依存はない。

最初のスクリプトは有限範囲の数式確認、後二つは指定した有限な関係式と中心公式の厳密な恒等式検証である。全Abel変形比較、一般nでの証明、モジュライの代数性、グラフ量子化の全高次積を機械的に証明するものではない。

## 検証の状態

- 原稿の主要証明を直接点検した。全Artin比較は引用する一次定理の仮定・射・係数環に照合した。
- 量子化のmonic分裂、QGr係数変更、Abel平坦性、次数スカラーの整合性、初commutatorと形式自己写像による全Artin普遍性を独立に点検した。相対augmentation Ext、形式一般ファイバーの中心、Veroneseの全持上げ、Serre周期からの次数分離の依存関係も点検した。
- HH¹による全自己同値剛性、framed群oid比較、Aut(X)の同変slice、形式粗商とArtin graded認識を点検した。stack化のArtin比較は有限忠実平坦細分と全Čech環がArtinであることを確認した。
- 固定元のOre局所化・重なり・有限Čech、飽和性・正周期豊富性、RHomの有限自由模型、対角dg加群のcompact持上げを点検した。smoothnessの主証明は未検証の非可換積Morita同定に依存しない。Serre存在・HH¹対角剛性、有限鎖formalityによるambient CY同型を独立に点検した。
- 有限型族について、補助次数によるグラフ式の停止、任意係数上のPBW・monic分裂、滑らかな古典点、全非零hでの中心と小行列式による任意基底変更を点検した。明示的potentialの有限自由対角複体・Hessian自己双対性と、中心差のKoszul解消による絶対bimodule CYへの移行も独立に点検した。
- 分離型有限族の相対加群双対、torsion導来関手の比較、非有界局所化、χ・Serre消滅、compact生成・proper性・基底変更を独立に点検した。有限windowには全変数を正の補助重みとするKoszul持上げを用いる。相対Serreは左右共通の局所化bimoduleの双対から合成まで両立する形で証明した。正周期の有限開条件と任意基底変更後の豊富性も点検した。
- 次数2の一般楕円型topについて、有限AS正則開条件、相対potential複体、全lower係数のPBW、次数6以下の有限中心行列、topだけに依存する分母、中心元の普遍正則性と任意基底変更を点検した。全体の中心・族の強Noether性・tailsのsmoothnessを結論していないことも確認した。
- 上記三つのPython計算は2026-11-20に `make verify` で実行して全件成功。分離型族の計算では167種類の単語簡約を使用した。Sklyanin中心元は全係数の自由代数恒等式として検証した。
- 現行v0.4はLuaLaTeXで67頁に組版済み。最終ログに未解決参照・文献警告・欠落文字・overfull/underfullはない。全67頁をレンダリングして目視確認し、新しい中心元構成等の頁も拡大して確認した。TeXの入力・ラベル・引用とローカルMarkdownリンクに参照切れはない。
- 使用したエンジンはLuaHBTeX 1.18.0。必要なluatexjaと和文フォントを備える環境で組版した。VS Code設定の検査とrecipe相当CLIは確認済みだが、VS Code UIのビルド操作とSyncTeXのクリック動作は実行していない。
- 形式証明器は使っていない。包括的な優先権調査、次数1の一般楕円型topの有限量子化、次数2の一般楕円型族の強Noether性と相対tails、有限非零hでのsmooth性、全ncモジュライの代数性・成分数の検証は未完了。

## 保存と外部依存

GitHub mainが正本。PDF、ZIP、組版中間物、キャッシュは追跡しない。通常コミット・mainへのpushとhub更新にはGitHubの対象repoへの書込み権限が必要だが、組版・有限計算には認証不要。入力となる他研究の具体的commitと定理は [文献と依存](../research/literature.md) に記載する。
