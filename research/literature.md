# 文献・依存関係・新規性の範囲

2026-11-21（JST） / v0.21。完全な書誌は [references.bib](../references.bib)。以下は使用する一次資料の具体的な箇所、現行論文での適用とその限界を示す。外部論文のPDFは収録しない。

## 1. 他研究からの数学的入力

### poisson-del-pezzo

確認した正本はmain commit **4834ea4f3e13bff4d6c5793cec9b169d8f1ad56f**、主原稿v1.4。

[固定した主原稿](https://github.com/uedakazushi/poisson-del-pezzo/blob/4834ea4f3e13bff4d6c5793cec9b169d8f1ad56f/papers/poisson-del-pezzo.tex)

- 定理7.3、label `thm:relative-poisson`：任意基底変更と両立する二重ベクトル束とJacobi錐。次数1はA^n、次数2はGr(2,n+1)のPlücker錐。商で割る前のambient Jacobi/Casimir公式を含む。
- 定理8.8、label `thm:poisson-moduli`：正規形の係数開集合と有効座標変換群による全族の商表示。
- 定理9.2、label `thm:affine-coarse-moduli`：古典del PezzoおよびPoissonモジュライの有限対角・分離的アフィン粗空間。`coarse.tex` を上記固定commitで確認。判別式主開のaffine性、還元群と全有限stabilizer、Luna I §4 p.90が入力。本研究では対称化した中心方程式のshadowに適用し、全非可換Isomの閉埋込みから有限対角を得る。
- 定理9.6、label `thm:coarse-flat-locus`：Poisson粗空間のCohen–Macaulay性と、粗忘却射の平坦locusが古典粗空間のsmooth locusの逆像に等しいこと。上記commitの `papers/sections/coarse.tex` の証明を確認。Luna slice上の有限群不変環と被約ファイバー `C_X/Aut(X)`、fiber内の滑らかな稠密開、正則性の忠実平坦降下を用いる。本研究ではΘ̄のétale局所環が忠実平坦であることを介して移す。
- 補題10.1 `lemma:cone-lci`、定理10.3 `thm:poisson-resolution`、命題10.4 `prop:plucker-terminal`：上記commitの `papers/sections/singularities.tex` を確認。Plücker錐のlci判定、相対零切断blow-upのGrassmann線束表示、Gorenstein terminal性とdiscrepancy n。Θがétaleで零切断の逆像をschemeとして保つことから本研究へ移す。粗空間のterminal性やその解消には適用しない。
- 補題8.7：全ての対象XでH⁰(T_X)=0。注意8.5、label `rem:deck-action`：被覆対合はPoissonパラメータに−1で作用。命題9.4、label `prop:generic-deck-stabilizer`：両次数・全n≥2でAut(X)=μ₂となる稠密開。形式群oidと一般点の粗符号商の入力。命題9.4の非空性・開性の証明を確認した。次数2の普遍接線因子は滑らかな四次係数空間へ全射するため、その一般点にもこの稠密開が適用できる。非零Pは被覆対合に固定されず、因子の一般点のPoisson安定化群は自明となる。これが粗空間の接線判別因子Hで `ord_H Δ=1` を保つための入力である。
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
| De Deken–Lowen, *Abelian and derived deformations in the presence of Z-generating geometric helices*, JNCG 5 (2011), 477–505, DOI 10.4171/JNCG/83 | [出版版](https://ems.press/content/serial-article-files/30497)、Proposition 4.4 (p.495)、Theorem 4.5、Proposition 4.6 (p.496) | Proposition 4.4は平坦な線型Z-代数変形bからのAbel変形がQmod(b)であることを同定する。Theorem 4.5はm≤nの有向Ext¹,²消滅の下で逆方向との同値を与える。Proposition 4.6は局所有限・有限生成・noetherian性等を冪零変形へ持ち上げる。全ての正負捻りの高次Ext消滅は不要 |
| Lowen–Van den Bergh, *Deformation theory of abelian categories*, Trans. AMS 358 (2006), 5441–5483, DOI 10.1090/S0002-9947-06-03871-2 | [arXiv:math/0405226](https://arxiv.org/pdf/math/0405226)、取得したv1のPropositions 3.4, 3.7 | injective/coflatによる圏の平坦性、Hom-flatな線型圏の加群圏。出版版とは番号が異なる。本文のAbel平坦性はnoetherian基底に限定 |
| 同上の[出版版](https://win.uantwerpen.be/~wlowen/pdf%20papers/TAMS-DeformationTheory.pdf) | Definition 8.2、Theorem 8.17、Appendix BのPropositions B.1, B.3 | 射が自然同型類である群oid擬関手の比較。B.1/B.3は対象集合を固定した代表と自己同値のstrictな代表に使用。B.4の同型類全単射を群oid同値と読み替えない |
| Kontsevich, *Deformation quantization of Poisson manifolds*, LMP 66 (2003), 157–216, DOI 10.1023/B:MATH.0000027508.00421.bf | [著者最終稿](https://www.ihes.fr/~maxim/TEXTS/DefQuant_final.pdf)、§§4.6.2,6,8、§7のP3 | graph formality、twisted mapによる中心元、GL同変性。一般の非線型座標変換への厳密同変性ではない |

これらの比較・量子化原理は既知である。本研究では、次数1・2・一般nの相対錐への適用、monic商の任意基底での分裂、O-markedな圏の同変降下を示す。さらに初commutatorと完備局所環の自己写像を使い、構成した特定の量子化そのものが全Artin同型類に自然な全単射を与えることを証明した。`simultaneous_formal_comparison.tex` では、全方向の有限表示中心商族そのものにもこの比較を行う。可換sliceを選んだ各可換点で、その同じ有限族のArtin基底変更が全framed Abel変形群oidを表す。詳細と有限基底全体のtailsとの区別は§5.8に記す。既知の比較の逆と正確に同じ形式座標を持つことは、この結論に不要である。

接空間と微小自己同値のHochschildによる説明には、Lowen–Van den Bergh, *Hochschild cohomology of abelian categories and ringed spaces*, Adv. Math. 198 (2005), 172–221, DOI 10.1016/j.aim.2004.11.010 の [著者稿](https://cantate.be/site/hochschild_ab.pdf)、Theorems 3.1, 4.1.3, 6.1, 6.6、Corollaries 6.8・7.7.2・7.8.2と、Yekutieli, *The Continuous Hochschild Cochain Complex of a Scheme*, Canad. J. Math. 54 (2002), 1319–1337, DOI 10.4153/CJM-2002-051-8 の [修正版出版論文](https://www.math.bgu.ac.il/~amyekut/publications/diagonal/cjm.pdf)、Corollary 0.6を確認した。injective線型圏・Abel圏・幾何的Hochschild cohomologyの比較を用いる。HKRの積や括弧との両立は使わない。

## 3. 反標準認識と曲面の先行研究

- Mori–Ueyama, *A categorical characterization of quantum projective spaces*, [arXiv:1708.00167v4](https://arxiv.org/abs/1708.00167v4)。Definitions 2.1(5), 2.5, 3.4、Theorem 2.6(2)、Remark 3.5、§1.2を確認。豊富対からのsection環復元とcanonical bimoduleを使う。AS-GorensteinのパラメータだけではNakayama捻りを消せない。
- [Stacks Project, Tag 0FY3, Lemma 57.3.5](https://stacks.math.columbia.edu/tag/0FY3)：双対構造を持つSerre関手のYoneda一意性。これ自体はAbel同値の全認識を述べる定理ではない。
- Hong–Xu, *Poisson cohomology of del Pezzo surfaces*, J. Algebra 336 (2011), 378–390、[arXiv:1001.1082v2](https://arxiv.org/abs/1001.1082v2)、Theorem 3.9。5≤r≤8点の吹上げでdim H²_π=r+2、高次は消滅。次数1・2の曲面の10・9という接空間次元を新規結果と扱わない。
- Etingof–Ginzburg, *Noncommutative del Pezzo surfaces and Calabi–Yau algebras*, JEMS 12 (2010), 1371–1416、DOI 10.4171/JEMS/235、[出版版](https://ems.press/content/serial-article-files/31746)。三変数potentialと中心商によるfiltered量子化・generic半普遍性は先行結果。**Theorem 3.3.2は、正の生成重み `(a,b,c)`、`d=a+b+c`、斉次CY potential `Φ_d`を仮定すれば、任意のlower potential `Φ_<d`に適用できる。** (i)はCY性とHilbert級数、(ii)はfiltration次数d以下の非定数中心元の存在を与える。Proposition 7.3.1(ii)は同じ固定CY topに対するPBW同型 `gr A(Φ_d+Φ_<d)≅A(Φ_d)` を与える。一方、Definition 3.4.3、Lemma 7.1.5、Theorems 3.4.4–3.4.5のgeneric条件は可算個の開条件を伴い、そのまま一つの有限型開集合の主張に置き換えない。本稿の有限型族では、次数2の三次type-A代数、次数1のStephenson代数の具体的な有限開条件からtopのCY性を先に確認し、上の全lowerの定理、被約な普遍係数環での特殊化、活性次数6以下/9以下の中心方程式を組み合わせる。低次係数に依存しない分母と任意中央係数への基底変更は本稿の証明である。Proposition 8.1.1(i)の形式中心持上げ自体は孤立特異点を仮定しない。
- Rains, *Filtered deformations of elliptic algebras*, [arXiv:2107.13540v2](https://arxiv.org/abs/2107.13540v2)。Introに加え、Propositions 2.2–2.3、Theorems 2.12–2.13、Example 3.1を確認。固定された有限表示graded代数のfiltered変形の代数性と、楕円THCRのfiltered表示を扱う。Theorem 2.13の中心持上げにはtorsion translationの仮定があり、未確認のtop全体や本稿の全方向ambientの中心へ無条件に適用しない。全n・全O-markedモジュライの分類としては使わない。
- Abdelgadir–Okawa–Ueda, *Compact moduli of marked noncommutative cubic surfaces*, [arXiv:2404.00175](https://arxiv.org/abs/2404.00175)。Introとquiver markingを確認。例外集合に対応するquiver関係のGITモジュライであり、本研究のOのみを残す同値関係とは異なる。
- Okawa–Ueda, *AS-regular algebras from acyclic spherical helices*, [arXiv:2007.07620](https://arxiv.org/abs/2007.07620)。球面helixからの構成を比較した。一般次元での表示を検討する基礎であり、本稿で全変形のAS包絡存在を結論する根拠には用いていない。
- Okawa–Ueda, *Marked Artin–Schelter surfaces of del Pezzo types*, [arXiv:2508.04986v1](https://arxiv.org/abs/2508.04986v1) (2025)。Definitions 1.1・6.1、Theorem 6.4とその直前の構成・証明を一次本文で確認。markingはvery strong helixを含み、曲面のquiver potentialのモジュライと、種数1曲線・次数3の二線束・次数1の線束の組のモジュライを双有理に比較する。本稿のOのみを標識する全Abel同値、任意nの中心商族、指定Poisson shadowの次数5・4とS₅・S₄モノドロミーとは定義と射が異なる。helixを忘れる射と幾何的データの対応は未比較であり、この既存双有理性を本稿のδの値へ読み替えない。

Plücker座標環の正規性・Cohen–Macaulay性にはSvanes (1973) とDe Concini–Procesi (1981) の標準単項式理論を用いる。具体的書誌と一次資料URLはBibTeXに保持する。

### Kuznetsov成分：曲面の変形、局所幾何化、古典Torelli

2026-11-20〜21に以下の一次本文と適用条件を確認した。主証明はkuznetsov_surface.tex、kuznetsov_relative.tex、kuznetsov_shadow_obstruction.tex、kuznetsov_cyclic_fibres.tex、kuznetsov_intrinsic_period.tex。Ku固定の全Artin正規形はkuznetsov_gluing_normal_form.tex、一般一節点での延長判定はkuznetsov_nodal_extension.tex、有限Poisson群の周期による検出限界はkuznetsov_poisson_symmetry_obstruction.texに記す。候補の条件付き分類と零方向はkuznetsov_hessian_rigidity.tex、kuznetsov_hessian_counterexample.tex、kuznetsov_degree_one_candidate_geometry.tex。

| 一次資料と参照箇所 | この研究で使う内容と限界 |
|---|---|
| Kuznetsov, *Hochschild homology and semiorthogonal decompositions*, [arXiv:0904.4330v1](https://arxiv.org/abs/0904.4330), Proposition 8.1・Theorem 8.5、PDF p.23 | Oの右直交のHHは最高polyvectorを除く。証明のAt(O)=0から制限写像そのものを同定する。未確認の刊行先を付けない。Theorem 8.9の三様体の数値と曲面の計算は分ける |
| Orlov, *Projective bundles, monoidal transformations, and derived categories of coherent sheaves*, Izv. Math. 41 (1993), 133–141, DOI 10.1070/IM1993v041n01ABEH002182、[著者掲載PDF](https://homepage.mi-ras.ru/~orlov/papers/1992_Izv_Math.pdf)、§4 | 点blow-upの例外対象O_E(−1)と平面の引戻しによるSOD。J_i[−1]とO(−2L),O(−L)のHom・積は本稿で直接計算。Lは平面の直線で、基本偏極Hと区別する |
| Auroux–Katzarkov–Orlov, *Mirror symmetry for Del Pezzo surfaces: Vanishing cycles and coherent sheaves*, Invent. Math. 166(3) (2006), 537–582, DOI 10.1007/s00222-006-0003-4、[arXiv:math/0506166v1](https://arxiv.org/abs/math/0506166v1)・[著者PDF](https://homepage.mi-ras.ru/~orlov/papers/hmsratl.pdf)、Theorem 2.5、§§2.1・2.3、Construction 2.9、Remark 2.10 | 40頁の著者稿のp.7、pp.11–14を確認。三頂点の積とrank 2条件を持つtailによる有限代数模型を使う。pp.13–14の反標準heartの存在は条件付きであり、任意の有限代数からの無条件のAbel復元として引用しない |
| Toën–Vaquié, *Moduli of objects in dg-categories*, Ann. Sci. ENS 40 (2007), 387–444, [著者稿](https://www.math.univ-toulouse.fr/~btoen/ttt.pdf), Theorem 3.6、Corollaries 3.15・3.17・3.21–3.24、Lemma 3.25 | smooth proper dg圏のperfect対象のモジュライ、接複体RHom(E,E)[1]、simple対象のGm-gerbeと同型類の代数空間。同値が開条件であることは二圏の単位・余単位coneを使って記述する。全dg圏のモジュライの代数性の定理ではない |
| Lowen, *Obstruction theory for objects in abelian and derived categories*, Comm. Algebra 33 (2005), 3195–3223, [math/0407019v1](https://arxiv.org/abs/math/0407019), Theorem B・Theorem 6.10 | Abel変形での導来対象の持上げ。有限coflat次元の定式化と有限Tor次元の双対を区別し、perfect対象に用いる。自己Ext²の障害とExt¹のtorsor |
| Keller–Lowen, *On Hochschild cohomology and Morita deformations*, IMRN 2009(17), 3221–3235, DOI [10.1093/imrn/rnp050](https://doi.org/10.1093/imrn/rnp050), [著者掲載本文](https://win.uantwerpen.be/~wlowen/pdf%20papers/KellerLowenHochDefo.pdf) | 一般のHH²は非曲率Morita変形だけでは捉えられないという制約。今回はtilting対象を実際に持ち上げ、通常代数へ還元する |
| Perry, *Noncommutative homological projective duality*, Adv. Math. 350 (2019), 877–972, DOI 10.1016/j.aim.2019.04.052, [1804.00132v2](https://arxiv.org/abs/1804.00132), Lemmas 4.10・4.15(4) | 線形圏のsmooth proper性の基底変更と許容半直交成分への保存。全対象の有限Extだけでsmoothnessを結論していない |
| Lin–Rampazzo–Zhang, *Categorical reconstruction of del Pezzo surfaces: Hochschild–Serre algebras and spinor modifications*, [2609.10344v1](https://arxiv.org/abs/2609.10344), 2026-09-09、Theorem 1.2・§2.3・Propositions 3.4–3.5・Proposition 4.1・Theorem 4.2 | 次数≤4の滑らかな複素古典del Pezzo曲面はenhanced O^perpから復元される。古典曲面の一意性の入力であり、非可換族の幾何化の存在は別に証明。可換weighted MFのHS積は一般計算の目標。§4のSerre関手によるGeiser/Bertini認識と同変分岐周期も一次本文で確認。相対化・Artin復元と形式的局所Torelliへの適用は本稿で記述 |
| Keller, *On differential graded categories*, ICM Madrid 2006, Vol. II, 151–190, [刊行本文](https://www.imj-prg.fr/wp-content/uploads/2020/prix/keller2006.pdf), §5.1、Theorem 5.2(a) | mixed complexのMorita不変性・加法性。係数基底Rに対する相対HPに適用し、例外成分の奇数部分を除く。絶対HP(-/C)と混同しない |
| Elagin, *On equivariant triangulated categories*, [arXiv:1403.7027v2](https://arxiv.org/abs/1403.7027v2), Theorem 7.1 | 有限群位数が可逆なときのAbel圏と導来圏の同変化の比較。coherentな作用とdg模型を先に構成する |
| Baranovsky, *Orbifold Cohomology as Periodic Cyclic Homology*, [arXiv:math/0206256v2](https://arxiv.org/abs/math/0206256v2) (2002)、Theorem 1 (p.2)、Proposition 4 (p.5) | 体上の有限群同変mixed complexを固定点成分の直和で計算する既知の公式と引戻し自然性。番号は2002年6月30日のv2に固定し、出版版の番号と混同しない。相対基底方向の接続までこの定理単独から結論しない |
| Tabuada–Van den Bergh, *Additive invariants of orbifolds*, Geom. Topol. 22(5) (2018), 3003–3048, DOI 10.2140/gt.2018.22.3003、[刊行PDF](https://msp.org/gt/2018/22-5/gt-v22-n5-p12-s.pdf)、Theorem 1.1、Corollary 1.5(ii)、Example 1.11、式(1.12)、pp.3005–3007 | 引戻しと指標による固定点比較をmixed complexに適用し、係数変更との両立を確認する。本稿の相対化では同じtrace写像を構成し、特殊ファイバーの同型とperfectなconeへの導来Nakayamaを使う |
| Sheridan, *Formulae in noncommutative Hodge theory*, J. Homotopy Relat. Struct. 15 (2020), 249–299, DOI 10.1007/s40062-019-00251-2, [著者掲載PDF](https://www.pure.ed.ac.uk/ws/portalfiles/portal/144440775/1510.03795.pdf), Theorem 3.32、Corollary 4.13 | cyclic homologyにおけるMorita不変性とGetzler接続の自然性。接続とHodge filtrationの両方を残し、特殊ファイバー恒等という標識を利用する |
| Tu, *A remark on the B-model Comparison of Hodge structures*, [arXiv:2404.13805v1](https://arxiv.org/html/2404.13805v1), Theorem 0.1(3)、Lemma 0.1 | modified Todd類の平方根で補正したHKRによる、幾何Gauss–ManinとGetzler接続の族での比較。曲線のH¹上に非自明なTodd補正は残らない。有限Poisson群の節では滑らかな代数族の解析化に適用してから形式完成し、Artin商単独の水平自明化は使わない |
| Fisher, *On binary quartics and the Cassels–Tate pairing*, Res. Number Theory 8, 74 (2022), [DOI 10.1007/s40993-022-00376-z](https://link.springer.com/article/10.1007/s40993-022-00376-z), §2、(1)–(2) | 四次式の不変量I,JとJacobianのWeierstrass式。marked二次類の同定は不変量だけに依存せず、恒等へ還元するMöbius変換も直接記述する |
| Landesman, *The infinitesimal Torelli problem*, [arXiv:1911.02187v1](https://arxiv.org/abs/1911.02187v1), Theorem4.3, pp.5–6 | 曲線の周期写像の微分がSym²H⁰K→H⁰K²の双対である既知の公式の詳しい証明。本稿は分岐曲線の乗法を直接計算し、全古典点のKu変形の形式的閉埋込みへ適用 |
| Dimca–Sticlaru, *Hessian ideals of a homogeneous polynomial and generalized Tjurina algebras*, Documenta Math.20 (2015),689–705, [本文](https://emis.de/ft/9451), (1.2), Remark3.3(iii), DOI10.4171/DM/502 | Hessian小行列式をJacobian idealに加えたHessian algebra。d2候補の階数計算の既存の枠組み。Kuの二次差との同定を述べた文献ではない |
| Gurevich–Howe, *The Pieri Rule for GLn over Finite Fields*, [arXiv:2105.11520](https://arxiv.org/abs/2105.11520), §3.2 Proposition3.2.1 | 複素GLnの古典Pieri則を一次本文で確認。d2の一意な共通Schur因子とd1の重複度に用いる。有限体の主定理を用いるのではない |
| Poonen–Stoll, *The valuation of the discriminant of a hypersurface*, [arXiv:2510.14434v1](https://arxiv.org/abs/2510.14434v1) (2025)、Theorem 1.1 (p.1)、§2 (p.2)、Propositions 5.1–5.2 (pp.5–6) | 判別式の既約性、一般特異超曲面の一節点性、全空間が正則な一節点平滑化で判別式付値が1となることを使う。本稿の普遍Jacobian加群の反射性やカテゴリー的二次差の延長は同論文の結論ではない。番号はv1に固定する。著者の2026年6月30日版では該当命題が5.2–5.3に移動している |

基本公式、blow-up、tilting変形、perfect対象のモジュライ、同変化、巡回ホモロジーと接続、古典Torelliは先行研究の結果である。本稿はそれらを全O同値を含む具体的非可換族に適用する。中央巡回被覆の分解はstratifying idealを直接構成し、非可換・weightedの場合へ他論文の定理を無条件に拡張していない。巡回族のHess/8、Fermat全tensor、一般ファイバーの分離は本稿の具体計算と既存原理の組合せであり、包括的な優先権確認は未了である。

LRZの低次数HS積は**可換**重み付き多項式環上のgraded matrix factorizationsとdiagonalに依存する。非可換AS環上の積やPBW完全対称化との乗法互換性は同論文に含まれない。今回の非保存性の証明は、その未確認の乗法互換性を使わず、標識付き同変周期と楕円曲線の局所Torelliで行う。非可換HS積、一般の全方向二次公式、三様体の未完了候補は研究ノートに保持する。

**Ku固定のArtin正規形とAKOの範囲。** 三頂点とtailの有限代数はAKOの既知の模型である。本稿の [kuznetsov_gluing_normal_form.tex](../papers/sections/kuznetsov_gluing_normal_form.tex) は、可換交代積の近傍でU・Wの基底を変更し、積を `C(v)+Hess(P)(v)` に一意に規格化する。行列式条件は `Ψ(P)(p_i)=0`、`Ψ(P)=P+det Hess(P)/6` であり、Ψの形式逆によって三次形式の線型空間 `L_p=H⁰(X,−K_X)` と同一視される。持ち上げた強例外列・固定corner・Abel変形のHochschild比較・形式逆写像定理を用い、これがKuを固定する**全ての通常Artin Abel変形の標識付き同値類**を表すことを証明した。次元は次数1で2、次数2で3である。

AKOの条件付きheartの議論からこの全称性を引用してはいない。本稿では既に存在するAbel変形の形式ファイバーから積への写像を構成し、その形式同型の逆によって全Artin商上の存在を得る。有限パラメータ全体でのAbel heart、未切断の高次群oid、大域的な粗ファイバー表示はこの結論に含まない。gluing座標から規格化した中心超曲面表示への積・係数変換は未計算であり、Ψの式を実際のshadowやδ₂の式と同一視しない。

**一般一節点での延長判定。** [kuznetsov_nodal_extension.tex](../papers/sections/kuznetsov_nodal_extension.tex) では、普遍四次式の無限小安定化群のJordan型を調べ、Jacobian加群Mの非局所自由locusの余次元が少なくとも6であることを示す。長さ1の自由分解と深さ評価から無捩れ性・S₂を得て、反射的加群の高さ1交叉表示（[Stacks Tag 0AVB](https://stacks.math.columbia.edu/tag/0AVB)）を適用する。その結果、判別式を反転したMの切断の多項式延長は、既約判別式の一般点における一つのDVR格子への所属と同値になる。Poonen–Stollの入力は、その点を一節点として表し、横断平滑化の判別式付値を1と同定する部分である。

本稿の単純極補正 `C(F)^4 I₃(F)[Q]/Δ(F)` は巡回型locusで零となり、一般判別式点では零にならない。その非消滅と普遍加群の反射性は本文の証明および厳密な有限計算による。実際のδ₂がこのDVR格子に極を持たなければ全係数Hess/8が従うが、極の上界・消滅をGauss–Manin接続の正則特異性から導いたとは主張しない。

**有限Poisson群の奇数周期による検出限界。** [kuznetsov_poisson_symmetry_obstruction.tex](../papers/sections/kuznetsov_poisson_symmetry_obstruction.tex) は、非零Poisson構造の零因子Eが滑らかな楕円曲線である場合に限る。固定した有限群 `G⊂Aut(X,π)` に対し、非単位元の固定曲線はEに含まれ、`K=ker(G→Aut(E))` は中心巡回群、商は `E[d]` の部分群となる。滑らかな代数曲線上の射影族の形式完成について、上記固定点公式を相対trace・導来Nakayama・Sheridan/Tuの接続比較で相対化する。EとG作用を標識付きで固定すれば、Kuの奇数相対周期は `H¹_dR(E)^(⊕(|K|−1))` という定数のfiltered flat moduleになる。

次数1では `R_D=4A D²A−3(DA)²=(ℓ_D²/3) det Hess(A)` に沿う古典族 `F+tR_D=0` が、元の全ての有限Poisson群について同じ幾何作用とEを保つ。この族は各群の奇数同変周期には見えないが、`[R_D]≠0` なら内在的Bertini周期には局所Torelliにより見える。Bertini作用はPoisson方向に−1で作用し、ここで許した群には属さない。この結論は同変圏自体・全ての高次近傍・実際のNC二次差の不変性を述べない。

次数2のHessian共変候補の非消滅には、Eisenbud–Ulrich, *Duality and socle generators for residual intersections*, J. Reine Angew. Math. 756 (2019), 183–226, Appendix A, Theorem A.5（[著者稿](https://www.math.purdue.edu/~bulrich/papers/Duality-and-Socle-180119.pdf) Theorem 8.5）のArtin完全交叉のJacobian socle定理を使う。これは候補の性質であり、実際のδ₂との一般同定ではない。

**本稿の範囲と未解決点。** 二次有限決定性は少数変数の偶写像とArtin完全交叉の初等的な帰結として証明し、既存のδ₂へ適用する。内在的対合、曲線の周期微分、固定点公式、反射的加群の一般原理は上記の既知結果である。d2の多項式延長を仮定した剛性と一般節点DVR判定、単純極の曖昧さ、d1のH₁+sR₁分類と滑らかな零方向、有限Poisson群による検出限界、Ku固定の全Artin有限行列正規形は本文で証明する。実際のδ₂の全係数公式、一般節点での極消滅、d1の定数sの値、gluing模型からshadowへの係数変換、これらの組合せの包括的な優先権は未確認である。

### 逆被覆の分岐とモノドロミー

- Allcock–Hall, *Monodromy Groups of Hurwitz-type Problems*, [arXiv:0803.0237v1](https://arxiv.org/abs/0803.0237v1) (2008)。IntroductionのPDF pp.1,3を一次本文で確認した。単純分岐の局所モノドロミーは互換であり、連結な単純分岐次数4被覆のGalois閉包はS₄となる。この原理自体は古典的である。同論文の主結果はHurwitz空間自体のモノドロミーであり、本稿の一つの比較被覆の四分枝への作用とは異なる。刊行版の巻頁は今回確認せず、参照したarXiv版を引用する。
- [Stacks Tag 0C1B](https://stacks.math.columbia.edu/tag/0C1B)、Section 53.12の標数0のRiemann–Hurwitz公式を一次本文で確認した。次数2のB=1切断は種数1・次数4なので総分岐次数8であり、八つの単純分岐を検出すると追加の分岐がないと分かる。

本稿固有の計算は、両逆方程式のSylvester判別式、法11・19のBézout証明書、全lowerと全同値商を経たS₄・S₅、次数2のnormalizer符号捩れである。次数1の素数次数と互換による対称群判定、Galois対応、根号可解性の一般原理は既知の体論であり、原稿に必要な短い証明を記載する。これらの具体的比較射についての包括的な新規性調査は未完了。

### 有限族の全同値とVeronese復元

- Aitzhanova–Makar-Limanov–Umirbaev, *Automorphisms of Veronese subalgebras of polynomial algebras and free Poisson algebras*, J. Algebra Appl. **24** (2025), no.3, 2550095, DOI [10.1142/S0219498825500951](https://doi.org/10.1142/S0219498825500951)。[arXiv:2307.07823v1](https://arxiv.org/abs/2307.07823v1) §5、Corollaries 4–5、PDF p.11の本文を確認。二変数以上の多項式環について、全d乗根を取れる体上でVeroneseの全自己同型がd-graded自己同型へ持ち上がり、核がd乗根スカラーとなる。d-gradedは同論文のZ/d次数付けであり、通常のZ次数保存とは区別する。本稿の中央多項式部分の持上げと関連する既知結果である。本稿の `thm:ncdp-veronese-lift` は相対基底上の中央多項式環を内在的に認識し、二つの中央局所化から非可換Bを復元する。既知の多項式環の結論自体を新規としない。
- [Stacks Tag 06PH](https://stacks.math.columbia.edu/tag/06PH)、Lemma 80.11.7を確認。flat locally finite presentation群の自由作用には代数空間としてのfppf商がある。本稿の `lem:graded-isom-affine-quotient` は、次数1の同型行列とその逆から座標環の強Z次数付けを直接作り、商がさらにaffine有限表示であることを証明する。
- [Stacks Tag 02G8](https://stacks.math.columbia.edu/tag/02G8)、Lemma 29.36.12と [Tag 02GF](https://stacks.math.columbia.edu/tag/02GF)、Lemma 29.36.14を確認。有限型の射のunramified性をファイバーまたは余接加群で判定できる。`cor:finite-equivalence-unramified` では単位切断上の余接加群の支持を除き、群の平行移動から全同値スキームへ適用する。有限・flat・étaleな射やsmooth atlasとは同一視しない。

`thm:finite-anticanonical-isom` は既存の相対Serre・反標準豊富性を、構成した有限型Vの全基底変更上で使う。Veronese環の有限斉次表示、具体的なVeronese/tensor関手によるtails同値、有限高切断によるfppf降下は本文で証明する。同型関手とトーラス商の一般原理自体は標準的であり、相対非可換族へのこの適用について包括的優先権は未確認である。

`thm:finite-low-center-open` は既存の `lem:classical-casimir-center` と活性PBW filtrationを用いる。全次数の中心が最小であるというgeneric条件を、一つのZariski開へ読み替えない。固定qの有限行列だけを使う。`thm:low-center-zero-neighborhood` は方向解消上のδ_q/τを使い、全smooth係数・全射影方向の例外因子で単射性を確認する。properな悪条件像を除き、零切断近傍の非零部分全体で中心条件を得る。H→Eの開性と組み合わせた `cor:zero-neighborhood-full-graded-recognition` は、零方向・冪零基底を含めて通常Bからの全同値認識を与える。

### 有限型群oid・粗モジュライ・Artinの条件

以下は一次本文を確認した一般原理であり、それ自体を本研究の新規結果とはしない。

| 一次資料 | 適用箇所と範囲 |
|---|---|
| [Stacks 07VH](https://stacks.math.columbia.edu/tag/07VH)、Lemma 15.39.6；[039M](https://stacks.math.columbia.edu/tag/039M)、Lemma 41.11.3 | Noether有限型射の形式的smoothness、完成局所環によるétale判定。全Artin比較からsource完成を計算して実際のsmoothnessへ移す |
| [Stacks 052A](https://stacks.math.columbia.edu/tag/052A)、Proposition 29.28.1；[01V8](https://stacks.math.columbia.edu/tag/01V8)、Lemma 29.35.3 | generic flatnessとflat・有限表示・smooth fiberの判定。単位のfiberを群oid平行移動で全矢へ移す前に全sourceをflatにする。開集合が零切断を含むとはしない |
| [Stacks 06FI](https://stacks.math.columbia.edu/tag/06FI)、Theorem 97.17.2；[04YW](https://stacks.math.columbia.edu/tag/04YW) | flat有限表示群oidの商の代数性とunramified diagonalによるDM性。本稿はsmoothなfull群oidを先に構成する |
| [Stacks 0DUT](https://stacks.math.columbia.edu/tag/0DUT)、Theorem 106.13.9；[0DUW](https://stacks.math.columbia.edu/tag/0DUW)、Lemma 106.14.1 | finite inertiaによるKeel–Mori粗モジュライ代数空間と有限型性。各幾何安定化群が有限であるだけでは適用せず、inertia射自体の有限性を確認する。零切断近傍では古典Isomへの閉埋込みによる有限対角を使い、同Section 106.14のLemma 106.14.2から分離性を得る |
| [Stacks 06QJ](https://stacks.math.columbia.edu/tag/06QJ)、Proposition 101.28.9 | flat locally finitely presented inertiaの代数stackは代数空間上のgerbe。さらにfinite étale inertiaなら、smooth DM部分問題の粗空間もsmoothと分かる。分離性は別に必要 |
| [Stacks 02HY](https://stacks.math.columbia.edu/tag/02HY)、Lemma 37.12.2；[025G](https://stacks.math.columbia.edu/tag/025G)、Theorem 41.14.1 | Artin持上げ判定とétale monomorphismの開埋込み。HH¹剛性により通常graded矢H→Eに適用する |
| [Stacks 06PL](https://stacks.math.columbia.edu/tag/06PL)、Lemma 97.18.3 | 自明作用のclassifying stackが代数的となるには群がflat lfpであることが必要十分。V=A²、D={x=0,y≠0}、G=V⊔Dの反例に適用し、可換形式近傍だけからの大域化を否定する |
| [Stacks 07T0](https://stacks.math.columbia.edu/tag/07T0)、§98.1；[07XP](https://stacks.math.columbia.edu/tag/07XP)、§98.13、Example 98.13.2 | limit preservation、RS、effective formal objects、openness of versalityを分ける。本稿の構成族のeffectivityと、混合Isomによる可換特殊fiberを持つ任意の既存M族との同値の有効化を区別。全M自体へのArtin代数化基準を確認済みとはしない |

`thm:zero-neighborhood-full-dm` は、同じ有限型nc族の全同値スキームに、低次数のweighted-linear認識とCasimir Jacobianによる全source持上げを加えて上記の商原理を適用する。`thm:generic-full-dm-stack` はその非零開部分、`cor:generic-finite-inertia-coarse` はさらにinertiaをfinite化した開の粗空間である。一般平坦性だけから零切断を残すとはせず、方向解消上の有限中心行列とJΩ|Z=Idを使う。全点のAbel比較と任意の族の混合Isomを加えた `thm:zero-neighborhood-open-full-moduli` により、さらに零切断を保ってUを全M内の開部分と同定する。対称化中心の可換模型と古典対角を使う `thm:zero-neighborhood-finite-diagonal` が有限対角を与える。この具体的組合せの包括的優先権調査は未了である。

[Stacks 02HM](https://stacks.math.columbia.edu/tag/02HM)、Lemma 37.8.10の有限表示かつ形式étaleの判定を、非零矢の(g,source)写像に使用する。[04YK](https://stacks.math.columbia.edu/tag/04YK) §100.9の不変開と商の対応により、対象開のfull restrictionはUの開部分スタックとなる。[04YY](https://stacks.math.columbia.edu/tag/04YY)、Lemma 101.6.2の相対inertia核によるrepresentability判定と、[04XB](https://stacks.math.columbia.edu/tag/04XB) §100.3の表示上の判定は、可換点の実際の有限型étale sliceに用いる。これらも一般原理として引用し、既存の形式商から未確認の大域商を推論しない。


### 全非可換点のAbel比較・開埋込み・有限対角

- Lowen–Van den Bergh (2005) の [arXiv原本](https://arxiv.org/pdf/math/0405227)、Theorem 4.1.3、Theorem 6.1、Corollary 6.8はB∞同値としてのMorita・有界導来・Ind比較を与える。各構成ファイバーのcoherent圏の有限ホモロジー次元とcompact窓を使って適用する。Theorem 3.1とRemark 3.5の全Abel障害理論からHH²-torsorと二次Maurer–Cartan障害を使う。全Abel変形が最初からdg窓を持つと仮定しない。
- Lowen, *Hochschild cohomology, the characteristic morphism and derived deformations*, Compositio Math. **144** (2008), 1557–1580、DOI [10.1112/S0010437X08003655](https://doi.org/10.1112/S0010437X08003655)、[arXiv:0707.2602](https://arxiv.org/abs/0707.2602)。出版版と原本のTheorems 3.22・4.18、Remark 4.20を確認。実際に持ち上がる有限窓上でAbel変形類とdg変形類を合わせ、Hochschild複体の一次Bocksteinを[π,−]と同定する。任意の導来対象の無条件の持上げには使用しない。
- 次数2の二次障害の成分がPlücker関係I₂をちょうど張ることを、任意の `Sym²(V*)/L` を核とする試験拡大で証明する。これにより `rank[π,−]=binom(n−1,2)` を得る。方向解消上で `d²=τA` と書く有限行列とproperな悪条件像の除去が、全係数・全方向の一様性を与える。HH³の一定次元性やHKRの括弧両立は仮定しない。
- Yekutieli Theorem 11.1の体は実数体を含む任意Kを許すことを原文で確認した。[Stacks 0321](https://stacks.math.columbia.edu/tag/0321)、Lemma 10.158.8で係数体K/CをArtin環へ持ち上げ、有限分離拡大による有限étale降下で任意の剰余体を扱う。無限代数閉包をfppf被覆としない。
- 任意M族の反標準環にはDDL §3.3・Corollary 3.16の豊富列復元を使う。NoetherなZ-代数から環のNoether性と有限表示を本文で導く。負の軌道Homは相対Serreと有向ACMから消滅させる。
- [Stacks 04TK](https://stacks.math.columbia.edu/tag/04TK)、[04SZ](https://stacks.math.columbia.edu/tag/04SZ) により混合Isomの滑らかな群oid商が代数空間となる。局所有限表示monomorphismに全Artin持上げを適用し、[02HY](https://stacks.math.columbia.edu/tag/02HY) と代数空間版 [05W5](https://stacks.math.columbia.edu/tag/05W5) で開埋込みを得る。全Mの代数性を前提としない。
- Luna, *Slices étales*, Mémoires SMF **33** (1973), 81–105、DOI [10.24033/msmf.110](https://doi.org/10.24033/msmf.110)、[一次PDF](https://www.numdam.org/article/MSMF_1973__33__81_0.pdf)、I §4 Corollaire p.90を確認。affineスキームへの還元群作用で全stabilizer有限なら作用射有限という結果を、古典モジュライに適用する。非可換の全同値群oidへ直接還元群作用の定理を適用せず、shadowの古典Isomへ閉埋込みする。
- [Stacks 0DUA](https://stacks.math.columbia.edu/tag/0DUA) はproper inertiaの標的に対するstabilizer preserving locusの開性。[0DUS](https://stacks.math.columbia.edu/tag/0DUS) と [0DUE](https://stacks.math.columbia.edu/tag/0DUE) は粗空間のétale降下とwell-nigh affine被覆。可換点の実際の粗étale模型 `T/Aut(X)` と完成環 `R_X^Aut(X)` へ適用する。

これらの一般比較・商定理は既知である。本研究では、全方向の有限中心商について全点のAbel接空間を制御し、全同値を保った開埋込みと有限対角へ結び付ける。優先権は未確認である。


### 実際のPoisson比較とその幾何

- Anne Pichereau, *Poisson (co)homology and isolated singularities*, Journal of Algebra **299** (2006), no. 2, 747–777, DOI [10.1016/j.jalgebra.2005.10.029](https://doi.org/10.1016/j.jalgebra.2005.10.029)、[arXiv:math/0511201v2](https://arxiv.org/pdf/math/0511201v2)、Introductionの式(3)、PDF p.3を確認。三変数のJacobian Poisson括弧とCasimir超曲面への降下は既知である。本稿の新しい証明対象は、同じ中心元と全低次数交換子からの相対式、非被約係数上のPlücker恒等式、全O保存同値と基底変更に関する降下である。Pichereauの孤立特異点を仮定したPoissonコホモロジーの結論は本稿へ輸入しない。
- [Stacks 039M](https://stacks.math.columbia.edu/tag/039M) のNoether局所環と完成によるétale判定、[02GH](https://stacks.math.columbia.edu/tag/02GH) のétale locusの開性・étale射の平坦性と開写像性を、全可換点の形式比較へ適用する。
- [0DUA](https://stacks.math.columbia.edu/tag/0DUA) により零切断を保ってstabilizer preservingへ縮小し、[0DUS](https://stacks.math.columbia.edu/tag/0DUS) と [0DUE](https://stacks.math.columbia.edu/tag/0DUE) によって粗空間のCartesian正方形とétale射を得る。一般のétale射がstabilizer preservingであるとは仮定しない。
- [082J](https://stacks.math.columbia.edu/tag/082J) の代数空間版Zariski Main TheoremでΘ・shの準アフィン性と粗空間のスキーム性を得る。[0805](https://stacks.math.columbia.edu/tag/0805) はblow-upの平坦基底変更。これらは既知の一般定理であり、本稿ではPoisson側の既存幾何を移す。
- 原稿 `sec:poisson-shadow-comparison` のPoisson構成と上の入力を分けて点検した。次数2の全一般次数4は `sec:degree-two-shadow-degree` の中心torsor・exact fullEq・正規形・全lower・同じ群の商による追加の証明である。次数1も全lower・Poisson正規化・中心torsorと同じ群の商によって全一般次数5を得た。全同値降下・étale比較・一般次数・対称群モノドロミーの組合せについて包括的な優先権確認は未了である。

### 有限正規化・零切断の分枝・基底変更

以下の一次資料を2026-11-20に確認し、主原稿 `sec:finite-normalization-boundary` に適用した。

| 一次資料 | 適用箇所と範囲 |
|---|---|
| [Stacks 02LR](https://stacks.math.columbia.edu/tag/02LR) | 分離的準有限射に対するZariski主定理。正規な構成近傍を、その関数体拡大による相対正規化へ開埋込みする。正規性だけから有限性を結論しない |
| [Stacks 03GR](https://stacks.math.columbia.edu/tag/03GR) | Nagata基底上の相対正規化の有限性。本件の有限型複素スキームに適用し、関数体拡大による正規化を有限射とする |
| [Stacks 054F](https://stacks.math.columbia.edu/tag/054F) | 局所Noetherスキームの特殊化をDVRの射で実現する。境界点へ到達するDVRの一般点を正規化の一般点に取る。有限型C上の閉点や余次元1点だけに限定しない |
| [Stacks 034F](https://stacks.math.columbia.edu/tag/034F) | 正規性のsmooth局所性・smooth射による保存。判別式を反転した有限étale五次代数と、有限étale領域でのスタック引戻しの正規性に適用する |
| [Stacks 0ALJ](https://stacks.math.columbia.edu/tag/0ALJ)、[09ZL](https://stacks.math.columbia.edu/tag/09ZL) | 完備化によるHensel対と、その上の有限étale代数の一意な持上げ。零切断上の五枚の分裂を形式完成へ持ち上げる。Zariski開上の分裂は結論しない |

[Stacks 0GMJ](https://stacks.math.columbia.edu/tag/0GMJ) のスタックの正規化と、[081J](https://stacks.math.columbia.edu/tag/081J) のsmooth基底変更との可換性も一次本文を確認した。有限型C上のatlasに適用し、必要なら引戻しの被約化を別に正規化できることを用いる。

正規化は任意の基底変更と可換せず、有限正規化の粗スタックへの引戻しも正規とは限らない。主原稿 `prop:stack-pullback-finite-normalization` の `t=x²=y²` によるatlas `C[x,y]/(x²−y²)` が具体的な障害を与える。smooth基底変更との可換性を、一般にsmoothでない粗射へ適用してはならない。次数2の最高活性商の1+3形式模型も、この制約のため全Poisson粗空間へはまだ移送していない。

Zariski主定理・Nagata有限性・Hensel持上げ・判別式による非分岐判定は既知の原理である。本件で証明するのは、全同値不変な逆係数の正則延長、次数1の全零切断上の五枚と四枚の欠落、次数2のtrace不変量・接線判別因子・符号二次体を用いた各可換点上の欠落分岐点への適用である。この組合せについて包括的な新規性・優先権の確認は未了である。境界点を新しい非可換対象として構成したとは主張しない。

### Binary quarticの正規形と次数比較

- Christian Böhning, *The Rationality Problem in Invariant Theory*, [著者公開稿](https://www.math.uni-hamburg.de/home/boehning/research/invariant_theory_book.pdf)、191頁版、§3.3.1、Proposition 3.3.1.2・Corollary 3.3.1.3、本文pp.98–99（PDF pp.110–111）を確認。一般安定化群H=V₄、normalizer N(H)≅S₄、N(H)/H≅S₃、二係数固定部分によるsectionは既知である。著者稿の公開年は未確認。同名のarXiv:0904.0899v1は78頁と表示されるため、版や命題番号を同一視していない。
- 本稿では作用を f↦(det M)⁻²f(Mx) と固定し、cross-ratio・Lie軌道・二反射を直接計算する。新たに比較する内容は、規格化したSklyanin中心のshadow写像との同変性、二係数の次数4が全5係数へ保存されること、中心torsorと全Abel同値の商への接続である。古典的な正規形・normalizer自体を新規とはしない。

## 4. Compact持上げ、Serre、鎖formality、降下

| 一次資料 | 確認箇所と本稿での役割 |
|---|---|
| De Deken–Lowen (2011)、上記出版版 | Proposition 5.8（p.499）は平坦Abel変形で導来還元がcompactなら元もcompactとする。Proposition 5.9（p.500）はbounded aboveな生成系の持上げ。dg圏の対角に対しては同じcoinduction towerの論法を本文で直接証明し、Abel圏の定理を無説明で適用していない |
| Keller, *Deriving DG categories*, Ann. Sci. ENS 27 (1994), 63–102、DOI 10.24033/asens.1689、[出版版](https://www.numdam.org/article/ASENS_1994_4_27_1_63_0.pdf) | §§4.3, 8.2。compact生成系によるdg加群模型、導来Morita理論。必要なR-K-flat模型を選ぶ |
| Lowen–Van den Bergh, *On compact generation of deformed schemes*, Adv. Math. 244 (2013), 441–464、DOI 10.1016/j.aim.2013.04.024、[著者稿](https://win.uantwerpen.be/~wlowen/pdf%20papers/compactgen.pdf) | Proposition 3.7、Proposition 5.1。後者はample line bundleとH²(O)=0を持つ射影スキームの全Abel infinitesimal deformationのcompact生成。一般的先行結果として比較。本稿の任意基底変更・飽和性・proper性は有限Ore Čechで直接証明 |
| Shoikhet, *A proof of the Tsygan formality conjecture for chains*, Adv. Math. 179 (2003), 7–37、DOI 10.1016/S0001-8708(02)00023-3、[arXiv:math/0010321v2](https://arxiv.org/abs/math/0010321v2) | Theorem 2.2.7、§2.2.8、§§3.2–3.3。Kontsevich写像と対をなす鎖formality、零次項HKR、Poisson twist。本稿では多項式graphに制限して冪零係数上の有限和とし、任意基底変更を証明する |
| Dolgushev, *A formality theorem for Hochschild chains*, Adv. Math. 200 (2006), 51–101、DOI 10.1016/j.aim.2004.10.017、[arXiv:math/0402248v4](https://arxiv.org/abs/math/0402248v4) | Theorem 3。局所鎖formalityの線型座標変換に関する同変性。非線型座標変換の厳密同変性を仮定しない |
| Dolgushev, *The Van den Bergh duality and the modular symmetry of a Poisson variety*, Selecta Math. 14 (2009), 199–228、DOI 10.1007/s00029-008-0062-z、[arXiv:math/0612288v3](https://arxiv.org/abs/math/0612288v3) | Theorem 3、Definition 1、Proposition 1。一変数h進・滑らかなaffine複素多様体・自明なcanonicalという設定で、無捩れVan den Bergh双対化bimoduleと形式Poisson構造のunimodularityを比較する。Proposition 1は先頭項が至る所非零の形式体積の存在を与える。任意Artin係数上のambient CYは有限鎖twistで別に証明する。一方、`relative_center_lift.tex` は中央差Koszulで絶対CYへ移してこの絶対定理を適用し、体積密度の重み零成分から相対発散零を導く |
| Stacks Project、[Tag 0572](https://stacks.math.columbia.edu/tag/0572)、Lemma 37.23.6 | fppf被覆の局所準有限細分。局所Artin C基底では有限忠実平坦な局所Artin被覆に細分でき、全Čech環も局所Artinになる。この帰結から形式関手の等化子降下を証明し、stack化後のArtin完成を同定 |

上記一次資料の該当定理・係数環・射の定義を2026-11-20に確認した。Artin近傍の相対Serre公式はsmooth proper模型とHH¹対角剛性から証明する。分離型の有限パラメータ族では、相対局所コホモロジーと局所化bimoduleの双対から別に証明する。いずれもAS-Gorenstein indexだけから無捩れなSerre公式を結論していない。ambient CYはbimodule同型の主張であり、negative cyclic CY構造や非正則基底上のbalanced dualizing complexの全公理を付加していない。

## 5. 有限パラメータ族、局所双対、smoothness

### 5.1. Potential、負の補助次数、既知の中心式

- Ginzburg, *Calabi–Yau algebras*, [arXiv:math/0612139v3](https://arxiv.org/abs/math/0612139v3)、2007。Proposition 5.1.9と式(5.1.8)のHessian対角複体、Theorem 5.3.1(iii)の完全性とCY、Proposition 8.1.3(ii)のtensor flip対称性を確認。原資料の半単純基底の設定を任意係数環へ無説明で拡張しない。分離型では随伴次数のKoszul完全性、楕円型では三次AS正則代数の極小解消とファイバーごとの完全性を用い、自己双対性と任意基底変更を本文で証明する。
- Etingof–Ginzburgの上記一次定理を2026-11-20に再確認。負の補助次数によるfiltered量子化の一般原理は既知の枠組みと重なる。本稿は両次数・全nへの中央係数の付加、分離型の有限Casimir式、商の普遍自由性と規格化族の非零hでの普遍中心を具体化する。分離型の明示式そのものの新規性は未確定である。
- 同論文の参考文献[R]が指す [RainsのMagma形式中心元](https://math.mit.edu/~etingof/delpezzocenter) は取得を確認。E6/E7/E8の式があり、E7は `xy−q yx=t z+c1` 等の規約でzを消去した式。本稿の証明入力には使っていない。本稿の次数1中心との明示式の比較では、分母、関係式、正規化と中央係数の扱いの照合が残る。

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

### 5.4. 相対曲線の切断環と強・積Noether性

- Keeler, *Ample filters of invertible sheaves*, J. Algebra 259 (2003), no.1, 243–283、DOI 10.1016/S0021-8693(02)00557-4；Corrigendum, J. Algebra 507 (2018), 592–598、DOI 10.1016/j.jalgebra.2018.03.024。[訂正を含むarXiv:math/0108068v5](https://arxiv.org/abs/math/0108068v5) のTheorems 1.3, 1.5, 7.13–7.14とErratum Theorem E2.5を2026-11-20に一次本文で確認した。Theorem 1.3の条件(A4)は、任意の固定線束HについてH⊗L_mが最終的に豊富となることからample filterを与える。Theorems 7.13–7.14は、可換noetherian環上のproper schemeについて、数値的quasi-unipotenceとあるL_mの豊富性からσ-amplenessを判定し、左右Noetherなtwisted homogeneous coordinate ringを与える。Theorem 1.5はprojective scheme上のcoherent層について、豊富線束の冪に任意のnef線束をtensorしたときの一様な高次コホモロジー消滅である。Erratum Theorem E2.5はその証明の基底変更による還元を修正し、結論を維持する。これらの定理は基底を体・被約環に限定せず、スキームの滑らかさ・整性も仮定しない。
- Keeler, *Noncommutative ampleness for multiple divisors*, J. Algebra 265 (2003), no.1, 299–311、[出版社ページ](https://www.sciencedirect.com/science/article/pii/S0021869303001261)、DOI 10.1016/S0021-8693(03)00126-1、[arXiv:math/0210417](https://arxiv.org/abs/math/0210417)、BibTeX key `KeelerMultiple2003`。出版社の書誌とabstractを確認した。Chanの多重斉次切断環を背景とし、THCRのtensor積のNoether性を含む先行研究として比較する。**本文の定理番号・完全な仮定・一般係数基底への適用範囲は未確認**であり、本稿の証明の数学的依存には加えない。本稿の相対積Noether性は、上記の確認済みFujita消滅と評価イデアルによって直接証明する。
- 本稿では、点曲線の二重対角線を理想(h,δ)で解消し、σ₀=idの滑らかな相対種数1曲線を構成する。最高次中心商の相対THCR同定を先に証明し、任意noetherian基底変更後に上の定理を適用する。σは基底上で各曲線の次数を保ち、相対数値同値類に恒等に作用する。中心正則拡大とfiltered PBWにより全lower・全nに拡張する。
- 積のNoether性は `lem:elliptic-bisection-noetherian` で別に証明する。二曲線の積上の二重切断環について、右イデアルの評価像を高い象限で安定させ、上の一様消滅で有限生成を得る。残る有限幅の行・列は各因子のNoether性で扱う。評価元の係数加群のflat性やイデアルのsaturationは仮定せず、導来projection formulaと両包含を使う。二つの普遍的に正則な中心元とfiltered PBWを経て、全n・全noetherian基底変更で `A^op⊗A` と `B^op⊗B` のNoether性を得る（`cor:elliptic-product-noetherian`）。片側の強Noether性だけから非可換tensor積のNoether性を推論しない。
- 上記のσ-ampleness/Noether原理や体上のSklyanin表示自体は既知である。本稿の可換極限を含む有限な開近傍、任意基底変更、二重切断環、中央多項式係数、全nの相対tailsへの適用という組合せの優先権は未確認。曲線表示は活性最高次商のものであり、n次元tails全体が曲線のcoherent圏になるとは主張しない。

次数1ではStephensonの §2.1、式(2.1.9)、§3の次数1線束の幾何を使う。本稿では有限被覆上で二重対角線を解消し、無限遠の切断P・QとσQ=Pから `L=O(P)` を構成する。次数1〜4の全射性と次数2線束の評価列から全次数生成、一般点のσ⁶≠idと階数比較から中心商の相対THCR同定を得る。強Noether性は上記Keelerの定理から、積は偶数Veroneseと次数2の二重切断環から得る。悪い閉集合の固有像・有限像による縮小と、有限忠実平坦降下を明記した。Stephensonの体上の幾何を相対定理と読み替えただけではない。

### 5.5. 滑らかな有限開近傍とatlasの接空間障害

`finite_smoothness.tex` の `thm:finite-family-smooth-open` は、次数1・2の分離型族と一般楕円型族の全n≥2を扱う。各構成族の中で全斉次式が滑らかな可換del Pezzo模型を与える任意の点について、smooth properな有限型Zariski開近傍を証明する。楕円型では各古典楕円型topの有限開近傍が前提であり、任意の非零hや任意のlower係数でsmoothであるとは主張しない。

証明は、Noetherな二重次数付き積上の平坦な対角、その有限部分解消、相対Serre双対による逆向きのHom複体のperfect性を用いる。特殊ファイバーの `HH¹(X)=0` と `X×X` の有限ホモロジー次元から得る射を、有限自由複体の消去によって開近傍へ持ち上げ、対角をcompact対象の直和因子にする。properなdg代数一般についてsmoothnessの開性を引用したものではない。反標準列の豊富性の開条件と交わらせると、任意の許されるnoetherian基底変更で非可換del Pezzo条件が成り立つ。幾何学的ファイバーのcoherent圏のホモロジー次元はnで、その有界導来圏はcompact圏と一致する（`cor:finite-family-ncdp-open`）。非正則基底上の全有界coherent導来圏までこの一致を拡張しない。

一方、`prop:one-parameter-atlas-obstruction` は、一つの共通量子化パラメータhを持つ表示族のPoisson成分のKodaira–Spencer階数がh=0で高々1であることを示す。全変形のPoisson接空間次元は次数1でn、次数2でbinom(n+1,2)なので、全n≥2で接写像が不足する。係数や座標枠を動かしても共通因子hのため一次のPoisson方向は増えず、これらの一方向族は可換点で形式的にsmoothではない。全方向の同時中心商はこの不足を解消し、そのArtin完成の完全性を§5.8の方法で証明する。有限型基底全体でのsmooth atlasは引き続き別の問題である。

### 5.6. 全方向を含む同時ambient族

Mori–Ueyama, *The classification of 3-dimensional noetherian cubic Calabi–Yau algebras*, J. Pure Appl. Algebra 223 (2019), no.5, 1946–1965、DOI 10.1016/j.jpaa.2018.08.009。[arXiv:1606.00183v3](https://arxiv.org/abs/1606.00183v3) のTheorem 3.4とCorollary 3.8を一次資料で確認した。前者は、二生成元四次cyclic tensorの二つの一次端点微分が独立で、二階端点微分の四成分の共通零点がP¹×P¹にないことを3-CYの必要十分条件とする。後者は二生成元四次potentialのJacobian代数について3-CY性と整域性の同値を与える。最高次の正則開集合と、同時中心商の普遍正則性を示す際の全複素ファイバーの整域性に使う。曲線の滑らかさやbinary quarticの判別式非零は要求しない。

本稿はこの判定から、四次式の偏極と交代形式Pを縮約する作用素 `T_(U,P)(ab)=Ũ(P♭a,P♭b,−,−)` による明示的十分条件 `g₂=det(1+4T)≠0` を得る。g₂(U,0)=1なので、全四次係数の零切断を含む有限主開である。活性binary quarticでは `g₂=1−16Ih⁴+128Jh⁶` となる。次数1ではStephensonの例外点と分離型Ore拡大によりΔ条件をambientから除き、`(1+A₄(D))(5+A₄(D))≠0` を得る。これらはambientの正則性の十分条件である。§5.9の相対THCR表示は特異・非被約なGorenstein曲線も扱い、楕円判別式の非零性を要求しない。両次数とも全体ファイバーのHilbert関数を固定してから、被約普遍係数環の関係行列で任意基底変更の平坦性を証明する。全方向の中心元と普遍正則な有限中心商は次項、同じ有限族のArtin完成は§5.8で扱う。中心構成と圏論的性質のための追加主開は存在を示したもので、最小の非消滅多項式は未計算である。

### 5.7. 同じambientの規格化中心と全方向の貼合せ

**相対局所中心。** `relative_center_lift.tex` の `lem:relative-formal-center-lift` と `prop:relative-finite-center-lift` は、正次数の中央変数sと内部次数0の係数cを持つ同じpotential表示について、次数4または6、完全対称化座標のz²係数1/2、可換極限Fという規格化を保つ中心元を与える。入力は先に証明したh-flat性と無捩れ相対3-CY性である。中心の存在を使って平坦性を示す循環はない。

- [Etingof–Ginzburg, Proposition 8.1.1(i), pp.1407–1408](https://ems.press/content/serial-article-files/31746) は、先頭potentialがxyz−yxz、正の生成重みの和がd、potentialの重み付き次数がd以下という形式設定で中心持上げを与える。(i)には孤立特異点条件がなく、後続の中心全体やcohomologyに関する主張の仮定と区別する。証明はRees変数を中央とするR=C[u]上の相対微分形式を用いている。本稿は中央変数の任意個数、全内部次数、z²係数の規格化、同じ代数への帰還、sの分母を導入しない有限代数化を明記する。
- [Dolgushev, Theorem 3、Definition 1、Proposition 1](https://arxiv.org/pdf/math/0612288) の適用では、中央係数c,sも座標に含めた滑らかな複素affine空間を使う。中央差のKoszul分解で相対CYから絶対CYへ移し、相対Kontsevich写像を内部次数0の部分に制限して元のambientとgauge同定する。相対二重ベクトル上では絶対グラフ公式と相対公式が一致する。得られた不変体積fωの密度の重み0部分f₀(c,h)は中央単元なので、標準相対体積の発散零が従う。活性多項式Poincaréホモトピーとtwisted H⁰写像から所要の中心を作る。Dolgushevの未確認の相対定理を仮定していない。
- 有限代数化はΩ=Sym(F)+hηという有限線型方程式の余核類を扱う。零切断の各局所環での完備化の忠実平坦性により、その類を消すf≡1 mod hが存在する。形式級数にh=1を代入する操作ではない。中心性と規格化は多項式恒等式なので、非平坦・非被約を含む任意の基底変更で保たれる。退化potentialの中心全体がFで生成されるとは主張しない。

**次数2の全係数・全方向中心。** `simultaneous_degree_two_center.tex` の `thm:simultaneous-degree-two-central-family` は、四次式の全係数と全Plücker方向を含む零切断の有限主開近傍で、規格化した中心元と普遍的に正則な中心商を与える。退化した四次式の個々のファイバーでPoisson中心が増えることと、整な普遍係数chart上の中心の核が `Sym⁴K⊕OF` であることを区別する。パラメータで除した交換子とz²係数を組み合わせた商束上の写像は、generic点で単射である。普遍方向空間が整で商束が局所自由なので、これは層として全体で単射となる。全零切断近傍の局所有限中心を入力にして、規格化中心の差をSym⁴Kとする短完全列を得る。全ファイバーでのkernelの一定性は要求しない。

| 一次資料 | 確認箇所と本稿での役割 |
|---|---|
| Guo–Lu–Sharpe, *Classical sheaf cohomology rings on Grassmannians*, [arXiv:1605.01410v2](https://arxiv.org/pdf/1605.01410), 2017 | Theorem 2.3、PDF pp.5–6。標準商束の双対が本稿のKに対応する。Borel–Weil–Bottの重み `(m,m,4,0,…,0)` から `H¹(Gr(2,E*),Sym⁴K(m))=0` が全m≥0で成立し、`H⁰(Sym⁴K)=0` となる。dim E=3はP²上のO(m−4)として直接処理する |
| Svanes, *Arithmetic Normality for Projective Embeddings of Flag Manifolds*, Math. Scand. 33 (1973), 55–68、[DOI 10.7146/math.scand.a-11471](https://doi.org/10.7146/math.scand.a-11471) | Theorem (3.7)は標準線束の切断乗法の全射、Theorems (4.3), (4.5)は旗多様体の射影埋込みの算術的正規性を与える。Plücker錐の正規性に使う。次数別切断環の同定 `H⁰(G,O_G(m))=C[C]_m` も得られ、研究ノートの形式jetによる別証明の入力となる |
| Stacks Project、[Tag 0AY8, Lemma 37.53.6](https://stacks.math.columbia.edu/tag/0AY8) | proper射、正規整な標的、被約な源、源の既約成分が標的を支配しgeneric fiberのH⁰が標的の関数体であることを仮定して `q_*O_Y=O_X` を与える。本稿の方向解消のproper birational射はこの条件を満たす。A₄の有限局所自由性とprojection formulaにより、方向空間上の有限中心切断を同じambientの切断へ降ろす |
| Mori–Ueyama (2019)、上記一次本文 | Corollary 3.8。最高次CY代数の整域性を全複素ファイバーに適用し、中央多項式拡大とPBW filtrationでambient全体へ移す。z²係数1/2により中心元が各ファイバーで非零であるため、次数別の掛算が局所分裂単射となり、任意基底変更後の正則性と商の平坦性を得る |

BWB消滅で規格化中心のtorsorを自明化する。局所中心が存在しない閉集合のproper像を除き、零切断を含むGL(E)不変主開をReynolds作用素で選ぶ。その逆像上の中心を正規錐へ降ろし、中心自身も同変に選ぶ。主開と中心をP↦−Pでも対称にすれば、中心はJ²を法としてSym(F)に一致する。中心の短完全列は局所分裂するので任意基底変更後も完全だが、その基底変更後の層が除した交換子のkernel全体であるとは主張しない。滑らかな係数の開近傍では、さらに像が部分束となりkernelの基底変更との両立も得られる。上の一次資料の指定箇所と、普遍係数の核・有限中心持上げの適用条件を2026-11-20に確認した。全係数への構成と既知の中心公式との一致・優先権は未確認である。

**次数1の全方向中心。** `simultaneous_degree_one_center.tex` の `lem:degree-one-all-top-finite-center` は、楕円判別式を使わず、`((1+αh⁴)(5+αh⁴))≠0` 上のWeierstrass topと全12個のlower係数に既存の23未知数中心行列を適用する。Etingof–Ginzburg Theorem 3.3.2(ii)の入力は固定した斉次CY topと任意lower potentialであり、genericまたは孤立特異点を仮定しない。この局所中心の分母はtop係数とhだけに依存する。これは共通の相対形式補題とは別の局所証明である。

大域的な主張 `thm:simultaneous-degree-one-central-family` は、全四次・六次係数と全D方向を扱う。GL(E)と両立する方向次数4までの中心jetを全係数の有理数恒等式で検算し、除した交換子についてI⁵を法とする中心jetを得る。方向空間P(E*)の `H¹(Sym⁶K(m))=0 (m≥5)` は偏極微分とその明示的な右逆から証明する。この高次消滅で全形式jetを貼り合わせ、blowup上の切断から同じambientのJ進完成へ降ろし、有限余核とArtin–Rees・Reynoldsにより有限中心元へ代数化する。有限jetの計算だけを厳密な中心性の証明とはしていない。全ファイバーの整域性と次数別局所分裂により、中心商の任意基底変更に対する正則性・平坦性を得る。

### 5.8. 同じ有限中心商族の全Artin比較

`simultaneous_formal_comparison.tex` の `lem:simultaneous-artin-abel-family` は、同時中心商を局所Artin環へ基底変更し、その次数別有限自由性から平坦な切断Z-代数変形を作る。De Deken–Lowen [Proposition 4.4, p.495](https://ems.press/content/serial-article-files/30497)によりQmodが平坦Abel変形を与え、Proposition 4.6と§§3.1、3.3により通常のQGrと一致する。有限型基底全体の強Noether性や相対tailsのsmoothnessを、このArtin比較の前提にはしていない。

`thm:simultaneous-central-all-artin` では、滑らかな可換点で係数の可換sliceを選ぶ。その有限族の完備局所環は、次数1では通常の形式円板、次数2では通常の形式円板とPlücker錐の完備化の積であり、既に求めた全Abel形式環と同じ表示を持つ。可換方向のKodaira–Spencer写像と一次交換子によるPoisson方向の写像がともに同型なので、自然変換に対応する完備局所環の自己写像は同型となる。HH¹によるframed自己同値の剛性と合わせ、同じ有限中心商族のArtin基底変更が全framed変形群oidを表す。次数2の二次Plücker関係を含む全形式環を使っており、接空間の一致だけから高次障害の消滅を結論していない。

以上により、同じ有限代数族の全Artin変形に対する形式的完全性を得る。有限基底上の強・積Noether性、相対tails・Serre式、smooth properな有限開近傍は、次項の独立した証明による。この有限族の全O保存同値の認識は§3に記した有限表示の結果で得た。全可換零切断を含む開部分のatlasは構成した。全モジュライを被覆するatlasは未解決である。既存の比較理論の一般原理は先行研究であり、全方向の有限中心商の構成、有限jetによる貼合せ、同じ族の全Artin比較という組合せの包括的な優先権確認は未了である。

### 5.9. 全topの退化曲線、Noether降下、有限基底上のnc族

**次数2の全二元四次式。** `degree_two_gorenstein_curve.tex` の `lem:degree-two-all-top-gorenstein-curve` と `thm:degree-two-all-top-thcr` は、全binary quartic係数のh=0を含む有限主開上で、解消point curveをP¹の有限平坦二重被覆として構成し、同じ活性最高次ambientの中心商を相対THCRと同定する。trace分裂 `p_*O=O⊕N⁻¹`、`deg N=2` により、節点・尖点・可約曲線とf=0の非被約な二重P¹を含めてGorenstein種数1と双対化層の自明性を得る。非被約ファイバーのnilradicalはO(−2)であり、`lem:degree-two-double-cover-cohomology` は正の成分次数を持つ線束のH¹消滅を、このnilradicalを含めて証明する。成分ごとの次数の保存からKeelerのTheorem 1.3を適用し、相対Fujita消滅から `lem:degree-two-gorenstein-bisection` の積Noether性を得る。全lower項と中央多項式係数への拡張は `cor:degree-two-all-top-strong-product`。行列式・blowup・分母を払ったshift恒等式の全係数検算は `verify_degree_two_gorenstein_curve.py` であり、最後のσ⁴検査だけmod h²と明記する。

**次数1の尖点を含む全Weierstrass top。** `degree_one_integral_curve.tex` は階数2の被覆 `k²=−α` を用い、三次根や `γ=6β−4k³` を可逆化しない表示でpoint curveを構成する。全幾何ファイバーは整なGorenstein種数1曲線で、α=β=0の尖点も含む。相対smooth locusの切断P・Qから次数1のLと大域生成な次数2のL₂を得て、正次数線束のH¹消滅と有限個の低次数の全射性でTHCRを同定する。偶数Veroneseを使う積Noether性と有限忠実平坦降下により、`thm:degree-one-all-top-noether` は全top・全lower・全nの任意Noether基底変更を扱う。Stephensonの体上の分類・幾何とKeelerの一般原理は既知の入力であり、退化を含む相対構成の証明は本文に記す。

**零方向を含むNoether性の降下。** `noether_descent.tex` の `lem:graded-jacobson-noether` は、可換Noether環R、`J⊂Jac(R)`、各次数が有限R加群である非負次数付き代数Cについて、C/JCのNoether性をCへ持ち上げる。J進随伴次数環はC/JC上の有限個の中央変数による商なのでNoetherであり、斉次イデアルの初項を有限生成元で消去した後、各内部次数の有限加群にKrull交叉を適用する。[Stacks Tag 00IQ, Lemma 10.51.5(2)](https://stacks.math.columbia.edu/tag/00IQ) を確認した。平坦性や完備性はこの補題の仮定ではない。

一般のJでは `R→R̂_J×∏R[a_i⁻¹]` を使う（`lem:completion-punctured-flat-cover`、`prop:noether-completion-punctured-gluing`）。完成の平坦性は [Tag 00MB](https://stacks.math.columbia.edu/tag/00MB)、スペクトル全射による忠実性は [Tag 00HQ](https://stacks.math.columbia.edu/tag/00HQ) による。完成の像がV(J)を、有限個の主開がその補集合を覆うため、完成自体を忠実平坦と仮定する必要がない。代わりに全ての1+Jを可逆化するJacobson局所化も使えるが、一つの有限表示局所化への置換は主張しない。方向解消のproper性は悪条件の像を除いて有限主開を選ぶためだけに使い、Noether性をproper射の平坦降下で得てはいない。これにより `thm:simultaneous-strong-product-noether` は、全係数の零切断を含む不変有限主開上の同じ同時ambient・中心商とその積について、任意Noether基底変更後の左右Noether性を与える。

**相対CY、tailsとsmooth proper開近傍。** `simultaneous_relative_geometry.tex` は上のNoether入力を使う。`lem:graded-fiberwise-projective` は有限な次数零Hom複体の行列消去から相対projective性を証明する。非零方向での活性potential複体、中央多項式係数のPBW filtration、中央差Koszulと、零方向の可換Koszul解消から、全ファイバーの無捩れCY同型を得る。相対対角のExtの最低次数は基底上の線束であり、左右作用の差を被約な普遍係数環上で消し、Koszul体積でその線束を有限開上自明化する。恒等式を確立してから任意の非被約基底へ移すのが `thm:simultaneous-relative-cy` である。体上のCY性を直接相対CY性と呼び替えたものではない。

`thm:simultaneous-relative-tails` は同じ有限族についてAbel平坦性、局所コホモロジー、飽和性・有向ACM・χ・豊富性、有限compact窓、相対proper性と無捩れSerre式 `S=(−(n−1))[n]` を与える。ここでは§5.3の既知の双対原理に加え、本稿の有限対角・相対局所双対の証明を使い、非正則基底に体上のbalanced dualizing定理を無条件に適用しない。さらに `thm:simultaneous-smooth-ncdp-open` は積代数上の有限部分対角解消、相対Serre双対、可換点のHH¹消滅を使い、**滑らかな全可換正規形の零切断を含む有限型開集合**で、同じ中心商がsmooth properなnc del Pezzo族となることを証明する。全係数の零切断では古典方程式自体が特異な場合もあるため、そこまでsmoothnessを主張しない。

これらと§5.8を合わせ、全framed Abel Artin変形を実現する同じ有限型nc族を得る。双対・ample filter・THCR・Krull交叉・忠実平坦降下の一般原理は既知である。全topの退化曲線、全独立方向への降下、同じ有限中心商の相対圏論的性質と全Artin比較を組み合わせた範囲の包括的な優先権は未確認である。全同値認識は§3の有限型開上で得た。追加開条件の明示、低次数中心が増える層での基本シフト復元、全モジュライのatlasと成分数は残る。

### 5.10. 同じ開近傍の低次数Hochschild剛性

[Stacks Tag 0BDI](https://stacks.math.columbia.edu/tag/0BDI)、Lemma 36.31.1はpseudo-coherent複体のファイバーコホモロジー次元の上半連続性と基底変更を与える。[Tag 0BCD](https://stacks.math.columbia.edu/tag/0BCD)、Lemma 15.77.7はperfect複体をある点のファイバーBetti数と同じ階数の有限自由模型で表せることを述べる。両本文を確認した。

`prop:simultaneous-hochschild-rigid-open` はsmooth properな有限窓dg模型の対角を使い、Hochschild複体が係数perfectで任意基底変更に可換することを直接証明する。単位のconeのTor振幅下界を2へ開化することで、非平坦基底でもHHの負次数消滅・HH⁰=基底・HH¹消滅を得る。可換点の入力は既存のHKR・Kodaira消滅・PoissonDP補題8.7である。nc点の対角Artin剛性には既存の `lem:diagonal-bimodule-rigidity` を適用する。一般のAbel変形とdg Hochschildの比較を追加仮定なしに結論していない。

## 6. 公表前に残る研究・文献上の課題

優先順位の高い比較・調査は次の六点である。

1. **Kuznetsov成分の一般二次差と既存模型の比較。** Ku固定の全Artin有限行列正規形から反標準軌道の積を復元し、中心超曲面の係数へ移す。次数2の一般一節点DVR格子での極消滅、次数1の多項式延長と定数sを検査する。有限Poisson群の奇数周期では残存R₁方向を検出できないため、内在的Serre対合の周期またはgluingの積を使う。AKOの有限代数、Artin普遍性、非可換吹上げ・marked quiverの既存構成との対応と優先権を調べる。
2. **全方向中心構成の比較と明示化。** 同じambient上の全方向中心と有限中心商、同じ族のArtin完成を既存の形式中心持上げ・filtered楕円代数・全Abel変形理論と比較する。追加の主開条件の明示、中心元の選択の違い、既知の公式との関係を調べる。
3. **全方向有限族と既存理論の比較。** 全topの退化曲線、強・積Noether性の零方向への降下、同じ族の相対tails・Serre・smooth proper開近傍を、既存のTHCR・filtered変形・圏の変形理論と比較する。Keelerのmultiple divisors論文の本文と正確な仮定を確認し、体上・相対基底上の適用範囲を整理する。同じ有限族の全Artin普遍性と、全O同値による有限型atlasを区別する。
4. **滑らかな開集合の明示。** 得られた有限部分対角解消とHom複体から、具体的な係数の非消滅条件を計算する。開近傍の存在証明と、その判別式の明示は異なる状態である。
5. **全O同値と大域モジュライ。** 零切断を含む有限型DM開部分Uの全点Artin普遍性、有限対角、Poissonモジュライへのétale比較、正規CM準アフィン粗空間、shadowの平坦性と粗射の正確な平坦locus、比較射の次数5・4とS₅・S₄モノドロミーを得た。次は比較射の開像と有限正規化の境界、Uの被覆範囲と可換locusに接しない成分、特殊安定化群の不変式を調べる。Toën–Vaquiéの固定dg圏の対象モジュライを、可変な全O-marked圏のモジュライと同一視しない。
6. **退化曲線を含む構成と新規性。** 解消point curve、次数1の尖点と次数2のribbonを含む相対THCR、二重切断環による積Noether性、smoothnessの有限開近傍を、既存の楕円代数・非可換del Pezzo・変形圏の構成と比較する。中心増大層を含む適用範囲と、各主張の優先権を確認する。

一般nでの全Abel形式群oid、nc多様体条件のArtin持上げ、形式粗商、具体量子化の完全性、任意指数Veronese復元、有限型族のCasimir・普遍中心・相対双対、全topの退化曲線を含む相対THCRと積Noether性、全方向の同時中心商・相対tails・smooth proper開近傍・全Artin比較という組合せについて、包括的な優先権調査は未了。変形・compact持上げ・formality・CY potentialの中心存在・Sklyanin中心元・Borel–Weil–Bott・σ-ampleness・THCRのtensor積に関する一般結果は既知の研究として区別する。非可換del Pezzo曲面の各定義、AS Z-代数、marked quiver、非可換吹上げとの比較も継続する。講演概要にある未公表の一般次数の主張は確立済み定理として引用しない。
