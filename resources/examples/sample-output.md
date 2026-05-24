# Domain Map: Momentum Strategy on QQQ Constituents
Date: 2026-05-24
Goal: Build and backtest a 20-day momentum rotation strategy with monthly rebalancing

## Dimensions
| Dimension | Coverage | Threshold | Status |
|-----------|----------|-----------|--------|
| Data Layer | 45% | 60% | 🔴 |
| Signal Generation | 70% | 60% | 🟢 |
| Execution & Cost | 30% | 60% | 🔴 |
| Risk Management | 55% | 60% | 🟡 |
| Backtesting & Validation | 40% | 60% | 🔴 |
| Live Deployment | 10% | 50% | 🔴 |

## Critical Blind Spots (Top 3)
1. **Execution & Cost**: User cannot estimate market impact for mid-cap QQQ constituents. 
   → Action: Read "Trading Costs and Execution" by Kissell & Glantz, Ch. 3–5.
2. **Backtesting & Validation**: User conflates in-sample optimization with out-of-sample testing. 
   → Action: Implement walk-forward analysis with 3-year training / 1-year test windows.
3. **Data Layer**: User unaware of survivorship bias in QQQ historical constituent lists. 
   → Action: Source point-in-time constituent data from Norgate or QuantConnect.

## Launch Decision
- [ ] GO — Start project. Parallel track: patch Execution & Cost to 60% (est. 4–6 hrs)
- [x] NO-GO — First patch Data Layer and Execution & Cost to 60%. Estimated time: 1 weekend

## Re-audit Triggers
- When backtest Sharpe exceeds 2.0, revisit Backtesting & Validation (overfitting check)
- When ready to go live, revisit Live Deployment (paper trade for 2 weeks first)
