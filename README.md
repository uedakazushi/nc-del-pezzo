# 次数1・2の非可換del Pezzo n-fold

**2026-11-20（JST） / v0.1 — 現行研究一式**

最初に [研究方針](00_research_plan.md) を読む。対象は一般の `n ≥ 2`、次数 `d=1,2`。構造対象 **Oだけを標識**し、豊富列や基本偏極の選択を忘れ、射には全てのO保存完全Abel同値を採用する。

## 現在の到達点

- **全Abel Artin変形の同型類関手を計算。** 滑らかな可換点で、次数1は `b(n,1)+n` 変数の冪級数環、次数2は `b(n,2)` 次元の形式円板と `Gr(2,n+1)` のPlücker錐の頂点完備化の積となる。有限自己同型群では割っていない。
- **各可換点の形式分枝は一つ。** 次数2・`n≥3`では特異であり、一次Poisson方向の二次障害は `Q∧Q`。通常の多様体の変形方向では相殺できない。全ncモジュライの成分数は未決定。
- **Poisson零切断の完備化への量子化の降下。** 任意の冪零係数上でmonic中心商が次数ごとに自由。座標変換同変性と次数スカラーの自然恒等化により、O-markedなtailsの形式族が得られる。
- **追加仮定付きの全同値の認識。** 反標準軌道環からの復元と、二つ以上の中心一次変数による任意指数のVeronese同型の持上げ。次数1・2では中心一次Casimirは共に `n−1` 個。相対Serre、saturation、反標準豊富性、普遍中心条件を省略しない。
- **次数の圏論的識別。** 明示した反標準ACM・相対perfect条件の下で、反標準Euler多項式の第n差分から `d(n−1)^n` を復元する。
- **相対Extと形式一般ファイバーの中心。** 冪零段階の中心商は左右で唯一のaugmentation Ext `Ext_B^(n+1)(R,B)=R(n−1)` を持つ。固定した任意の非零Poisson方向では、`C((h))` 上の量子中心はCasimir多項式環そのものであり、Veronese持上げの代数的仮定が実現する。

全Abel形式変形、相対Serre条件を課したnc多様体の問題、重み付きAS超曲面による部分問題を区別する。AS包絡の存在や無捩れなSerre公式を形式局所環だけから推論しない。包括的な新規性の確認は未了。

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
