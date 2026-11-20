# 文献・依存関係・新規性の範囲

2026-11-20（JST） / v0.7。完全な書誌は [references.bib](../references.bib)。以下は使用する一次資料の具体的な箇所を示す。外部論文のPDFは収録しない。

## 1. 他研究からの数学的入力

### poisson-del-pezzo

確認した正本はmain commit **4834ea4f3e13bff4d6c5793cec9b169d8f1ad56f**、主原稿v1.4。

[固定した主原稿](https://github.com/uedakazushi/poisson-del-pezzo/blob/4834ea4f3e13bff4d6c5793cec9b169d8f1ad56f/papers/poisson-del-pezzo.tex)

- 定理7.3、label `thm:relative-poisson`：任意基底変更と両立する二重ベクトル束とJacobi錐。次数1はA^n、次数2はGr(2,n+1)のPlücker錐。商で割る前のambient Jacobi/Casimir公式を含む。
- 定理8.8、label `thm:poisson-moduli`：正規形の係数開集合と有効座標変換群による全族の商表示。
- 補題8.7：全ての対象XでH⁰(T_X)=0。注意8.5、label `rem:deck-action`：被覆対合はPoissonパラメータに−1で作用。命題9.4、label `prop:generic-deck-stabilizer`：両次数・全n≥2でAut(X)=μ₂となる稠密開。形式群oidと一般点の粗符号商の入力。命題9.4の非空性・開性の証明を確認した。
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
| 同上の[出版版](https://win.uantwerpen.be/~wlowen/pdf%20papers/TAMS-DeformationTheory.pdf) | Definition 8.2、Theorem 8.17、Appendix BのPropositions B.1, B.3 | 射が自然同型類である群oid擬関手の比較。B.1/B.3は対象集合を固定した代表と自己同値のstrictな代表に使用。B.4の同型類全単射を群oid同値と読み替えない |
| Kontsevich, *Deformation quantization of Poisson manifolds*, LMP 66 (2003), 157–216, DOI 10.1023/B:MATH.0000027508.00421.bf | [著者最終稿](https://www.ihes.fr/~maxim/TEXTS/DefQuant_final.pdf)、§§4.6.2,6,8、§7のP3 | graph formality、twisted mapによる中心元、GL同変性。一般の非線型座標変換への厳密同変性ではない |

これらの比較・量子化原理は既知である。本研究では、次数1・2・一般nの相対錐への適用、monic商の任意基底での分裂、O-markedな圏の同変降下を示す。さらに初commutatorと完備局所環の自己写像を使い、構成した特定の量子化そのものが全Artin同型類に自然な全単射を与えることを証明した。既知の比較の逆と正確に同じ正規化を持つことは、この結論に不要である。

接空間と微小自己同値のHochschildによる説明には、Lowen–Van den Bergh, *Hochschild cohomology of abelian categories and ringed spaces*, Adv. Math. 198 (2005), 172–221, DOI 10.1016/j.aim.2004.11.010 の [著者稿](https://cantate.be/site/hochschild_ab.pdf)、Theorems 3.1, 6.1, 6.6、Corollaries 7.7.2・7.8.2と、Yekutieli, *The Continuous Hochschild Cochain Complex of a Scheme*, Canad. J. Math. 54 (2002), 1319–1337, DOI 10.4153/CJM-2002-051-8 の [修正版出版論文](https://www.math.bgu.ac.il/~amyekut/publications/diagonal/cjm.pdf)、Corollary 0.6を確認した。injective線型圏・Abel圏・幾何的Hochschild cohomologyの比較を用いる。HKRの積や括弧との両立は使わない。

## 3. 反標準認識と曲面の先行研究

- Mori–Ueyama, *A categorical characterization of quantum projective spaces*, [arXiv:1708.00167v4](https://arxiv.org/abs/1708.00167v4)。Definitions 2.1(5), 2.5, 3.4、Theorem 2.6(2)、Remark 3.5、§1.2を確認。豊富対からのsection環復元とcanonical bimoduleを使う。AS-GorensteinのパラメータだけではNakayama捻りを消せない。
- [Stacks Project, Tag 0FY3, Lemma 57.3.5](https://stacks.math.columbia.edu/tag/0FY3)：双対構造を持つSerre関手のYoneda一意性。これ自体はAbel同値の全認識を述べる定理ではない。
- Hong–Xu, *Poisson cohomology of del Pezzo surfaces*, J. Algebra 336 (2011), 378–390、[arXiv:1001.1082v2](https://arxiv.org/abs/1001.1082v2)、Theorem 3.9。5≤r≤8点の吹上げでdim H²_π=r+2、高次は消滅。次数1・2の曲面の10・9という接空間次元を新規結果と扱わない。
- Etingof–Ginzburg, *Noncommutative del Pezzo surfaces and Calabi–Yau algebras*, JEMS 12 (2010), 1371–1416、DOI 10.4171/JEMS/235、[出版版](https://ems.press/content/serial-article-files/31746)。三変数potentialと中心商によるfiltered量子化・generic半普遍性は先行結果。**Theorem 3.3.2は、正の生成重み `(a,b,c)`、`d=a+b+c`、斉次CY potential `Φ_d`を仮定すれば、任意のlower potential `Φ_<d`に適用できる。** (i)はCY性とHilbert級数、(ii)はfiltration次数d以下の非定数中心元の存在を与える。Proposition 7.3.1(ii)は同じ固定CY topに対するPBW同型 `gr A(Φ_d+Φ_<d)≅A(Φ_d)` を与える。一方、Definition 3.4.3、Lemma 7.1.5、Theorems 3.4.4–3.4.5のgeneric条件は可算個の開条件を伴い、そのまま一つの有限型開集合の主張に置き換えない。本稿の有限型族では、次数2の三次type-A代数、次数1のStephenson代数の具体的な有限開条件からtopのCY性を先に確認し、上の全lowerの定理、被約な普遍係数環での特殊化、活性次数6以下/9以下の中心方程式を組み合わせる。低次係数に依存しない分母と任意中央係数への基底変更は本稿の証明である。Proposition 8.1.1(i)の形式中心持上げ自体は孤立特異点を仮定しない。
- Rains, *Filtered deformations of elliptic algebras*, [arXiv:2107.13540v2](https://arxiv.org/abs/2107.13540v2)。Introに加え、Propositions 2.2–2.3、Theorems 2.12–2.13、Example 3.1を確認。固定された有限表示graded代数のfiltered変形の代数性と、楕円THCRのfiltered表示を扱う。Theorem 2.13の中心持上げにはtorsion translationの仮定があり、未確認のtop全体や本稿の全方向ambientの中心へ無条件に適用しない。全n・全O-markedモジュライの分類としては使わない。
- Abdelgadir–Okawa–Ueda, *Compact moduli of marked noncommutative cubic surfaces*, [arXiv:2404.00175](https://arxiv.org/abs/2404.00175)。Introとquiver markingを確認。例外集合に対応するquiver関係のGITモジュライであり、本研究のOのみを残す同値関係とは異なる。
- Okawa–Ueda, *AS-regular algebras from acyclic spherical helices*, [arXiv:2007.07620](https://arxiv.org/abs/2007.07620)。球面helixからの構成を比較した。一般次元での表示を検討する基礎であり、本稿で全変形のAS包絡存在を結論する根拠には用いていない。

Plücker座標環の正規性・Cohen–Macaulay性にはSvanes (1973) とDe Concini–Procesi (1981) の標準単項式理論を用いる。具体的書誌と一次資料URLはBibTeXに保持する。

## 4. Compact持上げ、Serre、鎖formality、降下

| 一次資料 | 確認箇所と本稿での役割 |
|---|---|
| De Deken–Lowen (2011)、上記出版版 | Proposition 5.8（p.499）は平坦Abel変形で導来還元がcompactなら元もcompactとする。Proposition 5.9（p.500）はbounded aboveな生成系の持上げ。dg圏の対角に対しては同じcoinduction towerの論法を本文で直接証明し、Abel圏の定理を無説明で適用していない |
| Keller, *Deriving DG categories*, Ann. Sci. ENS 27 (1994), 63–102、DOI 10.24033/asens.1689、[出版版](https://www.numdam.org/article/ASENS_1994_4_27_1_63_0.pdf) | §§4.3, 8.2。compact生成系によるdg加群模型、導来Morita理論。必要なR-K-flat模型を選ぶ |
| Lowen–Van den Bergh, *On compact generation of deformed schemes*, Adv. Math. 244 (2013), 441–464、DOI 10.1016/j.aim.2013.04.024、[著者稿](https://win.uantwerpen.be/~wlowen/pdf%20papers/compactgen.pdf) | Proposition 3.7、Proposition 5.1。後者はample line bundleとH²(O)=0を持つ射影スキームの全Abel infinitesimal deformationのcompact生成。一般的先行結果として比較。本稿の任意基底変更・飽和性・proper性は有限Ore Čechで直接証明 |
| Shoikhet, *A proof of the Tsygan formality conjecture for chains*, Adv. Math. 179 (2003), 7–37、DOI 10.1016/S0001-8708(02)00023-3、[arXiv:math/0010321v2](https://arxiv.org/abs/math/0010321v2) | Theorem 2.2.7、§2.2.8、§§3.2–3.3。Kontsevich写像と対をなす鎖formality、零次項HKR、Poisson twist。本稿では多項式graphに制限して冪零係数上の有限和とし、任意基底変更を証明する |
| Dolgushev, *A formality theorem for Hochschild chains*, Adv. Math. 200 (2006), 51–101、DOI 10.1016/j.aim.2004.10.017、[arXiv:math/0402248v4](https://arxiv.org/abs/math/0402248v4) | Theorem 3。局所鎖formalityの線型座標変換に関する同変性。非線型座標変換の厳密同変性を仮定しない |
| Dolgushev, *The Van den Bergh duality and the modular symmetry of a Poisson variety*, Selecta Math. 14 (2009), 199–228、DOI 10.1007/s00029-008-0062-z、[arXiv:math/0612288v3](https://arxiv.org/abs/math/0612288v3) | Theorem 3。一変数h進・滑らかなaffine複素多様体・自明なcanonicalという設定でunimodularityと無捩れ双対性を比較。本稿の任意Artin係数はこの定理の直接適用ではなく、有限鎖twistと有限自由対角分解で証明 |
| Stacks Project、[Tag 0572](https://stacks.math.columbia.edu/tag/0572)、Lemma 37.23.6 | fppf被覆の局所準有限細分。局所Artin C基底では有限忠実平坦な局所Artin被覆に細分でき、全Čech環も局所Artinになる。この帰結から形式関手の等化子降下を証明し、stack化後のArtin完成を同定 |

上記一次資料の該当定理・係数環・射の定義を2026-11-20に確認した。Artin近傍の相対Serre公式はsmooth proper模型とHH¹対角剛性から証明する。分離型の有限パラメータ族では、相対局所コホモロジーと局所化bimoduleの双対から別に証明する。いずれもAS-Gorenstein indexだけから無捩れなSerre公式を結論していない。ambient CYはbimodule同型の主張であり、negative cyclic CY構造や非正則基底上のbalanced dualizing complexの全公理を付加していない。

## 5. 有限パラメータ族、局所双対、smoothness

### 5.1. Potential、負の補助次数、既知の中心式

- Ginzburg, *Calabi–Yau algebras*, [arXiv:math/0612139v3](https://arxiv.org/abs/math/0612139v3)、2007。Proposition 5.1.9と式(5.1.8)のHessian対角複体、Theorem 5.3.1(iii)の完全性とCY、Proposition 8.1.3(ii)のtensor flip対称性を確認。原資料の半単純基底の設定を任意係数環へ無説明で拡張しない。分離型では随伴次数のKoszul完全性、楕円型では三次AS正則代数の極小解消とファイバーごとの完全性を用い、自己双対性と任意基底変更を本文で証明する。
- Etingof–Ginzburgの上記一次定理を2026-11-20に再確認。負の補助次数によるfiltered量子化の一般原理は既知の枠組みと重なる。本稿は両次数・全nへの中央係数の付加、分離型の有限Casimir式、商の普遍自由性と規格化族の非零hでの普遍中心を具体化する。分離型の明示式そのものの新規性は未確定である。
- 同論文の参考文献[R]が指す [RainsのMagma形式中心元](https://math.mit.edu/~etingof/delpezzocenter) は取得を確認。E6/E7/E8の式があり、E7は `xy−q yx=t z+c1` 等の規約でzを消去した式。本稿の証明入力には使っていない。次数1の一般楕円型topへの拡張では、分母、関係式、正規化と中央係数の扱いを照合する。

### 5.2. 次数2の一般楕円型topと有限型係数への適用

| 一次資料 | 確認箇所・仮定 | 本稿での使用範囲 |
|---|---|---|
| Belmans–Raedschelders, *Derived categories of noncommutative quadrics and Hilbert squares*, IMRN 2020 (19), 6042–6069、DOI 10.1093/imrn/rny192、[arXiv:1605.02795v2](https://arxiv.org/pdf/1605.02795) | Example 3.11、式(75)–(76)。三次type-A関係式と除外集合 `{a²=b²=c²}∪{[0:0:1],[0:1:0]}` を明記 | `a=1+2βh²/3`, `b=−2+2βh²/3`, `c=αh²` とし、`a(a²−b²)≠0` を有限なAS正則条件として使う。h=0では元の三生成元表示を使い、多項式環に戻す。原論文AS1987の本文は未取得であり、ここで確認した具体的分類の出典はこの一次研究論文である |
| Artin–Tate–Van den Bergh, *Modules over regular algebras of dimension 3*, Invent. Math. 106 (1991), 335–388、[p.336](https://gdz.sub.uni-goettingen.de/fulltext/PPN356556735_0106/00000342?_format=xml)、[p.338](https://gdz.sub.uni-goettingen.de/fulltext/PPN356556735_0106/00000344?_format=xml)、[p.349](https://gdz.sub.uni-goettingen.de/fulltext/PPN356556735_0106/00000355?_format=xml)の一次資料 | §2 p.338は次数一生成の3次元正則代数のNoether性をATV1990 (8.1)として明記。Theorem 3.9 p.349は大域次元とGK次元がともにd≤4の正則Noether代数の整域性。Theorem II p.336は3次元正則代数が中心上有限加群となる条件を対応する自己同型σの有限位数性と同値にする | 三次type-Aの全正則複素ファイバーのNoether性・整域性に使用。滑らかな楕円point curveだけに制限する必要はない。Theorem IIは有限位数で中心が増大し得ることの根拠であり、有限開集合上で中心全体を一つの四次中心元で生成できると仮定しない。族の係数環上のNoether性や強Noether性はこれらの体上の定理から結論しない。GDZの該当三頁を直接取得して確認 |
| De Laet, *On the center of 3-dimensional and 4-dimensional Sklyanin algebras*, J. Algebra 487 (2017), 244–268、DOI 10.1016/j.jalgebra.2017.05.032、[arXiv:1612.06158v1](https://arxiv.org/pdf/1612.06158) | §5.2の四次中心元の式とTheorem 5.3。三次代数がAS正則であれば表示した元は中心的。表示された元が特別なパラメータで零になる可能性は排除していない | 最高次中心元の既知の式として引用する。本稿ではhを逆元にせず多項式係数の除算で可換極限へ延長し、九項の自由代数恒等式と正規化を `verify_cubic_top.py` で検算。自由語でのz²係数と整列基底での係数を区別する |

`papers/sections/elliptic_top.tex` の定理 `thm:elliptic-finite-central-family` は、これらの体上の結果をそのまま相対定理と呼び替えたものではない。最高次代数の各次数の有限局所自由性、全lowerに対する普遍PBW性、22未知数・活性次数6以下の中心方程式、低次係数を戻した際の三角行列、中心商の普遍正則性を証明している。局所化の分母が最高次係数だけに依存するため、lower係数にn−1個の中央一次変数の任意の斉次多項式を代入できる。

Sklyanin代数、四次中心元、固定CY topのfiltered変形の存在は既知である。本稿で区別している内容は、可換楕円型点を含む有限な開近傍、任意中央係数・任意基底変更、全nの重み付き超曲面への適用である。この組合せの包括的な新規性確認は未了。有限hの相対tailsと、滑らかな可換点を含むsmooth properな開近傍には、以下の相対曲線表示・積のNoether性・有限部分対角解消を用いる。中心全体の生成や全O-markedモジュライの有限型atlasを最高次構成だけから結論しない。

### 次数1のWeierstrass型とStephensonの分類

Stephenson, *Algebras associated to elliptic curves*, Trans. AMS 349 (1997), no.6, 2317–2340、[DOI 10.1090/S0002-9947-97-01769-8](https://doi.org/10.1090/S0002-9947-97-01769-8)。一次PDFのp.2318の定義とTheorem 1.1、pp.2336–2338の解消(5.5)・Theorem 5.7を確認した。重み1・2の二生成元代数S(a,b,c)は、明示的な11点を除けばAS正則Noether整域で、重み(1,2,3)の多項式Hilbert級数を持つ。これは有限除外の分類定理であり、genericという語を有限開へ読み替えたものではない。

本稿ではWeierstrass型potentialを階数6の有限忠実平坦被覆でこの標準形へ移し、例外点を避ける十分条件を `(1+αh⁴)(5+αh⁴)≠0` と具体化した。分類と固定CY topの全lower PBW・非スカラー中心元の存在は既知である。普遍係数上の相対CY、23未知数・活性次数9以下の中心行列、lower係数に依存しない分母、任意の非被約基底変更、全nの中央斉次係数への適用は本文で証明する。これらを組み合わせた相対構成の優先権は未確認。

### 5.3. 有限族の相対双対とsmoothnessの入力

| 一次資料 | 確認箇所・本稿での役割と限定 |
|---|---|
| Reyes–Rogalski–Zhang, *Skew Calabi–Yau algebras and homological identities*, Adv. Math. 264 (2014), 308–354、DOI 10.1016/j.aim.2014.07.010、[arXiv:1302.0437v2](https://arxiv.org/pdf/1302.0437) | Lemma 1.2。体上の連結次数付き代数についてskew CYとAS正則性を比較し、対角の双対からaugmentation Extを求めるHom–tensor随伴を証明する。本稿の体ファイバーに適用し、有限GK次元はHilbert級数から別途確認する。非正則係数環上の絶対AS正則性は主張せず、係数についてperfectな加群の相対双対を同じ随伴から本文で直接証明 |
| Yekutieli–Zhang, *Serre duality for noncommutative projective schemes*, Proc. AMS 125 (1997), 697–707、DOI 10.1090/S0002-9939-97-03782-9、[著者掲載出版版](https://www.math.bgu.ac.il/~amyekut/publications/nc-serre/paper.pdf) | Lemma 4.1はQGrの導来Homを切断加群の極限で記述。Theorem 4.2は体上の連結次数付き左右Noether環とbalanced dualizing complexを仮定し、局所双対・projective双対・χ等を与える。Corollary 4.3はAS–Gorensteinの場合のχ、cohomological dimension、dualizing sheaf、classical Cohen–Macaulay性。一般には双対bimoduleのNakayama捻りが残る。本稿の非正則基底上の無捩れ相対Serre式は、この絶対定理の直接適用ではなく、相対CYからの局所コホモロジーと局所化bimoduleの計算による |
| Toën–Vaquié, *Moduli of objects in dg-categories*, Ann. Sci. ENS (4) 40 (2007), 387–444、DOI 10.1016/j.ansens.2007.05.001、[出版版](https://www.numdam.org/article/ASENS_2007_4_40_3_387_0.pdf) | Lemma 2.8(1)はlocally perfectならperfect加群が相対pseudo-perfect、(2)はsmoothなら逆方向、(3)は両条件の下での同値。Theorem 3.6はDefinition 2.4の意味でfinite typeなdg圏の対象モジュライの局所幾何性・局所有限表示性。finite typeはhomotopically finitely presentedなdg代数によるMorita模型を要求し、通常代数の有限表示と異なる。Corollary 2.13はsmooth properからこの有限性を導く。proper性とSerre自己同値だけで対角のperfect性を代用しない。また固定dg圏の対象モジュライの定理を、可変な全O-marked圏のモジュライの代数性と同一視しない |

上記三論文の指定箇所を2026-11-20に一次資料で確認した。飽和性、有向ACM、χ、compact生成、相対proper性、perfect圏のSerre双対は `finite_tails.tex` と `elliptic_relative.tex` に記述する。対角のperfect性としてのsmoothnessは、それらを入力とする `finite_smoothness.tex` の別証明による。滑らかな開近傍の幾何学的ファイバーでは、smooth性によりcoherent対象がcompactとなり、Serre公式によりホモロジー次元がちょうどnであることを得る。Serre公式だけでsmoothnessや全coherent対象のperfect性を推論したものではない。

### 5.4. 相対楕円曲線と強Noether性

- Keeler, *Ample filters of invertible sheaves*, J. Algebra 259 (2003), no.1, 243–283、DOI 10.1016/S0021-8693(02)00557-4；Corrigendum, J. Algebra 507 (2018), 592–598、DOI 10.1016/j.jalgebra.2018.03.024。[訂正を含むarXiv:math/0108068v5](https://arxiv.org/abs/math/0108068v5) のTheorems 1.5, 7.13–7.14とErratum Theorem E2.5を一次資料で確認した。Theorems 7.13–7.14は、可換noetherian環上のproper schemeについて、数値的quasi-unipotenceとあるL_mの豊富性からσ-amplenessを判定し、左右Noetherなtwisted homogeneous coordinate ringを与える。Theorem 1.5はprojective scheme上のcoherent層について、豊富線束の冪に任意のnef線束をtensorしたときの一様な高次コホモロジー消滅である。Erratum Theorem E2.5はその証明の基底変更による還元を修正し、結論を維持する。いずれも基底を体や被約環に限定しない。
- 本稿では、点曲線の二重対角線を理想(h,δ)で解消し、σ₀=idの滑らかな相対種数1曲線を構成する。最高次中心商の相対THCR同定を先に証明し、任意noetherian基底変更後に上の定理を適用する。σは基底上で各曲線の次数を保ち、相対数値同値類に恒等に作用する。中心正則拡大とfiltered PBWにより全lower・全nに拡張する。
- 積のNoether性は `lem:elliptic-bisection-noetherian` で別に証明する。二曲線の積上の二重切断環について、右イデアルの評価像を高い象限で安定させ、上の一様消滅で有限生成を得る。残る有限幅の行・列は各因子のNoether性で扱う。評価元の係数加群のflat性やイデアルのsaturationは仮定せず、導来projection formulaと両包含を使う。二つの普遍的に正則な中心元とfiltered PBWを経て、全n・全noetherian基底変更で `A^op⊗A` と `B^op⊗B` のNoether性を得る（`cor:elliptic-product-noetherian`）。片側の強Noether性だけから非可換tensor積のNoether性を推論しない。
- 上記のσ-ampleness/Noether原理や体上のSklyanin表示自体は既知である。本稿の可換極限を含む有限な開近傍、任意基底変更、二重切断環、中央多項式係数、全nの相対tailsへの適用という組合せの優先権は未確認。曲線表示は活性最高次商のものであり、n次元tails全体が曲線のcoherent圏になるとは主張しない。

次数1ではStephensonの §2.1、式(2.1.9)、§3の次数1線束の幾何を使う。本稿では有限被覆上で二重対角線を解消し、無限遠の切断P・QとσQ=Pから `L=O(P)` を構成する。次数1〜4の全射性と次数2線束の評価列から全次数生成、一般点のσ⁶≠idと階数比較から中心商の相対THCR同定を得る。強Noether性は上記Keelerの定理から、積は偶数Veroneseと次数2の二重切断環から得る。悪い閉集合の固有像・有限像による縮小と、有限忠実平坦降下を明記した。Stephensonの体上の幾何を相対定理と読み替えただけではない。

### 5.5. 滑らかな有限開近傍とatlasの接空間障害

`finite_smoothness.tex` の `thm:finite-family-smooth-open` は、次数1・2の分離型族と一般楕円型族の全n≥2を扱う。各構成族の中で全斉次式が滑らかな可換del Pezzo模型を与える任意の点について、smooth properな有限型Zariski開近傍を証明する。楕円型では各古典楕円型topの有限開近傍が前提であり、任意の非零hや任意のlower係数でsmoothであるとは主張しない。

証明は、Noetherな二重次数付き積上の平坦な対角、その有限部分解消、相対Serre双対による逆向きのHom複体のperfect性を用いる。特殊ファイバーの `HH¹(X)=0` と `X×X` の有限ホモロジー次元から得る射を、有限自由複体の消去によって開近傍へ持ち上げ、対角をcompact対象の直和因子にする。properなdg代数一般についてsmoothnessの開性を引用したものではない。反標準列の豊富性の開条件と交わらせると、任意の許されるnoetherian基底変更で非可換del Pezzo条件が成り立つ。幾何学的ファイバーのcoherent圏のホモロジー次元はnで、その有界導来圏はcompact圏と一致する（`cor:finite-family-ncdp-open`）。非正則基底上の全有界coherent導来圏までこの一致を拡張しない。

一方、`prop:one-parameter-atlas-obstruction` は、現在の表示族のPoisson成分のKodaira–Spencer階数がh=0で高々1であることを示す。全変形のPoisson接空間次元は次数1でn、次数2でbinom(n+1,2)なので、全n≥2で接写像が不足する。係数や座標枠を動かしても共通因子hのため一次のPoisson方向は増えず、これらの族は可換点で形式的にsmoothではない。半古典方向を稠密に実現することとsmooth atlasを与えることを区別する。

### 5.6. 全方向を含む同時ambient族

Mori–Ueyama, *The classification of 3-dimensional noetherian cubic Calabi–Yau algebras*, J. Pure Appl. Algebra 223 (2019), no.5, 1946–1965、DOI 10.1016/j.jpaa.2018.08.009。[arXiv:1606.00183v3](https://arxiv.org/abs/1606.00183v3) のTheorem 3.4を一次資料で確認した。二生成元四次cyclic tensorの二つの一次端点微分が独立で、二階端点微分の四成分の共通零点がP¹×P¹にないことが3-CYの必要十分条件である。この有限次元の条件を、properな射の閉像の補集合として使う。曲線の滑らかさやbinary quarticの判別式非零は要求しない。

本稿はこの判定から、四次式の偏極と交代形式Pを縮約する作用素 `T_(U,P)(ab)=Ũ(P♭a,P♭b,−,−)` による明示的十分条件 `g₂=det(1+4T)≠0` を得る。g₂(U,0)=1なので、全四次係数の零切断を含む有限主開である。活性binary quarticでは `g₂=1−16Ih⁴+128Jh⁶` となる。次数1ではStephensonの例外点と分離型Ore拡大によりΔ条件をambientから除き、`(1+A₄(D))(5+A₄(D))≠0` を得る。これらはambientの正則性の十分条件であり、相対楕円曲線の構成には別に楕円判別式が必要である。両次数とも全体ファイバーのHilbert関数を固定してから、被約普遍係数環の関係行列で任意基底変更の平坦性を証明する。一次中心商まで構成したが、全有限基底での中心元・tails・atlasは未解決である。この同時構成の新規性・先行する全方向量子化との一致は未確認。

## 6. 公表前に残る研究・文献上の課題

優先順位の高い比較・調査は次の五点である。

1. **同時ambientの中心元。** 両次数の有限型ambient族と全一次中心商は得た。同じ代数上の全高次の中心方程式を、既存の形式中心持上げ・filtered楕円代数の結果と比較し、零切断を含む有限解を構成する。
2. **全方向の相対tailsと局所完全性。** 一方向族で得た強/積Noether性・Serre・smoothnessを、同時中心商の構成後に拡張する。全Artin形式環と全一次接方向の一致だけでatlasを結論しない。
3. **滑らかな開集合の明示。** 得られた有限部分対角解消とHom複体から、具体的な係数の非消滅条件を計算する。開近傍の存在証明と、その判別式の明示は異なる状態である。
4. **全O同値と大域モジュライ。** 有限表示族から一般nc点の全同値の商、全モジュライの有限型atlas、可換locusに接しない成分へ進む。Toën–Vaquiéの固定dg圏の対象モジュライを、可変な全O-marked圏のモジュライと同一視しない。
5. **相対楕円構成と新規性。** 解消point curve、相対THCR、二重切断環による積Noether性、smoothnessの有限開近傍を、既存の楕円代数・filtered変形・変形圏の相対理論に比較する。中心増大層を含む適用範囲と、各主張の優先権を確認する。

一般nでの全Abel形式群oid、nc多様体条件のArtin持上げ、形式粗商、具体量子化の完全性、任意指数Veronese復元、有限型族のCasimir・普遍中心・相対双対、一般楕円型topの相対曲線表示・積Noether性、およびsmooth properな有限開近傍という組合せについて、包括的な優先権調査は未了。変形・compact持上げ・formality・Sklyanin中心元・σ-amplenessの一般結果は既知と明記する。非可換del Pezzo曲面の各定義、AS Z-代数、marked quiver、非可換吹上げとの比較も継続する。講演概要にある未公表の一般次数の主張は確立済み定理として引用しない。
