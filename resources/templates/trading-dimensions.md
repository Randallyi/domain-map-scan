# Quantitative Trading Dimensions

Use this template when the domain involves strategy development, backtesting, 
or systematic trading.

## Dimensions

1. **Data Layer**
   - Definition: How raw market data is sourced, cleaned, and validated before analysis
   - Key concepts: survivorship bias, look-ahead bias, adjust vs. unadjusted prices, tick vs. OHLCV
   - Safe-to-proceed: Can identify 3+ data quality issues that invalidate backtests

2. **Signal Generation**
   - Definition: Transforming raw data into actionable trading signals
   - Key concepts: momentum vs. mean reversion, parameter sensitivity, regime detection, factor crowding
   - Safe-to-proceed: Can explain why a signal works in one market but fails in another

3. **Execution & Cost Modeling**
   - Definition: Translating theoretical signals into real-world orders with friction
   - Key concepts: slippage, market impact, transaction costs, order types, liquidity constraints
   - Safe-to-proceed: Can estimate how a strategy's Sharpe degrades from 10bps to 50bps cost assumption

4. **Risk Management**
   - Definition: Controlling downside and preserving capital across market conditions
   - Key concepts: position sizing (Kelly, fixed fractional), max drawdown, tail risk, correlation breakdown
   - Safe-to-proceed: Can calculate position size given a 2% account risk and 5% stop-loss

5. **Backtesting & Validation**
   - Definition: Simulating strategy performance with statistical rigor
   - Key concepts: in-sample vs. out-of-sample, walk-forward, overfitting, Sharpe vs. Sortino
   - Safe-to-proceed: Can design a walk-forward test that prevents data snooping

6. **Live Deployment & Monitoring**
   - Definition: Transitioning from simulation to production with observability
   - Key concepts: paper trading, execution logs, drift detection, kill switches, API rate limits
   - Safe-to-proceed: Can list 3 failure modes that appear only in live trading, not backtests
