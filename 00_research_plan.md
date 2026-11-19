# 研究方針：次数1・2の非可換del Pezzo n-fold

**2026-11-20（JST） / v0.1。再開時に最初に読む。**

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

主原稿 `def:ample-model` はHilbert関数を持つ豊富列型の問題A、`def:nc-dp-stack` は標準compact圏の相対Serre・反標準豊富性等を備えたnc多様体の問題Mを定義する。重み付きAS超曲面の表示を持つ部分問題は別に記号化する。fppf stack化によるモジュライ問題の定義と、代数スタック・有限型atlasの構成は別である。

元の成分数決定という目標のうち、可換点における全Abel変形の形式分枝数は解決した。全体の成分数には一般nc点と代数化が残る。このため、現在は全Artin比較・同変な形式族・全O同値の認識を、公表価値のある一つの論理単位として先に完成させる。

## C. 主要到達点と確実性

| 主張 | 状態・仮定 | 証明の所在 |
|---|---|---|
| 全O-marked Abel Artin変形の同型類関手は、d1で滑らかな形式円板、d2で通常の形式円板×Plücker錐の完備化 | 証明を記述し、一次比較定理の適用条件を点検。通常の局所Artin環全体。有限Aut(X)は未商 | `thm:abel-formal-ring` |
| 各可換点は一形式分枝、d2・n≥3で特異、二次障害Q∧Q | 上の形式環から証明。全ncスタックの成分定理ではない | `cor:abel-quadratic-obstruction` |
| 任意の冪零係数上の中心商は次数ごとに自由、任意基底変更と両立 | monic分裂で証明、DVRのtorsion-free判定を一般化していない | `thm:nilpotent-universal-quantization` |
| Poisson零切断の形式完備化にO-marked tailsの族が降下 | 固定formality、正規形の線型群、次数スカラーのcoherent trivializationで証明。全Abel比較の逆とは未証明 | `thm:quantization-descent` |
| 全O同値は反標準軌道環から認識可能 | 相対perfect/Serre、反標準豊富性、section復元等の追加仮定付き | `prop:ncdp-relative-anticanonical-hom` |
| 任意指数rのVeronese同型の持上げはμr-torsor | 二つ以上の中心一次変数、中心多項式環上平坦、普遍的低次中心条件の下で証明 | `thm:ncdp-veronese-lift` |
| dは反標準Euler多項式から内在的に復元でき、族で局所定数 | 反標準saturation・高次Ext消滅・相対perfect条件付き | `prop:ncdp-intrinsic-degree` |
| 冪零段階の中心商は左右で唯一のaugmentation Ext `R(n−1)` を次数n+1に持つ | R分裂Koszul持上げと平坦中心商のchange of ringsで証明。通常の絶対AS正則性やSerre公式ではない | `prop:nilpotent-weighted-as`, `prop:flat-central-hypersurface-ext` |
| 固定した全ての非零Poisson方向の形式一般ファイバーはCasimir多項式環を普遍中心に持つ | 古典generic active fiberの幾何学的整性とh係数帰納で証明。Artin商・有限複素hへの特殊化には適用しない | `thm:formal-generic-center`, `cor:formal-generic-veronese` |

一般原理のLowen–Van den Bergh・Lowen・De Deken–Lowen・Yekutieli・Kontsevichと、入力となるPoisson構造定理は既知・既存の入力である。曲面の接空間次元10・9も先行研究で既知。一般nの適用・復元・降下の新規性について包括的な優先権確認は未了。

## D. 未解決の核心と次の一手

1. **相対Serreと通常の周期化。** 全Abel変形のZ-代数から反標準軌道へ進み、canonical bimodule、Nakayama自己同型、基底線束、豊富性、section saturationを確認する。AS指標n−1だけを根拠に無捩れを仮定しない。
2. **構成した量子化の全変形に対する完全性。** 全Artin同型類の比較は得たが、固定したambient graph量子化がその逆となることは別問題。アフィン局所化・sheafification・section化でのformalityの比較から着手する。
3. **有限型族と一般nc点。** 活性三変数の重み(1,2,3)/(1,1,2)にn−1個の中心変数を加える模型について、EG型potentialの中心元・PBW平坦性を係数環全体で確認する。形式パラメータ1への代入を行わない。
4. **全体の既約成分。** 適切な有限型atlasと全同値の商を構成した後、可換locusに接しない成分の不存在または存在を判定する。可換点の形式環の整性だけで結論しない。

## E. 依存・再開・検証

- 相対Poisson錐と商：`poisson-del-pezzo` main `4834ea4f3e13bff4d6c5793cec9b169d8f1ad56f`、主原稿v1.4の定理7.3・8.8。
- O-marked枠組み：`nc-cubic-threefold-moduli` main `6c35d2c84671c2538e61836a6bf3a511392eacce`、主原稿v22。三次三様体固有の次数一生成・指数2・残余圏の結論を無条件に輸入しない。
- 一次資料・具体的な適用条件・優先権未確認点は [文献と依存](research/literature.md)。証明の重複は研究ノートへ置かない。
- `make verify` はn=2,…,8のHilbert/monic基底・Euler差分・二次障害を正確整数計算で確認する。一般の証明を有限計算で代替していない。
- 組版・PDF確認の実施状況と環境は [再現手順](docs/reproduction.md)。生成・証明点検・計算・組版・GitHub反映・hub更新はそれぞれ確認する。
