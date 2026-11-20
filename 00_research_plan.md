# 研究方針：次数1・2の非可換del Pezzo n-fold

**2026-11-20（JST） / v0.7。再開時に最初に読む。**

正本は [uedakazushi/nc-del-pezzo](https://github.com/uedakazushi/nc-del-pezzo) のmain。研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。続いて [研究ノート](research/research_notes.md)、[主原稿](papers/nc-del-pezzo.tex)、[再現手順](docs/reproduction.md) を読む。

## A. 研究一般の原則と保存許可

1. **目標と方針。** 数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究全体の価値を最大化する。重要な変更では現在の理由と元の目標の解決済み・未解決部分を簡潔に整理し、有効な方針として書き換える。変更履歴を積み上げない。
2. **主張の確実性。** 証明済み、追加仮定付き、証明未完成、予想、計算的観察を区別する。仮定、依存、証明所在、未解決箇所を明記する。原稿の証明、今回の点検、実行した計算を別の状態とする。誤りは依存結果と関係する要約・方針にも反映し、有用な反例や障害はノートへ整理する。既知結果と本研究の成果、新規性未確認を区別する。
3. **先行研究。** 主要な主張の一次資料を読み、既存結果の仮定・範囲と本研究の貢献を Introduction で比較する。未確認の内容・書誌情報を推測しない。必要な識別子・参照箇所を保持するが、外部PDFや検索結果を大量収録しない。
4. **公表用論文。** 原則として日本語 LuaLaTeX を用い、十分な証明と明確な仮定を備える。現在の結果を理解しやすい順に統合し、数学的価値に応じて分割・統合する。有効で公表価値のある成果・証明を軽量化のために削らない。未完成原稿を完成と扱わない。
5. **研究ノート。** 現在有効な着想、補題、例、計算、反例、本質的な障害、文献比較を整理する。日誌・実況・全試行履歴・重複説明は収録しない。再取得が難しい情報は保持する。論文にある完全な証明は再掲せず参照する。
6. **研究再開。** 現行の一式から目標・到達点・核心・次の着手方法を理解できるようにする。必要な知識を会話だけに残さず、記法・ファイル名・参照・主張の状態を整合させる。
7. **現行一式の軽量化。** 方針・ノート・論文と必要なソース、文献、コード、入力、証明書、再現手順だけを保持する。旧版ZIP、旧稿、バックアップ、ログ、編集記録、入れ子ZIP、キャッシュ、中間生成物は追跡しない。数学的内容と検証可能性は維持する。Library段階のbundleには組版済みPDFも含める。
8. **保存許可と管理段階。** GitHub管理前は区切りごとに自己完結した現行bundleを承諾不要でLibraryへ保存する。ユーザーが本repoを指定した現段階では `main` が正本であり、通常コミットとmainへのpushを承諾不要で行う。15〜30分を目安に区切り、並行変更を保持する。force pushとGitHub Actionsの追加・起動は行わない。Libraryへの定常的な二重保存・ZIP作成は不要で、push失敗時の緊急保存か明示的依頼に限る。既存Libraryファイルは明示的指示なしに削除しない。
9. **原稿配置と再現可能性。** 主原稿は `papers/nc-del-pezzo.tex`。research-hubの `papers/paper-template.tex`、`papers/README.md` とlatexmk・VS Code設定を参考にし、LuaLaTeX・latexmk・LaTeX WorkshopでPDFとSyncTeXを `build/` に生成する。改名時はinput・文献・root指定と全案内を更新する。日付・版、生成、証明点検、計算、組版、GitHub反映、緊急Library保存は別々の確認状態とする。
10. **hub更新義務。** 区切りには本repoの原稿・ノート・方針・READMEを先に保存し、続いてhubの該当項目へ到達点、確実性、障害、次の一手、依存、正本・再開先、実際の資料確認日を反映する。最新hubと並行変更を確認し、詳細todo・証明・履歴を重複させない。実質的変化なしの日付更新は不要。成果保存とhub更新の成否を別々に確認し、失敗時は未反映項目と理由を報告する。

## B. この研究の目標と定義

一般のn≥2に対して、次数1・2の非可換del Pezzo多様体を構造対象Oだけを標識したAbel圏として扱い、全O保存同値によるモジュライと既約成分を研究する。偏極・豊富列・AS包絡は存在条件と選択データを区別する。

主原稿 `def:ample-model` はHilbert関数を持つ豊富列型の問題A、`def:nc-dp-stack` は標準compact圏の相対Serre・反標準豊富性・Serre周期n−1・有向ACM条件を備えたnc多様体の問題Mを定義する。重み付きAS超曲面の表示を持つ部分問題は別に記号化する。fppf stack化によるモジュライ問題の定義と、代数スタック・有限型atlasの構成は別である。

元の成分数決定という目標のうち、可換点における全Abel変形群oid、有限自己同型群による形式商、全Artin変形の中心超曲面表示とnc多様体条件、形式分枝数は解決した。有限パラメータでは、両次数の分離型族と一般楕円型族について、普遍PBW・ambient CY・正則な中心商・強Noether性・相対tails・Serre公式を得た。一般楕円型では最高次point curveの解消と相対twisted homogeneous coordinate ringを使い、さらに曲線の積の評価イデアルから積代数のNoether性も証明した。この入力と相対Serre双対により、対角の有限部分解消を可換ファイバーで分裂させ、その分裂を有限開近傍へ持ち上げた。従って両族とも、全n≥2で滑らかな全可換模型の有限型開近傍に実際のsmooth properなnc del Pezzo族を与える。

一方、これらの一方向の中心商族は共通量子化パラメータhを持つため、可換点でのPoisson Kodaira–Spencer像が高々1次元となり、全変形に対するsmooth atlasではない。この具体的障害を踏まえ、次数1の一般topについても、Stephensonの分類から明示的な有限AS開条件を得て、23未知数の中心構成、次数1線束による相対THCR、有限被覆からの強・積Noether性の降下まで進んだ。さらに両次数の全独立Poisson方向を直接含む有限型ambient族と全一次中心商を構成した。次数1の開条件は `(1+A₄(D))(5+A₄(D))≠0`、次数2は四次式の偏極と交代形式から定まる作用素Tについて `g₂=det(1+4T)≠0` と明示できる。これらのambient条件は楕円判別式を可逆化せず全零切断を含む。現在の核心は、この同じambient族上での中心元の同時持上げである。元の全体の成分数決定には、全O同値による商、可換locusに接しない成分の検討がなお必要である。中心商のsmoothnessの開集合は存在を証明した段階であり、具体的な判別式や全有限hのsmoothnessは得ていない。

## C. 主要到達点と確実性

| 主張 | 状態・仮定 | 証明の所在 |
|---|---|---|
| framed全Abel Artin形式環は、d1で滑らかな形式円板、d2で通常の形式円板×Plücker錐の完備化 | 証明を記述し、一次比較定理の適用条件を点検。通常の局所Artin環全体 | `thm:abel-formal-ring` |
| 各可換点は一形式分枝、d2・n≥3で特異、二次障害Q∧Q | 上の形式環から証明。全ncスタックの成分定理ではない | `cor:abel-quadratic-obstruction` |
| 任意の冪零係数上の中心商は次数ごとに自由、任意基底変更と両立 | monic分裂で証明、DVRのtorsion-free判定を一般化していない | `thm:nilpotent-universal-quantization` |
| Poisson零切断の形式完備化にO-marked tailsの族が降下 | 固定formality、正規形の線型群、次数スカラーのcoherent trivializationで証明 | `thm:quantization-descent` |
| 構成した量子化自体が全framed Abel Artin変形群oidを分類する | 同型類の自然な全単射を、HH¹消滅による自己同値剛性で群oid同値に強化 | `thm:concrete-quantization-all-artin`, `thm:quantization-framed-groupoid` |
| 全Abel Artin変形は通常の次数付き中心超曲面表示を持つ | 表示の存在を証明。相対augmentation Ext条件付き。表示の一意性・絶対AS正則性は主張しない | `cor:all-artin-weighted-hypersurface-presentation` |
| 枠を忘れた形式群oidは `[Spf R_X/Aut(X)]`、粗商は正規CM整域 | 有限群不変sliceと既存Poisson商から証明。一般点のμ₂粗商は両次数で特異 | `thm:unframed-formal-quotient`, `cor:generic-nc-formal-sign-quotient` |
| 全Artin中心商の飽和性・有向ACM・正周期豊富性・compact生成・smooth proper性 | 固定被覆元のOre局所化、有限Čechと対角dg加群のcompact持上げで証明。後者はDDL Proposition 5.8の論法を直接記述。任意基底変更に両立 | `thm:artin-saturation-acm`, `lem:dg-compact-nilpotent-lift`, `thm:artin-smooth-proper` |
| 相対Serre公式 `S_R≅(−(n−1))[n]` と、M・超曲面部分問題・全Abel変形のArtin完成の一致 | smooth properなperfect圏の対角bimoduleをHH¹=0で比較。全Db(coh)への主張ではない | `prop:serre-from-smooth-proper-lift`, `thm:all-artin-are-nc-dp` |
| Artin近傍の全O同値は通常のgraded同型を次数スカラーで割ったもの | 基本シフトをHH¹剛性で認識し、飽和性で復元。普遍中心条件不要 | `prop:artin-full-graded-recognition`, `thm:all-artin-are-nc-dp` |
| 全O同値は反標準軌道環から認識可能 | 相対perfect/Serre、反標準豊富性、section復元等の追加仮定付き | `prop:ncdp-relative-anticanonical-hom` |
| 任意指数rのVeronese同型の持上げはμr-torsor | 二つ以上の中心一次変数、中心多項式環上平坦、普遍的低次中心条件の下で証明 | `thm:ncdp-veronese-lift` |
| dは反標準Euler多項式から内在的に復元でき、族で局所定数 | 一般には反標準ACM・相対perfect条件付き。定義したMでは条件を満たし次数1・2が開閉分解 | `prop:ncdp-intrinsic-degree`, `cor:defined-moduli-degree-separation` |
| 冪零段階の中心商は左右で唯一のaugmentation Ext `R(n−1)` を次数n+1に持つ | R分裂Koszul持上げと平坦中心商のchange of ringsで証明。通常の絶対AS正則性やSerre公式ではない | `prop:nilpotent-weighted-as`, `prop:flat-central-hypersurface-ext` |
| ambient量子化は無捩れな重み付き相対CY同型を持つ | Kontsevich–Shoikhetの対と体積形式を固定。発散零・有限鎖twist・有限自由対角分解による証明。任意冪零係数・任意基底変更 | `thm:nilpotent-ambient-cy`, `cor:dp-ambient-cy` |
| 固定した全ての非零Poisson方向の形式一般ファイバーはCasimir多項式環を普遍中心に持つ | 古典generic active fiberの幾何学的整性とh係数帰納で証明。Artin商・有限複素hへの特殊化には適用しない | `thm:formal-generic-center`, `cor:formal-generic-veronese` |
| 負の補助次数を持つJacobian括弧の有限パラメータ量子化 | 任意中央係数、任意基底変更、全有限hで有限表示・自由基底。グラフの補助次数評価とmonic商で証明 | `thm:negative-auxiliary-algebraization` |
| 両次数の分離型potentialの明示的中心元と普遍PBW基底 | P≤5、Q≤3。d2はp5=0。唯一のoverlapと全係数多項式恒等式で証明し、厳密計算を実行 | `thm:explicit-finite-pbw-casimir` |
| 全n≥2で滑らかな可換点を含む有限型平坦Abel族 | 明示的な偏微分検査と基底・Gabriel商で証明。有限hでMの全条件を満たす主張ではない | `prop:finite-family-smooth-points`, `prop:finite-pbw-abel-family` |
| 規格化した有限型族の全非零hで中心はCasimir多項式環 | 最高記号のPoisson中心と次数別小行列式で任意基底変更まで証明。n≥3でVeronese持上げの代数的仮定が成立 | `thm:finite-parameter-universal-center`, `cor:finite-parameter-veronese-input` |
| 分離型ambientは全有限hで相対bimodule CY | potential対角複体のfiltered Koszul完全性・自己双対性、中心差の正則列で証明。tails Serreとは区別 | `prop:finite-separated-relative-cy`, `prop:finite-separated-absolute-cy` |
| 分離型中心商の相対局所コホモロジー、飽和性、ACM、χ、全シフト豊富性 | 全有限h・任意の許されるnoetherian基底変更で証明。非正則基底にも相対双対を直接適用 | `thm:finite-relative-local-cohomology`, `thm:finite-tails-cohomology`, `prop:finite-full-shift-ample` |
| 分離型tailsのcompact生成、相対proper性、Serre公式S=(−r)[n] | smooth性を仮定せず、局所化bimoduleの双対を計算。有限個のtwistからなるcompact生成元も構成 | `prop:finite-window-proper`, `thm:finite-tails-relative-serre` |
| 正周期rの相対豊富性は滑らかな可換点の有限型開近傍で成立 | 有限個の次数の余核の消滅と相対Serre消滅で証明。任意の許される基底変更 | `prop:finite-periodic-generation`, `cor:finite-periodic-ampleness` |
| 次数2の一般楕円型topと任意lower項を持つ普遍PBW・ambient CY・中心商族 | 各古典楕円型点の有限型開近傍。中心元の分母はtop係数だけに依存。任意非被約基底変更でも平坦・中心元正則 | `lem:elliptic-universal-lower-pbw`, `thm:elliptic-finite-central-family` |
| 上記次数2族は全nで稠密開の古典Poisson対を半古典極限に持つ | lower係数へn−1個の中央変数の斉次多項式を代入。全nc点のatlasではない | `cor:elliptic-general-dimension`, `prop:elliptic-semiclassical-coverage` |
| 次数2の一般楕円型族の強Noether性、相対tails、有限compact生成元 | 各古典楕円型topの有限開近傍。二重対角線の解消・相対THCR・Keelerの定理・中心/filtered持上げにより任意noetherian基底変更で証明 | `thm:elliptic-relative-thcr`, `cor:elliptic-strong-noetherian`, `thm:elliptic-relative-tails` |
| 次数2一般楕円型族の積代数 `Bᵒᵖ⊗B` の左右Noether性 | 二重切断環の評価イデアルと相対Fujita消滅、二つの中央正則元、filtered持上げから証明。任意noetherian基底変更 | `lem:elliptic-bisection-noetherian`, `cor:elliptic-product-noetherian` |
| 両次数の分離型族と一般楕円型族は、滑らかな可換点の有限開近傍でsmooth proper | 全n≥2。有限部分対角解消・相対Serre双対・HH¹(X)=0を使う。全有限hへの主張ではなく、具体的な開条件の計算も未了 | `lem:serre-pseudoperfect-to-perfect`, `thm:finite-family-smooth-open` |
| 上記開近傍を縮めれば実際の重み付き超曲面型nc del Pezzo族、幾何学的coherent次元はn | 反標準豊富性の開集合と交わらせる。任意の許されるnoetherian基底変更。非正則基底上の全Db(coh)と相対perfect圏の同一視はしない | `cor:finite-family-ncdp-open` |
| 次数1の一般楕円型top・任意lower係数の普遍PBW・ambient CY・正則中心商 | Stephensonの分類から `Δ(1+αh⁴)(5+αh⁴)≠0` の有限AS開を具体化。中心は次数9以下・23未知数、追加分母はtopだけに依存。任意基底変更・全nの中央係数代入を許す | `lem:degree-one-elliptic-top-as-open`, `thm:degree-one-finite-central-family`, `cor:degree-one-elliptic-general-dimension` |
| 次数1一般楕円型の相対THCR、強・積Noether性、相対tails・Serre・有限窓 | 次数1線束の曲線表示は階数6の有限忠実平坦被覆上。Noether性は元の最高次開集合へ降下。全lower・全n・任意noetherian係数変更 | `thm:degree-one-relative-thcr`, `cor:degree-one-product-noetherian`, `thm:degree-one-relative-tails` |
| 両次数の全独立Poisson方向を含む有限型ambient族 | 全可換係数の零切断を含む明示的な有限主開で普遍的に次数別平坦。d1は `(1+A₄(D))(5+A₄(D))≠0`、d2は `g₂=det(1+4T)≠0`。活性binary quarticでは `g₂=1−16Ih⁴+128Jh⁶`。有限中心元・相対tailsは未証明 | `thm:simultaneous-degree-one-ambient`, `thm:simultaneous-poisson-ambient` |
| 上の同時ambient族の一次厚化における全Poisson方向の中心商 | 古典方程式の対称化が中心かつ普遍正則。全有限基底への持上げとは区別 | `prop:simultaneous-first-order-center` |
| 一つのhを持つ中心商族は可換点でsmooth atlasにならない | Poisson Kodaira–Spencer像は高々1次元、全変形の通常の可換変形による接空間商はnまたはbinom(n+1,2)次元 | `prop:one-parameter-atlas-obstruction` |

一般原理のLowen–Van den Bergh・Lowen・De Deken–Lowen・Yekutieli・Kontsevichと、入力となるPoisson構造定理は既知・既存の入力である。曲面の接空間次元10・9も先行研究で既知。一般nの適用・復元・降下の新規性について包括的な優先権確認は未了。

## D. 未解決の核心と次の一手

1. **同時ambient族の中心元。** 両次数の全独立Poisson方向を含む普遍的に平坦な有限表示を得た。次はその同じ代数上で、内部次数6または4の古典方程式を中心元へ持ち上げる。次数1はD方向、次数2はPlücker錐の頂点を含める。一次厚化の中心元を出発点とし、有限個の次数の中心方程式とその可解性を調べる。次数2の降下候補は研究ノート第17項にあり、最初にEtingof–Ginzburg Proposition 8.1.1(i)の中央多項式係数への相対化と、同じambient内での次数4の規格化解を確認する。貼合せのH¹消滅と、未証明の局所中心持上げを区別する。別の形式量子化に中心があることを、現在のambientの解と読み替えない。
2. **同時中心商から圏の局所完全性へ。** 中心元が得られた後、その普遍正則性、相対tails・smoothnessと全Artin変形への写像を証明する。既存の一方向族には強・積Noether性と対角分裂の方法が揃ったが、全方向ambientへの移植には改めて入力が必要である。全一次接方向の実現だけで高次の形式的完全性やsmooth atlasを結論しない。
3. **有限開集合の明示と大域的な復元。** 有限生成元から作る対角の部分解消・持上げ射を低次元で具体化し、smoothnessを保証する有限個の行列条件を求める。一般楕円型の中心は有限位数パラメータで増大し得るため、分離型の普遍中心定理を転用しない。全O同値による商、一般nc点の被覆、可換locusに接しない成分を別々に調べる。形式一分枝性から全成分数を推論しない。
4. **公表範囲と先行研究。** 全Artin群oid、両次数の相対楕円曲線、積Noether性、有限開近傍のsmoothness、全方向ambient族を現在の論理順序で統合した。既存のfiltered CY・楕円量子化・AS Z-代数との比較を進める。Sklyanin中心元、固定topのPBW性、σ-amplenessとFujita消滅は既知であり、普遍係数の比較・一般nへの適用・対角分裂の組合せの優先権は未確認。大域分類は未解決として明記する。

## E. 依存・再開・検証

- 相対Poisson錐・商・自己同型：`poisson-del-pezzo` main `4834ea4f3e13bff4d6c5793cec9b169d8f1ad56f`、主原稿v1.4の定理7.3・8.8、補題8.7、注意8.5、命題9.4。
- O-marked枠組み：`nc-cubic-threefold-moduli` main `6c35d2c84671c2538e61836a6bf3a511392eacce`、主原稿v22。三次三様体固有の次数一生成・指数2・残余圏の結論を無条件に輸入しない。
- 一次資料・具体的な適用条件・優先権未確認点は [文献と依存](research/literature.md)。証明の重複は研究ノートへ置かない。
- `make verify` はn=2,…,8のHilbert/monic基底・Euler差分・二次障害・符号粗商の接空間次元と、分離型の全係数PBW overlap・中心交換子・内部次数・補助次数を検査する。さらに三次Sklyanin中心元の自由代数内の九項証明書、パラメータ置換と可換極限を厳密計算する。分離型とSklyanin中心の検算はhの有限jetではない。`verify_elliptic_curve.py` はpoint curveの行列式、blowup、分母を払ったshiftの恒等式を厳密検算し、σ⁴の非自明性だけは明示したmod h²計算で確認する。`verify_degree_one_top.py` はWeierstrassからStephensonへの変数変換、関係式のイデアル、AS開多項式、cyclic syzygyを有理係数の自由代数で厳密に検算する。`verify_degree_one_curve.py` は解消曲線の両chart・無限遠因子・shiftと関係式を全係数の恒等式で検算し、σ⁶の非自明性だけmod h²を使う。一般の証明を有限次元の数値例で代替していない。
- 組版・PDF確認の実施状況と環境は [再現手順](docs/reproduction.md)。生成・証明点検・計算・組版・GitHub反映・hub更新はそれぞれ確認する。
