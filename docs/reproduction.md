# 再現手順と検証範囲

2026-11-20（JST） / v0.10

## 組版

リポジトリ直下で実行する。

```bash
latexmk
```

または `make pdf`。主原稿は `papers/nc-del-pezzo.tex`、出力は `build/nc-del-pezzo.pdf`、SyncTeXも同じ場所。`.latexmkrc` はmainを基準に入力と文献の相対パスを解決する。

必要な環境：LuaLaTeX、latexmk、BibTeX、luatexja、luatexja-preset、amsmath/amsfonts/amsthm、mathtools、geometry、booktabs、longtable、hyperref、原ノ味明朝・原ノ味角ゴシック（HaranoAji）。TeX Live相当の環境を想定する。主原稿は `\usepackage[haranoaji]{luatexja-preset}` を使い、システム側のNotoフォントを要求しない。TeXは外部PDFや非公開データを読み込まない。

VS Codeでは推奨拡張LaTeX Workshopを入れる。recipeはworkspace rootを作業ディレクトリとして `.latexmkrc` を明示指定する。実質的に同じCLIは次の通り。

```bash
latexmk -norc -r .latexmkrc papers/nc-del-pezzo.tex
```

## 有限計算

```bash
make verify
# 個別には
python3 computations/verify_formal_geometry.py
python3 computations/verify_finite_families.py
python3 computations/verify_cubic_top.py
python3 computations/verify_elliptic_curve.py
python3 computations/verify_degree_one_top.py
python3 computations/verify_degree_one_curve.py
python3 computations/verify_degree_one_center_jet.py
python3 computations/verify_degree_two_gorenstein_curve.py
python3 computations/verify_degree_one_integral_curve.py
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

最初のスクリプトは有限範囲の数式確認、分離型とSklyanin中心の二つは指定した有限な関係式と中心公式の厳密な恒等式検証である。全Abel変形比較、一般nでの証明、モジュライの代数性、グラフ量子化の全高次積を機械的に証明するものではない。

## 検証の状態

今回の証明点検は、有限基底の全同値認識・有限表示アフィン商・低次数中心開・Hochschild剛性・unramified性、およびその入力である相対projective性・逆向きHomの有限性・積の対角・smooth proper開近傍を対象とした。上流の全PBW・AS分類・Noether降下を今回再び独立に検証したとは扱わない。以下の既存部分の確認状況も含め、証明の点検と有限計算の実行を区別する。


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
- 上記九つのPython計算は2026-11-20に実行して全件成功。分離型族の計算では167種類の単語簡約を使用した。Sklyanin中心元は全係数の自由代数恒等式、次数1の中心jetは明示したmod h⁶の全係数恒等式として検証した。全top曲線の二つの計算では、尖点・非被約ribbonを含む普遍恒等式を確認し、shiftの非自明性を検出する項目だけ有限jetと区別した。
- 次数1の有限開・相対CY・普遍PBW・23未知数の中心構成を独立に点検し、変数変換の全係数恒等式の計算を実行した。相対曲線の両chart、次数1線束、有限被覆の全逆像での縮小、全次数生成、中心の零像、忠実平坦降下、偶数Veroneseによる積Noether性、全nのtailsと有限窓も独立に点検した。
- 両次数の同時ambient表示を独立に点検した。次数1のΔを除くAS開と明示的主開、次数2のMori–Ueyama条件と明示行列式g₂、全体ファイバーの一定Hilbert関数からの普遍平坦性、全一次中心商を確認した。行列式のtensor縮約・Hessian係数・活性3×3行列への帰着も照合した。続く同時中心の構成では、両次数の全可換係数・全方向について有限中心元と普遍正則性を証明した。有限基底上の相対tailsには、以下の独立したNoether性・相対対角の証明を用いる。
- 主原稿v0.10をLuaLaTeXで148頁に組版した。最終ログに未解決参照・未解決引用・欠落文字・overfull/underfullがないことを確認した。全148頁の縮小一覧と、表紙・目次・主要結果・相対Hochschild・全Artin比較・全同値認識・低次数中心・今後の問題・文献を含む23頁を拡大表示して確認した。PDFと同じ場所にSyncTeXがあり、PDFより新しいTeX・BibTeXソースがないことも確認した。
- 使用したエンジンはLuaHBTeX 1.18.0。素の検証環境ではlualatex.fmtが不足したため、既存のTeX環境を有効にして再実行し成功した。必要なluatexjaと和文フォントを備える環境で再生成できる。和文倍率とaddjfontfeatureに関する設定警告2件は残るが、欠落文字はない。VS Code設定の検査とrecipe相当CLIは確認済みだが、VS Code UIのビルド操作とSyncTeXのクリック動作は実行していない。
- 相対中心持上げの同じambientへのgauge同定、中央差Koszulによる絶対CY、Dolgushevの絶対定理と体積の重み射影、有限余核の局所化を独立に点検した。次数2は普遍係数上の層の単射性・中心部分束・方向空間上のH¹消滅とproper降下を点検した。次数1は23未知数局所中心・普遍jet・高次H¹消滅・Artin–Reesによる有限代数化を点検した。普遍係数上の中心の計算と、特殊ファイバーの中心が増えることを区別している。
- 同じ有限中心商族からの全Artin比較は、DDL Proposition 4.4の仮定、flatな構造対象、初交換子、同じ全形式環の自己写像という順で点検した。有限基底上のtailsのsmooth proper性は、このArtin比較に仮定していない。
- 全top曲線の二つの節を独立に点検した。次数2の有限平坦二重被覆・trace分解・ribbonのO(−2)・任意基底変更、次数1の階数2被覆・尖点を含む曲線・無限遠Cartier因子と次数1線束を確認した。全次数生成と中心の零像、Keelerのample filter・訂正込みFujita消滅から、全top・全lower・全nの強・積Noether性へ移る論理を点検した。
- 次数別Krull交叉によるJacobson根基からのNoether持上げ、完成＋頂点外の有限積の忠実平坦性、方向解消のproperな悪条件像の除去を独立に点検した。環全体の完成と次数付きの係数変更を区別し、方向解消そのものを平坦と仮定していない。
- 次数零の有限三項Hom複体によるファイバー別projective性、全方向ambientの有限対角解消、被約な普遍基底上の最低次数線束・左右作用と任意非被約基底変更を独立に点検した。零方向のKoszul最小解消への有限スカラー消去、有限compact窓、相対tails・Serre、二重対角とHH¹を使うsmooth properな有限開近傍まで、依存関係と循環がないことを点検した。
- 有限型V上でVeroneseの有限斉次表示、具体的なVeronese/tensor関手によるtails復元、compact軌道上だけのSerre比較、有限高切断でのfppf降下、Isomと逆写像の有限方程式、重み±1の行列成分による強Z次数付けとアフィン商を点検した。n≥3の元のBへの持上げとは区別している。
- 非零方向上で完全対称化の活性filtrationブロック、最高記号の非零性、中央P上のファイバー自由性、被約普遍基底でのC_mの一定階数とP-加群分裂を点検した。固定qの交換子行列とδ_q/hの古典還元から、全smooth f・全非零rayについて低次数中心開の非空性を証明した。全中心最小性や具体的な最大小行列式の一括計算は行っていない。
- smooth properなdg模型のHochschild複体のperfect性・基底変更、単位coneのTor振幅下界、非被約係数へのHH¹消滅を点検した。安定化群の単位余接加群、群の平行移動、ファイバーによるunramified判定から全同値スキームのquasi-finite unramified性を点検した。基底上の有限性・flatness・étaleness・atlasは未証明としている。
- Stacks Tags 06PH・0BDI・0BCD・02G8・02GF、およびAMU2025のarXiv原本Corollaries 4–5を一次資料で確認した。AMU2025の体上の多項式Veronese持上げを新規結果とはしていない。
- 形式証明器は使っていない。追加の中心分母・Noether開・smoothな開集合の最小非消滅条件の明示、構成族外の全O同値・低次数中心の増大層での基本シフト認識、全ncモジュライの有限型atlas・成分数、および包括的な優先権調査は未完了。Keelerのmultiple divisors論文は書誌とabstractのみ確認済みで、本文定理の仮定・番号を推測していない。

## 保存と外部依存

GitHub mainが正本。PDF、ZIP、組版中間物、キャッシュは追跡しない。通常コミット・mainへのpushとhub更新にはGitHubの対象repoへの書込み権限が必要だが、組版・有限計算には認証不要。入力となる他研究の具体的commitと定理は [文献と依存](../research/literature.md) に記載する。
