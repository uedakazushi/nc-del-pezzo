# 再現手順と検証範囲

2026-11-20（JST） / v0.18

## 組版

リポジトリ直下で実行する。

```bash
latexmk
```

または `make pdf`。主原稿は `papers/nc-del-pezzo.tex`、出力は `build/nc-del-pezzo.pdf`、SyncTeXも同じ場所。`.latexmkrc` はmainを基準に入力と文献の相対パスを解決する。

必要な環境：LuaLaTeX、latexmk、BibTeX、luatexja、luatexja-preset、amsmath/amsfonts/amsthm、mathtools、mathrsfs、geometry、booktabs、longtable、hyperref、原ノ味明朝・原ノ味角ゴシック（HaranoAji）。TeX Live相当の環境を想定する。主原稿は `\usepackage[haranoaji]{luatexja-preset}` を使い、システム側のNotoフォントを要求しない。TeXは外部PDFや非公開データを読み込まない。

VS Codeでは推奨拡張LaTeX Workshopを入れる。recipeはworkspace rootを作業ディレクトリとして `.latexmkrc` を明示指定する。実質的に同じCLIは次の通り。

```bash
latexmk -norc -r .latexmkrc papers/nc-del-pezzo.tex
```

## 有限計算

新しい曲面の計算は `verify_surface_kuznetsov.py`。標準ライブラリの有理数演算で、点配置代数の相対規格化Hochschild複体を直接作る。三点一直線・六点が同一二次曲線上・八点を通り一点で特異な三次曲線がないことも検査する。一般の曲面に対する証明は原稿の射影frameの議論に置く。Jacobian環のHilbert係数は古典公式だけを検査し、非可換HS積の計算とはしない。

```bash
make verify
# 個別には
python3 computations/verify_surface_kuznetsov.py
python3 computations/verify_formal_geometry.py
python3 computations/verify_finite_families.py
python3 computations/verify_cubic_top.py
python3 computations/verify_elliptic_curve.py
python3 computations/verify_degree_one_top.py
python3 computations/verify_degree_one_curve.py
python3 computations/verify_degree_one_center_jet.py
python3 computations/verify_degree_two_gorenstein_curve.py
python3 computations/verify_degree_one_integral_curve.py
python3 computations/verify_poisson_shadow.py
python3 computations/verify_degree_one_shadow_top.py
python3 computations/verify_degree_two_shadow_top.py
```

Python 3の標準ライブラリのみを使用する。`n=2,...,8` と両次数について、重み付き単項式の独立な計数、monic中心商の基底、簡約Hilbert級数、反標準部分列の第n差分を照合する。次数2の全四添字に対して `P=εQ+ε²R` の二次Plücker係数を記号的に展開し、具体的な障害方向を確認する。さらに二次標準Plücker単項式を独立に数え、符号粗商の接空間次元の閉公式と照合し、両次数の特異性を確認する。

さらに `verify_finite_families.py` は、有理数係数の多項式環 `Q[h,p1,...,p5,q1,q2,q3]` 上で唯一のPBW overlapと明示的Casimirの三つの交換子を厳密に簡約する。係数やhの数値特殊化、h進有限jetによる検査ではなく、全係数の多項式恒等式を確認する。次数2のp5=0特殊化、両次数の内部斉次性、補助重みによる停止性、中心補正項がmonic二次項を保つことも照合する。定数項p0,q0は中心性に影響しないため計算から省いている。

`verify_cubic_top.py` は有理数係数多項式環上の自由代数で、四次Sklyanin中心元の九項交換子証明書を両生成元について確認する。type-Aパラメータ置換、zの消去関係、C0恒等式、多項式として正規化した中心元のh=0極限も照合する。同時ambient族については、一般binary quarticの3×3行列式 `det(1+4T)=1−16Ih⁴+128Jh⁶` と偶四次式への特殊化も厳密に検算する。SymPyなど追加依存はない。

`verify_elliptic_curve.py` はpoint curveの行列式、blowup後の式、分母を払ったshiftの曲線保存とその正則性を有理係数多項式として確認する。最後のσ⁴の検査だけはmod h²と明示した一次計算で、一般点での非自明性を検出する。

`verify_degree_one_top.py` は `Q[h,k,rho]` 上の自由代数で、Weierstrass型からStephenson型への巡回potentialと二つの関係式の変換、有限被覆でのρの可逆性、明示的AS開条件、重み付きcyclic syzygyを厳密に検算する。数値特殊化や有限jetではない。

`verify_degree_one_curve.py` はStephenson曲線の行列式、有限座標と無限遠のblowup、Weierstrassへの同定、無限遠因子P+Q、shiftと逆写像、二つの関係式、σQ=Pを有理数上の多項式恒等式として検算する。σ⁶の非自明性だけは明示したmod h²の計算である。

`verify_degree_one_center_jet.py` は `Q[h,a0,...,a4,b0,...,b6]/(h⁶)` 上の語簡約により、次数1の普遍4次中心jetの全3交換子を厳密に検証する。係数の数値特殊化は行わず、内部次数6と完全対称化座標のz²係数1/2も確認する。各簡約は交換子補正でh次数を増やすため有限回で止まる。これは有限jetの証明書であり、厳密な有限中心元の公式ではない。全中心元の存在には、論文の局所中心・高次H¹消滅・有限線型方程式による代数化を使う。

`verify_degree_two_gorenstein_curve.py` は独立な全四次係数上で、point行列の行列式、二重対角線のblowup、古典二重被覆、分母を払ったshiftと正則持上げを有理係数多項式として検証する。四次式が零の非被約ribbonも含む。σ⁴の非自明性のみmod h²の一次検査である。

`verify_degree_one_integral_curve.py` は `Q[k,gamma,h]` 上で、三次根の尺度変更を除いたpoint行列、有限・無限遠chart、Weierstrassとの同定と尖点、shift・逆写像・関係式、切断P,QとCartier因子を厳密に検証する。楕円判別式を可逆化せず、σ⁶の非自明性だけmod h²で確認する。既存の多項式演算をimportして使うため、関連計算ファイルを同じ `computations/` に保つ。

`verify_poisson_shadow.py` はn=2,...,6で、Fの独立な1・2階jetと方向係数を整数係数多項式として扱い、両次数の全生成元のJacobiatorとCasimir条件を照合する。次数2ではPlücker関係で先に零とせず、Jacobiatorが原稿に書いたPlücker多項式倍の和に厳密に一致することを検証する。係数の数値特殊化や非零方向だけの検査ではない。一般nの証明と全同値降下は原稿の議論である。

`verify_degree_one_shadow_top.py` はh=1の斉次活性二係数族について、分母を払った中心元の交換子を12項・22項の自由語関係証明書で確認する。完全対称化の全7次元空間と特殊化での厳密な階数からgeneric中心の一意性を確認し、Poisson側のy二次項を消去した後の有理係数写像の次数5を支える恒等式・分子分母の互いに素性を検算する。探索で用いた外部CASへの依存はなく、固定証明書だけを標準ライブラリで検証できる。

`verify_degree_two_shadow_top.py` はh=1の最高活性対称binary quarticについて、De Laet中心式の完全対称化、逆関係、次数4の有理式、互いに素性と平方拡大の奇数位数を厳密に検証する。さらにnormalizerの二反射によるS₃作用、shadow写像の全係数同変性、正規形とLie軌道の行列式 α(4β²−α²)/2 を有理数・多項式演算で確認する。既存 `verify_cubic_top.py` の演算と中心元の九項証明書も再利用・実行する。全Θの次数4には、原稿の中心torsor・全lower・共通開・全同値の商の証明を別に使う。有限計算だけでモジュライの主張を証明したとは扱わない。

両shadow証明書はSylvester行列式を除算なしのsubset展開で厳密計算する。次数1は9×9行列から一般判別式のJ次数6・定数最高係数・I=0特殊化を検証し、法19のBézout恒等式で平方因子がないことを確かめる。全depressionとh尺度変更の係数恒等式も検算する。次数2は7×7行列による全二係数判別式、短いS₃不変式表示、B=1の八次分岐多項式と法11のBézout恒等式、smoothな分岐点の証人、符号二次体の反不変式を検算する。数値根や算術的Galois群の特殊化を幾何学的群の証明に代用しない。

次数1の追加計算では、零切断上の因子分解 `f(T;0,0)=Tq(T)`、`D₁(0,0)=7812256185000000000` と、形式逆の二次項を有理係数で検証する。次数2では全5係数のbinary quarticに対する `u=2 tr(T²)`、`v=(4/3) tr(T³)`、`det(q+2T)=q³−uq+2v`、ΔのPoisson次数12を検証する。一般四次式の `Disc(f)=256(I³−27J²)` もSylvester resultantで全係数を検証する。接線の横断族 `x²(x−y)(x−2y)+εy⁴` の判別式はresultantで全ε係数を検証し、ε一次項−32を確認する。二係数商の原点で四つの逆関係Jacobianが36,−162,−81,−81となることも検算する。有限正規化、全商上の消滅位数、全零切断への特殊化は原稿の幾何学的証明に依存する。

最初のスクリプトは有限範囲の数式確認、分離型とSklyanin中心の二つは指定した有限な関係式と中心公式の厳密な恒等式検証である。全Abel変形比較、一般nでの証明、モジュライの代数性、グラフ量子化の全高次積を機械的に証明するものではない。

## 検証の状態

今回（v0.18）はKuznetsov成分の二節の証明を作成し、Hochschild制限、tiltingのシフト・積、全通常Artin変形の復元、相対基底変更、同値bimoduleのétale性、Torelli入力による粗射の降下を相互に独立点検した。被覆対合による偶数次数の制約と、一般ファイバーの二者択一も点検した。δ₂の値、非可換Hochschild–Serre乗法、ρ_Ku=sh、および一般5・4枚のconstancyは未計算・未証明である。形式証明器は使用していない。

`python3 computations/verify_surface_kuznetsov.py` を実行し、一般位置の有理点配置、相対Hochschild複体のd¹d⁰=0、階数(d⁰,d¹)=(9,16),(8,15)、HH次元(1,0,8),(1,0,6)を厳密有理数で確認した。古典Jacobian環のHilbert係数も確認した。これは全変形の圏同値や非可換HS積の機械証明ではない。既存12本の全再実行は今回行っていない。

現行原稿v0.18は既存recipe `latexmk -norc -r .latexmkrc papers/nc-del-pezzo.tex` により244頁のPDFとSyncTeXの生成に成功した。最終ログにはLaTeXエラー、未解決参照・引用、欠落文字、overfull/underfull boxがなく、BibTeXの警告もない。表紙、関係する目次・Introductionの主定理、新第35・36節（196–208頁）、文献（241–244頁）の一覧画像と、新節の主要表示式・定理の拡大画像を確認した。今回、変更していない全頁の表示を再点検したとは扱わない。

既存の証明点検の対象は `finite_normalization_boundary.tex` であり、一般有限正規化・最大有限locus・粗零切断の逆像、次数1の正則不変量とmonic五次模型・零切断上の五枚・形式分裂、次数2のtrace不変量・接線素因子・符号二次体からの欠落分岐点を内部で独立に点検した。接線因子から古典係数空間への優勢性と、余接加群の支持の有限像によって全零切断へ結論を延ばす段階も確認した。正規化と粗射の基底変更を無条件に交換できない反例を含める。最高活性二係数商の形式模型1+3は研究ノートで証明し、全モジュライへの移送は未証明と区別した。Stacksの正規化・Zariski主定理・DVR特殊化・Hensel持上げの一次本文と、固定PoissonDPの全商表示・一般自己同型群を照合した。

既存の一般次数5・4、中心torsor・全lower・全同値商、一般S₅・S₄と符号二次体、Poisson shadow・粗空間・解消の点検結果は保持する。上流の全PBW・AS分類・Noether降下・全Abel比較を今回すべて再検証したとは扱わない。

計算資産12本は2026-11-20に成功した結果を保持する。既存の両shadow計算の実行記録では、既存の一般判別式・有限体Bézout証明書・符号二次体に加え、次数1の零係数での五次式分解・非零判別式・二次Hensel jet、次数2の全binary quartic trace不変量・活性三次特性多項式・接線判別式の横断例・四つの逆関係Jacobianの厳密検算に成功した。importされる既存 `verify_cubic_top.py` も同時に成功した。これらを含む既存12本は今回のKuznetsov研究では変更・再実行していない。形式証明器による検証は行っていない。


- 原稿の主要証明を直接点検した。全Artin比較は引用する一次定理の仮定・射・係数環に照合した。
- 量子化のmonic分裂、QGr係数変更、Abel平坦性、次数スカラーの整合性、初commutatorと形式自己写像による全Artin普遍性を独立に点検した。相対augmentation Ext、形式一般ファイバーの中心、Veroneseの全持上げ、Serre周期からの次数分離の依存関係も点検した。
- HH¹による全自己同値剛性、framed群oid比較、Aut(X)の同変slice、形式粗商とArtin graded認識を点検した。stack化のArtin比較は有限忠実平坦細分と全Čech環がArtinであることを確認した。
- 固定元のOre局所化・重なり・有限Čech、飽和性・正周期豊富性、RHomの有限自由模型、対角dg加群のcompact持上げを点検した。Artin族のsmoothnessはdg加群の冪零持上げから証明する。Serre存在・HH¹対角剛性、有限鎖formalityによるambient CY同型を独立に点検した。
- 有限型族について、補助次数によるグラフ式の停止、任意係数上のPBW・monic分裂、滑らかな古典点、全非零hでの中心と小行列式による任意基底変更を点検した。明示的potentialの有限自由対角複体・Hessian自己双対性と、中心差のKoszul解消による絶対bimodule CYへの移行も独立に点検した。
- 分離型有限族の相対加群双対、torsion導来関手の比較、非有界局所化、χ・Serre消滅、compact生成・proper性・基底変更を独立に点検した。有限windowには全変数を正の補助重みとするKoszul持上げを用いる。相対Serreは左右共通の局所化bimoduleの双対から合成まで両立する形で証明した。正周期の有限開条件と任意基底変更後の豊富性も点検した。
- 次数2の一般楕円型topについて、有限AS正則開条件、相対potential複体、全lower係数のPBW、次数6以下の有限中心行列、topだけに依存する分母、中心元の普遍正則性と任意基底変更を点検した。全体の中心を一定とはしていないことも確認した。強Noether性は次の相対曲線構成で別に証明する。
- Artinのcompact持上げと相対Serre対角剛性を独立に再点検し、既存の仮定下で成立することを確認した。後者には導来結合律と、既に存在する対象の間の射をHH¹で持ち上げるという区別を明記した。
- 楕円型のpoint curve解消、σの正則延長、degree1・2からの生成、中心元の零像、相対THCR同定、任意noetherian基底変更後のNoether性、全nのCY・相対tails・有限窓を独立に点検した。Keelerの訂正を含む一次資料の適用条件も確認した。
- 楕円曲線の二重切断環のNoether性を、右イデアルの評価像の安定、Keeler Theorem 1.5とErratum Theorem E2.5による一様消滅、有限幅の行・列の有限生成から証明し、独立に点検した。評価元の係数加群のflat性やsaturationを仮定しないこと、任意の非被約noetherian基底にも適用できることを確認した。二つの中心正則拡大とfiltered PBWによる `B^op⊗B` の普遍的なNoether性も点検した。
- 両次数の分離型族と一般楕円型族について、全n≥2で、各構成族内の任意の滑らかな可換点の有限型開近傍にsmooth proper性を証明した。二重tailsのMorita模型と対角、平坦syzygyを持つ有限部分解消、相対Serre双対による逆向きHomのperfect性、HH¹消滅による右逆の持上げと有限支持の除去を点検した。反標準豊富性の開条件との共通部分ではnc del Pezzo条件が成り立ち、幾何学的coherent圏のホモロジー次元はnである。任意の有限hでsmoothであるという主張ではない。
- 一つのhを持つ中心商族のPoisson Kodaira–Spencer階数がh=0で高々1となる命題を点検した。全Poisson接空間の次元nまたはbinom(n+1,2)との比較により、これらの族自体は可換点のsmooth atlasではない。これは有限族の存在・smooth proper性と両立する。
- 基礎的なPython計算資産について2026-11-20の成功確認を保持する。分離型族の計算では167種類の単語簡約を使用した。Sklyanin中心元は全係数の自由代数恒等式、次数1の中心jetは明示したmod h⁶の全係数恒等式として検証した。全top曲線の二つの計算では、尖点・非被約ribbonを含む普遍恒等式を確認し、shiftの非自明性を検出する項目だけ有限jetと区別した。
- 次数1の有限開・相対CY・普遍PBW・23未知数の中心構成を独立に点検し、変数変換の全係数恒等式の計算を実行した。相対曲線の両chart、次数1線束、有限被覆の全逆像での縮小、全次数生成、中心の零像、忠実平坦降下、偶数Veroneseによる積Noether性、全nのtailsと有限窓も独立に点検した。
- 両次数の同時ambient表示を独立に点検した。次数1のΔを除くAS開と明示的主開、次数2のMori–Ueyama条件と明示行列式g₂、全体ファイバーの一定Hilbert関数からの普遍平坦性、全一次中心商を確認した。行列式のtensor縮約・Hessian係数・活性3×3行列への帰着も照合した。続く同時中心の構成では、両次数の全可換係数・全方向について有限中心元と普遍正則性を証明した。有限基底上の相対tailsには、以下の独立したNoether性・相対対角の証明を用いる。
- 使用したエンジンはLuaHBTeX 1.18.0。必要なluatexjaと和文フォントを備える環境で再生成できる。和文倍率とaddjfontfeatureに関する既存の設定警告、および既存の分数記法に対するamsmathの警告、数式フォントのサイズ代替の警告は残るが、欠落文字や組版の破綻はない。VS Code設定の検査とrecipe相当CLIは確認済みだが、VS Code UIのビルド操作とSyncTeXのクリック動作は実行していない。
- 相対中心持上げの同じambientへのgauge同定、中央差Koszulによる絶対CY、Dolgushevの絶対定理と体積の重み射影、有限余核の局所化を独立に点検した。次数2は普遍係数上の層の単射性・中心部分束・方向空間上のH¹消滅とproper降下を点検した。次数1は23未知数局所中心・普遍jet・高次H¹消滅・Artin–Reesによる有限代数化を点検した。普遍係数上の中心の計算と、特殊ファイバーの中心が増えることを区別している。
- 同じ有限中心商族からの全Artin比較は、DDL Proposition 4.4の仮定、flatな構造対象、初交換子、同じ全形式環の自己写像という順で点検した。有限基底上のtailsのsmooth proper性は、このArtin比較に仮定していない。
- 全top曲線の二つの節を独立に点検した。次数2の有限平坦二重被覆・trace分解・ribbonのO(−2)・任意基底変更、次数1の階数2被覆・尖点を含む曲線・無限遠Cartier因子と次数1線束を確認した。全次数生成と中心の零像、Keelerのample filter・訂正込みFujita消滅から、全top・全lower・全nの強・積Noether性へ移る論理を点検した。
- 次数別Krull交叉によるJacobson根基からのNoether持上げ、完成＋頂点外の有限積の忠実平坦性、方向解消のproperな悪条件像の除去を独立に点検した。環全体の完成と次数付きの係数変更を区別し、方向解消そのものを平坦と仮定していない。
- 次数零の有限三項Hom複体によるファイバー別projective性、全方向ambientの有限対角解消、被約な普遍基底上の最低次数線束・左右作用と任意非被約基底変更を独立に点検した。零方向のKoszul最小解消への有限スカラー消去、有限compact窓、相対tails・Serre、二重対角とHH¹を使うsmooth properな有限開近傍まで、依存関係と循環がないことを点検した。
- 有限型V上でVeroneseの有限斉次表示、具体的なVeronese/tensor関手によるtails復元、compact軌道上だけのSerre比較、有限高切断でのfppf降下、Isomと逆写像の有限方程式、重み±1の行列成分による強Z次数付けとアフィン商を点検した。n≥3の元のBへの持上げとは区別している。
- 非零方向上で完全対称化の活性filtrationブロック、最高記号の非零性、中央P上のファイバー自由性、被約普遍基底でのC_mの一定階数とP-加群分裂を点検した。固定qの交換子行列とδ_q/hの古典還元から、全smooth f・全非零rayについて低次数中心開の非空性を証明した。全中心最小性や具体的な最大小行列式の一括計算は行っていない。
- smooth properなdg模型のHochschild複体のperfect性・基底変更、単位coneのTor振幅下界、非被約係数へのHH¹消滅を点検した。安定化群の単位余接加群、群の平行移動、ファイバーによるunramified判定から全同値スキームのquasi-finite unramified性を点検した。この段階のunramified性だけからsourceのflatnessやatlasを推論していない。零切断全体を保つ近傍上のsmooth atlasには、後述のCasimir Jacobianによる別証明を使う。
- Stacks Tags 06PH・0BDI・0BCD・02G8・02GF、およびAMU2025のarXiv原本Corollaries 4–5を一次資料で確認した。AMU2025の体上の多項式Veronese持上げを新規結果とはしていない。
- 全係数基底の横断sliceについて、実際のclassifying mapの余接空間が可逆であることと形式自己写像の逆写像補題を照合した。全Artin射の一意性から可換矢の完成を計算し、source・targetのsmoothnessを独立に点検した。可換零切断の幾何学的saturationと方向イデアルの一致は別々に証明した。
- 非空稠密開のfull群oidについて、一般平坦性を全sourceに適用してから幾何学的ファイバーの単位を平行移動する順序を点検した。DM性、次元、慣性の有限化・平坦化、gerbe判定と粗空間のsmoothnessを独立に点検した。零切断を残すatlasや全モジュライ内の開性はここから結論しない。
- 通常graded同型からの射の単射性、基本シフトの持上げに使うperfect bimoduleとHH¹剛性、HH⁰による既定の還元への調整を点検した。fppf有限データの降下による極限保存、可換特殊ファイバーの全framed変形の完備局所有効性、構成モデル間の射の有効性を区別した。任意の許容族の混合同値層を得た後は、可換特殊ファイバーを持つ任意の既存M(R)族との同値も有効化する。全Mに無条件のformal GAGAを主張するものではない。
- 形式的普遍性と単位でのsmoothnessだけでは対象側のfull atlasを得られない群スキームの反例を点検した。非平坦な追加安定化群が可換点へ特殊化せず集積することを、有限型行列条件と区別した。
- Stacks Tags 07VH・039M・0529・052A・01V8・04TK・06FI・04YW・06N3・0DUT・0DUW・06QJ・06QH・02HY・025G・06PL・07T0・07XPの該当主張を一次資料で確認した。新しいモジュライの構成には一般平坦性、群oid商、Keel–Moriを既知結果として使う。
- 方向解消上で中央部分の商が全体で束になること、除した交換子の線束の捩れ、全smooth係数・全方向の古典Poisson中心、悪い閉集合のproper像の除去を独立に点検した。これとH→Eの開性から零切断近傍全体の通常B認識、未商化のμ_r-torsorを導く証明も点検した。
- 非零方向のweighted-linear認識を低次数完全対称化の部分束と商で点検した。d1の二重交換子補正を含む反交換子公式、d2の次数3・d1の次数5の多項式比較、共通ambientと規格化中心の等式を独立に確認した。
- ambientの除した交換子とz²係数による分裂核、Casimir係数に沿う微分JΩ、例外因子上の恒等、proper押下、平方零中心差が厳密にI·P_eへ入ることを独立に点検した。実targetでの一意補正から(g,source)のétale性、全零切断近傍のsource・target smoothness、fullな有限型DM商を点検した。d2・n≥3の可換部分の特異性を保持している。
- 可換点の有限型étale sliceについて、classifying mapと実横断面に適合する完成環、étale locusの有限群不変affine縮小、任意基底の相対安定化群への単射、残余gerbe同型を独立に点検した。Stacks 039M・04YY・04XBの一次本文を確認した。
- `verify_formal_geometry.py` と一般点の次元式の n=2,3,4,5 の計算は同日の成功確認を保持する。モジュライの代数性や全一般次数の証明を有限例の計算実験で確認したとは扱わない。
- 全非可換ファイバーで、coherent/Ind圏・標準有界導来dg圏・有限窓のB∞比較を一次資料の仮定に照合した。滑らかなfull部分問題の接空間のHH²への単射、半連続性、HH²-torsor補正を点検した。次数2の二次Plücker障害からI₂*→HH³の単射を得る試験環の議論、実際に持ち上がる有限窓の第一Bockstein、方向解消上のd²=τAとproperな悪条件像の除去を独立に点検した。HH³消滅・一定次元性や任意dg対象の持上げを仮定していない。
- 任意M族の反標準環のNoether性・有限表示を周期Z-代数から導き、DDL Corollary 3.16のtails-projectivityを確認した。負のHomには相対Serreと有向ACMを使う。混合同値層、U→Mの表現可能な局所有限表示monomorphism、全Artin比較からの開埋込みを独立に点検した。任意剰余体K/Cには係数体切断と有限分離拡大による有限étale降下を使い、無限代数閉包をfppf被覆にしていない。
- 普遍全同値スキームの被約性から重み付き線型性を延長する議論、対称化中心のmonic可換模型とsmoothな開条件、古典Isomへの有限閉条件による埋込みを独立に点検した。古典有限対角の入力はPoissonDP固定commitの定理9.2とLuna I §4 p.90で確認した。Keel–Mori、stabilizer preserving locus、粗空間のétale降下の適用条件を点検し、一般慣性の自明性・有限だが零切断では非平坦な慣性・実際の粗完備局所環を区別した。
- Lowen–Van den Bergh (2005) Theorems 3.1・4.1.3・6.1、Corollary 6.8、Lowen (2008) characteristic morphismのTheorems 3.22・4.18とRemark 4.20、Yekutieli Theorem 11.1の係数体条件を一次資料で確認した。Stacks 0321・04SZ・05W5・0DUA・0DUS・0DUEと、既存の02HY・04TK・0DUT・0DUWの適用範囲を確認した。
- 次数1の全lower復元、h=1での中心分母・線型ブロックの非消滅、depressed Poisson正規形と全同値商、両次数のS₅・S₄、次数2の符号二次体の捩れを内部で独立に点検した。次数1のαが全商の原始元であること、一般中間体・deck変換の不存在、分枝選択の最小拡大次数、次数1の根号復元の不存在も点検した。その有限計算証明書を保持し、今回の実行範囲は本節冒頭に記す。
- 形式証明器は使っていない。追加の中心分母・Noether開・smoothな開集合の最小非消滅条件の明示、構成族外の全O同値・低次数中心の増大層での基本シフト認識、全Mの代数性・全対象の被覆・成分数、および包括的な優先権調査は未完了。Keelerのmultiple divisors論文は書誌とabstractのみ確認済みで、本文定理の仮定・番号を推測していない。

## 保存と外部依存

GitHub mainが正本。PDF、ZIP、組版中間物、キャッシュは追跡しない。通常コミット・mainへのpushとhub更新にはGitHubの対象repoへの書込み権限が必要だが、組版・有限計算には認証不要。入力となる他研究の具体的commitと定理は [文献と依存](../research/literature.md) に記載する。
