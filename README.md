# 次数1・2の非可換del Pezzo n-fold

**2026-11-20（JST） / v0.8 — 現行研究一式**

最初に [研究方針](00_research_plan.md) を読む。対象は一般の `n ≥ 2`、次数 `d=1,2`。構造対象 **Oだけを標識**し、射には全てのO保存完全Abel同値を採用する。GitHub mainが正本である。

## 中心となる到達点

**全独立Poisson方向を同時に含む有限表示中心商族を構成し、この同じ族が全framed Abel Artin変形を実現することを証明した。** 両次数の全可換係数の零切断を含む有限型主開上で、中心元は任意の非被約基底変更後にも正則であり、商は次数別に有限局所自由となる。

- **次数1：** 方向空間は `E* ≅ A^n`。ambientの明示的開条件は `g₁=(1+A₄(D))(5+A₄(D))≠0`。4次までの座標不変な中心jetを全係数の厳密計算で与え、`P(E*)` 上の `H¹(Sym⁶K(m))=0 (m≥5)` により全高次へ持ち上げ、有限線型方程式で代数化する。
- **次数2：** 方向空間は `Gr(2,n+1)` のPlückerアフィン錐。ambientの明示的開条件は `g₂=det(1+4T)≠0`。中央多項式係数上の形式中心と `H¹(Sym⁴K(m))=0 (m≥0)` から、錐の頂点を含めて中心元を構成する。全四次係数を許すが、退化ファイバーの中心全体が一定階数とは主張しない。
- **全Artin普遍性：** 滑らかな可換点で係数空間の横断sliceを選ぶと、この有限中心商のArtin基底変更が全framed変形を分類する。DDLの線型変形とAbel変形の比較、初交換子、既存の全完備局所環を使う。全方向族の有限基底上の相対tails・smooth proper性やatlasは、ここから自動的には従わない。

中心元のためには、ambientの明示条件に加えて零切断上で1となる有限な追加分母を選ぶ。その存在を証明した段階であり、最小行列式や中心元の全方向に共通する閉じた公式は未計算である。次数1の4次jetを有限パラメータでの厳密な中心公式とは扱わない。

## 形式モジュライと圏論的結果

framed形式環は、次数1では `b(n,1)+n` 変数の冪級数環、次数2では `b(n,2)` 次元の形式円板とPlücker錐の頂点完備化の積である。各可換点の形式分枝は一つ。次数2・`n≥3` は特異で、二次障害は `Q∧Q`。通常の多様体の変形方向では相殺できない。

HH¹(X)=0によってframed自己同値は消え、枠を忘れた形式群oidは `[Spf R_X/Aut(X)]` となる。一般点での被覆対合の符号粗商は両次数とも特異であり、正規Cohen–Macaulay整域である。粗商のArtin点と変形同型類は区別する。

全Abel Artin変形について、通常の重み付き中心超曲面表示、飽和性・有向ACM・全正周期の豊富性・compact生成・smooth proper性と、perfect圏のSerre公式 `S=(−(n−1))[n]` を証明した。Artin近傍の全O保存同値は、通常のgraded環同型を次数スカラーで割ったものとして認識できる。別に、条件を明示した反標準section復元と、中心一次変数による任意指数Veronese持上げを保持する。

## 有限基底上で圏論まで確立した部分族

両次数の分離型族・一般楕円型の一方向族では、全n≥2で普遍PBW、ambientの無捩れな相対CY、普遍正則な中心商を得ている。分離型では中心元を有限式で与え、非零パラメータの普遍中心も計算した。一般楕円型では有限中心行列と、次数1・2の線束を持つ相対曲線のtwisted homogeneous coordinate ringを使う。

これらの部分族には、任意noetherian基底変更後の強Noether性・積Noether性、相対tails・Serre公式・有限compact生成窓を証明した。対角の有限部分解消を用いることで、滑らかな可換点の有限型開近傍で実際のsmooth properなnc del Pezzo族となる。全有限パラメータでのsmoothnessは主張しない。

一方向族のPoisson Kodaira–Spencer像は高々1次元であり、それだけでは全変形のatlasにならない。上の同時中心商がこの接空間不足を解消し、その全Artin普遍性も得た。次は全方向族への有限基底上の圏論的結果の拡張に取り組む。

## 残る核心と確実性

**次の課題は全方向中心商族の強・積Noether性、相対tailsとsmoothness、全O同値による有限型atlas、大域的な全既約成分数である。** 特異な活性最高次式を持つ方向も扱う必要があり、滑らかな楕円曲線の表示だけでは尽くせない。

原稿に証明を記述し、主要部分を独立に点検した研究稿である。有限計算の証明書は実行しているが、形式証明器による検証と包括的な優先権調査は未了。各定理の仮定・依存と確認範囲は方針・文献・再現手順に記載する。

## 読む順序

| 資料 | 役割 |
|---|---|
| [研究方針](00_research_plan.md) | 一般原則と保存許可、現目標、到達点、次の着手方法 |
| [研究ノート](research/research_notes.md) | 有効な補題、計算、反例・障害、残問 |
| [文献と依存](research/literature.md) | 一次資料の参照箇所、他repoの固定commit、既知結果との比較 |
| [主原稿](papers/nc-del-pezzo.tex) | 日本語LuaLaTeXによる本文と証明。分割節は `papers/sections/` |
| [再現手順](docs/reproduction.md) | 組版、計算、依存関係、検証の実施範囲 |

`latexmk` または `make pdf` で `build/nc-del-pezzo.pdf` とSyncTeXを生成する。有限チェックは `make verify`。PDF・ZIP・組版中間物はGitで追跡しない。

## 研究間の関係

[poisson-del-pezzo](https://github.com/uedakazushi/poisson-del-pezzo) の相対Jacobi錐・Poisson商スタックを入力とし、[nc-cubic-threefold-moduli](https://github.com/uedakazushi/nc-cubic-threefold-moduli) のO-marked Abel圏の枠組みを重み付きの次数1・2へ展開する。研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。
