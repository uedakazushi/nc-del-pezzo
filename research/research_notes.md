# 研究ノート：次数1・2のnc del Pezzo n-fold

2026-11-20（JST） / v0.15。証明本文は主原稿、一次資料の位置は [文献と依存](literature.md)。この文書は現在有効な知識と障害を整理する。

## 1. 形式局所環と数値

`n≥2`, `r=n−1` とする。通常のdel Pezzoモジュライの次元は

\[
b_{n,1}=\binom{n+3}{4}+\binom{n+5}{6}-n^2,
\qquad b_{n,2}=\binom{n+4}{4}-(n+1)^2.
\]

全Abel Artin変形の同型類関手は、次数1で `C[[t,D]]`、次数2で `C[[t,p]]/(Plücker)`。主原稿 `thm:abel-formal-ring` に証明があり、量子化比較の適用条件とArtin試験環への自然性を点検した。形式証明器による検証ではない。

| n | 次数1の形式次元＝接空間次元 | 次数2の形式次元 | 次数2の接空間次元 |
|---:|---:|---:|---:|
| 2 | 10 | 9 | 9 |
| 3 | 37 | 24 | 25 |
| 4 | 107 | 52 | 55 |
| 5 | 260 | 99 | 105 |

次数2の差は `(n−1)(n−2)/2`。`n=3` は一つのPlücker二次式で定まる24次元の形式超曲面、接空間25次元。一般には正規・Cohen–Macaulay整域であり、可換点で形式分枝は一つ。

具体的な障害方向は `Q=e_0∧e_1+e_2∧e_3`（`n≥3`）。`q_{0123}(Q)=1` であり、二次への延長が存在しない。`P=εQ+ε²R` のPlücker式の `ε²` 係数は `q(Q)` なので、二次補正も通常の変形も救済しない。

## 2. 全Abel変形と表示の区別

`Ext^q(O(aH),O(bH))=0` は `a≤b`, `q>0` に対してKodaira消滅から従う。DDL Theorem 4.5が必要とするのはこの有向側の消滅であり、曲面の負の捻りの `H²` は消えない。

各線対象は一意な同型類として持ち上がるため、全変形は平坦なsection Z-代数で表せる。DDLのこの定理だけでは、通常の一つの次数シフトによる周期化や重み付きAS包絡は出ない。一方、本稿の具体量子化の全Artin普遍性を加えると、全ての変形について通常の非負次数付き中心超曲面表示が存在する（`cor:all-artin-weighted-hypersurface-presentation`）。さらに第17項の有限型同時中心商は、可換点の通常変形slice上で同じ全framed Artin変形を分類する（`thm:simultaneous-central-all-artin`）。表示自体を追加標識にはしない。全同値のgraded持上げには、第4項のHH¹剛性と飽和性を用いる。

構造対象の標識忘却は、自然同型類で切断したframed 1群oidでは同値になる。全Abel同値はOの一意な持上げを保ち、標識同型の差はスカラー自然同型で吸収できる。標識を忘れた未切断2群oidにはスカラー自然変換が残る。一方、O標識を保つ自然自己同型は恒等だけである。

全形式環は、compact生成・相対smooth proper性・Serre公式・反標準豊富性・飽和性を持ち上げた `thm:all-artin-are-nc-dp` によって、定義したMと重み付き超曲面部分問題のArtin完成に同定される。さらに第4項の全点Abel変形比較と混合同値層により、全可換locusを含むMの開部分Uが同じ有限型中心商族で表される。Mの全対象がこの表示を持つという大域的主張はしていない。

## 3. 任意基底上の量子化で確定したこと

Poissonパラメータのイデアル `J` が冪零なら、固定したKontsevichグラフ公式は有限和となる。中心元 `Ω=U_π(F)` を取り、`F` がzに関してmonic二次であることから、各次数で

\[
S_{R,\ell}=(\Omega\star S_{R,\ell-m})\oplus W_{R,\ell},
\quad W_R=\langle z\text{の指数が0または1の単項式}\rangle_R
\]

を得る。証明は除法の商写像と `1+K` の有限幾何級数による。`R`の被約性・整域性・平坦な基底変更を仮定しない。

中心的な一次Casimirは両次数とも `n−1` 個。活性な三変数の重みは次数1で `(1,2,3)`、次数2で `(1,1,2)`。次数2の中心変数を `n−2` 個と数えてはならない。

正規形の変換群はambient変数に線型に作用する。KontsevichのGL同変性により中心商も同変。中央の次数スカラー `αλ(a)=λ^{deg a}a` は、右加群上の

\[
M\otimes_{B,\alpha_\lambda}B\longrightarrow M,
\qquad m\otimes a\longmapsto\lambda^{\deg m}ma
\]

で整合的に恒等化される。この同型はOの標識を保ち、群の乗法と両立するので、`~G`-torsorが大域的に存在しなくても `G=~G/Gm` 商へ圏の形式族を降下できる。次数付き代数そのものを同じように降下したとは主張しない。

`QGr(B)` の任意係数変更は、R′作用付き対象とGabriel商の両立から確認した。Abel平坦性はinjective/coflat判定による。可換還元で重み付き商が通常のスキームと一致することには、超曲面がambientの安定化群非自明な部分を避ける補題を使う。

平方零係数では `U₂(F,π)=0`：π頂点の二本の辺を受けられるのがF頂点だけであり、多重辺は禁止される。従って `Ω=F`、積の一次補正は `π/2`、純Poisson方向に余分な一次可換変形は混入しない。

この具体的量子化Qは全framed Abel Artin変形の同型類を自然に分類する（`thm:concrete-quantization-all-artin`）。証明の要点は、一次commutatorの完全列 `0→H¹(T_X)→T Def^O_X→H⁰(∧²T_X)→0` 上で接写像が同型になることと、既知の自然な比較を合成すると同じ完備Noether局所環の自己写像になることである。余接空間で同型の自己写像は随伴次数環・各Artin商・完備環の順に同型になるため、Plücker錐の特異点でも使える。異なる二つの形式空間の接空間だけを比較する議論ではない。

従って通常の次数付き中心超曲面表示が全Artin同型類について存在し、相対augmentation Ext条件も付随する。Qが既知の比較の逆そのものと一致する必要はなく、両者は形式座標の自己同型だけ異なり得る。full groupoidへの強化はHH¹剛性、相対Serre性は第8項の議論による。第11項の特別な族では補助次数による有限性を証明してから特殊化し、第13項では次数2の一般楕円型topを有限開集合上で別に構成する。第17項の全方向族は、同じ有限表示ambientの形式中心を有限線型方程式によって代数化し、その中心商の全Artin普遍性も証明する。固定したグラフ量子化とpotential表示の全高次項を同じ座標で同一視することや、一般の形式級数への値1の代入は行わない。

## 4. 全O同値と反標準環

Artin近傍では、`HH¹_Ab(QCoh X)=H⁰(T_X)⊕H¹(O_X)=0` により、特殊ファイバーで恒等に自然同型な全Abel自己同値は恒等に自然同型である。Oを保たない自己同値にも適用できる。Lowen–Van den Berghのinjective線型圏比較を使い、小拡大上の差を内部導分にする証明が `lem:abel-infinitesimal-aut-rigidity` にある。

全O同値Fと二つの次数シフトs,s′について、`(s′)^{-1}FsF^{-1}` は特殊ファイバーで恒等となるから `Fs≅s′F`。intertwinerの選択差はR×、次数mでλ^mとなる。豊富性と飽和性から `Eq^O(QGr B,QGr B′)=Isom_gr(B,B′)/R×` を得る（`prop:artin-full-graded-recognition`）。graph量子化表示には第8項が全仮定を供給する。この認識は普遍中心条件やSerre公式を使わない。

Serre関手から `H=S^{-1}[n]` を復元する。`(O,H)` の豊富性、section復元、`End(O)=C`、隣接Hom非零の条件下で、O保存全同値は反標準軌道環の次数付き同型を次数スカラーで割ったものになる。相対版ではHom・Serre・perfect性・基底変更・降下を仮定する。

AS-Gorenstein index `r=n−1` だけでは `S=(−r)[n]` を結論しない。Nakayama捻りが残り得る。相対的に `S=(−r)⊗L[n]` なら反標準環の第m成分は `B_{rm}⊗L^{-m}`。通常のVeroneseとの同一視にはこの捻りを追跡する。

重み付き環の全シフト列の豊富性から、r倍シフト列の豊富性を無条件には推論しない。例えば重み付き射影空間の残留安定化群はその推論を妨げる。本件のArtin族では自由な可換模型と有限Ore被覆を用いて別途証明する。有限型族では有限次数による生成検査とSerre消滅により、滑らかな可換点の有限開近傍で証明する。この議論は第18項の全独立方向族にも適用できる。

### 有限基底での全同値スキーム

第18項のsmooth proper開Vでは、反標準列の全Hom・飽和性・相対Serre・豊富性・基底変更が揃う。完全Abel同値は標準dg導来圏のcompact対象を保つので、Serre比較は `O(−ri)` の軌道上だけで行えばよい。全coherent対象をcompactと仮定する必要はない。整合的な反復から通常の `B^(r)` のgraded同型を得て、intertwinerの差は次数スカラーとなる（`thm:finite-anticanonical-isom`）。

右Noether環BのVeronese Rも右Noetherである。右ideal Iに対し剰余次数への射影を使うと `(IB)∩R=I`。R_+の有限右生成元は代数生成元になり、augmentationの有限syzygyから斉次関係式も有限個にできる（`lem:veronese-finite-presentation`）。生成元と逆向き生成元の像、関係式と逆写像条件を有限方程式として課すとIsom_grを表す。

Isomの座標環Aにおいて、次数1の同型行列と逆行列の成分は重み±1で、`1=Σu_ij v_ji`。これが強Z次数付けを与え、`Spec A→Spec A₀` はG_m-torsorになる。A₀は有限型であり、次数零部分の形成は任意基底変更に可換する。このため全同値層はV×V上アフィン有限表示である（`lem:graded-isom-affine-quotient`）。coherent tailsの降下は、有限個の射とcocycleを共通の高次数でstrictにしてgraded加群の忠実平坦降下に帰着する。

安定化群Gの単位切断eに沿う `e*Ω_(G/V)` は有限加群であり、可換点では既存のArtin剛性により零となる。その支持を除き、幾何ファイバー上の群平行移動を使うと、全同値スキームはquasi-finite unramifiedになる（`cor:finite-equivalence-unramified`）。幾何学的自己同値群は有限だが、基底上の射自体の有限性・flatness・étalenessは別である。例えばS=Spec k[t]上の群S⊔D(t)は、D(t)だけでZ/2の非自明元を加えるとaffine有限表示quasi-finite étaleだが有限でない。

### 全同値群oidの完成と可換零切断近傍のDM表示

全係数表示では `g₁=n²`, `g₂=(n+1)²` 個の座標自由度がある。可換点xで、全Artin classifying mapに沿って `Ĉ_V,x≅R_X[[u₁,…,u_g]]` となる。係数空間の横断sliceへの制限はR_X上同型であるため、環だけの積表示を三角な自己準同型で修正し、`lem:formal-endomorphism-inverse` を使う。次数2のPlücker特異性を接空間だけで無視していない。

固定した可換矢α:x→yの持上げは、同じframed変形を与える二つのパラメータと一意なframed矢である。従って完成は `R_X[[u_g,v_g]]`、sourceとtargetは各部分変数環の包含で、相対次元gのsmooth射になる（`thm:equivalence-source-formal-smooth`）。有限Aut(X)の別の元は固定αの完成へ混ざらない。座標作用群oidからの射もこの点でétaleである。

可換零切断Zは全同値でschemeとして保存される。幾何学的には、非零方向の中央一次非零因子uと `B^(r)` の可換性から `u^(i+j)[a,b]=0` を得てB自体を可換にし、`[x_i,y]=D_i z` または `[x_i,x_j]=p_ij z` と矛盾させる。非被約基底についてはArtin graded認識とzの自由直和因子で方向イデアルを検出し、完成環のKrull交叉から `s*J_Z=t*J_Z` へ戻す。一般のZhang twistについての可換tails判定ではなく、この族の中央regular元と低次数表示を使う。

非零方向では、低次数の完全対称化を同型とする有限開を取る。d2のgraded同型はx→Mx′, z→cz′、d1はx→Mx′, y→βy′, z→γz′、γ²=β³となる（`lem:nonzero-graded-isom-weighted-linear`）。d1の非線型加算q2を排除する式は `yq+qy=2Sym(qy)−(D²q/6)(y²+A4)` であり、Sym²E·y成分が2βq2となる。zが積に入る非零方向でも、単元係数はindecomposablesでなく対称化部分束の商から確認できる。

座標変換gを除くと、ambientが同一となり、残る係数差はd1でSym⁶K、d2でSym⁴Kだけである。この係数方向ではambientの関係式が厳密に変わらない。方向解消上のambient次数eに対し、除した交換子とz²係数λの組は、Sym^e Kによる商上で例外因子の全点で単射である。古典中心商のPoisson中心=Pから、ambient中央元はp+cFとなり、λがF方向を検出するためである。properな悪条件像を除くと、この核と分裂は任意基底変更に保たれる。

中心元ΩをCasimir係数に沿って微分すると、`JΩ:Sym^e K→Sym^e K` を得る。例外因子ではΩ=FなのでJΩ=Id。再びproperな悪条件像を除きJΩを可逆にする（`prop:casimir-jacobian-zero-neighborhood`）。小拡大R′→Rの核Iについて、実際のtargetの中心差Δは、部分束の分裂により `P_e∩IA_e=IP_e` に入る。従って `ξ=JΩ⁻¹Δ` の一意な平方零補正で中心元を一致させられる。

これにより非零方向の全矢上で `(g,source):E→G_d×W` はétaleとなる。可換矢の完成計算と合わせ、**零切断Z全体を含む一つの開Wで全source・targetがsmooth**、相対次元gとなる（`thm:full-source-smooth-zero-neighborhood`）。中央係数に関する離散的な別の分枝は許し、座標作用G×W→Eの全射性は仮定しない。

商 `U=[W/E_W]` は整な有限型DMスタックで、全可換模型と全framed Artin変形を含む（`thm:zero-neighborhood-full-dm`）。d1とd2・n=2ではsmooth、d2・n≥3では可換locusが非smooth点の集合およびその被約閉構造となる。任意の対象開のfull restriction商は、source・targetが開射であることからUの開部分スタックである。特に非零方向のNはsmoothで、次元はb(n,1)+nまたはb(n,2)+2n−1となる。

一般の有限型群oidについては、単位smooth開とgeneric flatnessを用いれば非空稠密開で同じ結論に達する（`lem:generic-flat-full-groupoid`）。全sourceをflatにしてから幾何fiberの単位を平行移動する順序が必要であり、この一般論だけではZを残せない。本族のZ近傍全体の構成には上のCasimir補正を用いる。

可換点XではΓ=Aut(X)不変な軌道接空間の補空間Nを選ぶ。実slice `T⊂(f+N)×C_(n,d)` の完成はR_Xであり、矢の完成R_X[[u,v]]にsourceのu=0を入れるとtargetのR_X[[v]]となる。従ってT→Uは可換点でétale。Γ不変なaffine開へ縮小し、次数スカラーの核とΓ↪G_dの有効性により `[T/Γ]→U` はrepresentable étaleとなる（`cor:finite-etale-slice-near-classical`）。可換点の残余gerbe上で同型、その形式完備化は既存の[Spf R_X/Γ]である。以下の全点変形比較でUのM内での開性を、有限対角でsliceのstabilizer preserving性と粗空間上のétale性を得る。

### 非可換点の全Abel Artin変形

主原稿 `sec:noncommutative-abel-versality`。各幾何学的ファイバーで `Q=Ind(coh Q)`、`D^b(coh Q)=Perf(C)` を用い、Lowen–Van den BerghのAbel Hochschild比較とMorita不変性から `C_Ab(Q)≃C(C)` をB∞代数として得る（`prop:noncommutative-abel-hochschild`）。従って全Abel変形の接空間はHH²(C)、障害空間はHH³(C)であり、相対剛性開上ではHH¹=0である。有向ACMと豊富列により構造対象Oは一意に持ち上がり、標識の差はスカラー自然同型で調整できる。任意のAbel変形自体に有限窓dg模型の持上げが存在すると仮定していない。

Uが全同値に関してfullであることから `T_u U→HH²_Ab(Q_u)` は単射である。滑らかな部分ではその次元は `D₁=b(n,1)+n`、`D₂=b(n,2)+2n−1` なので、HH²の下界はD_dとなる（`lem:full-substack-hochschild-lower-bound`）。d1とd2・n=2では古典点のHH²が既にD_dであり、perfect HH複体の上半連続性によって零切断全体を含む開上で等号となる（`prop:smooth-types-abel-versal`）。

d2・n≥3では古典点の `m=dim HH²=b(n,2)+binom(n+1,2)` はD₂より大きい。全古典変形環の二次関係を全小拡大で調べると、普遍一次障害の成分の張る空間はPlücker二次式の空間に一致する。その双対のHH³への単射を通じて、非零可分解πにおける `[π,−]:HH²→HH³` の階数は `c=binom(n−1,2)=m−D₂` となる（`lem:quadratic-relations-hochschild-rank`）。これは一次元変形族の実際のHH複体の第一Bocksteinであり、Lowenのcharacteristic morphismと変形した導来圏の比較を使う（`lem:hochschild-first-bockstein`）。

この階数を全方向で一様化するにはproperな方向解消を使う。被約な例外因子τ=0の近くで単位coneを次数2以上の有限自由複体に取り、可逆ブロックを消去して次数2の階数をmにする。例外因子上でHH²=mなので次の微分は `d²=τA` と書け、Aの階数cの小行列式は例外因子の各点近くで非零となる。頂点外のHH²>D₂という悪条件の閉包は例外因子を避けるため、そのproper像を除いて、**全零切断を保つ一つの開**で非零方向のHH²=D₂を得る（`prop:degree-two-uniform-minimal-hochschild`）。HH³の次元一定性は要らない。

滑らかなsourceとKodaira–Spencer写像の全射性があれば、小拡大上の任意のAbel持上げと構成族の持上げとの差はHH²⊗Iのtorsorで測られ、パラメータの一次補正で消せる（`lem:smooth-source-abel-versal`）。HH³の消滅を要求しない。非零点のこの議論と、特異な可換点も含む既存の全Artin比較を合わせて、同じ零切断近傍の**全ての点**でUのframed Artin変形群oidと全O標識Abel変形群oidが同値となる（`thm:all-points-abel-artin-versality`）。

この比較は任意の剰余体拡大K/Cに対しても成立する（`lem:abel-versality-arbitrary-residue-field`）。変形比較とformalityをK上で直接適用し、有限型HH複体・階数条件・proper方向解消は基底変更する。無限個の変形データを有限生成体へ降下させる議論は使わない。局所Artin C環の小拡大には、K/Cの形式的滑らかさから整合的な係数体を取れる（Stacks Lemma 10.158.8, Tag 0321）。atlasの点は有限分離剰余体拡大後に取り、全忠実性とfppf降下で元の小拡大へ戻す。

### 全モジュライの対角と開埋込み

主原稿 `sec:open-full-moduli`。任意の許容されるNoether基底T上のMの対象について、Serre反周期から復元した反標準環Rは右Noetherかつ斉次有限表示である（`lem:arbitrary-anticanonical-finite-presentation`）。有限表示は選んだ豊富Z代数の周期性と増大列条件から得る。Rの有限生成元・有限関係式と逆写像の条件により、構成族同士に限らない全O同値を `Isom_gr(R,R′)/G_m` として表す。従って**全Mの対角はaffine有限表示**である（`prop:full-moduli-affine-diagonal`）。M全体にatlasが存在することをこの時点で仮定しない。

混合同値層を用いると、fullな射 `U→M` は表現可能な局所有限表示monomorphismとなる（`prop:constructed-substack-representable-lfp`）。任意T→Mとの積は、構成族WとTの間の同値スキームをsmoothな群oidで割った代数空間である。全剰余体でのArtin比較によりこの積の射は形式的étale、局所有限表示性からétaleとなり、monomorphismなので開埋込みである（`prop:all-point-formal-comparison-open`）。よってUは全滑らかな可換模型を含むMの開部分スタックである。

任意の既存のM族が一つの可換ファイバーを持てば、その点のZariski開近傍でUに入る。局所基底で閉ファイバーが可換なら基底全体でUに入る（`cor:familywise-classical-neighborhood`）。これは全Mの被覆、全成分数、可換locusに接しない対象の分類を結論しない。

### 有限対角・分離粗空間・一般安定化群

主原稿 `sec:separated-coarse-moduli`。全sourceがsmoothでWが被約であることから全同値スキームも被約であり、非零方向で成り立つ重み付き線型化の係数恒等式が零方向まで延長される（`lem:all-graded-isom-weighted-linear`）。従って `F^sh=Sym⁻¹(Ω)` による可換超曲面は全同値に関して自然である。全零切断を保って滑らかな可換族へ縮め、可換模型への射 `sh:U→D_(n,d)` を得る（`lem:commutative-central-shadow`, `prop:representable-commutative-shadow`）。この射は代数空間で表現可能で、零切断上では元の可換模型を返す。次項のPoisson構造とétale比較は、低次数交換子による追加の構成である。

全同値スキームEは、二つの可換模型間の同型スキームJの閉部分スキームである。閉条件は、生成元の非線型加算の消滅と、正逆変換が有限個の非可換関係式を保つ条件である。入力 `poisson-del-pezzo` v1.4・定理9.2の可換モジュライの有限対角からJは有限であり、Eも有限となる（`thm:zero-neighborhood-finite-diagonal`）。従って**全可換locusを含むUは有限対角を持つ分離的な有限型DMスタック**であり、Keel–Moriにより分離的・整・同次元の有限型粗代数空間 `M^nc_(n,d)` を持つ（`cor:zero-neighborhood-separated-coarse`）。慣性の平坦性を零切断まで要求していない。

有限慣性によって、可換点のétale slice `[T/Γ_X]→U` は縮小後に全点でstabilizer preservingとなる。一般の可換模型のΓ_X=μ₂は係数方向に自明、Poisson方向に符号で作用するので、非零方向のstabilizerは自明となる。よってUの一般安定化群は自明であり、非零部分に滑らかな代数空間の稠密開が存在する（`cor:stabilizer-preserving-slice-generic-trivial`）。一般論としては、affine quasi-finite慣性のgeneric有限性をmonic関係の分母払いで有限化し、generic flatnessからfinite étale慣性と滑らかな粗空間を得る方法も有効である（`cor:generic-finite-inertia-coarse`）。本族では上の有限対角と符号作用によって、零切断近傍と一般安定化群まで確定する。

粗空間上でも `T/Γ_X→M^nc_(n,d)` はétaleで、スタックと粗空間の正方形はCartesianとなる。従って実際の粗空間の可換点での完備局所環は `R_X^(Γ_X)` であり、その局所環は正規・Cohen–Macaulay・解析的に一分枝である（`cor:algebraic-coarse-local-model`）。Γ_X=μ₂ならétale局所模型は `A^b×Spec(C[C_(n,d)]^(2))` の原点近傍で、既存の符号商の接空間次元と特異性は実際の粗空間にも適用できる。特殊なΓ_Xの不変式と非可換点の安定化群増大の具体的分類は残る。

### 実際のPoisson shadowとétale比較

証明は主原稿 `sec:poisson-shadow-comparison`。低次数交換子をd1では `[x_i,y]=D_i z`、d2では `[x_i,x_j]=p_ij z` と書く。対称化中心Fに対し `Π=ι_dF(D∧∂y∧∂z)` または `ι_dF(P∧∂z)` と置くと、FはCasimirとなり、Jacobi恒等式はd1で可換な三導分、d2でPlücker関係の多項式恒等式から従う（`lem:shadow-jacobian-poisson`）。d2では非被約環上でPを局所的に分解可能と仮定しない。`verify_poisson_shadow.py` は独立な1・2階jet上で全JacobiatorとそのPlücker倍表示を厳密に照合する。

ambientの反自己同型 `ρ(x)=x, ρ(y)=y, ρ(z)=−z` と、中心の規格化・中央多項式部分から `ρΩ=Ω` を得る（`lem:shadow-even-z`）。従ってFはzについて偶で、z²係数1/2の規格化により `F=z²/2+f`。これで低次数Poisson括弧は元の交換子に正確に一致する。重み付き線型な全同値では、中心式の尺度と3-vectorの逆尺度が相殺し、Poissonテンソルそのものを保存する。任意基底変更と合成にも両立するため、表現可能な `Θ:U→P_(n,d)` を得る（`prop:poisson-shadow-morphism`）。中心元の単元倍は規格化で消える。中央Casimir多項式の加算はambientのPoissonテンソルを変えないが超曲面を変えるため、異なる中心構成の無条件な同一視はしない。

Projのx₀-chartでzのmonic二次式の基底を使うと、Poissonテンソルが零である条件は方向係数が全て零である条件と一致する。この議論はn=2と非被約係数を含み、零Poisson構造の逆像が可換零切断Dであることをschemeとして与える。方向イデアルJについて `F^sh≡F mod J²`、Poissonテンソルの差はJ³に入り、古典・Poisson両接写像は恒等になる。同じ形式環R_Xの自己写像とHH¹剛性を用いて可換点の群oid完成が同型となる（`prop:poisson-shadow-formal-comparison`）。高次で形式写像自体が恒等とは主張しない。

有限表示の完成判定とétale locusの開性により、全可換零切断を含む一つの開へ縮めてΘを分離的étaleにできる。標的の有限慣性を使ってさらにstabilizer preservingにする（`thm:poisson-shadow-etale`）。開像は零切断を含む。Θはquasi-finite separatedなので準アフィンである。

### Shadowの平坦性・粗空間・零切断の解消

PoissonDP v1.4の相対Jacobi錐を通じて、`sh=pΘ` は準アフィン・有限表示・平坦・全射、相対次元d1でn、d2で2n−1となる（`cor:shadow-flat-cone-fibers`）。固定古典模型X上のファイバーはJacobi錐C_Xへのétale射を持つスキームで、像は頂点を含む開、頂点の逆像は一点。正規CM Gorensteinで純次元だが、ファイバー全体の連結性・既約性やC_Xへの開埋込みは未証明である。d1とd2・n=2でshはsmooth、d2・n≥3の非smooth locusの台はD。n=3は5次元quadric錐、n≥4はnon-lciである。

粗空間の正方形はCartesianで、`Θ̄:M^nc→N` は分離的étale。Poisson粗空間Nのaffine性と正規CM性、Zariski Main TheoremによりM^ncは正規CMな整な準アフィンスキームとなる。PoissonDP定理9.6と忠実平坦降下から `Flat(sh̄)=sh̄⁻¹((M^cl)_sm)`（`thm:coarse-shadow-etale-flat-locus`）。したがって古典粗空間の特異点上では全点で非flatである。粗ファイバーは非被約になり得るため、被約化の `C_X/Aut(X)` へのétale比較と区別する。

d2では平坦基底変更により `Bl_D U=U×_P Bl_D P`。PoissonDP定理10.3・命題10.4から、これはD上滑らかなDMスタックで、射は表現可能projective、零切断外で同型、例外因子は相対Gr(2,n+1)、法束O(−1)となる。`K_tildeU=ρ*K_U+nE` で、Uはatlas上Gorenstein terminal（`cor:nc-shadow-zero-blowup-resolution`）。n=2では元から滑らかな相対A³の零切断blow-up、n≥3では特異点解消である。粗空間のGorenstein性・terminal性・解消を主張しない。

### 形式同型から大域的一意性を導けない障害

`δ=[K(M^nc):K(N)]` は正整数で、δ=1、Θ̄が開埋込み、Θが開埋込みは同値（`prop:poisson-shadow-degree-one-criterion`）。非空開へ縮めてもδは変わらない。反例 `V=Spec C[t,(1+t²)⁻¹,(1+3t²)⁻¹]` に符号作用を入れた `h:[V/μ₂]→[A¹/μ₂], h(t)=t+t³` は、表現可能分離的étaleかつstabilizer preserving、零gerbeで恒等、零の逆像一つ、形式近傍同型である。それでも粗射 `b=a(1+a)²` は次数3である（`ex:etale-shadow-not-open-immersion`）。非対角の同値関係のsource像が零を避けつつ零へ集積するため、単純な悪条件像の除去では単射化できない。

### 最高活性部分の逆係数写像

最高活性部分の逆係数写像は主原稿 `sec:shadow-top-inverse` に整理した。h=1・中央変数なしのd1二係数族 `A₄=αx⁴, A₆=βx⁶` では、規格化中心のshadowは `z²/2+y³/3−2αx²y²+c x⁴y+d x⁶` である。c,dの厳密有理式と12項・22項の自由語中心証明書を `prop:degree-one-shadow-top-center` に記載した。同じ座標ならαはx²y²係数から、βはcから復元できる。一方、Poisson側で `y=Y+2αx²` と正規化した `I=c−4α², J=d+2αc−16α³/3` の係数写像は一般次数5（`prop:degree-one-shadow-top-degree-five`）。C(α,β)=C(α,I)と、Jのαに関する互いに素な次数5/2の有理式を用いる。

d2のh=1・対称binary quartic `U=α(x⁴+y⁴)/4+βx²y²` では、同じ座標のshadow `z²/2+A(x⁴+y⁴)/4+Bx²y²` への係数写像が一般次数4（`prop:binary-shadow-generic-degree-four`）。De Laet中心式の完全対称化変換と、b=−2+2β/3,c=αについてのc²=R(b,B), A=cL(b,B)から体の塔を計算する。両次数とも自由語恒等式・有理関係式・互いに素性を標準ライブラリだけの新規証明書で検証した。これらの最高活性計算だけでは、下位係数への各分枝の延長、構成開への所属、全同値での非同一視までは証明したことにならない。次数2の下位係数は次の三角復元で別に扱う。この二つの数値だけから全Θの次数を結論せず、次数2では以下の中心torsorと座標商の比較を加える。次数1の全次数や下界は未決定である。

次数2ではさらに、既存の22変数中心方程式のうち「整列基底の定数項=U₀、z²係数=1/2」という規格化を固定し、Sym座標で再規格化すると、全lower写像が `V_j=L_j(U₄,h)U_j+Q_j(U₃,...,U_(j+1))` という三角形になる（`cor:binary-shadow-lower-triangular`）。分母がtopだけに依存し、各lower係数の重みが4−jであることが入力。h=0でL_j=1という事実に加え、`z′=hz, U′=h²U` と中心の一意性から `L_j(h²U₄,1)=L_j(U₄,h)` を得るので、h=1でも各L_jの行列式は非零有理関数である。したがってこの選択した係数族では全lowerが各top分枝に一意に持ち上がり、固定座標の全係数写像も次数4。中央一次変数Kを加えた斉次族でも、線型ブロックは `L_j⊗id_(Sym^(4−j)K)` となる。次数2の全方向中心・共通nc開・全座標群と全同値への接続は次項で扱う。次数1の全lower復元はまだ行っていない。

### 次数2の全Poisson比較の一般次数4

主原稿 `sec:degree-two-shadow-degree`、定理 `thm:degree-two-shadow-degree-four`。全n≥2で δ_(n,2)=4 を証明した。中心の選択と共通開への所属は、実際のデータ T=(P,U mod Sym⁴K,Ω) を使って処理する。Tは規格化中心のaffine torsorであり、全方向族Wからの写像はCasimir Jacobianによりétale。全同値群oidはTのG₂作用群oidの引戻しと厳密に一致するので、Uの非零部分は像のG₂飽和の商 [O^sat/G₂] となる。同じ中心関係式を与える元のCasimir座標の複数分枝は、生成元恒等の同型で消える。元のCasimir写像の有理可逆性は不要である。

最高活性部分ではPGL₂が作用し、対称二係数平面Sは一般安定化群H=V₄の固定部分となる。一般target v∈Sの逆像uについて G_u⊂G_v=H、両者の位数4からuもSに入る。従って全5係数の写像も次数4。normalizer商S₃の6倍はsource・targetで同じであり、余分な因子はない。中央一次変数Kを加えた全lowerは既存の三角式で各top分枝へ一意に復元できる。最後のU₀は Ωctrl(a,U₀)=Ωctrl(a,0)+κ⁻¹U₀ というtorsorの線型座標である。固定Pの全群は活性変数への中央一次式の加算も含み、選んだ整列中心切断自体の同変性を仮定しない。

同じ座標群による商図式はCartesianで、Poisson側の一般安定化群は自明なので、全O保存Abel同値で割っても次数4が残る。四つの一般逆像は全て共通のnc開に属し、互いに非同値である。非空Zariski開への縮小でも開埋込みにならず、有理切断もない。一般target上では整な次数4有限étale被覆となる一方、可換点のファイバー長は1なので、可換点を含むZariski開近傍で有限・properにすることはできない。完成局所環の同型とこの大域的多価性は両立する。分解体・モノドロミー、開像、零切断への境界は未計算であり、四価性からGalois群や各固定古典模型のファイバーの既約性を決めない。

### 基本シフトの開条件と形式対象

通常のgraded同型をスカラーで割った `H→E` はmonomorphismである。全シフト上の自然同型の成分λ_iと忠実な隣接Homから `λ_(i+1)/λ_i=c` が一定となり、核が次数スカラーに一致する。HH¹=0開上では、EのArtin矢Fに対する `s₂⁻¹Fs₁F⁻¹` をperfect可逆bimoduleで表し、対角剛性で恒等化する。指定した還元比較との差はHH⁰=Rの単元なので持ち上げて調整できる。従って `H→E` はétale monomorphism、すなわち開埋込みである（`thm:ordinary-graded-arrows-open`）。この矢の開性だけでは、一つの対象開W上の全矢がHに入るとは言えない。

抽象商 `[V/E]` は有限fppf被覆上のV点・E矢と有限cocycleで記述でき、limit preservingでaffine有限表示対角を持つ。これはsourceのflatnessなしで成立する。可換特殊ファイバーを持つ完備Noether局所R上の形式対象は、一意なslice写像の両立系 `C_X→R/m^a` を逆極限して同じ有限族B_Rで実現できる。構成族の二模型間の形式同値もaffine同型スキームにより一意に実現される。さらに全Mのaffine対角により、**任意の既存のM(R)対象で特殊ファイバーが可換なら**、その形式比較は構成族との実際の同値へ一意に実現される（`cor:arbitrary-classical-family-effective`）。可換特殊ファイバーを仮定しない全Mのformal GAGAを主張するものではない。

### 形式普遍性だけからの大域化を阻む一般反例

一般の有限型群oidでは、sourceの非smooth locus N⊂EがZに接しなくても、s(N)の閉包がZと交わる可能性がある。sourceはproperとは分からないため、像を閉集合として除くことはできない。generic flatnessで取ったWがZを含むことも保証されない。

この不足を示す一般反例は `V=A²_(x,y)`, `D={x=0,y≠0}`, `G=V⊔D`。D上だけZ/2の非自明元を加え、Vに自明に作用させる。G→Vはaffine有限表示quasi-finite unramifiedで単位上étale。原点を特殊点とする全Artin基底ではDが空となり、変形はVの形式環で完全に表される。しかし原点の任意の開近傍はDと交わり、Gはそこでは非flatで、`[V/G]` は代数スタックにならない（Stacks 06PL）。従って有限表示対角・全Artin普遍性・単位smoothnessだけでは零切断近傍のatlasを導けない。詳細な群構造と証明は `ex:formal-versality-not-open`。

本族でこの障害を避ける追加の入力は、Casimir Jacobianによる全sourceのsmooth性、非可換点を含む全点でのAbel Artin比較、および任意M族との混合同値層の有限表示性である。可換点だけの形式普遍性から開性を推論する一般原理を使ったわけではない。

## 5. Veronese持上げの有効範囲

`P=Sym E⊂Z(B)`、`rank E≥2`、`B`がP平坦、かつ普遍的に `Z(B)_r=P_r` なら、`Isom_gr(B,B′)→Isom_gr(B^(r),B′^(r))` は `μ_r`-torsor。証明は次数1中心による `P^(r)` の認識、射影空間束の偏極付き復元、中心変数u,vでの局所化と

\[
B=B[u^{-1}]\cap B[v^{-1}]
\]

による貼合せを使う。次数1生成は要求しない。`n≥3`では `rank E=r=n−1≥2`、`n=2`ではr=1なので持上げ問題自体がない。

**適用できない領域。** 可換点では中心がB全体であるため普遍中心条件は成立しない。Artin量子化でも、`h²=0`なら多くの `h b` が中心になり、形式generic fiberでの中心計算を零切断近傍へ移せない。全方向有限族では、以下の証明により固定低次数中心条件を零切断近傍の非零部分全体で確保した。第11項の規格化族では全非零hで中心を直接証明し、次数ごとの最大小行列式から任意基底変更を得た。

### 全方向有限族の稠密開への適用

非零方向上でK=ker Dまたはker Pを取り、P=Sym Kとする。活性filtrationの最高次中心元は非零である。完全対称化写像の活性次数別ブロックが可逆で、Ωのz²係数が1/2だからである。最高次AS整域から `gr B=P⊗(A_top/(ω_top))` を得る。全閉ファイバーで `C=B/(K)B` のHilbert級数が一定となり、被約普遍係数上の有限行列の階数判定から各C_mが局所自由になる。次数別の分裂を選ぶと `B≅P⊗C` がP-加群同型となる（`lem:simultaneous-central-flatness`）。この同型そのものを移すので非被約基底でもP-flatである。

固定qに対し、生成元との交換子 `δ_q:B_q/P_q→⊕_w Hom(V_w,B_(q+w))` の最大階数開U_qは普遍的に `Z(B)_q=P_q` を満たす。任意の滑らかな可換係数fと非零方向ξで `(f,hξ)` をC[[h]]へ引戻すと、δ_q/hの還元は古典Poisson交換子であり、`lem:classical-casimir-center` から商上単射。従って有限型行列のある最大小行列式はこの直線上の非零正則関数となり、U_qは全てのこのようなrayと非空開で交わる（`thm:finite-low-center-open`）。形式級数へ有限hを代入する議論ではない。

n≥3では一つのq=r=n−1を固定するだけで、二中心変数によるVeronese持上げと第4項の認識を組み合わせられる。したがって稠密開U_r上で `Eq^O=Isom_gr(B,B′)/G_m`（`cor:finite-full-graded-recognition`）。n=2はr=1なのでV全体で成立する。全中心の最小性を示す無限個の開条件の交叉は不要である。重み付きgraded同型には高重み変数への同次数多項式の加算も含め、線型変数変換だけに狭めない。

### 零切断全体を保つ一様化

方向解消ν:Y→Vを、d1ではO_(P(E*))(−1)、d2ではO_(Gr(2,E*))(−1)の全空間から作る。νはproperで零外同型であり、例外因子は全smooth係数×全射影方向である。KはY上の束となり、Sym^q K→ν*B_qは例外因子上ではmonic z除法、零外では中央P分裂により全ファイバーで単射となる。従って商Q_qは全Yで束である。交換子をtautological sectionτで割った写像Q_q→M_q⊗O(1)は、例外因子の全点で古典Poisson中心=Pにより単射となる。悪い階数locusのproper像を除けばZ⊂V°かつV°\Z⊂U_qを得る（`thm:low-center-zero-neighborhood`）。νを平坦とは仮定しない。

q=n−1に取り、第4項のH→Eの開性と可換零切断の幾何学的saturationを使う。V°上の全閉矢は両端が可換か両端がU_qに入るためHに属す。従って開埋込みH→Eは全射、すなわち同型である（`cor:zero-neighborhood-full-graded-recognition`）。これにより冪零方向と零への特殊化を含む任意基底上の全同値が通常Bから復元され、未商化のVeronese制限もμ_(n−1)-torsorとなる。sourceの平坦性には第4項のCasimir Jacobian補正による別の証明を用いる。


## 6. 次数の内在性

Hilbert級数は次数1で `(1−t+t²)/(1−t)^(n+1)`、次数2で `(1+t²)/(1−t)^(n+1)`。反標準軌道のHomが `B_{rm}` に一致し高次Extが消えるなら、`χ(O,H^mO)` の第n差分は `d r^n`。相対RHomperfectかつ基底変更両立ならdは局所定数。主原稿で定義したMにはSerre周期n−1と有向ACM条件を課しているので、この仮定が満たされる。従ってMのd=1,2は開閉に分かれるが、各次数の既約成分数は依然不明。広い豊富列型Aについては同じ結論を主張しない。

## 7. 相対augmentation Extと形式一般ファイバーの中心

任意の可換Rと冪零Jについて、Aの各次数がR自由で、A/JAが重み付き多項式環なら、augmentationと対角のKoszul分解が同じシフトと階数で持ち上がる。各syzygyはR射影であり、全短完全列はR分裂する。双対分解の最上位にaugmentationを付け、冪零誤差を持つ縮約を逆転させると、左右で `Ext_A^i(R,A)=0 (i≠N)`、頂点で `R(W)` が従う。主原稿 `prop:nilpotent-weighted-as`。

中心商BがR平坦ならchange of ringsにより `Ext_B^{n+1}(R,B)=R(n−1)`、他の次数は零。本件のmonic分裂は商の平坦性を任意基底変更込みで保証する。このExt計算単独では通常の絶対global/injective dimension、Calabi–Yau性、Nakayama消去を結論しない。ambientの相対CY同型は第10項の別証明による。

中心正則性だけでは普遍的正則性は出ない。`R=k[t], A=R[x], Ω=tx` は正則だが、t=0ではΩ=0となる。商のR平坦性という仮定を落としてはならない。

固定した複素点 `(X,π≠0)` の適合Casimir環 `P=C[s_1,…,s_{n−1}]` については、古典Poisson中心を正確に計算できる。`K=Frac(P)` 上の活性三変数超曲面は幾何学的整である。次数1はyの三次項が平方にならないこと、次数2はf4が平方なら全体の分岐四次式に重複因子が生じるか活性P¹が特異点になることを使う。一般rank2と幾何学的整性から分数体中心はK、monic P自由基底から切断環の中心はP。

従って `hπ` の量子化を内部次数ごとに完備化した環の中心は次数別に `P_ℓ[[h]]`、`C((h))` 上の形式一般ファイバーでは `C((h))[s]` となる。中心の最低h係数を順に引く証明であり、任意のC((h))-代数への基底変更でも有限交換子行列の核が保たれる。P上の自由性と合わせ、**全ての固定した非零Poisson方向の形式一般ファイバー**でVeronese持上げの代数的仮定を実現する。

これは条件付き復元定理の代数的仮定を実際に与える。C((h))上のtailsの相対Serre条件や、有限複素hへの特殊化を同時に証明したことにはならない。第8項のSerre公式は局所Artin基底とその基底変更についてのものであり、C((h))への無条件の移行ではない。Artin商の追加中心とは両立する、異なる基底上の主張である。

## 8. Artin族の相対幾何とSerre公式

局所Artin R上で交換子がmBに入るため、固定斉次元fのad_fは冪零。B₀上で非零な固定fの冪は左右正則Ore集合となる。一般の係数変更T上で任意の非零元を取る主張ではない。例えばT=C[t]/t²のtxは零因子である。

次数2ではx_i、次数1ではx_iとy⋆zで被覆する。後者ではy,zがともに可逆となり、z⋆y^{-1}が次数1の単元になる。`B_f⊗_B B_g≅B_fg` は平坦性・可換還元・有限filtrationから従う。有限Čechは任意の加群に対する導来sectionを計算し、q≥0でKodaira消滅を持ち上げて `B_q≅RHom(O,O(q))` を得る。非平坦な加群のČech項自体が基底上平坦とは限らない。

全整数qのČech複体は有界R自由で、還元コホモロジーは有限次元。有限な冪零摂動によって有界有限自由模型へ縮約できる。これがRHomの相対perfect性と任意基底変更を与える。任意の正周期rの豊富性はcoherent対象の有限m-filtrationと相対Serre消滅・生成から証明する。

smooth性は `lem:dg-compact-nilpotent-lift` を対角dg加群へ適用する。補題はDDL Proposition 5.8の論法の直接証明であり、特殊ファイバーでcompactなdg加群はArtin基底上でcompactとなる。各対象のcoinduction towerを**先に作ってから直和**することが重要で、coinduction自体の直和可換性を仮定しない。重み付き二重tailsの平坦な対角 `Δ_{p,q}=B_{p+q}` も構成するが、主証明はその積Morita同定を必要としない。

smooth proper模型Aに対してA*=RHom_R(A,R)が相対Serre関手を表す。`S_R(1)^{n−1}[−n]` の核Pは対角に還元され、HH¹(X)=0からP≅A。写像の持上げ障害がHH¹であることを使っており、まだ存在しない対象の持上げに必要なHH²を省略した議論ではない。これにより `S_R≅(−(n−1))[n]`。

相対Serreの対象はPerf。R=C[ε]/ε²の自明族でもO_X⊗Cはcoherentだがcompactではなく、全Db(coh)を同じ圏としない。

fppf stack化のArtin完成は `lem:artin-stackification-comparison` により変わらない。局所Artin C基底のfppf被覆は有限忠実平坦な局所Artin被覆で細分でき、その全Čech重なりも同じ試験環内にある。枠付き形式関手h_RXの等化子降下を用いるので、正次元基底上の未証明の全比較は不要。

## 9. 有限自己同型群と形式粗商

HH¹剛性によりframed群oidは離散なh_RXに同値。枠を忘れると `[Spf R_X/Γ_X]`、Γ_X=Aut(X)となる。有限Γ_Xに不変な軌道接空間の補空間Nを係数表現内に取り、G×(f+N)→Uの形式逆を使えば、`R_X≅completed O_(H¹T_X×C_n,d),0` をΓ_X同変に選べる。特異錐の任意作用の線型化を仮定していない。

不変式環は正規Cohen–Macaulay整域で同じ次元を持つ。poisson-del-pezzo命題9.4の稠密開ではΓ_X=μ₂で、通常の変形方向には恒等、Poisson方向には符号反転として作用する。従って粗形式商は形式円板とPoisson錐の第二Veroneseの完備化の積。粗商の接空間次元はd1で `b(n,1)+binom(n+1,2)`、d2で `b(n,2)+n(n+1)^2(n+2)/12`。

| n | d1の次元／粗接空間次元 | d2の次元／粗接空間次元 |
|---:|---:|---:|
| 2 | 10 / 11 | 9 / 12 |
| 3 | 37 / 40 | 24 / 39 |
| 4 | 107 / 113 | 52 / 95 |
| 5 | 260 / 270 | 99 / 195 |

全n≥2で両次数とも粗商は特異。粗商のArtin点を変形同型類と取り違えない：εQ≠0と零は異なる軌道だが、符号不変式は偶数次なのでC[ε]/ε²上で同じ粗点へ写る。

## 10. 体積形式とambient CY

標準体積形式に関してambient括弧の発散は恒等的に零。d1は混合偏微分の可換性、d2は `Σ p_ij f_ij=0` による。d2のArtin係数Pを二つのベクトルの外積へ持ち上げる必要はない。

Kontsevich–Shoikhetの対を固定すると鎖formalityは有限な冪零twistで定義でき、各随伴次数のHKRにより擬同型。体積形式に対応する `HH_N(A/R)_W` の類を、有限自由対角分解の双対性で `A^!→A(W)[−N]` へ移す。還元がKoszul同型なのでconeは冪零完全性補題で消える。このbimodule CY同型は任意基底変更と両立する。

N=n+2、W=n+5またはn+3。これはDolgushevの既知のunimodularity原理の相対・重み付き適用であり、negative cyclic CY構造まで主張していない。中心商の随伴複体の計算単独をbalanced dualizing complexやtails Serre双対の証明としない。

## 11. 有限パラメータ族・中心公式・補助次数の障害

主証明は原稿 `sec:finite-auxiliary-quantization`。ここでは再開に必要な選択と適用範囲を整理する。

### 二つの構成

負の補助次数を持つJacobian括弧では、r次グラフ項が補助次数を少なくともrだけ下げる。各入力に対する積とCasimir持上げが有限多項式となり、全有限h・任意中央係数で量子化できる。中心元の最高補助項がz²/2+V_topなので、filtered monic除法により商はx^a y^b z^ε（ε≤1）を基底に持つ。グラフ係数の具体値を計算することなく有限表示の存在まで証明できる。

別に分離型potentialでは `[x,y]=h z`, `[y,z]=h P'(x)`, `[z,x]=h Q'(y)`。P≤5、Q≤3とし、d2はp5=0とする。中心元は

Ω = z²/2 + P + Q − h² Sym(P''Q'')/12 + (2/3)h⁴p5(3q1q3−q2²)x − (3/2)h⁶p5q3²P'。

これは全係数の厳密公式で、h-adic打切りではない。唯一のoverlap zyx、三つの中心交換子、両方の内部次数と補助次数を `computations/verify_finite_families.py` で有理数係数のまま検証する。グラフ量子化とこのpotential量子化を同じ座標で同一視していない。

| 次数 | 内部重み x,y,z | 補助重み x,y,z | 内部関係次数 | 分離型の係数次数 |
|---|---|---|---|---|
| 1 | 1,2,3 | 6,10,15 | 6 | deg p_i=6−i, deg q_j=6−2j |
| 2 | 1,1,2 | 3,4,6 | 4 | deg p_i=4−i（p5=0）, deg q_j=4−j |

中央変数sは両次数ともn−1個、内部次数1・補助次数0。グラフ族ではd2のx⁴と全active三次以下、d1のx次数≤3のA4(x,s)yとx次数≤5のA6(x,s)を許す。分離型potentialは計算可能な部分族であり、混合項を含むグラフ族とは区別する。

### 非空性と普遍中心

滑らかな可換点はd2の `z²/2+x⁴+s1 y³+Σs_i⁴`、d1の `z²/2+y³+s1 x⁵+Σs_i⁶`。全偏微分の共通零は原点だけで、重み付きambientの非自由点も避ける。従って全n≥2で非空な滑らかな可換開集合を含む有限型族が得られる。

最高補助式を `z²/2+x⁴+s1 y³` または `z²/2+y³+s1 x⁵` に固定し、低い補助次数の係数を全て動かす。h≠0で中心は正確にC[s]。最高記号の曲面はFrac C[s]上幾何学的整で、Jacobian括弧のrankが2だからPoisson中心は基礎体だけ。量子中心の正の補助次数をこれで排除する。係数空間×Gmの各内部次数の交換子行列から既知の直和因子C[s]_mを除くと全閉点で単射となり、最大小行列式によって任意基底変更も成立する。全次数に共通の新たな分母は不要。

従ってn≥3ではVeronese持上げの二つ以上の中心一次変数・中心上平坦性・普遍中心の仮定を有限hで実現する。これは環同型についての結果であり、全O保存Abel同値の認識とは区別する。分離型では第12項により相対Serre・section飽和性が全hで成立し、反標準豊富性も滑らかな可換点の開近傍で成立する。そのsmooth proper開では第4項の反標準認識と降下の証明を適用できる。

分離型ambientではpotentialのHessian対角複体の随伴次数がKoszul複体となり、巡回自己双対性から相対3CYを得る。中央変数の左右差の正則列で絶対化すると `A^!_Λ=A(n+5)[−n−2]`（d1）、`A(n+3)[−n−2]`（d2）。任意有限h・任意係数変更で成立する。商のtailsのsmooth性には別の対角の議論が必要であり、第15項で滑らかな可換点の有限開近傍について証明する。

### 負の補助次数という方法の障害

d2でx⁴,y⁴,z²が全て現れると、D=max(4a,4b,2c)に対してa+b+c≤D。d1のx⁶,y³,z²でもD=max(6a,3b,2c)に対してa+b+c≤D。従って正の補助重みによる厳密な次数低下は不可能であり、この方法だけでは一般Poisson方向を被覆できない。

分離型を任意の低補助次数cyclic V(x,y)に替えても、三規則の唯一のoverlapは巡回恒等式 `[x,∂x V]+[y,∂y V]=0` で解消する。このPBW拡張はEG Corollary 7.4.1(ii)とも一致する。ただし明示した中心公式は分離型だけに適用する。混合potentialとグラフ量子化の同定・中心元の具体式は別の課題。

固定したhomogeneous CY topへの全lower potentialの普遍係数拡大には、基底がfiltration帰納法で張ることと、全複素特殊化で独立であること（EG Proposition 7.3.1(ii)）を使える。有限な多項式係数の関係は全複素点で消えるので恒等的に消える。varying elliptic topの有限開条件とは別の段階である。次数2では第13項の具体的AS正則領域を使い、この両段階を完成した。

EGのgenericはDefinition 3.4.3により可算個の閉集合の補集合。RainsのE7/E8中心元の原計算は [EG付属計算](https://math.mit.edu/~etingof/delpezzocenter) にMagma形式である。現在の定理はこの未検証の一般公式に依存しない。一般topを扱う際に、関係式の規約と分母・h=0での正規化を確認する。

## 12. 分離型有限族の相対tails

証明は原稿 `sec:finite-tails`。Λはnoetherianな可換C代数で、非正則・非被約でもよい。N=n+2、d=n+1、(l,D)=(n+3,4)または(n+5,6)、r=l−D=n−1とする。

ambientの相対CYから、Λ-perfectなA加群Mに対して `RHom_A(M,A)=D_ΛM(l)[−N]` を直接導く。中央正則元のchange of ringsはB加群について `RHom_B(M,B)=D_ΛM(r)[−d]` を与えるが、MがB-perfectであるとはいわない。切断加群B/B≥qに適用してcolimitを取ると `RΓ_B(B)=B^∨(r)[−d]`。

一般Mに対するsmashing表示は、ambientの切断加群がA-perfectであることと、A・Bのtorsion導来関手の比較から得る。後者のTor₁は内部次数q,…,q+D−1に支持され、q′≥q+Dからの遷移が零になる。これにより局所化を非有界導来圏でも扱え、全シフトのcompact性が従う。構造対象のRHomは

\[
R\operatorname{Hom}(O,O(t))=
\begin{cases}
B_t&t\ge0,\\
B_{-t-r}^{\vee}[-n]&t\le-r,\\
0&-r<t<0
\end{cases}
\]

となり、飽和性、有向ACM、proper性、任意の許される基底変更を得る。coherent加群の有限型自由解消とsmashing表示から相対Serre消滅・χを証明する。相対Serre公式はHom次元の比較だけではなく、局所化bimoduleLの双対 `D_ΛL≅L(−r)[n]` を構成して合成との両立を保証する。原稿 `thm:finite-tails-relative-serre`。

有限compact生成元は `E=⊕_{j=0}^{l−1}O(j)`。中央変数にも補助重み1を与え、活性重みをd2で(6,8,12)、d1で(12,20,30)にすると、ambient全体の随伴次数が可換多項式環となる。そのaugmentation Koszul分解をfilteredに持ち上げると、両端のshiftが0,lで中間は厳密にその間にある。BとのtensorのTorは二つともtorsionなので、tailsで有限な完全複体を得て、連続するl個のtwistから全twistが生成される。C=REnd(E)はΛ-perfectで基底変更に両立する。Cの対角のC^e-perfect性は、第15項の有限部分対角解消とHH¹消滅により、滑らかな可換点の有限開近傍で成立する。全有限パラメータでのsmooth性は主張しない。

正周期の生成を有限化する補題も得た。j=0,…,r−1に対してr倍twistの有限和からO(−j)への全射を可換点で選び、次数付き余核Q_jを作る。生成元の最大重みをwとすると、連続するw個の高次数部分が零になる有限開条件だけで、その先の全次数が零になる。j=0の全射を反復して添字を任意に大きくできる。全基底変更後のSerre消滅と合わせ、滑らかな可換点のZariski開近傍で反標準列が相対的に豊富となる。原稿 `prop:finite-periodic-generation`、`cor:finite-periodic-ampleness`。

## 13. 次数2の一般楕円型topの有限構成

証明は原稿 `sec:elliptic-degree-two-finite`。巡回potentialの最高項を

\[
U_4=\frac\alpha4(x^4+y^4)
+\beta\left(\frac23x^2y^2+\frac13xyxy\right)
\]

とし、全lower項Σc_ij Sym(x^iy^j)、i+j≤3、を自由に加える。h≠0でzを消去すると三次type-A代数となり、a=1+2βh²/3、b=−2+2βh²/3、c=αh²。具体的な十分正則条件は `Δ_AS=a(a²−b²)≠0` で、h=0の全点を含む。h=0でzを消去することはなく、三変数多項式環を使う。

EGの固定CY topへのPBW定理を、被約な普遍係数環での生成・全閉点での独立性によって拡張する。各有限filtration段階は局所自由となり、その分裂により任意の非被約基底変更も扱える。相対ambient CYはpotential対角複体の全ファイバーでの完全性と次数ごとの局所分裂で証明する。

中心元の有限構成には活性次数6以下だけを使う。`F_4A` の階数は22で、交換子をhで割った写像Dのh=0での核はC⊕CF。20本の独立な中心方程式と、定数項c00・整列基底のz²係数1/2の規格化を合わせて22次の正則行列を選ぶ。低次係数を戻しても重みによる三角性から行列式はtop係数α,β,hだけに依存する。EG Theorem 3.3.2(ii)は全CY top・全lower項について次数4以下の非定数中心元の存在を保証するため、選んだ解は残りの全中心方程式も満たす。これは可算generic条件を有限開条件に読み替える議論ではない。

中心元Ωの最高項は全閉点で非零で、AS整域性から普遍的に正則となる。商は普遍的に次数別平坦。分母がtop係数だけに依存するため、c_ijを中心一次変数s_1,…,s_(n−1)の次数4−i−jの任意斉次多項式で置き換えられる。これが全nへの展開を可能にする。異なる四根を持つ二変数四次式はGL₂変換で上の形となるので、稠密開の古典Poisson対をh=0と第一交換子で実現できる。

De Laetの最高次中心元Cについて、自由代数の九項恒等式で[C,x]と[C,y]が関係イデアルに属することを `verify_cubic_top.py` で厳密検証する。`(C−C0)/h²` は係数の多項式除算であってhの可逆化ではない。正規化した中心元のh=0極限はz²/2+u4。自由語でz²係数1/2と見えても、x,y語の整列でz²項が増えるため、有限行列による規格化との比較は**整列基底での係数**を用いる。

全複素ファイバーのNoether性と普遍係数族の強Noether性は異なる。後者は次項の相対曲線表示で別に証明する。高次の中心も有限位数の楕円パラメータで増え得る。従って分離型の普遍中心定理を一般楕円型へ転用しない。半古典方向の稠密被覆は、全ncモジュライのatlasや全O保存同値の認識を意味しない。

## 14. 一般楕円型族の相対曲線表示と強Noether性

完全な証明は主原稿 `sec:elliptic-relative`。適用範囲は各古典楕円型top `α(4β²−α²)≠0, h=0` の有限開近傍であり、AS正則領域全体への主張ではない。縮小の条件はtop係数だけに依存するので、lower係数には任意の中央斉次多項式を代入できる。

三次関係式のpoint curveはP¹×P¹上の(2,2)式H=0である。h=0でH=2δ²、δ=uV−vUとなり、単にその特殊ファイバーを取ると楕円曲線が失われる。理想(h,δ)で周囲をblow upし、strict transformを取る。h-chartのw=δ/hにより、特殊ファイバーは正しい重み付き楕円曲線 `z²/2+α(x⁴+y⁴)/4+βx²y²=0` となる。point shiftも正則な自己同型σに延長され、σ₀=id。重み2の生成元は大域切断z=δ/hとして回復する。

L=p₁*O(1)、L_m=L⊗σ*L⊗…⊗(σ^(m−1))*Lとすると、最高次中心商は `D=⊕H⁰(E,L_m)` に同型であり、任意基底変更に両立する。証明順序は、ambientからDへの写像、次数1・2の有限開での全射、正次数線束のH¹消滅による全次数の全射、Ωの零像、Hilbert階数比較である。Ωの像は全射性を示してからDの中心元として扱う。一般点でσ⁴≠idは `t∘σ⁴=t+4hw mod h²` で分かり、非零の次数4中心切断を排除する。これは有限位数の特殊点を全て除く主張ではない。

任意noetherian基底上でLは相対的に豊富、σは相対数値同値類に恒等に作用する。訂正を含むKeelerのTheorems 7.13–7.14からDは左右Noetherとなる。正の次数の中心正則元による拡大とfiltered PBW持上げにより、全lower係数・全nのambientと中心商が強Noetherとなる。

### 積代数のNoether性

可換係数に関する強Noether性だけでは `B^op⊗_ΛB` のNoether性は出ない。本件では、二つの相対THCRの積を楕円曲線の積上の二重次数付き切断環として扱い、別に証明した（`lem:elliptic-bisection-noetherian`、`cor:elliptic-product-noetherian`）。二重斉次右イデアルの評価像J_mnは、右側の線束の大域生成によって増加する。noetherianな積曲面上でこの有向和は有限段階に安定する。Keelerの相対Fujita消滅（Theorem 1.5と訂正E2.5）から、高象限では一つの有限成分の積が安定したイデアル層の全切断を生成する。残る有限幅の行・列は、それぞれ一方のTHCR上のNoether加群となる。

評価に用いるイデアル成分は基底上flatとは限らない。この点は、曲線の積の基底上flat性と、正次数の外積線束の導来大域切断が有限射影で次数0に集中することにより、projection formulaで処理する。中央正則元を二度持ち上げ、さらにfiltered PBWを用いることで、全lower項・全nについて `A^op⊗_ΛA` と `B^op⊗_ΛB` は任意noetherian基底変更後も左右Noetherとなる。この積の性質が第15項の対角構成を支える。

### 相対tails

相対CY、中心元の普遍正則性、有限射影な次数部分を用い、第12項の局所双対・smashing・Serreの議論を適用する。有限生成元は `⊕_{j=0}^{n+2}O(j)`。中央変数に補助重み1、活性変数に(M,M,2M), M>1を与えると、随伴次数は中央多項式環と最高次代数のtensor積である。最高次potentialのaugmentation分解と中央Koszul分解をfilteredに持ち上げ、長さn+3の窓を得る。滑らかな可換点の有限開近傍で反標準周期も豊富になる。

`verify_elliptic_curve.py` はHの行列式、blowup式、正則shift、分母を払った曲線保存を全係数の多項式として確認する。σ⁴の部分のみmod h²の計算であり、全次数の恒等式と区別する。THCR同定・強Noether性・tailsは本文の証明であり、この計算だけから結論しない。

## 15. 有限型の分離型・楕円型族のsmoothな開近傍

証明は主原稿 `sec:finite-smoothness`。対象は次数1・2の分離型族と一般楕円型族である。全斉次式が滑らかな可換del Pezzo多様体Xを与える係数点のまわりで、対角がperfectとなる有限型Zariski開近傍を得た（`thm:finite-family-smooth-open`）。反標準周期の豊富性の開集合と交わらせると、定義した重み付き超曲面部分問題の族となる（`cor:finite-family-ncdp-open`）。各幾何学的ファイバーでは `D^b(coh)=Perf`、coherent圏のホモロジー次元はちょうどnである。非正則基底上の全 `D^b(coh)` を相対perfect圏と同一視する主張ではない。

証明の有限性は次の三点にある。

- **coherentな対角。** 二重次数付き環 `B^op⊗_S B` のNoether性を、分離型では可換随伴次数環、楕円型では第14項の積THCRから得る。第一象限の対角加群 `Δ_{a,b}=B_{a+b}` は有限生成かつS-flatである。各方向のtorsionを順に割ると、有限外積twistのMorita模型は `D=C^op⊗^L_SC`、対角の像Mは標準のC-bimoduleになる。証明は `lem:finite-family-product-diagonal`。
- **射の持上げを有限複体へ帰着。** Δの自由解消を長さq>2nで切ったcompact複体P_qを取る。特殊ファイバーX×Xの有限ホモロジー次元とHH¹(X)=0により、写像P_q→対角の右逆が存在し、そのExt¹障害は零になる。既存の相対Serre bimoduleとcoinductionの随伴により `RHom_D(M,P_q)` はS-perfectで、基底変更にも両立する。MのD-perfect性を先に仮定する循環はない（`lem:serre-pseudoperfect-to-perfect`）。
- **有限開集合でのretraction。** 上のHom複体の有限自由模型から単元微分を消去すると、特殊点の近傍で次数1の項が消え、射を実際に持ち上げられる。対角上の合成のconeもS-perfectなので、その支持を除く有限開条件で合成が同型になる。従ってMはP_qの直和因子であり、smooth性が従う。

この証明は、proper性・Serre公式・全Artin近傍のsmooth性だけから一般的な開性を推論していない。対角の有限部分解消と、射の持上げ・coneの消滅を支える有限複体を用いる。得られる開集合は存在を証明したもので、実際の生成行列や判別式の明示公式は未計算である。元の係数空間の全点や全有限hでsmooth性が成り立つとはいわない。原稿の論理点検と、楕円曲線・shiftの補助恒等式の厳密計算は実施したが、smoothness自体の形式証明器による検証ではない。

### 一つのhによるatlasの障害

上で構成した一方向の中心商族は、全交換子が共通の因子hを持つ。可換点で `h=εa`、他の係数を `λ=λ₀+εv` と動かしても、一次交換子は `εa J(λ₀)` だけであり、vの変化は一次Poisson成分へ寄与しない。従ってKodaira–Spencer像を通常の可換変形で割ると、像は高々1次元の `Cπ₀` に含まれる。

一方、全Abel変形のPoisson接空間の次元は次数1でn、次数2で `binom(n+1,2)` で、n≥2ではいずれも1より大きい。HH¹(X)=0のため、この不足を微小自己同値で吸収することもできない。従って現在の共通h表示族から全O-markedモジュライへの射は、固定した可換原像で形式的にsmoothではない（`prop:one-parameter-atlas-obstruction`）。係数・座標枠を動かした同種の族を並べるだけでは、可換点を含むsmooth atlasにならない。

これは、個々の有限族が非可換del Pezzo条件を満たすこと、異なるπ₀を選んで半古典方向を稠密に被覆できることと両立する。第17項の独立Poisson座標による有限型中心商族はこの一次方向の不足を解消し、全framed Artin変形まで実現する。さらに第18項では同じ族の強・積Noether性、相対tailsと、滑らかな全可換零切断を含むsmooth properな有限開近傍を得る。第4・5項でこの有限族の全O同値を認識したが、全モジュライの被覆と有限型atlasの結論はなお得ていない。次数2の基底にはPlücker二次関係があり、全接方向が自由に二次へ延長されるとは限らない。

## 16. 次数1の一般楕円型topの有限構成

証明は主原稿 `sec:elliptic-degree-one-finite`。最高次式を `F6=z²/2+y³/3+αx⁴y+βx⁶` とし、`Δ=4α³+9β²` を反転する。階数6の有限忠実平坦被覆 `k²=−α, ρ³=6β−4k³` 上でρは可逆であり、`y=ρY+kx²` によりh≠0の二生成元表示をStephensonの `S(a,b,c)` へ移す。`a=1+kh², b=ρh², c=−2` に対し11例外点を避ける十分条件は `(1+αh⁴)(5+αh⁴)≠0` となる。kを反転しないためα=0も含む。h=0ではzを消さず、三生成元表示で通常の多項式環に戻る。

potential解消から相対3-CY、Etingof–Ginzburgの固定CY topに対する定理から全12 lower係数のPBW性を得た。普遍係数環の被約性と次数別の有限行列を使い、任意の非被約基底変更まで移す。中心構成には `F6A` の23未知数と出力次数7,8,9の行列だけを用いる。古典核は `C·1⊕C·F`、次数1,…,6の核を除いた階数は1,2,3,4,5,6。定数項とz²係数を規格化した行列の行列式は、lower項を戻しても三角性によってtopだけに依存する。

従って全n≥2で中央一次変数n−1個の斉次係数を自由に代入でき、普遍的に平坦で正則な中心超曲面族を得る。ambientの明示的AS開と、中心構成の追加の有限行列の開条件は異なる。全次数の一様な整列基底、有限開全体での中心の生成、全O同値のatlasは結論していない。相対曲線・強Noether性・積Noether性は次の別の構成から得る。

### 次数1の線束と相対tails

`thm:degree-one-relative-thcr` は、上の階数6被覆でStephenson曲線の二重対角線を `(h,δ)` のblowupによって解消する。有限chart `q=t+hw` の特殊曲線は `3w²+6kt²+2ρt³+ρ=0` であり、`y=ρt+k, z=ρw` によってWeierstrass曲線と同定される。無限遠の切断PとQはσQ=Pを満たし、`L=O(P)` は次数1、`L⊗σ*L=p₁*O(1)` は次数2となる。PとQの合流をCartier因子として扱い、全特殊ファイバーのchartとshiftの正則性を確認した。

THCRにはx,y,zを重み1,2,3で写す。zは普遍基底で先に `[x,y]/h` として正則に定義し、その後に基底変更する。次数1〜4の有限な生成条件と `D_mD₂=D_(m+2)`（m≥3）を使う。degree4を初期条件に入れることは必要であり、可換ファイバーで `D₂D₂→D₄` は全射ではない。全射を得た後、一般点でσ⁶≠idであることから最高次中心元の像を零とし、Hilbert階数比較で同型を得る。

曲線のbad locusの固有像を取り、さらに有限被覆の像を除いて基底を縮める。元の基底の全逆像で構成するため、有限忠実平坦性が保たれる。強Noether性はKeelerの定理から、積のNoether性は次数2の偶数Veroneseと既存の二重切断環の補題から得て、忠実平坦に降下する。全lower・全nへの移行は普遍PBW filtrationを使う。相対CYのshiftはn+5、中心元は次数6、Serreは `(-(n−1))[n]`、compact窓は `⊕_{j=0}^{n+4}O(j)`。これで第15項の有限対角分裂を次数1の一般楕円型にも適用できる。

## 17. 独立Poisson方向の同時中心商と全Artin普遍性

主原稿 `sec:simultaneous-poisson` は、両次数で全方向を有限関係式へ直接入れる。次数1はn個のD_i、次数2はPlücker錐のp_ijを係数とし、可換係数の零切断全体を含む明示的な有限主開でambientの次数別有限局所自由性を証明した。`sec:relative-center-lift`、`sec:simultaneous-degree-one-center`、`sec:simultaneous-degree-two-center` は同じambient内に中心元を構成し、追加の有限主開上で普遍的に正則かつ次数別平坦な中心商を与える。任意の非被約基底変更を許す。両次数ともn≥2全体を扱う。

### 全係数を含む明示的なambient開集合

次数1の明示的開条件は `(1+A₄(D))(5+A₄(D))≠0`。その根拠となるWeierstrass topのAS正則性には楕円判別式Δ≠0は不要である。αβ≠(0,0)では平方根kの一方でρ≠0を選んでStephensonへ移せ、αβ=(0,0)は `C[y,z][x;δ]`、δ(y)=hz, δ(z)=−hy²という分離型Ore拡大となる。第16項の滑らかな相対曲線にはΔ≠0が必要だが、第18項の整なGorenstein種数1曲線は節点・尖点も扱い、強・積Noether性のための判別式条件を除く。

次数2の開条件も明示的に与えられる。`Ũ(ξ,ξ,ξ,ξ)=U(ξ)` と規格化した四重線型化と `P♭(a)=P(a,−)` を用い、`T_(U,P)(ab)=Ũ(P♭a,P♭b,−,−)` により `Sym²E` の線型作用素を定める。十分条件は `g₂(U,P)=det(1+4T_(U,P))≠0` であり、P=0ではg₂=1となる。非零Pの核Kに対してTはK·Eを殺すので、全空間の行列式は活性商 `Sym²(E/K)` 上の3×3行列式に一致する。

証明は `lem:simultaneous-explicit-as-determinant`。Mori–Ueyama Theorem 3.4の行列Mについて、4Mの非対角成分の差は `3(u₁v₂−v₁u₂)` なので、共通零点は対角上に限られる。そこで `p=(r,s), a=su−rv` と置けば `P♭a=hp` かつ `4M(p,p)=(1+4T)(a²)` となり、g₂≠0が共通零点を排除する。端点微分が従属なら巡回tensorは基底変換後に純四乗となるが、commutator-squareの非対称成分がこれを妨げる。四次式の重根の有無を問わず適用できる。全複素ファイバーの一定Hilbert関数と被約普遍基底から、任意基底変更の平坦性を得る。

活性binary quarticを `f=a u⁴+4b u³v+6c u²v²+4d uv³+e v⁴` と書くと、`I=ae−4bd+3c²`、`J=ace+2bcd−ad²−b²e−c³` に対し `g₂=1−16Ih⁴+128Jh⁶` である。偶四次式 `f=α(u⁴+v⁴)/4+βu²v²` では `(1−4βh²/3)((1+2βh²/3)²−α²h⁴)` となる。`computations/verify_cubic_top.py` は一般3×3行列式とこの特殊化の恒等式を有理数係数多項式環で検算し、既存の中心元証明書とともに実行済みである。g₂の非零性はAS正則性の十分条件であり、必要条件ではない。

両次数とも零切断の一次厚化では、古典方程式の完全対称化が中心元であり、monic二次項から普遍正則性と商の次数別局所自由性を得る（`prop:simultaneous-first-order-center`）。以下の有限中心元はこの一次中心商と一致する。次数1では四次までの中心jetを保持し、次数2では反対代数と方向の符号反転の対称性を使って一致を保証する。

### 同じambient内の相対形式中心と有限局所化

証明は `lem:relative-formal-center-lift` と `prop:relative-finite-center-lift`。内部次数0の係数環を `R₀=C[c,ρ(c)⁻¹]`、正次数の中央変数をs、活性三変数をx,y,zとする。仮定は同じpotential表示のh進完備化がh-flatで、還元が `R₀[s,x,y,z]`、相対potential対角がperfectかつ無捩れ3-CYであることである。既存の同時ambientの次数別平坦性を先に使い、potential複体をh=0のKoszul複体から持ち上げる。最高次式の楕円判別式や可換超曲面の滑らかさは仮定しない。

完全対称化で同じambientの乗法を移し、活性三変数だけを微分する相対Kontsevich写像により形式Poisson構造π_hと元の代数への同型を取る。全Hochschild cochainの内部次数0部分への制限には、次数を保つbar–Koszul比較とホモトピーを使う。従って単に別の星積の中心を作る議論にはならない。

絶対包絡代数から中央係数に相対的な包絡代数への商は、左右のc,sの差による中央正則列である。そのKoszul分解と相対CY同型から、複素数上の絶対CY同型を得る。π_hにはc,s方向のベクトル成分がないので、全変数のKontsevichグラフは相対グラフと一致する。この同じ絶対量子化へDolgushevのTheorem 3を適用し、`L_(π_h)(fω)=0` を満たす可逆な形式密度fを得る。fの内部次数0成分 `f₀(c,h)` は中央単元であり、体積形式の重みの成分を取ると `f₀ L_(π_h)ω=0`。従って標準の相対体積形式に関しても発散が零となる。

相対多項式Poincaréホモトピーで活性三変数のCasimirを積分し、twistしたformalityのH⁰と上の同型で同じambientの形式中心へ戻す。積分の分母は正整数だけであり、sを有理関数へ拡大しない。全内部次数は4または6に保たれる。z²係数はR₀[[h]]の元なので、その中央単元で割って1/2に規格化できる。

有限局所化は `Ω=Sym(F)+hη` の中心性・規格化を、内部次数dとd+w_x,d+w_y,d+w_zの有限線型方程式にする。右辺の余核類はh進形式解によって消える。各素イデアルp⊃(h)で局所環のh進完備化が忠実平坦なので、余核類の消滅イデアルは(h)と和を取ると全環になる。従って一つの `f≡1 mod h` を反転すれば、同じ有限表示代数の中で厳密な中心元が得られる。係数空間全体の完備化を無条件に忠実平坦と見なしていない。これは形式級数へh=1を代入する手順でもない。

この証明は [Etingof–Ginzburg, Proposition 8.1.1(i), §§8.1–8.2](https://ems.press/content/serial-article-files/31746) の中心持上げと [Dolgushev, Theorem 3・Proposition 1](https://arxiv.org/abs/math/0612288) の絶対unimodularityを用いる。中央係数の多項式性、内部次数、同じambientへの同定を本稿で追跡した。原稿の論理と一次資料の適用範囲は点検したが、形式証明器による検証ではない。

### 次数2：全四次係数の中心層とPlücker錐への降下

主定理は `thm:simultaneous-degree-two-central-family`。滑らかな四次式だけでなく、全係数空間 `𝔉=Sym⁴E` と全Plücker錐の積上で、零切断全体を含むGL(E)不変な有限主開を取れる。その上の同じambientに内部次数4の中心Ωがあり、完全対称化によるz²係数は1/2、零切断ではFに等しい。方向を反転した反対代数との平均により `Ω≡z²/2+Sym(U) mod J²` とできる。追加の主開の存在は証明したが、その最小多項式や全中心元の閉公式は未計算である。

方向空間は `G=Gr(2,E*)`、標準完全列は `0→K→E⊗O_G→Q→0`、`L=det(Q*)=O_G(−1)` である。`q:Y=𝔉×Tot(L)→𝔉×C(Gr)` は閉incidence部分の射影なのでproperで、頂点の外では同型になる。局所的にP=hP₀とする。

古典側の内部次数4の核は、普遍係数の層として `Sym⁴K⊕O F` である。中心候補を `w=f₄+zf₂+cz²` とし、u,vとの括弧のz係数を比較すると `f₂U_u=f₂U_v=0`、`∂_u f₄=2cU_u`、`∂_v f₄=2cU_v` を得る。普遍係数とGrassmann chartの環は整域であり、U_uは零多項式ではないため、普遍環上ではf₂=0となる。滑らかな四次式の各方向でも同じ計算が成立する。一方、特殊化したUが活性u,vを全く含まなければ、ファイバーには `z Sym²K` も中心として現れる。普遍核の計算と特殊ファイバーの核の計算は異なる。

有限な完全対称化座標を取り、z²係数をλとする。hで除した交換子は、フレーム変換を含めると `D:A₄→(E*⊗A₅⊕A₆)⊗L*` であり、標的のL*を落としてはならない。`C₄=A₄/Sym⁴K` 上の `j=(D̄,λ̄)` は、滑らかな一つの零方向点でファイバー上単射である。Yが整でC₄が局所自由なので、jは普遍係数上の層として単射となる。この段階で全ファイバー上の単射性やjの分裂は要求しない。

相対有限持上げによって、Yの全零切断の近傍に規格化中心がある。coker(j)の(0,1/2)の類が生成する巡回部分層の支持を除けば、その類は茎で零になる。ファイバーだけで零になる条件ではない。そこでj(e)=(0,1/2)を満たす商束の切断eが一意に存在し、λ̄(e)=1/2からOeは直和因子となる。中心層Z₄はOeの逆像であり、`0→Sym⁴K→Z₄→O→0` は局所分裂し、Z₄自体もA₄の部分束になる。この列は任意基底変更後も完全だが、基底変更後の中心全体との一致は一般には主張しない。滑らかな係数の零切断近傍では、jの最大階数条件からDの像も部分束となり、除した交換子のkernelは基底変更と可換する。

Borel–Weil–Bottによる `Sym⁴K⊗O_G(m)` の重みは `(m,m,4,0,…,0)`。m=0,1は長さ2の置換、m=2,3は重複、m≥4は優越重みなので、全m≥0でH¹=0、m=0でH⁰=0となる。n=2ではG=P²、K=O(−1)を直接使う。Y→Gのaffine性と `p_*O_Y=⊕_(m≥0)O_G(m)` によりY上でもH¹が消え、affine係数との積と錐側の主開への局所化でも保たれる。この消滅が中心torsorを自明化し、H⁰消滅が零切断でΩ=Fを与える。

良い開集合の閉補集合のproper像を除けば、錐側に全零切断を含む開集合ができる。その補集合のイデアルとJの和は全環なので、`g≡1 mod J` の主開を選べる。Reynolds作用素でgと中心切断を不変に取れる。座標環と同変準連接層の大域切断はrationalかつ局所有限な表現であり、形式完成全体を無条件に平均していない。Plücker錐の正規性とqのproper birational性から `q_*O_Y=O_X`、有限局所自由なA₄とのprojection formulaで中心が錐へ降下する。

BWBの規約は [Guo–Lu–Sharpe, Theorem 2.3](https://arxiv.org/pdf/1605.01410)、proper降下は [Stacks Project, Tag 0AY8](https://stacks.math.columbia.edu/tag/0AY8)、活性最高次代数の整域性は [Mori–Ueyama, Corollary 3.8](https://arxiv.org/pdf/1606.00183) で確認した。Bottの原論文や未提示の一般中心公式に依存するという意味ではない。

**形式jetによる別の証明法。** 普遍係数上の古典核を使えば、局所形式中心との差の最低h係数を中央なSym⁴Kから引く操作により、規格化中心jetの持上げの差は `Sym⁴K(r)` となる。H¹は全r≥0で消えるため、F mod hから全高次のjetを貼り合わせられる。Plücker埋込みのprojective normalityにより `H⁰(G,O(m))=C[C(Gr)]_m`、従って `Γ(O_Y/I^r)=O_X/J^r` であり、完全対称化を使って同じambientのJ進完成へ降下できる。有限中心方程式の余核は局所完備化の忠実平坦性、またはArtin–Reesと行列式の議論で消せる。主原稿はより短い有限torsor法を採用するが、この形式法は局所入力が形式段階に限られる場合にも使える。

### 次数1：明示中心jetと高次障害の消滅

主定理は `thm:simultaneous-degree-one-central-family`。全四次・六次係数と全方向Dに対し、ambient開集合の中の一つのGL(E)不変主開 `g≡1 mod J` 上で、内部次数6の規格化中心Ωを得る。古典超曲面の滑らかさもWeierstrass判別式の非零性も、中心の存在には不要である。

方向空間G=P(E*)では `Sym⁶K` のH¹は低次数で非零になり得る。n=2ではK=O_(P¹)(−1)なので、H¹(O(−6))≠0である。一方、`H¹(G,Sym⁶K(m))=0` は全n≥2、m≥5で成立する。証明は商が線束である完全列 `0→Sym⁶K(m)→Sym⁶E⊗O(m)→Sym⁵E⊗O(m+1)→0` と、二組の変数の作用素δ=Σt_i∂_(u_i)、ε=Σu_i∂_(t_i)による明示的な右逆である。重みw=m−4≥1が必要な分母を正にする。

低次数を越えるため、`eq:degree-one-fourth-center-jet` のGL(E)自然なΩ_≤4を使う。A=A₄、B=A₆、A^(j)=D^jA、B^(j)=D^jBとし、二次補正は `−Sym(A^(2)y²+B^(2)y)/6+(A^(1))²/12`、四次補正は同式の有限な導分式である。全係数の厳密計算証明書 `computations/verify_degree_one_center_jet.py` は `[Ω_≤4,a]∈J⁶A₁` を全生成元について検証する。方向をD=h∂uとしたときのh次数0から5の恒等式であり、Ω_≤4自身が全次数で中心であるという意味ではない。

このjetはhで除した交換子についてI⁵まで解く。相対形式中心との差の古典核は `Sym⁶K⊕O F` で、`(y²+A₄)g₁=0` のmonic性から全係数環で計算できる。中央なSym⁶Kを引く帰納により、次のjetへの局所持上げは常に可能で、その差はSym⁶K(r)となる。r≥5のH¹消滅で全高次を貼り合わせる。方向のblowup上の `Γ(O_Y/I^r)=C[E*]/J^r` と完全対称化により、同じambientの完成へ降下する。

有限方程式の未知数を `J⁵ker λ⊂(A₁)₆` に取ると、中心性の標的は次数7,8,9の有限加群である。形式解が余核のJ進交叉に入ることから、Artin–Reesと行列式の議論で `1−a, a∈J` を消滅元に取れる。Reynoldsで不変な分母と解を選び、`Ω−Ω_≤4∈J⁵(A₁)₆` を保つ厳密な有限中心へ移す。全係数環のJ進完備化の忠実平坦性を仮定しない。

### 両次数の普遍正則性と商の平坦性

各複素ファイバーで、零方向のambientは多項式環、非零方向では中央多項式環と活性AS整域のfiltered PBW代数である。完全対称化座標でz²係数が1/2なので、Ωは全ファイバーで非零となる。従って各内部次数の乗法 `A_(m−d)→A_m`（中心次数d=4または6）は全閉点で単射であり、有限局所自由加群の最大階数判定により局所分裂する。その余核も有限局所自由である。

この議論は既に選んだ同じ基底上で各次数について成立するため、無限個の開集合の共通部分を取らない。任意の非平坦・非被約基底変更後もΩは左右正則で、B=A/(Ω)は次数別平坦である。各ファイバーのNoether性だけから強Noether性・積Noether性は推論せず、第18項で別に証明する。追加の有限開条件は存在を示したもので、ambientの明示的g₁,g₂だけで全中心構成が完成したという主張ではない。

### 同じ有限中心商の全framed Artin普遍性

証明は `thm:simultaneous-central-all-artin`。滑らかな可換点Xを固定し、通常の係数空間で座標軌道に横断するaffine slice Tを選ぶ。全方向中心商をTと方向錐の積へ引き戻した有限型族B_Vについて、可換零方向点の完成は次数1でC[[t,D]]、次数2でC[[t,p]]/(Plücker)となる。追加の中心構成の分母は零方向で単元なので、この完成を変えない。

任意のArtin点aに対し、`b_ij=(B_a)_(j−i)` は可換section Z-代数の平坦線型変形である。DDL Proposition 4.4から `Qmod(b)=QGr(B_a)` は平坦Abel変形となり、Proposition 4.6からNoether性も持ち上がる。πB_aは次数別平坦なB_aに完全な商関手を適用した対象なので平坦である。ここには有限型基底全体での強Noether性やsmooth tailsを入力しない。

一次交換子は全Poisson方向を与え、零方向ではΩ=Fなので、接写像は `0→H¹(T_X)→T Def^O_X→H⁰(∧²T_X)→0` の核と商の双方で同型となる。一次Ore局所化によってこの交換子がtailsの初括弧に等しいことを確認する。既知の全形式環R_Xと同じ表示の完備環の間の自然変換を自己準同型に直し、`lem:formal-endomorphism-inverse` を適用すれば、全Artin環上の全単射を得る。HH¹剛性により自然同型類を射とする全framed群oidにも強化できる。

従って、一つの固定した有限表示中心商族のArtin基底変更が、Xの全framed Abel変形を実現する。グラフ量子化Qと全高次の座標が文字通り一致する必要はなく、中心元とsliceの選択は形式パラメータの自己同型を変え得る。次数2では全Plücker環を比較しているため、二次障害を接空間だけの計算で消していない。有限型基底上のtailsとsmooth proper性は次項で別に証明する。追加の開条件は零切断で単元なので、同じ族のArtin完成とこの普遍性を変えない。

## 18. 全方向族のNoether性と有限基底上の相対幾何

`thm:simultaneous-strong-product-noether` と `thm:simultaneous-smooth-ncdp-open` により、両次数・全n≥2の同じ有限中心商族は、滑らかな全可換模型の零切断を含む有限型開近傍で実際の非可換del Pezzo族となる。全可換係数を含む段階で強・積Noether性、無捩れな相対CY、相対tails・Serreと有限生成窓を得て、smooth proper性と反標準周期の豊富性は滑らかな可換零切断の近傍へさらに制限して得る。方向を一つに固定したり、楕円判別式を可逆化したりする必要はない。

### 特異な活性最高次式への曲線表示

**次数1。** `sec:degree-one-integral-curve` は階数2の被覆 `k²=−α` のみを使い、`γ=6β−4k³` の三次根を取らない。尺度変更を除いたpoint曲線を二重対角線でblow upすると、特殊方程式は `−3w²−6kt²−2t³−γ=0` である。無限遠のu微分は常に−2なので、`α=β=0` の尖点でも切断P,Qは相対smooth locusに残る。曲線を幾何学的被約に保ち、次数1の `L=O(P)` の相対豊富性を保つと、各成分の正整数次数の和が1であることから全ファイバーは整となる。従ってsmoothnessを仮定しないGorenstein種数1曲線で十分である。

`L⊗σ*L=p₁*O(1)` は大域生成される。正次数線束のH¹消滅、次数1〜4の有限な生成検査、`D_mD₂=D_(m+2)`（m≥3）により同じ最高次中心商をTHCRと同定する（`thm:degree-one-all-top-thcr`）。偶数Veroneseの二重切断環、正次数の中央拡大、PBW filtration、有限忠実平坦降下から、全top・全lower・全nでstrong／product Noether性を得る（`thm:degree-one-all-top-noether`）。`verify_degree_one_integral_curve.py` は全係数の行列式・blowup・shift・因子分解を厳密検証し、σ⁶の非自明性だけをmod h²で検証する。

**次数2。** `sec:degree-two-gorenstein-curve` は全binary quartic fを扱う。解消point曲線の第一射影を有限平坦な二重被覆として保ち、そのtrace分裂を `p₁*O_E=O_(P¹)⊕N⁻¹`、`deg N=2` と書く。ファイバーには節点・尖点・可約曲線に加え、f=0の非被約な二重P¹も入る。後者のnilradicalはO_(P¹)(−2)である。双対化層は全ファイバーで自明で、Lの成分ごとの正次数とnilradicalの完全列から正次数線束のH¹消滅を得る。非被約ファイバーで被約曲線の次数だけを見て消滅を推論していない。

次数1・2の生成検査と高次数の評価列により、同じ最高次中心商を相対THCRに同定する（`thm:degree-two-all-top-thcr`）。二重切断環の評価イデアルの安定と相対Fujita消滅はこのGorenstein族にも適用でき、全lower項・全nのstrong／product Noether性へ移る（`cor:degree-two-all-top-strong-product`）。`verify_degree_two_gorenstein_curve.py` は普遍係数上の補助恒等式を検証する。曲線表示やNoether性そのものは本文の幾何学的証明による。

### properな方向解消だけでは降下できない理由

方向解消 `q:Y→X` はproperで頂点外では同型だが、頂点上で平坦ではない。これはNoether性の忠実平坦降下にそのまま使えない。具体的に `R=C[x,y]`、`q=Bl₀ A²→A²`、`M=R/(x²,y²)` とする。Mの非零元xyは、x-chart `y=xt` では `x²t=0`、y-chart `x=sy` では `sy²=0` となり、qへの引戻しで零になる。従って `q_*O_Y=O_X` でも、一般の有限加群やその間の写像を忠実に検出できるとは限らない。この例は中心切断のprojection formulaによる降下と、イデアル上昇列の降下を混同しないために保持する。

代わりに `lem:graded-jacobson-noether` を使う。RがNoether、`J⊂Jac(R)`、非負次数付き中央R代数Cの各C_dがR有限で、C/JCがNoetherならCもNoetherである。核心は、gr_J CがC/JC上の有限変数中央多項式環の商であることと、斉次イデアルの初項を有限個持ち上げたHに対して有限R加群C_d/H_dへKrull交叉を適用できることである。Rの完備性もC_dの平坦性も不要であり、無限級数をCの元として扱わない。

一般の `J=(a₁,…,a_s)` には `R→R̂_J×∏R[a_i⁻¹]` という忠実平坦被覆を使う（`lem:completion-punctured-flat-cover`）。完成側ではJがJacobson根基に入り、零方向商は有限型可換環なので上の補題が使える。頂点外では方向解消が同型であり、全topの曲線表示を任意Noether基底へ変更できる。方向空間上の悪い集合のproper像を除き、`g≡1 mod J` の不変主開を選んだ後、この二つを貼り合わせる。積代数にも総内部次数を使って同じ議論が適用される。これが `thm:simultaneous-strong-product-noether` の入力と降下の役割分担である。

### 相対projective解消と無捩れCY

`lem:graded-fiberwise-projective` は、次数別有限射影なNoether次数付き代数T上の有限生成・係数平坦な加群Mに対し、全幾何ファイバーのprojective dimensionが一様にa以下なら、相対的な有限projective解消を構成する。有限自由部分解消のsyzygyは係数平坦であり、次数零のHomの有限三項複体を単元小行列式で消去することで、ファイバー上の分裂を実際の分裂へ持ち上げる。この局所有限性を確認せず、ファイバーのExt消滅だけからHomの基底変更を推論しない。

これをNoetherな `A^e_S` 上の対角へ適用する。全ファイバーではpotentialの相対3-CYと中央差のKoszul解消により、長さN=n+2、内部shift l=n+5（d1）またはn+3（d2）の無捩れCY同型がある。相対双対の唯一のコホモロジーHの最低内部次数部分Lを線束として取り出し、`H≅A(l)⊗_S L` とする。左右の作用の差は全複素ファイバーで零であり、普遍係数環の被約性と各次数の射影性から恒等的に零となる。零切断の体積形式を持ち上げてLを有限開で自明化すると、`A^!_S≅A(l)[−n−2]` を得る（`thm:simultaneous-relative-cy`）。確認後の同型は非被約基底にも変更できる。

### 有限生成窓とsmooth properな開近傍

augmentationの有限projective解消を係数基底で自由化し、零方向点での非零scalar成分を有限回消去する。その成分は同じ内部shift間の係数環の元なので、有限個の単元小行列式を反転して同じ消去を有限開近傍で実行できる。残るshiftは可換weighted Koszul解消と一致し、両端はAとA(−l)、他は1,…,l−1である。中心商とtensorしたTorは係数環とその中心次数分のshiftだけで、tailsでは消える。従って `⊕_(j=0)^(l−1) O(j)` がcompact生成窓になる（`lem:simultaneous-finite-window`）。

強Noether性、次数別有限射影性、普遍正則な中心、上のCY同型により、既存の相対局所双対とtorsion比較を同じ全方向族に適用できる。相対tailsは平坦Abel族であり、飽和性、有向ACM、χ、全シフト豊富性、proper性、Serre公式 `S_R≅(−(n−1))[n]` を持つ（`thm:simultaneous-relative-tails`）。相対の対象はcompact圏であり、非正則基底上の全Db(coh)ではない。

積Noether性により二重次数付き対角は有限部分解消を持つ。滑らかな可換点Xで長さq>2nまで取ると、X×Xのホモロジー次元とHH¹(X)=0により右逆とそのExt¹消滅が得られる。相対Serreにより対応するHom複体は係数perfectなので、この右逆を有限開へ持ち上げ、合成のconeの支持を除く。対角は有限perfect複体の直和因子となる。正周期n−1の豊富性の有限開条件を加えて、全滑らかな可換零切断の近傍に `𝔐_(n,d)^(O,hyp)` の族を得る（`thm:simultaneous-smooth-ncdp-open`）。幾何学的ファイバーではDb(coh)がcompact圏に一致し、ホモロジー次元はnである。

これらの証明は原稿に記述し、曲線、降下、相対解消、有限窓と対角持上げの入力を独立に点検した。補助計算の実行は幾何学的証明や形式証明器による検証とは区別する。有限型開近傍の存在と全Artin普遍性だけでは全O同値によるatlasを結論しないが、第4項の全群oidのsmooth性と全点比較を加えると、全可換locusを含むMの開部分Uのatlasを得る。全Mの被覆と全成分数は未解決である。

### 有限開近傍の相対Hochschild剛性

smooth properな有限窓dg代数Cでは、`HH=RHom_(C^e)(C,C)` が係数perfectで任意基底変更に可換する。単位cone `F=Cone(O→HH)` は全滑らかな可換零方向点で次数2未満のコホモロジーが消える。有限自由複体の消去でこの条件を開化し、局所的にFを次数2以上だけの複体へ取れる。任意の非平坦基底変更でも同じ下界を保つため、相対コホモロジー層で `HH^{<0}=0, HH⁰=O, HH¹=0` となる（`prop:simultaneous-hochschild-rigid-open`）。非affine基底の大域HH群とは区別する。

その開内のnc点では、既存の対角bimoduleのArtin剛性を適用できる（`cor:noncommutative-diagonal-artin-rigidity`）。これは既に存在するperfect持上げ同士の同型を持ち上げる主張であり、あらゆるAbel変形のdg模型や全モジュライのatlasをこの消滅だけから結論しない。全Abel変形との比較には第4項のB∞比較・HH²の上下界・小拡大torsorを用いる。

## 19. 優先する未解決点

1. **全Mの被覆と大域成分。** 全可換locusを含む整な有限型開Uと、全Mのaffine有限表示対角は得た。Uの閉包と補集合、可換locusに接しない対象・成分の有無を調べ、全Mの代数性と全成分数へ進む。Uの開性と一分枝性から全Mの既約性を推論しない。
2. **Poisson比較の残る次数・被覆の幾何。** 次数2のδ=4、中心torsorと全同値の比較、共通開への所属は確定した。次は四分枝の分解体・モノドロミー、開像と可換点への境界を調べる。次数1では23変数中心方程式とlower重みから三角復元を検討し、Poisson側のy平行移動を含む商を比較してδを求める。特殊自己同型群Γ_Xに対する粗不変式の具体化も残る。
3. **低次数中心が増える境界と明示条件。** 得た零切断近傍の外側でも反標準環による同値認識は有効である。基本シフトの根と追加の同値を調べ、交換子行列・中心元の追加分母・smoothness・Casimir Jacobian・HH²階数・可換模型の判別式による有限開条件を具体化する。全次数の中心最小性を一つの有限条件で保証したとはみなさない。
4. **公表と文献比較。** 全可換locusを含む有限型開DMモジュライ、全点Abel Artin比較、実際のPoisson比較とその相対幾何を主軸に成果をまとめる。一般変形理論・Jacobian Poisson構造・既存Poisson幾何・THCR・Keel–Mori等の入力と本稿の適用を区別する。AMU2025の多項式Veronese結果、Keelerのmultiple divisors論文の本文と適用範囲、および組合せの包括的優先権の確認は継続する。
