# 文献・依存関係・新規性の範囲

2026-11-20（JST） / v0.1。完全な書誌は [references.bib](../references.bib)。以下は使用する一次資料の具体的な箇所を示す。外部論文のPDFは収録しない。

## 1. 他研究からの数学的入力

### poisson-del-pezzo

確認した正本はmain commit **4834ea4f3e13bff4d6c5793cec9b169d8f1ad56f**、主原稿v1.4。

[固定した主原稿](https://github.com/uedakazushi/poisson-del-pezzo/blob/4834ea4f3e13bff4d6c5793cec9b169d8f1ad56f/papers/poisson-del-pezzo.tex)

- 定理7.3、label `thm:relative-poisson`：任意基底変更と両立する二重ベクトル束とJacobi錐。次数1はA^n、次数2はGr(2,n+1)のPlücker錐。商で割る前のambient Jacobi/Casimir公式を含む。
- 定理8.8、label `thm:poisson-moduli`：正規形の係数開集合と有効座標変換群による全族の商表示。
- 定理8.13・命題8.14：古典Poissonモジュライの次数ごとの既約性と次数の区別。これは全ncモジュライの成分定理ではない。
- `quantization.tex`：固定Poisson方向の形式量子化と重み付き次数の保存。今回の任意冪零基底でのmonic分裂、同変な圏の降下をこのrepoで進める。

使用仮定は、複素数体、滑らかで射影的、n≥2、−K=(n−1)H、H ample、H^n=1または2。非滑らかな境界に結果を拡張していない。

### nc-cubic-threefold-moduli

確認した正本はmain commit **6c35d2c84671c2538e61836a6bf3a511392eacce**、主原稿v22。

[固定した研究一式](https://github.com/uedakazushi/nc-cubic-threefold-moduli/tree/6c35d2c84671c2538e61836a6bf3a511392eacce)

`abel_marked_moduli.tex` のO-marked全Abel同値、反標準軌道、豊富列の選択を忘れる規約と、`abel_cubic_deformations.tex`・`abel_formal_descent.tex` の全Artin変形を比較した。三次三様体固有の次数一生成、二次包絡、指数2、残余圏の比較は本件の定理として輸入しない。本稿のVeronese復元は指数r=n−1を扱い、中心の一次変数を二つ以上使う一般命題として証明する。

## 2. 全Abel変形と量子化

| 一次資料 | 確認箇所 | 使用内容と限定 |
|---|---|---|
| Lowen, *Algebroid prestacks and deformations of ringed spaces*, Trans. AMS 360 (2008), 1631–1660, DOI 10.1090/S0002-9947-07-04354-1 | [著者掲載出版版](https://win.uantwerpen.be/~wlowen/pdf%20papers/TAMS-AlgebroidPrestacksRingedSpaces.pdf)、Theorems 3.14, 3.26 | acyclic affine basis・localizationを介する全Abel変形とalgebroid変形の比較 |
| Yekutieli, *Twisted deformation quantization of algebraic varieties*, Adv. Math. 268 (2015), 241–305, DOI 10.1016/j.aim.2014.09.003 | [arXiv:0905.0488v5](https://arxiv.org/abs/0905.0488v5)、Corollaries 7.5, 11.2, Theorem 11.1 | H¹(O)=H²(O)=0によりordinaryな変形同値類へ降ろす。可換積も動くCor.11.2を使い、固定sheaf星積を扱うCor.11.3の追加仮定を省略しない |
| De Deken–Lowen, *Abelian and derived deformations in the presence of Z-generating geometric helices*, JNCG 5 (2011), 477–505, DOI 10.4171/JNCG/83 | [出版版](https://ems.press/content/serial-article-files/30497)、Proposition 4.4、Theorem 4.5、Proposition 4.6 | m≤nの有向Ext¹,²消滅、豊富列持上げとQmod、局所有限・noetherianの持上げ。全ての正負捻りの高次Ext消滅は不要 |
| Lowen–Van den Bergh, *Deformation theory of abelian categories*, Trans. AMS 358 (2006), 5441–5483, DOI 10.1090/S0002-9947-06-03871-2 | [arXiv:math/0405226](https://arxiv.org/pdf/math/0405226)、取得したv1のPropositions 3.4, 3.7 | injective/coflatによる圏の平坦性、Hom-flatな線型圏の加群圏。出版版とは番号が異なる。本文のAbel平坦性はnoetherian基底に限定 |
| Kontsevich, *Deformation quantization of Poisson manifolds*, LMP 66 (2003), 157–216, DOI 10.1023/B:MATH.0000027508.00421.bf | [著者最終稿](https://www.ihes.fr/~maxim/TEXTS/DefQuant_final.pdf)、§§4.6.2,6,8、§7のP3 | graph formality、twisted mapによる中心元、GL同変性。一般の非線型座標変換への厳密同変性ではない |

これらの比較・量子化原理は既知である。本研究では、次数1・2・一般nの相対錐への適用、monic商の任意基底での分裂、O-markedな圏の同変降下を示す。さらに初commutatorと完備局所環の自己写像を使い、構成した特定の量子化そのものが全Artin同型類に自然な全単射を与えることを証明した。既知の比較の逆と正確に同じ正規化を持つことは、この結論に不要である。

接空間のHochschildによる説明には、Lowen–Van den Bergh, *Hochschild cohomology of abelian categories and ringed spaces*, Adv. Math. 198 (2005), 172–221, DOI 10.1016/j.aim.2004.11.010 の [著者稿](https://cantate.be/site/hochschild_ab.pdf)、Theorem 3.1、Corollaries 7.7.2・7.8.2と、Yekutieli, *The Continuous Hochschild Cochain Complex of a Scheme*, Canad. J. Math. 54 (2002), 1319–1337, DOI 10.4153/CJM-2002-051-8 の [修正版出版論文](https://www.math.bgu.ac.il/~amyekut/publications/diagonal/cjm.pdf)、Corollary 0.6を確認した。主証明はcommutatorの完全列で完結し、HKRの積や括弧との両立は使わない。

## 3. 反標準認識と曲面の先行研究

- Mori–Ueyama, *A categorical characterization of quantum projective spaces*, [arXiv:1708.00167v4](https://arxiv.org/abs/1708.00167v4)。Definitions 2.1(5), 2.5, 3.4、Theorem 2.6(2)、Remark 3.5、§1.2を確認。豊富対からのsection環復元とcanonical bimoduleを使う。AS-GorensteinのパラメータだけではNakayama捻りを消せない。
- [Stacks Project, Tag 0FY3, Lemma 57.3.5](https://stacks.math.columbia.edu/tag/0FY3)：双対構造を持つSerre関手のYoneda一意性。これ自体はAbel同値の全認識を述べる定理ではない。
- Hong–Xu, *Poisson cohomology of del Pezzo surfaces*, J. Algebra 336 (2011), 378–390、[arXiv:1001.1082v2](https://arxiv.org/abs/1001.1082v2)、Theorem 3.9。5≤r≤8点の吹上げでdim H²_π=r+2、高次は消滅。次数1・2の曲面の10・9という接空間次元を新規結果と扱わない。
- Etingof–Ginzburg, *Noncommutative del Pezzo surfaces and Calabi–Yau algebras*, JEMS 12 (2010), 1371–1416、[出版版](https://ems.press/content/serial-article-files/31746)。Theorem 3.3.2、Definition 3.4.3、Theorems 3.4.4–3.4.5、§3.5、Proposition 8.1.1。三変数potentialと中心商によるfiltered量子化・generic半普遍性は先行結果。genericを一つのZariski開集合と自動的に読み替えず、任意の中心多項式係数で同じ結果が成立すると推論しない。
- Rains, *Filtered deformations of elliptic algebras*, [arXiv:2107.13540v2](https://arxiv.org/abs/2107.13540v2)。Introと中心拡張の枠組みを確認。楕円代数からのfiltered変形は有限パラメータ族を研究する次の出発点。全n・全O-markedモジュライの分類としては使わない。
- Abdelgadir–Okawa–Ueda, *Compact moduli of marked noncommutative cubic surfaces*, [arXiv:2404.00175](https://arxiv.org/abs/2404.00175)。Introとquiver markingを確認。例外集合に対応するquiver関係のGITモジュライであり、本研究のOのみを残す同値関係とは異なる。
- Okawa–Ueda, *AS-regular algebras from acyclic spherical helices*, [arXiv:2007.07620](https://arxiv.org/abs/2007.07620)。球面helixからの構成を比較した。一般次元での表示を検討する基礎であり、本稿で全変形のAS包絡存在を結論する根拠には用いていない。

Plücker座標環の正規性・Cohen–Macaulay性にはSvanes (1973) とDe Concini–Procesi (1981) の標準単項式理論を用いる。具体的書誌と一次資料URLはBibTeXに保持する。

## 4. 公表前に残る文献上の課題

一般nでの全Abel形式環、具体量子化の全Artin普遍性、任意指数Veronese復元、同変な圏の降下という組合せについて、包括的な優先権調査は未了。既存の非可換del Pezzo曲面の様々な定義、AS Z-代数、marked quiver、非可換吹上げとの比較を深める必要がある。講演概要にある未公表の一般次数の主張は確立済み定理として引用していない。
