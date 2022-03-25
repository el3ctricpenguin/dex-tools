# dex-tools
裁定取引用のコードの断片
- ccxt_quote_standalone.py: ccxtに対応している取引所名と通貨ペア、買うロットを投げると板を足し合わせて、平均bid/ask価格を出してくれる。
- mexc_quote.py: 上記と似たような機能のものをMEXCのAPIを直接叩いて書いたバージョン。
- oneinch_quote.py: コイン名とロットを投げるとUSDT建ての購入価格/売却価格が返ってくる。
