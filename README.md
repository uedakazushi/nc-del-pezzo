# 次数1・2の非可換del Pezzo n-fold

**2026-11-20（JST） / v0.3 — 現行研究一式**

最初に [研究方針](00_research_plan.md) を読む。対象は一般の `n ≥ 2`、次数 `d=1,2`。構造対象 **Oだけを標識**し、豊富列や基本偏極の選択を忘れ、射には全てのO保存完全Abel同値を採用する。

## 現在の到達点

- **全Abel Artin変形群oidを計算。** 滑らかな可換点で、framed形式環R_Xは次数1で `b(n,1)+n` 変数の冪級数環、次数2で `b(n,2)` 次元の形式円板と `Gr(2,n+1)` のPlücker錐の頂点完備化の積となる。HH¹(X)=0によりframed自己同値は消え、枠を忘れると `[Spf R_X/Aut(X)]` となる。
- **各可換点の形式分枝は一つ。** 次数2・`n≥3`では特異であり、一次Poisson方向の二次障害は `Q∧Q`。通常の多様体の変形方向では相殺できない。全ncモジュライの成分数は未決定。
- **Poisson零切断の完備化への量子化の降下。** 任意の冪零係数上でmonic中心商が次数ごとに自由。座標変換同変性と次数スカラーの自然恒等化により、O-markedなtailsの形式族が得られる。
- **具体的量子化が全Artin変形を実現。** 固定したグラフ量子化そのものが、各可換点のframed変形の同型類関手に自然な全単射を与える。全てのAbel Artin変形が通常の非負次数付き代数の中心超曲面商で表示でき、相対augmentation Ext条件も満たす。
- **全Artin変形が定義したnc多様体になる。** 有限Ore被覆から切断環の飽和性、有向ACM、任意の正周期の豊富性、compact生成とproper性を証明。対角dg加群のcompact性を持ち上げてsmooth性を得て、HH¹剛性から `S_R≅(−(n−1))[n]` を同定する。従ってM・重み付き超曲面部分問題・全Abel変形のArtin完成が一致する。
- **Artin近傍での全O同値の認識。** 通常の次数付き環同型を次数スカラーで割ったものと一致する。特殊ファイバーのHH¹剛性と飽和性を使うため、可換点でも成立する。別に、一般の基底で反標準軌道環から復元する条件付き定理と、二つ以上の中心一次変数による任意指数Veronese持上げを保持する。
- **一般の可換点の形式粗商。** Aut(X)=μ₂の稠密開では、Poisson錐の第二Veroneseによる符号商。両次数・全n≥2で特異だが、正規Cohen–Macaulay整域で一分枝。粗商のArtin点と変形同型類は区別する。
- **両次数・全次元の有限パラメータ族。** 特別なPoisson方向で、負の補助次数によりグラフ量子化とCasimir持上げを有限多項式化。別に分離型potentialの普遍PBW基底と、次数1ではh⁶までの有限な中心元公式を証明した。全係数・全有限hで平坦であり、各n≥2で滑らかな可換点を含む。一般の楕円的最高次項を被覆するとは主張しない。
- **有限非零hの普遍中心とambient CY。** 最高補助式を規格化した族では、任意基底変更後も中心はちょうどn−1個の一次Casimirの多項式環。n≥3では任意指数Veronese持上げの代数的仮定を満たす。分離型ambientの無捩れな相対bimodule CY同型も全有限hで証明。有限hのtailsのsmooth proper性・Serre公式は未証明。
- **次数の圏論的識別。** 反標準Euler多項式の第n差分から `d(n−1)^n` を復元する。Serre周期n−1・有向ACM条件を課した本稿のMでは次数1・2が開閉に分かれる。
- **相対Ext・ambient CY・形式一般ファイバーの中心。** 中心商は `Ext_B^(n+1)(R,B)=R(n−1)` を持つ。Kontsevich–Shoikhetの対と体積形式を固定すれば、任意の冪零係数上で無捩れなambient CY同型が得られる。固定した任意の非零Poisson方向では、`C((h))` 上の中心はn−1変数のCasimir多項式環となり、Veronese持上げの代数的仮定が実現する。

証明本文と依存する一次定理の適用条件を点検した研究稿であり、形式証明器による検証や包括的な優先権確認は未了。**未解決の核心は一般の楕円的最高次項の有限型量子化、有限hのtailsのnc多様体条件、一般nc点、有限型atlasと全体の既約成分数**。Artin完成の一致を大域の一致へ拡張していない。相対Serreの対象はperfect圏であり、特異なArtin基底上の全有界coherent導来圏とは区別する。

## 読む順序

| 資料 | 役割 |
|---|---|
| [研究方針](00_research_plan.md) | 一般原則と保存許可、現目標、到達点、次の着手方法 |
| [研究ノート](research/research_notes.md) | 有効な計算、適用条件、反例・障害、残問 |
| [文献と依存](research/literature.md) | 一次資料の参照箇所、他repoの固定commit、既知結果との比較 |
| [主原稿](papers/nc-del-pezzo.tex) | 日本語LuaLaTeXによる本文と証明。分割節は `papers/sections/` |
| [再現手順](docs/reproduction.md) | 組版、計算、依存関係、検証の実施範囲 |

`latexmk` または `make pdf` で `build/nc-del-pezzo.pdf` とSyncTeXを生成する。数式の有限チェックは `make verify`。PDF・ZIP・組版中間物はGitで追跡しない。

## 研究間の関係

[poisson-del-pezzo](https://github.com/uedakazushi/poisson-del-pezzo) の相対Jacobi錐・Poisson商スタックを入力とし、[nc-cubic-threefold-moduli](https://github.com/uedakazushi/nc-cubic-threefold-moduli) のO-marked Abel圏の枠組みを重み付きの次数1・2へ展開する。本repoがこのnc研究の正本であり、研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。
