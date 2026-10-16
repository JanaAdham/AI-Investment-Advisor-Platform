# EGX Egyptian Stocks Historical Data 2021-2026

## Overview
This dataset contains historical stock price data for companies listed on the Egyptian Stock Exchange (EGX), also known as the Cairo Stock Exchange. The data is sourced from Yahoo Finance.

## Dataset Structure

```
EGX/
├── all_stocks_list.csv      # Complete list of all Egyptian stocks
├── failed_stocks.csv        # Stocks with no available data
└── raw/
    ├── SYMBOL_CompanyName/
    │   └── SYMBOL.csv       # Historical OHLCV data
    └── ...
```

## Data Fields

Each stock CSV file contains:

| Column | Description |
|--------|-------------|
| Date | Trading date (index) |
| Open | Opening price (EGP) |
| High | Highest price of the day (EGP) |
| Low | Lowest price of the day (EGP) |
| Close | Closing price (EGP) |
| Volume | Number of shares traded |
| Dividends | Dividend payments |
| Stock Splits | Stock split information |

## Key Statistics

- **Market**: Egyptian Stock Exchange (EGX)
- **Currency**: Egyptian Pound (EGP)
- **Total Companies**: ~237 listed stocks
- **Date Range**: 2021 - Present
- **Update Frequency**: Updated periodically

## Sample Companies

| Symbol | Company Name |
|--------|--------------|
| COMI | Commercial International Bank |
| HRHO | Hermes Holding |
| TMGH | Talaat Moustafa Group |
| EAST | Eastern Company |
| SWDY | Elsewedy Electric |
| ETEL | Telecom Egypt |
| ESRS | Ezz Steel |
| PHDC | Palm Hills Development |

## Use Cases

- Stock price prediction using ML/DL models
- Technical analysis and indicator development
- Portfolio optimization
- Market trend analysis
- Backtesting trading strategies
- Academic research on emerging markets

## Data Source

Data collected from Yahoo Finance via the `yfinance` Python library. Stock symbols identified using `investpy` library.

## Author & Rights

**Created by**: Mahmoud Al-Refaey  
**GitHub**: [github.com/mahmoudalrefaey](https://github.com/mahmoudalrefaey)  
**Kaggle**: [kaggle.com/mahmoudalrefaey](https://www.kaggle.com/mahmoudalrefaey)  
**Email**: dev.mahmoudrefaey@gmail.com  
**Contact**: Feel free to reach out for collaborations or questions.

All rights reserved by the author. This dataset is shared for educational and research purposes.

## Citation

If you use this dataset, please cite:
```
Egyptian Stock Exchange (EGX) Historical Data
Author: Mahmoud Al-Refaey
Source: Yahoo Finance
Year: 2026
Kaggle: https://www.kaggle.com/datasets/mahmoudalrefaey/egx-egyptian-stocks-2021-2026
```

## License

This dataset is released under CC0 1.0 Universal (Public Domain).

## Disclaimer

This data is provided for educational and research purposes only. It should not be considered as financial advice. Always verify data accuracy before making investment decisions.

## Acknowledgments

- Yahoo Finance for providing the historical data
- Egyptian Stock Exchange (EGX)
