# 研究方針：次数1・2の非可換del Pezzo n-fold

**2026-11-20（JST） / v0.16。再開時に最初に読む。**

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

元の成分数決定という目標のうち、可換点における全Abel変形群oid、有限自己同型群による形式商、全Artin変形の中心超曲面表示とnc多様体条件、形式一分枝性は解決した。両次数の全独立Poisson方向を直接含む有限型ambient族を、次数1では `(1+A₄(D))(5+A₄(D))≠0`、次数2では四次式の偏極と交代形式の縮約による `g₂=det(1+4T)≠0` 上で構成した。同じambientに全方向中心を貼り合わせ、全可換係数の零切断を含む有限主開で、普遍正則・次数別有限局所自由な中心商を得た。次数2はGrassmann上のH¹消滅、次数1は普遍4次中心jetと5次以後のH¹消滅を使う。この同じ有限族のArtin基底変更が全framed Abel変形を実現する。

有限基底上の圏論的性質も全方向族について得た。次数1の尖点を含む整なGorenstein曲線、次数2の可約・非被約曲線を含む有限平坦二重被覆から、全topの相対THCRとその積のNoether性を証明した。方向の頂点では、次数別有限性とKrull交叉、および完成と頂点外を合わせた忠実平坦被覆を使う。これにより任意Noether基底変更後の強・積Noether性が成立する。有限な次数零Hom複体から同じambientの相対projective対角と無捩れCY同型を構成し、全方向中心商の相対tails・Serre公式・有限compact窓を得た。さらに滑らかな全可換模型の零切断を含む有限型開近傍では、同じ族は実際のsmooth properなnc del Pezzo族となる。

一方向族のPoisson Kodaira–Spencer像が高々1次元という障害は、全方向族と全Artin比較により解消した。分離型の明示的中心式・普遍中心と一般楕円型の具体的表示も保持する。全O保存同値を反標準Veroneseから認識し、方向のproper解消と基本シフトを保つ矢の開性によって、通常Bによる全同値認識を可換零切断全体の一つの開近傍へ広げた。weighted-linear認識とCasimir Jacobianによる持上げで全source・targetの滑らかさを証明し、全滑らかな可換模型を含む整な有限型DMスタックUを得た。その次元はb(n,1)+n、b(n,2)+2n−1である。次数1と次数2のn=2では滑らか、次数2のn≥3では可換部分にPlücker特異性が残る。

Uの全幾何学的点で全Abel Artin変形を同じ族が実現する。Abel Hochschildと有限窓dg模型を比較し、次数2・n≥3では二次Plücker障害の微分に一致する第一Bocksteinの階数を方向解消上で一様化する。任意のM族に対してもSerre周期・Noether性から有限表示反標準環とsection復元を得るため、全Mの対角は局所Noether site上でアフィン有限表示となる。混合同値層によりU→Mを表現可能な局所有限表示monomorphismとし、任意の剰余体を含む全点Artin比較から開埋込みを証明した。全Mの代数性を仮定せず、形式的普遍性だけから開性を結論しない。

さらに中心方程式の完全対称化から可換模型を構成し、全同値層をその古典Isomへ閉埋込みする。零切断を保った一つの縮小上でUは有限対角を持ち、分離的で整な有限型粗空間M^ncを得る。stabilizer preservingなétale sliceから、実際の粗空間のétale局所模型T/Aut(X)と完備局所環R_X^Aut(X)を得る。一般安定化群は自明であり、非零方向には稠密な滑らかな代数空間の開部分がある。

可換模型F^shにJacobian Poisson構造を付けることで、全O同値と任意の非被約基底変更に両立する射Θ:U→Pを構成した。全可換点でのframed完成は同型であり、全零切断を保つ開縮小後にΘは表現可能・分離的・étaleかつstabilizer preservingとなる。Poisson零切断のscheme論的な逆像も可換零切断に一致する。shadow射sh:U→Dはschemeで表現可能なquasi-affine平坦全射で、純相対次元はnまたは2n−1である。幾何学的ファイバーはJacobi錐へのétale射を持ち、正規・Cohen–Macaulay・Gorensteinとなる。全ファイバーの既約性は主張しない。

粗比較射M^nc→NもCartesianなétale射であり、M^ncは正規Cohen–Macaulayなquasi-affine schemeとなる。粗shadowの平坦点集合は古典粗空間M^clのsmooth locusの逆像にちょうど一致する。次数2・n≥3では可換零切断のblow-upが滑らかなDMスタックによる解消で、例外因子はD上の相対Gr(2,n+1)、法束はO(−1)、discrepancyはnである。Uはsmooth atlasの意味でGorensteinかつterminalとなる。粗空間のGorenstein性・terminal性は別問題である。

両次数で全n≥2のPoisson比較の一般次数を決定し、δ_(n,1)=5、δ_(n,2)=4を得た。規格化中心torsorと全同値群oidに、次数2のbinary quartic正規形、次数1のy二次平行移動による正規化、両次数の全lower復元を組み合わせる。一般モノドロミーはS₅・S₄、Galois閉包の次数は120・24である。次数1では内在的α=A₄(D)が原始元となり一般逆像は根号で選べず、両次数で中間体と非自明なdeck変換はない。符号二次体も明示した。大域的一意復元や次数の決定から、有限被覆の開像・境界と構成近傍外の成分へ研究の重点を移す。全Mの被覆・代数性・成分数は未解決である。

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
| 同じ有限型nc族の全O同値は反標準VeroneseのIsom/G_m | smooth proper開V全体。compactなSerre軌道と豊富列の復元、tailsのfppf降下を証明。V×V上アフィン有限表示、任意基底変更と両立 | `thm:finite-anticanonical-isom`, `lem:veronese-finite-presentation`, `lem:graded-isom-affine-quotient` |
| 全同値スキームは零切断を保った開近傍でquasi-finiteかつunramified | 安定化群の単位余接加群の支持を除く。各幾何学的自己同値群は有限。さらに下記の古典Isomへの閉埋込みによりanchorの有限性を証明。flatnessは要求しない | `lem:finite-type-equivalence-unramified-open`, `cor:finite-equivalence-unramified`, `thm:zero-neighborhood-finite-diagonal` |
| 同じ開近傍の相対HHは負次数零・HH⁰=基底・HH¹=0 | smooth properな有限dg模型のHochschild複体と単位coneのTor振幅。任意非平坦affine基底変更。nc点の存在するperfect対角持上げにも剛性 | `prop:simultaneous-hochschild-rigid-open`, `cor:noncommutative-diagonal-artin-rigidity` |
| 非零方向でBは中央Sym K上普遍平坦、固定q中心条件の非空稠密開が存在 | 被約普遍基底で活性filtrationと一定Hilbert関数からP-加群分裂を構成し任意基底へ移す。δ_q/hの古典Poisson中心で全smooth f・全非零rayとの交叉を証明 | `lem:simultaneous-central-flatness`, `thm:finite-low-center-open` |
| 非零方向の稠密開で全O同値は通常BのIsom/G_m | n≥3でq=n−1の普遍中心条件と相対Veronese持上げを適用。n=2はV全体で成立。全中心最小性は不要 | `cor:finite-full-graded-recognition` |
| 零切断全体を含む一つの開近傍で通常Bから全同値を認識 | 固定qの除した交換子を方向解消上の有限束で扱い、properな悪条件像を除く。q=n−1とH→Eの開性・零切断の同値不変性を併用。任意非被約基底を含む | `thm:low-center-zero-neighborhood`, `cor:zero-neighborhood-full-graded-recognition` |
| 可換矢の完成はR_X[[u_g,v_g]]、sourceとtargetは相対次元gでsmooth | full coefficient基底。g=n²または(n+1)²。classifying mapに沿う形式積と全framed射の一意性を使用。Plücker特異性は残る | `lem:full-coefficient-formal-slice`, `thm:equivalence-source-formal-smooth` |
| 可換零切断は全同値でschemeとして保存 | 非零方向の中央一次非零因子から幾何学的saturation、Artin graded認識とzの自由直和因子から方向イデアルの一致 | `lem:commutative-zero-equivalence-saturated`, `cor:zero-section-scheme-saturated` |
| 零切断を保った一つの開で全source・targetが相対次元gでsmooth | 低次数Sym同型からweighted-linear化、中央係数差の同定、ambient中心の分裂核とCasimir Jacobianのproper一様化、小拡大補正。全矢を保持 | `lem:normalized-ambient-center-near-zero`, `prop:casimir-jacobian-zero-neighborhood`, `thm:full-source-smooth-zero-neighborhood` |
| 全可換模型と全Artin変形を含む整な有限型DMスタックU | 次元b(n,1)+nまたはb(n,2)+2n−1。d1とd2・n=2はsmooth。d2・n≥3は可換locusが非smooth locusの被約構造。全M内での開性は下記の全点比較と混合同値層で証明 | `thm:zero-neighborhood-full-dm`, `thm:zero-neighborhood-open-full-moduli` |
| 可換点の実際の有限型étale slice [T/Aut(X)]→U | Aut(X)不変横断補空間とaffine縮小。representable étaleで残余gerbe上同型。有限慣性のproper性により全点でstabilizer preservingとなる縮小を取れる | `cor:finite-etale-slice-near-classical`, `cor:stabilizer-preserving-slice-generic-trivial` |
| 非零方向の非空稠密開のfull部分問題にsmooth irreducible有限型DM表示 | 零切断近傍のDM表示から非零対象開へ制限。Uおよび全Mの開部分スタック。さらに一般安定化群は自明で、稠密開は滑らかな代数空間 | `thm:generic-full-dm-stack`, `thm:zero-neighborhood-open-full-moduli`, `cor:stabilizer-preserving-slice-generic-trivial` |
| genericにfinite étale inertiaとsmooth irreducibleな粗代数空間 | 全Uの有限慣性・分離粗空間へ強化。一般安定化群は自明。次元b(n,1)+nまたはb(n,2)+2n−1 | `cor:generic-finite-inertia-coarse`, `cor:zero-neighborhood-separated-coarse`, `cor:stabilizer-preserving-slice-generic-trivial` |
| 基本シフトを保つ矢は全同値スキームの開部分群oid | H=Isom_gr(B)/G_m→Eはmonomorphismで、HH¹剛性とHH⁰による比較調整でformally étale。方向解消を加えることで、上記の零切断近傍全体のH=Eへ強める | `thm:ordinary-graded-arrows-open` |
| 有限型群oid商はlimit preserving、可換特殊fiberの形式対象はeffective | 全scheme上の商stackとNoether site上の圏論的解釈を区別。さらに任意の完備Noether局所基底上のM族も、可換閉fiberを持てば構成模型と実際に同値。混合同値層のaffine有限表示を使用 | `lem:finite-groupoid-limit-preserving`, `prop:commutative-formal-family-effective`, `cor:arbitrary-classical-family-effective` |
| Uの全幾何学的点で全framed Abel Artin変形を同じ有限族が実現 | Abel Hochschild・有限窓dg比較、HH²の下限と上半連続性。d2・n≥3はPlücker二次障害の微分と第一Bockstein、方向解消による階数の一様化。任意剰余体を扱う | `thm:all-points-abel-artin-versality`, `lem:abel-versality-arbitrary-residue-field` |
| 任意M族の反標準環は有限表示で圏を復元、全Mの対角はaffine有限表示 | 局所Noether C-schemeのfppf site。Serre周期による軌道環のNoether性、augmentationの有限syzygy、相対導来Serreと有向ACM、豊富列復元 | `lem:arbitrary-anticanonical-finite-presentation`, `prop:full-moduli-affine-diagonal` |
| U→Mは全可換模型を含む開埋込み | 混合同値層からrepresentable lfp mono、全点Artin比較から形式的étale。全Mの代数性を仮定しない。任意M族の可換fiberの周囲にもZariski近傍を得る | `prop:constructed-substack-representable-lfp`, `thm:zero-neighborhood-open-full-moduli`, `cor:familywise-classical-neighborhood` |
| 零切断近傍のUは有限対角を持つ分離的有限型DMスタック | 全graded同型のweighted-linear性を被約な全同値スキームへ延長。対称化した中心方程式の滑らかな古典Isomへ閉埋込み。古典対角の有限性を使用 | `lem:all-graded-isom-weighted-linear`, `lem:commutative-central-shadow`, `thm:zero-neighborhood-finite-diagonal` |
| 可換モジュライDへのshadow射U→Dは表現可能 | 選んだ中心元と完全対称化に付随し、零切断では元の可換模型。全安定化群の単射から表現可能。下記のPoisson比較によりschemeで表現可能なquasi-affine射へ強化 | `prop:representable-commutative-shadow`, `cor:shadow-flat-cone-fibers` |
| Uは分離的で整な有限型粗空間M^ncを持ち、一般安定化群は自明 | 有限慣性とKeel–Mori。一般可換点のμ₂が方向に符号作用し、stabilizer preserving slice上の非零方向では自由。零切断での慣性の平坦性は要求しない | `cor:zero-neighborhood-separated-coarse`, `cor:stabilizer-preserving-slice-generic-trivial` |
| 可換点の実際の粗空間はT/Aut(X)をétale局所模型に持ち、完備局所環はR_X^Aut(X) | 粗射との正方形はCartesian。可換点で正規CMかつ解析的一分枝。一般μ₂点は係数方向とPoisson錐の2次Veronese商の積の開部分 | `cor:algebraic-coarse-local-model` |
| 中心方程式のshadowは全同値に関手的なPoisson構造を持つ | 全基底でJacobian括弧のJacobi恒等式とweighted-linear同型の厳密な変換則を証明。ρ反自己同型でz偶性を得る。Poisson零切断の逆像はschemeとして可換零切断 | `lem:shadow-jacobian-poisson`, `lem:shadow-even-z`, `prop:poisson-shadow-morphism` |
| 全零切断を保った縮小でΘ:U→Pは表現可能・分離的・有限表示・étaleかつstabilizer preserving | 全可換点のframed完成同型とétale locusの開性、Poisson側の有限慣性から証明。像は全Poisson零切断を含む開部分。下記の一般次数5・4により開埋込みではない | `prop:poisson-shadow-formal-comparison`, `thm:poisson-shadow-etale` |
| sh:U→Dはquasi-affine平坦全射、純相対次元nまたは2n−1 | 幾何学的ファイバーはA^nまたはPlücker錐へのétale射を持ち、正規CMかつGorenstein。d1およびd2・n=2はsmooth、d2・n≥3の相対非smooth locusの台は零切断。全ファイバーの既約性は未証明 | `cor:shadow-flat-cone-fibers` |
| M^ncは正規CMなquasi-affine schemeで、粗shadowの平坦点はM^clのsmooth locusの逆像に一致 | 粗比較射M^nc→Nは分離的étaleかつ粗射との正方形はCartesian。PoissonDP定理9.2・9.6とZariski主定理、平坦性の忠実平坦降下を使用。粗ファイバーの被約性は主張しない | `thm:coarse-shadow-etale-flat-locus` |
| d2の零切断blow-upはn≥3で滑らかなDM解消、UはGorenstein terminal | Θの平坦基底変更でPoissonDP定理10.3・命題10.4を移す。例外因子は相対Gr(2,n+1)、法束O(−1)、discrepancy n。d2・n=2は既にsmooth。粗空間のterminal性は未判定 | `cor:nc-shadow-zero-blowup-resolution` |
| 有限一般次数δが1であることとΘの開埋込み性は同値 | 整正規な粗schemeとZariski主定理を使用。両次数でδ=5・4と決定したため開埋込みではない。μ₂同変なt↦t+t³は局所条件だけでは次数を決められない一般反例 | `prop:poisson-shadow-degree-one-criterion`, `ex:etale-shadow-not-open-immersion` |
| 指定した最高活性二係数写像の一般次数は、d1で5、d2で4 | h=1、中央変数とlowerなし。d1はPoisson側のy二次項を除く正規化後、d2は対称binary quarticの同座標shadow。自由語証明書・体の塔・互いに素性を証明し厳密計算を実行。全Θへの移行は下記の別証明を使う | `prop:degree-one-shadow-top-center`, `prop:degree-one-shadow-top-degree-five`, `prop:binary-shadow-generic-degree-four` |
| 次数2の選択した中心族では全lowerが三角的に有理復元され、固定座標の全係数写像も一般次数4 | 整列定数項・z²係数の一意な規格化、topだけの分母、lowerの重み、hの尺度変更を使用。中央一次変数への斉次代入を含む | `cor:binary-shadow-lower-triangular` |
| 次数2の全Poisson比較の一般次数は全n≥2で4 | 規格化中心torsorへのétale写像とexact fullEq、共通nc開、V₄安定化群による全binary quarticへの移行、全lower、同じ群のCartesian商を使用。一般4対象は全O保存Abel同値で非同値。開埋込み・有理切断はなく、可換点を含むZariski近傍で有限・properにはならない | `thm:degree-two-shadow-degree-four`, `cor:degree-two-four-sheet-consequences` |
| 次数1のPoisson比較の一般次数は全n≥2で5 | 全lowerの重み三角復元、h尺度変更、depressed Poisson形と同じ全座標群、中心torsorと共通開を使用。内在的α=A₄(D)が逆五次式の原始元。一般5対象は全O保存Abel同値で非同値 | `thm:degree-one-shadow-degree-five`, `prop:degree-one-intrinsic-inverse-quintic` |
| 一般モノドロミーは次数1でS₅、次数2でS₄ | Sylvester判別式、有限体Bézout、単純分岐、全lowerと全同値商を用いて証明。Galois閉包120・24、中間体なし、deck変換自明。両符号二次体を明示。次数1は根号による一般復元不可 | `sec:shadow-monodromy`, `cor:shadow-symmetric-field-consequences` |
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
| 両次数の全独立Poisson方向を含む有限型ambient族 | 全可換係数の零切断を含む明示的な有限主開で普遍的に次数別平坦。d1は `(1+A₄(D))(5+A₄(D))≠0`、d2は `g₂=det(1+4T)≠0`。活性binary quarticでは `g₂=1−16Ih⁴+128Jh⁶`。特異な最高次式も許す | `thm:simultaneous-degree-one-ambient`, `thm:simultaneous-poisson-ambient` |
| 上の同時ambient族の一次厚化における全Poisson方向の中心商 | 古典方程式の対称化が中心かつ普遍正則。全有限基底への持上げとは区別 | `prop:simultaneous-first-order-center` |
| 同じambient族の内部次数4・6の中心元と普遍正則な有限中心商 | 全可換係数・全方向の零切断を含むGL不変な有限主開。追加分母は存在証明。任意非被約基底変更後も正則・次数別有限局所自由 | `thm:simultaneous-degree-two-central-family`, `thm:simultaneous-degree-one-central-family` |
| 次数1の普遍4次中心jetと全高次の貼合せ | 全係数有理式の3交換子をmod h⁶で厳密検証。H¹(Sym⁶K(m))=0 (m≥5)と局所中心から全高次を構成。jetだけを全中心公式としない | `lem:degree-one-fourth-center-jet`, `lem:degree-one-center-high-cohomology` |
| 同じ有限中心商族が全framed Abel Artin変形を実現 | 滑らかな可換点の横断sliceに制限。DDL Proposition 4.4、初交換子、全形式環の自己同型を比較。全方向族の有限基底上のtailsとは別 | `thm:simultaneous-central-all-artin` |
| 全topの相対THCRと強・積Noether性 | d1は階数2被覆で節点・尖点を含む整なGorenstein曲線。d2は可約・非被約曲線を含む有限平坦二重被覆。全topの零切断を含む有限開、全lower・中央多項式係数を許す | `thm:degree-one-all-top-thcr`, `thm:degree-one-all-top-noether`, `thm:degree-two-all-top-thcr`, `cor:degree-two-all-top-strong-product` |
| 全方向族の強・積Noether性 | 全可換係数の零切断を含む不変有限主開。任意Noether基底変更。次数別Krull交叉と完成＋頂点外の忠実平坦被覆を使い、方向解消を平坦と仮定しない | `lem:graded-jacobson-noether`, `prop:noether-completion-punctured-gluing`, `thm:simultaneous-strong-product-noether` |
| 同じ全方向ambientの相対CY | Noether包絡上の有限対角解消、次数零Homの基底変更、最低次数線束と左右作用の比較。零切断を含む有限主開で無捩れ、任意非被約基底変更 | `lem:graded-fiberwise-projective`, `thm:simultaneous-relative-cy` |
| 全方向中心商の相対tails・Serre・有限compact窓 | 飽和性・ACM・χ・全シフト豊富性・proper性。Serreは `(−(n−1))[n]`、窓の長さはd1でn+5、d2でn+3。任意Noether基底変更 | `lem:simultaneous-finite-window`, `thm:simultaneous-relative-tails` |
| 全方向族は滑らかな全可換零切断の有限開近傍で実際のnc del Pezzo族 | 全n≥2。積の対角の有限部分解消とSerre、HH¹(X)=0、反標準豊富性。任意Noether基底変更後にsmooth proper、幾何学的coherent次元n | `thm:simultaneous-smooth-ncdp-open` |
| 一つのhを持つ中心商族は可換点でsmooth atlasにならない | Poisson Kodaira–Spencer像は高々1次元、全変形の通常の可換変形による接空間商はnまたはbinom(n+1,2)次元 | `prop:one-parameter-atlas-obstruction` |

一般原理のLowen–Van den Bergh・Lowen・De Deken–Lowen・Yekutieli・Kontsevichと、入力となるPoisson構造定理は既知・既存の入力である。曲面の接空間次元10・9も先行研究で既知。一般nの適用・復元・降下の新規性について包括的な優先権確認は未了。

## D. 未解決の核心と次の一手

両次数の一般次数5・4と一般モノドロミーS₅・S₄は、全lower、規格化中心torsor、全同値商を経た結果である。有限族のCasimir係数に余分な分枝があっても全同値群oidで同一視される。次数1のy正規化と全座標商の比較も完了し、係数次数だけからの推測ではない。自由語中心証明書、逆式、S₃同変性、Sylvester判別式と有限体Bézout証明書を再現資産として保持する。

1. **有限被覆の開像と境界。** δ_(n,1)=5、δ_(n,2)=4とS₅・S₄を出発点に、Poisson粗空間を各関数体拡大で正規化し、構成近傍の開像と欠落分枝を調べる。次数1の内在的逆五次方程式、次数2の符号二次体√((u³−27v²)D₂)を、中心分母・smooth proper開・Casimir Jacobianの条件と比較する。可換点での形式逆、全零切断上の一つの逆像、有限正規化上の残りの分枝を同時に記述する。係数判別式だけで全境界を同定しない。
2. **全域被覆と残る成分。** Uの全M内での開性は証明した。Uの外にあるM対象を、反標準環と許容豊富列から調べる。全可換locusがUに入ることと、可換locusに接しない成分の不存在は別である。中心超曲面表示の存在条件、他のHilbert一定な族、特殊化の可能性を具体的に調べ、全Mの代数性・被覆・成分数を段階的に判定する。
3. **特殊自己同型と粗空間の特異層。** M^ncの正規CM性・quasi-affine性、粗shadowの厳密な平坦点集合、可換点の局所模型T/Aut(X)は得た。次は特殊可換模型のAut(X)作用とR_X^Aut(X)を計算する。粗空間のGorenstein性・terminal性、非被約になり得る粗ファイバー、shadowの幾何学的ファイバーの既約性は、それぞれ追加の問題である。
4. **境界と明示条件。** 零切断を含む開近傍ではH=Eである。その外側の中心増大層で追加同値があるか、smooth proper性や全点Artin比較がどこまで延長するかを調べる。中心行列・分母・Noether開・CY線束・smoothness・Casimir Jacobian・Hochschild階数の非消滅条件を具体化する。全次数の中心条件を一つの有限開条件へ置き換えない。
5. **公表範囲と先行研究。** 全方向有限型nc族、全点Abel Artin比較、全M内の開性、有限対角、Poisson shadowとその相対幾何を一貫した中心結果として整理する。変形比較・THCR・Fujita消滅・Noether降下・同型関手・トーラス商・Keel–Mori・slice・Zariski主定理は既知の原理であり、組合せの包括的優先権は未確認。平坦点集合・Plücker解消・terminal性は固定commitのPoisson側の結果を移送している。多項式Veroneseの持上げにはAMU2025の先行結果を明示し、相対非可換復元との差を説明する。Keelerのmultiple divisors論文の本文と一般基底への仮定は引き続き確認が必要。

## E. 依存・再開・検証

- 相対Poisson錐・商・自己同型：`poisson-del-pezzo` main `4834ea4f3e13bff4d6c5793cec9b169d8f1ad56f`、主原稿v1.4の定理7.3・8.8・9.2、補題8.7、注意8.5、命題9.4。古典対角の有限性には定理9.2とLunaのaffine作用の結果を使用する。粗shadowの厳密な平坦点集合は定理9.6、各固定古典模型上の一般Poisson自己同型の自明性は命題9.5に依存する。錐の局所完全交叉判定・零切断解消・discrepancyは補題10.1・定理10.3・命題10.4を使用し、固定commitの本文と証明を確認した。
- O-marked枠組み：`nc-cubic-threefold-moduli` main `6c35d2c84671c2538e61836a6bf3a511392eacce`、主原稿v22。三次三様体固有の次数一生成・指数2・残余圏の結論を無条件に輸入しない。
- 一次資料・具体的な適用条件・優先権未確認点は [文献と依存](research/literature.md)。証明の重複は研究ノートへ置かない。
- `make verify` はn=2,…,8のHilbert/monic基底・Euler差分・二次障害・符号粗商の接空間次元と、分離型の全係数PBW overlap・中心交換子・内部次数・補助次数を検査する。さらに三次Sklyanin中心元の自由代数内の九項証明書、パラメータ置換と可換極限を厳密計算する。分離型とSklyanin中心の検算はhの有限jetではない。`verify_elliptic_curve.py` はpoint curveの行列式、blowup、分母を払ったshiftの恒等式を厳密検算し、σ⁴の非自明性だけは明示したmod h²計算で確認する。`verify_degree_one_top.py` はWeierstrassからStephensonへの変数変換、関係式のイデアル、AS開多項式、cyclic syzygyを有理係数の自由代数で厳密に検算する。`verify_degree_one_curve.py` は解消曲線の両chart・無限遠因子・shiftと関係式を全係数の恒等式で検算し、σ⁶の非自明性だけmod h²を使う。一般の証明を有限次元の数値例で代替していない。
- `verify_degree_one_center_jet.py` は独立な全係数上で4次補正の三つの交換子がmod h⁶で零となること、内部次数6と完全対称化のz²規格化を厳密に検証する。この有限jet証明書に、論文のH¹消滅と有限余核の議論を組み合わせて全中心元を得る。
- `verify_poisson_shadow.py` はFの1階・2階jetを独立変数とし、n=2,…,6でJacobian括弧のJacobiatorとPlücker関係による表示を厳密に検算する。一般n・任意基底の証明は主原稿の添字計算と全同値の変換則に置き、有限個の検算で置き換えない。
- `verify_degree_two_gorenstein_curve.py` と `verify_degree_one_integral_curve.py` は全独立係数のpoint行列・blowup・分母を払ったshiftと関係式を厳密検算する。d2の非被約ribbon、d1の尖点を除外しない。σ⁴・σ⁶の非自明性だけは明示したmod h²の検査である。強・積Noether性、相対CY・tails・smoothnessは論文の証明により、これらの計算だけから推論しない。
- 両shadow計算は中心の自由語証明書と逆有理式に加え、Sylvester判別式・有限体Bézout証明書を厳密検算する。次数1はdepressionとh尺度変更、次数2はnormalizer商S₃、全係数同変性、Lie行列式と符号二次体の反不変式も確認する。全モジュライの次数5・4とモノドロミーには、論文の中心torsor・共通開・全同値群oid・単純分岐の証明を別に用いる。
- 組版・PDF確認の実施状況と環境は [再現手順](docs/reproduction.md)。生成・証明点検・計算・組版・GitHub反映・hub更新はそれぞれ確認する。
