#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time
import warnings
from typing import Dict, List, Tuple, Optional
from collections import defaultdict, deque
try:
    import talib
except ImportError:
    import finta as talib
import requests
import json
import random
import math
from threading import Lock
import logging
from logger import AdvancedLogger
from api_manager import ApiManager

warnings.filterwarnings('ignore')

# ================= CONFIGURATION DES ALERTES =================
class AlertManager:
    def __init__(self):
        self.alert_file = 'trading_alerts.json'

    def save_alert(self, symbol, signal, confidence, price):
        alert = {
            'timestamp': datetime.now().isoformat(),
            'symbol': symbol,
            'signal': signal,
            'confidence': confidence,
            'price': price
        }

        with open(self.alert_file, 'a') as f:
            f.write(json.dumps(alert) + '\n')

        print(f"🚨 ALERTE: {symbol} - {signal} ({confidence:.0%}) à ${price}")

# ================= FIN CONFIGURATION =================

# Setup logging des erreurs
logging.basicConfig(
    filename='trading_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ProfessionalTradingSystem:
    def __init__(self):
        # Configuration des API avec les clés réelles fournies
        self.api_keys = {
            "alpha_vantage": "S1UW6ZGNLX7KM279",
            "finnhub": "d33d47pr01qib1p0ggkgd33d47pr01qib1p0ggl0",
            "twelvedata": "eeb5f38bdab0494e8e6434dddddd2588",
            "DEEPSEEK_KEYS": ["sk-ef08317d125947b3a1ce5916592bef00", "sk-d73750d96142421cb1098c7056dd7f01"],
            "SERPER_KEYS": ["047b30db1df999aaa9c293f2048037d40c651439"],
            "GEMINI_API_KEYS": ["AIzaSyBWXcwGdzoeUzbApSNLICkanNcm7BYzYcs", "AIzaSyAk6Ph25xuIY3b5o-JgdL652MvK4usp8Ms", "AIzaSyDuccmfiPSk4042NeJCYIjA8EOXPo1YKXU", "AIzaSyAQq6o9voefaDxkAEORf7W-IB3QbotIkwY", "AIzaSyDYaYrQQ7cwYFm8TBpyGM3dJweOGOYl7qw"],
            "GUARDIAN_KEY": ["07c622c1-af05-4c24-9f37-37d219be76a0"],
        }

        # Alert manager
        self.alert_manager = AlertManager()

        # AJOUTE CES LIGNES :
        self.logger = AdvancedLogger()
        self.api_manager = ApiManager()
        self.past_signals = []  # Pour stocker les signaux en attente d'évaluation

        # Univers de trading étendu avec les mêmes symboles que le deuxième script
        self.trading_universe = {
            # Actions US (30 principales)
            'AAPL': {'type': 'stock', 'sector': 'Technology', 'lot_size': 100},
            'MSFT': {'type': 'stock', 'sector': 'Technology', 'lot_size': 100},
            'GOOGL': {'type': 'stock', 'sector': 'Technology', 'lot_size': 100},
            'AMZN': {'type': 'stock', 'sector': 'E-commerce', 'lot_size': 100},
            'TSLA': {'type': 'stock', 'sector': 'Automotive', 'lot_size': 100},
            'META': {'type': 'stock', 'sector': 'Technology', 'lot_size': 100},
            'NVDA': {'type': 'stock', 'sector': 'Semiconductors', 'lot_size': 100},
            'JPM': {'type': 'stock', 'sector': 'Banking', 'lot_size': 100},
            'JNJ': {'type': 'stock', 'sector': 'Healthcare', 'lot_size': 100},
            'V': {'type': 'stock', 'sector': 'Financial Services', 'lot_size': 100},
            'PYPL': {'type': 'stock', 'sector': 'Financial Services', 'lot_size': 100},
            'ADBE': {'type': 'stock', 'sector': 'Technology', 'lot_size': 100},
            'NFLX': {'type': 'stock', 'sector': 'Entertainment', 'lot_size': 100},
            'DIS': {'type': 'stock', 'sector': 'Entertainment', 'lot_size': 100},
            'BA': {'type': 'stock', 'sector': 'Aerospace', 'lot_size': 100},

            # Forex Majors et Minors
            'EUR/USD': {'type': 'forex', 'sector': 'Currency', 'lot_size': 100000},
            'GBP/USD': {'type': 'forex', 'sector': 'Currency', 'lot_size': 100000},
            'USD/JPY': {'type': 'forex', 'sector': 'Currency', 'lot_size': 100000},
            'USD/CHF': {'type': 'forex', 'sector': 'Currency', 'lot_size': 100000},
            'AUD/USD': {'type': 'forex', 'sector': 'Currency', 'lot_size': 100000},
            'USD/CAD': {'type': 'forex', 'sector': 'Currency', 'lot_size': 100000},
            'NZD/USD': {'type': 'forex', 'sector': 'Currency', 'lot_size': 100000},
            'EUR/GBP': {'type': 'forex', 'sector': 'Currency', 'lot_size': 100000},
            'EUR/JPY': {'type': 'forex', 'sector': 'Currency', 'lot_size': 100000},
            'GBP/JPY': {'type': 'forex', 'sector': 'Currency', 'lot_size': 100000},
            'AUD/JPY': {'type': 'forex', 'sector': 'Currency', 'lot_size': 100000},
            'EUR/CAD': {'type': 'forex', 'sector': 'Currency', 'lot_size': 100000},
            'GBP/CAD': {'type': 'forex', 'sector': 'Currency', 'lot_size': 100000},

            # Indices Mondiaux
            'SPX': {'type': 'index', 'sector': 'US Index', 'lot_size': 10},
            'DJI': {'type': 'index', 'sector': 'US Index', 'lot_size': 10},
            'IXIC': {'type': 'index', 'sector': 'US Index', 'lot_size': 10},
            'RUT': {'type': 'index', 'sector': 'US Index', 'lot_size': 10},
            'FTSE': {'type': 'index', 'sector': 'UK Index', 'lot_size': 10},
            'DAX': {'type': 'index', 'sector': 'German Index', 'lot_size': 10},
            'CAC': {'type': 'index', 'sector': 'French Index', 'lot_size': 10},
            'NIKKEI': {'type': 'index', 'sector': 'Japanese Index', 'lot_size': 10},
            'HSI': {'type': 'index', 'sector': 'Hong Kong Index', 'lot_size': 10},
            'ASX': {'type': 'index', 'sector': 'Australian Index', 'lot_size': 10},
            'SSEC': {'type': 'index', 'sector': 'Chinese Index', 'lot_size': 10},
            'BSE': {'type': 'index', 'sector': 'Indian Index', 'lot_size': 10},

            # Métaux Précieux
            'XAU/USD': {'type': 'metal', 'sector': 'Gold', 'lot_size': 100},
            'XAG/USD': {'type': 'metal', 'sector': 'Silver', 'lot_size': 5000},
            'XPT/USD': {'type': 'metal', 'sector': 'Platinum', 'lot_size': 100},
            'XPD/USD': {'type': 'metal', 'sector': 'Palladium', 'lot_size': 100},
            'XCU/USD': {'type': 'metal', 'sector': 'Copper', 'lot_size': 100},
            'XAL/USD': {'type': 'metal', 'sector': 'Aluminum', 'lot_size': 100},

            # Crypto-monnaies
            'BTC/USD': {'type': 'crypto', 'sector': 'Cryptocurrency', 'lot_size': 1},
            'ETH/USD': {'type': 'crypto', 'sector': 'Cryptocurrency', 'lot_size': 1},
            'XRP/USD': {'type': 'crypto', 'sector': 'Cryptocurrency', 'lot_size': 1},
            'LTC/USD': {'type': 'crypto', 'sector': 'Cryptocurrency', 'lot_size': 1},
            'BCH/USD': {'type': 'crypto', 'sector': 'Cryptocurrency', 'lot_size': 1},

            # Pétrole et Commodities
            'USOIL': {'type': 'commodity', 'sector': 'Oil', 'lot_size': 100},
            'UKOIL': {'type': 'commodity', 'sector': 'Oil', 'lot_size': 100},
            'NGAS': {'type': 'commodity', 'sector': 'Natural Gas', 'lot_size': 100},
            'CORN': {'type': 'commodity', 'sector': 'Agriculture', 'lot_size': 100},
            'WHEAT': {'type': 'commodity', 'sector': 'Agriculture', 'lot_size': 100},
            'SOYBEAN': {'type': 'commodity', 'sector': 'Agriculture', 'lot_size': 100},
            'SUGAR': {'type': 'commodity', 'sector': 'Agriculture', 'lot_size': 100},
            'COFFEE': {'type': 'commodity', 'sector': 'Agriculture', 'lot_size': 100},
        }

        self.symbols = list(self.trading_universe.keys())
        self.update_interval = 45  # secondes entre les mises à jour (augmenté à 45s)
        self.historical_days = 90   # 90 jours d'historique
        self.min_confidence = 0.8  # confiance minimale pour les alertes (80%)
        self.max_positions = 5

        # Stockage des performances pour l'apprentissage
        self.performance_tracker = defaultdict(list)
        self.signals_history = deque(maxlen=500)
        self.last_update_time = defaultdict(lambda: datetime.min)
        self.last_signal_time = defaultdict(lambda: datetime.min)
        self.data_lock = Lock()
        self.market_data = {}
        self.learning_coefficients = defaultdict(lambda: 1.0)

        # Paramètres de trading optimisés par type d'actif
        self.trading_params = {
            'stock': {'stop_loss': 0.018, 'take_profit': 0.055, 'max_hours': 12},
            'forex': {'stop_loss': 0.0025, 'take_profit': 0.0065, 'max_hours': 8},
            'index': {'stop_loss': 0.015, 'take_profit': 0.038, 'max_hours': 10},
            'metal': {'stop_loss': 0.02, 'take_profit': 0.048, 'max_hours': 9},
            'commodity': {'stop_loss': 0.022, 'take_profit': 0.06, 'max_hours': 11},
            'crypto': {'stop_loss': 0.03, 'take_profit': 0.075, 'max_hours': 6}
        }

        # Horaires de trading optimaux par type d'actif (en UTC)
        self.optimal_trading_hours = {
            'stock': [(13, 30), (20, 0)],  # Ouverture US et clôture
            'forex': [(7, 0), (16, 0)],    # Recouvrement London/NY
            'index': [(13, 30), (20, 0)],   # Heures de marché US
            'metal': [(7, 0), (16, 0)],     # Heures de liquidité
            'commodity': [(8, 0), (17, 0)], # Heures de trading actif
            'crypto': [(0, 0), (23, 59)]    # 24/7
        }

        print("🚀 Initialisation du système de trading professionnel...")
        print(f"📊 Surveillance de {len(self.symbols)} instruments financiers")
        print(f"⏰ Mise à jour toutes les {self.update_interval} secondes")
        print(f"🎯 Seuil de confiance: {self.min_confidence*100}%")
        print("=" * 80)

    def fetch_market_data(self, symbol: str) -> Optional[pd.DataFrame]:
        """Récupère les données en temps réel via API avec gestion des quotas et logique améliorée"""
        now = datetime.now()
        # Le temps est maintenant géré par la boucle principale, nous retirons le verrou de 300s.

        try:
            # Essayer d'abord TwelveData avec des paramètres optimisés
            clean_symbol = symbol.replace('/', '')
            # On passe à un intervalle de 15min et on demande 200 points de données.
            url = f"https://api.twelvedata.com/time_series?symbol={clean_symbol}&interval=15min&outputsize=200&apikey={self.api_keys['twelvedata']}"

            response = requests.get(url, timeout=15)
            response.raise_for_status() # Lève une exception pour les codes d'erreur HTTP
            data = response.json()

            if "values" in data:
                df = pd.DataFrame(data["values"])
                df = df.rename(columns={
                    'datetime': 'Date', 'open': 'Open', 'high': 'High',
                    'low': 'Low', 'close': 'Close', 'volume': 'Volume'
                })
                df['Date'] = pd.to_datetime(df['Date'])
                df.set_index('Date', inplace=True)
                df = df.sort_index()

                for col in ['Open', 'High', 'Low', 'Close', 'Volume']:
                    df[col] = pd.to_numeric(df[col], errors='coerce')

                df = df.dropna()
                self.last_update_time[symbol] = now

                if len(df) < 50: # On demande plus de points pour les indicateurs
                    return None

                return df

        except Exception as e:
            logging.error(f"Erreur API TwelveData pour {symbol}: {str(e)}")

            # Fallback sur Alpha Vantage si TwelveData échoue, avec des données intraday
            try:
                url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={clean_symbol}&interval=15min&apikey={self.api_keys['alpha_vantage']}&outputsize=compact"
                response = requests.get(url, timeout=15)
                response.raise_for_status()
                data = response.json()

                key = "Time Series (15min)"
                if key in data:
                    df = pd.DataFrame.from_dict(data[key], orient='index')
                    df = df.rename(columns={
                        '1. open': 'Open',
                        '2. high': 'High',
                        '3. low': 'Low',
                        '4. close': 'Close',
                        '5. volume': 'Volume'
                    })
                    df.index = pd.to_datetime(df.index)
                    df = df.sort_index()
                    df = df.astype(float)

                    self.last_update_time[symbol] = now
                    return df

            except Exception as e2:
                logging.error(f"Erreur API AlphaVantage pour {symbol}: {str(e2)}")

        # Si les APIs échouent, on ne fait rien. Pas de données simulées.
        return None

    def calculate_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calcule les indicateurs techniques avancés avec combinaisons multi-périodes"""
        if df is None or len(df) < 100:
            return None

        close_prices = df['Close'].values
        high_prices = df['High'].values
        low_prices = df['Low'].values
        volume = df['Volume'].values

        # Indicateurs de base
        df['SMA_20'] = talib.SMA(close_prices, timeperiod=20)
        df['EMA_12'] = talib.EMA(close_prices, timeperiod=12)
        df['EMA_26'] = talib.EMA(close_prices, timeperiod=26)
        df['RSI_14'] = talib.RSI(close_prices, timeperiod=14)
        df['MACD'], df['MACD_Signal'], _ = talib.MACD(close_prices, fastperiod=12, slowperiod=26, signalperiod=9)
        df['ATR_14'] = talib.ATR(high_prices, low_prices, close_prices, timeperiod=14)

        # Indicateurs avancés supplémentaires
        df['BB_Upper_20'], df['BB_Middle_20'], df['BB_Lower_20'] = talib.BBANDS(close_prices, timeperiod=20)
        df['ADX_14'] = talib.ADX(high_prices, low_prices, close_prices, timeperiod=14)
        df['OBV'] = talib.OBV(close_prices, volume)
        df['Stoch_K'], df['Stoch_D'] = talib.STOCH(high_prices, low_prices, close_prices)

        # Moyennes mobiles multiples avec périodes de Fibonacci
        fib_periods = [3, 5, 8, 13, 21, 34, 55, 89]
        for period in fib_periods:
            if len(close_prices) >= period:
                df[f'SMA_{period}'] = talib.SMA(close_prices, timeperiod=period)
                df[f'EMA_{period}'] = talib.EMA(close_prices, timeperiod=period)

        # RSI multiples timeframes avec confirmation
        rsi_periods = [3, 6, 9, 14, 21]
        for period in rsi_periods:
            if len(close_prices) > period:
                df[f'RSI_{period}'] = talib.RSI(close_prices, timeperiod=period)

        # MACD avec différents paramètres
        macd_fast_periods = [6, 8, 12]
        macd_slow_periods = [13, 21, 26]
        for fast, slow in zip(macd_fast_periods, macd_slow_periods):
            if len(close_prices) > slow:
                macd, macd_signal, macd_hist = talib.MACD(close_prices, fastperiod=fast, slowperiod=slow, signalperiod=9)
                df[f'MACD_{fast}_{slow}'] = macd
                df[f'MACD_Signal_{fast}_{slow}'] = macd_signal
                df[f'MACD_Hist_{fast}_{slow}'] = macd_hist

        # Bollinger Bands avec déviations multiples
        for dev in [1, 1.5, 2]:
            for period in [10, 20, 50]:
                if len(close_prices) > period:
                    upper, middle, lower = talib.BBANDS(close_prices, timeperiod=period, nbdevup=dev, nbdevdn=dev)
                    df[f'BB_Upper_{period}_{dev}'] = upper
                    df[f'BB_Lower_{period}_{dev}'] = lower

        # Stochastic avec paramètres variés
        stoch_periods = [(7, 3, 3), (14, 3, 3), (21, 5, 5)]
        for fastk, slowk, slowd in stoch_periods:
            if len(close_prices) > fastk:
                k, d = talib.STOCH(high_prices, low_prices, close_prices,
                                  fastk_period=fastk, slowk_period=slowk, slowd_period=slowd)
                df[f'Stoch_K_{fastk}'] = k
                df[f'Stoch_D_{fastk}'] = d

        # ADX et Directional Movement avec confirmation
        for period in [7, 14, 21]:
            if len(close_prices) > period*2:
                df[f'ADX_{period}'] = talib.ADX(high_prices, low_prices, close_prices, timeperiod=period)
                df[f'Plus_DI_{period}'] = talib.PLUS_DI(high_prices, low_prices, close_prices, timeperiod=period)
                df[f'Minus_DI_{period}'] = talib.MINUS_DI(high_prices, low_prices, close_prices, timeperiod=period)

        # ATR pour le position sizing
        for period in [7, 14, 21]:
            if len(close_prices) > period:
                df[f'ATR_{period}'] = talib.ATR(high_prices, low_prices, close_prices, timeperiod=period)

        # Volume indicators avancés
        df['Volume_MA_5'] = talib.SMA(volume, timeperiod=5)
        df['Volume_MA_20'] = talib.SMA(volume, timeperiod=20)
        df['Volume_Ratio'] = df['Volume'] / df['Volume_MA_20']

        # Momentum et taux de changement multi-périodes
        for period in [3, 5, 10, 15]:
            if len(close_prices) > period:
                df[f'Momentum_{period}'] = talib.MOM(close_prices, timeperiod=period)
                df[f'ROC_{period}'] = talib.ROC(close_prices, timeperiod=period)

        # Williams %R avec différentes périodes
        for period in [7, 14, 28]:
            if len(close_prices) > period:
                df[f'Williams_R_{period}'] = talib.WILLR(high_prices, low_prices, close_prices, timeperiod=period)

        # CCI avec différentes périodes
        for period in [10, 20, 40]:
            if len(close_prices) > period:
                df[f'CCI_{period}'] = talib.CCI(high_prices, low_prices, close_prices, timeperiod=period)

        # Pattern recognition avancé
        patterns = [
            'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE', 'CDL3LINESTRIKE',
            'CDL3OUTSIDE', 'CDL3STARSINSOUTH', 'CDL3WHITESOLDIERS', 'CDLABANDONEDBABY',
            'CDLADVANCEBLOCK', 'CDLBELTHOLD', 'CDLBREAKAWAY', 'CDLCLOSINGMARUBOZU',
            'CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER', 'CDLDOJI',
            'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLENGULFING', 'CDLEVENINGDOJISTAR',
            'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE', 'CDLGRAVESTONEDOJI', 'CDLHAMMER',
            'CDLHANGINGMAN', 'CDLHARAMI', 'CDLHARAMICROSS', 'CDLHIGHWAVE',
            'CDLHIKKAKE', 'CDLHIKKAKEMOD', 'CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS',
            'CDLINNECK', 'CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH',
            'CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU',
            'CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR',
            'CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS',
            'CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE', 'CDLSPINNINGTOP',
            'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTAKURI', 'CDLTASUKIGAP',
            'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER', 'CDLUPSIDEGAP2CROWS',
            'CDLXSIDEGAP3METHODS'
        ]

        for pattern in patterns:  # Tous les patterns pour une analyse complète
            try:
                pattern_func = getattr(talib, pattern)
                result = pattern_func(df['Open'].values, high_prices, low_prices, close_prices)
                df[pattern] = result
            except:
                pass

        # Indicateurs personnalisés
        df['Price_Volume_Trend'] = df['ROC_5'] * df['Volume_Ratio']

        # Nettoyer les valeurs NaN
        df = df.fillna(method='bfill').fillna(method='ffill')

        return df

    def is_optimal_trading_time(self, asset_type: str) -> bool:
        """Vérifie si c'est le moment optimal pour trader cet actif"""
        now = datetime.utcnow()
        current_hour, current_minute = now.hour, now.minute

        optimal_ranges = self.optimal_trading_hours.get(asset_type, [(0, 0), (23, 59)])

        for start_hour, start_minute in optimal_ranges:
            current_time = current_hour * 60 + current_minute
            start_time = start_hour * 60 + start_minute

            if len(optimal_ranges) > 1:
                end_hour, end_minute = optimal_ranges[1] if optimal_ranges[0] == (start_hour, start_minute) else optimal_ranges[0]
                end_time = end_hour * 60 + end_minute

                if start_time <= current_time <= end_time:
                    return True
            else:
                return True

        return False

    def calculate_learning_coefficient(self, symbol: str) -> float:
        """Calcule un coefficient d'apprentissage basé sur la performance passée"""
        if symbol not in self.performance_tracker or len(self.performance_tracker[symbol]) < 5:
            return 1.0

        recent_performance = self.performance_tracker[symbol][-10:]
        success_rate = sum(1 for p in recent_performance if p > 0) / len(recent_performance) if recent_performance else 0.5

        # Ajuster le coefficient basé sur la performance
        if success_rate > 0.8:
            return 1.2
        elif success_rate > 0.6:
            return 1.1
        elif success_rate < 0.3:
            return 0.7
        elif success_rate < 0.5:
            return 0.9

        return 1.0

    def calculate_support_resistance(self, df: pd.DataFrame, lookback: int = 50) -> dict:
        """Calcule les niveaux de support et résistance avec méthode avancée et clustering"""
        if df is None or len(df) < lookback:
            return {}

        recent_data = df.iloc[-lookback:]
        highs = recent_data['High'].values
        lows = recent_data['Low'].values
        closes = recent_data['Close'].values

        # Méthode des pivots points avancée
        pivot = (np.max(highs) + np.min(lows) + closes[-1]) / 3
        r1 = (2 * pivot) - np.min(lows)
        s1 = (2 * pivot) - np.max(highs)
        r2 = pivot + (np.max(highs) - np.min(lows))
        s2 = pivot - (np.max(highs) - np.min(lows))

        # Méthode des plus hauts/plus bas récents
        local_maxima = []
        local_minima = []

        for i in range(2, len(recent_data)-2):
            if highs[i] >= highs[i-1] and highs[i] >= highs[i-2] and highs[i] >= highs[i+1] and highs[i] >= highs[i+2]:
                local_maxima.append(highs[i])
            if lows[i] <= lows[i-1] and lows[i] <= lows[i-2] and lows[i] <= lows[i+1] and lows[i] <= lows[i+2]:
                local_minima.append(lows[i])

        # Niveaux significatifs par clustering
        if local_maxima:
            resistance_levels = np.array(local_maxima[-5:]) if len(local_maxima) >= 5 else np.array(local_maxima)
            significant_resistance = np.mean(resistance_levels)
        else:
            significant_resistance = r1

        if local_minima:
            support_levels = np.array(local_minima[-5:]) if len(local_minima) >= 5 else np.array(local_minima)
            significant_support = np.mean(support_levels)
        else:
            significant_support = s1

        # Niveaux psychologiques (round numbers)
        current_price = closes[-1]
        psychological_levels = [
            round(current_price * 2) / 2,  # Demi-unité
            round(current_price),
            round(current_price / 10) * 10,
            round(current_price / 50) * 50,
            round(current_price / 100) * 100
        ]

        # Filtrer les niveaux proches du prix actuel
        psychological_support = [lvl for lvl in psychological_levels if lvl < current_price][-2:] if any(lvl < current_price for lvl in psychological_levels) else [significant_support]
        psychological_resistance = [lvl for lvl in psychological_levels if lvl > current_price][:2] if any(lvl > current_price for lvl in psychological_levels) else [significant_resistance]

        return {
            'pivot': pivot,
            'resistance1': r1,
            'resistance2': r2,
            'support1': s1,
            'support2': s2,
            'significant_support': significant_support,
            'significant_resistance': significant_resistance,
            'psychological_support': psychological_support,
            'psychological_resistance': psychological_resistance
        }

    def should_generate_signal(self, symbol: str) -> bool:
        """Détermine si un signal doit être généré pour ce symbole (éviter les répétitions)"""
        now = datetime.now()
        last_signal = self.last_signal_time[symbol]

        # Ne pas générer de signal si le dernier était il y a moins d'une heure
        if (now - last_signal).total_seconds() < 3600:
            return False

        # Vérifier le nombre de signaux récents pour ce symbole
        recent_signals = [s for s in list(self.signals_history)[-20:] if s['symbol'] == symbol]
        if len(recent_signals) >= 3:  # Maximum 3 signaux par heure
            return False

        return True

    def generate_ultra_precise_signal(self, df: pd.DataFrame, symbol: str) -> Tuple[str, float, dict]:
        """Génère un signal de trading ultra-précis avec analyse multi-couches"""
        if df is None or len(df) < 100:
            return "DONNÉES INSUFFISANTES", 0.0, {}

        # Vérifier si on doit générer un signal pour ce symbole
        if not self.should_generate_signal(symbol):
            return "SIGNAL RÉCENT EXISTANT", 0.0, {}

        current_price = df['Close'].iloc[-1]
        asset_type = self.trading_universe[symbol]['type']
        support_resistance = self.calculate_support_resistance(df)

        # Vérifier le moment de trading
        if not self.is_optimal_trading_time(asset_type):
            return "HORS HEURES OPTIMALES", 0.0, {}

        # Appliquer le coefficient d'apprentissage
        learning_coef = self.calculate_learning_coefficient(symbol)

        # Système de scoring avancé avec 12 facteurs
        signal_score = 0
        max_score = 48  # Score maximum possible

        # 1. Analyse de tendance multi-timeframe (8 points)
        trend_score = 0
        # Court terme (3, 5, 8)
        if all(df[f'SMA_3'].iloc[-1] > df[f'SMA_{p}'].iloc[-1] for p in [5, 8] if f'SMA_{p}' in df):
            trend_score += 2
        # Moyen terme (13, 21, 34)
        if all(df[f'SMA_13'].iloc[-1] > df[f'SMA_{p}'].iloc[-1] for p in [21, 34] if f'SMA_{p}' in df):
            trend_score += 3
        # Long terme (55, 89, 144)
        if all(df[f'SMA_55'].iloc[-1] > df[f'SMA_{p}'].iloc[-1] for p in [89, 144] if f'SMA_{p}' in df):
            trend_score += 3

        signal_score += trend_score

        # 2. Momentum et RSI multi-périodes (8 points)
        momentum_score = 0
        # RSI confluence
        rsi_bullish = all(30 < df[f'RSI_{p}'].iloc[-1] < 70 for p in [3, 6, 9] if f'RSI_{p}' in df)
        rsi_oversold = all(df[f'RSI_{p}'].iloc[-1] < 35 for p in [3, 6, 9] if f'RSI_{p}' in df)
        rsi_overbought = all(df[f'RSI_{p}'].iloc[-1] > 65 for p in [3, 6, 9] if f'RSI_{p}' in df)

        if rsi_oversold:
            momentum_score += 4
        elif rsi_overbought:
            momentum_score -= 4
        elif rsi_bullish:
            momentum_score += 2

        # Momentum positif multi-périodes
        momentum_pos = sum(1 for p in [3, 5, 10] if f'Momentum_{p}' in df and df[f'Momentum_{p}'].iloc[-1] > 0)
        momentum_score += momentum_pos

        signal_score += momentum_score

        # 3. Analyse MACD multiple (4 points)
        macd_score = 0
        macd_bullish = 0
        macd_bearish = 0

        for fast in [6, 8, 12]:
            for slow in [13, 21, 26]:
                macd_col = f'MACD_{fast}_{slow}'
                signal_col = f'MACD_Signal_{fast}_{slow}'
                if macd_col in df and signal_col in df:
                    if df[macd_col].iloc[-1] > df[signal_col].iloc[-1]:
                        macd_bullish += 1
                    else:
                        macd_bearish += 1

        if macd_bullish > macd_bearish:
            macd_score += 4
        elif macd_bearish > macd_bullish:
            macd_score -= 4

        signal_score += macd_score

        # 4. Bollinger Bands position (4 points)
        bb_score = 0
        for period in [10, 20, 50]:
            for dev in [1, 1.5, 2]:
                upper_col = f'BB_Upper_{period}_{dev}'
                lower_col = f'BB_Lower_{period}_{dev}'

                if upper_col in df and lower_col in df:
                    bb_width = df[upper_col].iloc[-1] - df[lower_col].iloc[-1]
                    bb_position = (current_price - df[lower_col].iloc[-1]) / bb_width

                    if bb_position < 0.1:  # Près de la bande inférieure
                        bb_score += 1
                    elif bb_position > 0.9:  # Près de la bande supérieure
                        bb_score -= 1

        signal_score += bb_score

        # 5. Analyse de volume avancée (4 points)
        volume_score = 0
        if 'Volume_Ratio' in df:
            volume_ratio = df['Volume_Ratio'].iloc[-1]
            if volume_ratio > 2.0 and current_price > df['Close'].iloc[-2]:
                volume_score += 4
            elif volume_ratio > 2.0 and current_price < df['Close'].iloc[-2]:
                volume_score -= 4
            elif volume_ratio < 0.5:
                volume_score -= 2  # Faible volume = manque de conviction

        signal_score += volume_score

        # 6. Support et résistance avancés (4 points)
        sr_score = 0
        distance_to_support = min(abs(current_price - s) for s in [
            support_resistance['significant_support'],
            *support_resistance['psychological_support']
        ]) / current_price if support_resistance['psychological_support'] else 0.05

        distance_to_resistance = min(abs(current_price - r) for r in [
            support_resistance['significant_resistance'],
            *support_resistance['psychological_resistance']
        ]) / current_price if support_resistance['psychological_resistance'] else 0.05

        if distance_to_support < 0.015:  # Proche d'un support fort
            sr_score += 4
        elif distance_to_resistance < 0.015:  # Proche d'une résistance forte
            sr_score -= 4

        signal_score += sr_score

        # 7. Pattern recognition avancé (4 points)
        pattern_score = 0
        bullish_patterns = ['CDLHAMMER', 'CDLENGULFING', 'CDLMORNINGSTAR', 'CDLPIERCING', 'CDL3WHITESOLDIERS']
        bearish_patterns = ['CDLSHOOTINGSTAR', 'CDLENGULFING', 'CDLEVENINGSTAR', 'CDLDARKCLOUDCOVER', 'CDL3BLACKCROWS']

        for pattern in bullish_patterns:
            if pattern in df.columns and df[pattern].iloc[-1] > 0:
                pattern_score += 2
                break

        for pattern in bearish_patterns:
            if pattern in df.columns and df[pattern].iloc[-1] > 0:
                pattern_score -= 2
                break

        signal_score += pattern_score

        # 8. ADX et force de tendance (4 points)
        adx_score = 0
        if 'ADX_14' in df:
            adx_value = df['ADX_14'].iloc[-1]
            plus_di = df['Plus_DI_14'].iloc[-1] if 'Plus_DI_14' in df else 0
            minus_di = df['Minus_DI_14'].iloc[-1] if 'Minus_DI_14' in df else 0

            if adx_value > 25:  # Tendance forte
                if plus_di > minus_di:
                    adx_score += 4
                else:
                    adx_score -= 4

        signal_score += adx_score

        # 9. Stochastic confluence (4 points)
        stoch_score = 0
        stoch_bullish = 0
        stoch_bearish = 0

        for period in [7, 14, 21]:
            k_col = f'Stoch_K_{period}'
            d_col = f'Stoch_D_{period}'

            if k_col in df and d_col in df:
                k_value = df[k_col].iloc[-1]
                d_value = df[d_col].iloc[-1]

                if k_value < 20 and d_value < 20 and k_value > d_value:
                    stoch_bullish += 1
                elif k_value > 80 and d_value > 80 and k_value < d_value:
                    stoch_bearish += 1

        if stoch_bullish > stoch_bearish:
            stoch_score += 4
        elif stoch_bearish > stoch_bullish:
            stoch_score -= 4

        signal_score += stoch_score

        # 10. Price-Volume Trend (4 points)
        pvt_score = 0
        if 'Price_Volume_Trend' in df:
            pvt_value = df['Price_Volume_Trend'].iloc[-1]
            if pvt_value > 0:
                pvt_score += 2
            else:
                pvt_score -= 2

        signal_score += pvt_score

        # Application du coefficient d'apprentissage
        signal_score *= learning_coef

        # Calcul de la confiance finale
        confidence = min(max(abs(signal_score) / max_score, 0), 1)

        # Seuil de confiance très élevé
        if confidence < self.min_confidence:
            return "CONFIANCE INSUFFISANTE", confidence, {}

        # Détermination du signal avec seuils dynamiques
        if signal_score >= 36:
            signal_type = "ACHAT FORT 🚀"
        elif signal_score >= 24:
            signal_type = "ACHAT MODÉRÉ 📈"
        elif signal_score <= -36:
            signal_type = "VENTE FORTE 🔻"
        elif signal_score <= -24:
            signal_type = "VENTE MODÉRÉE 📉"
        else:
            return "SIGNAL NEUTRE", confidence, {}

        # Calcul des targets optimisées
        targets = self.calculate_ultra_short_term_targets(df, symbol, signal_type, current_price, asset_type)

        # Mettre à jour le temps du dernier signal
        self.last_signal_time[symbol] = datetime.now()

        # Si le signal est de haute confiance, on ne le sauvegarde pas tout de suite.
        # On le passe à la chaîne de validation IA.
        if confidence >= self.min_confidence and ("FORT" in signal_type or "MODÉRÉ" in signal_type):
            print(f"🔎 Signal technique détecté pour {symbol}. Lancement de la validation par IA...")
            self.validate_signal_with_ai({
                'symbol': symbol,
                'signal': signal_type,
                'confidence': confidence,
                'price': current_price,
                'targets': targets,
                'type': asset_type,
                'sector': self.trading_universe[symbol]['sector']
            })

        return signal_type, confidence, targets

    def validate_signal_with_ai(self, analysis: dict):
        """
        Orchestre la chaîne de validation par IA pour un signal donné.
        """
        symbol = analysis['symbol']
        sector = analysis['sector']
        news_context = ""
        market_context = ""

        try:
            # 1. & 2. DeepSeek & Guardian pour les nouvelles
            print(f"   - Étape 1/3: Recherche d'actualités (DeepSeek & Guardian) pour {symbol}...")
            try:
                guardian_details = self.api_manager.get_api_details('Guardian Content')
                params = {'q': symbol, 'order-by': 'newest', 'show-fields': 'headline', 'page-size': 5}
                params[guardian_details['params']['api-key']] = guardian_details['key']
                response = requests.get(guardian_details['url'], params=params)
                response.raise_for_status()
                articles = response.json().get('response', {}).get('results', [])
                news_context += "Guardian News:\n" + "\n".join([f"- {a['fields']['headline']}" for a in articles]) + "\n\n"
            except Exception as e:
                news_context += "Guardian News: Not available.\n"
                logging.warning(f"Guardian API failed for {symbol}: {e}")

            # 3. Serper pour le contexte marché
            print(f"   - Étape 2/3: Recherche du contexte marché (Serper) pour {sector}...")
            try:
                serper_details = self.api_manager.get_api_details('Serper Search')
                headers = serper_details.get('headers', {})
                response = requests.post(
                    serper_details['url'],
                    headers=headers,
                    json={'q': f"Market sentiment and news for {symbol} and {sector} sector"}
                )
                response.raise_for_status()
                results = response.json().get('organic', [])
                market_context = "Market Context:\n" + "\n".join([f"- {r['title']}: {r.get('snippet', '')}" for r in results[:3]])
            except Exception as e:
                market_context = "Market Context: Not available.\n"
                logging.warning(f"Serper API failed for {symbol}: {e}")

            # 4. Gemini pour la synthèse et la décision finale
            print(f"   - Étape 3/3: Synthèse et décision finale (Gemini)...")
            try:
                gemini_details = self.api_manager.get_api_details('Gemini Generate Content')

                prompt = (
                    f"You are a senior financial analyst. A trading algorithm has generated a '{analysis['signal']}' signal for '{symbol}'.\n"
                    f"**Algorithm's Technical Analysis:** Confidence {analysis['confidence']:.0%}, Entry ${analysis['price']:.2f}, Target ${analysis['targets']['target_price']:.2f}, Stop ${analysis['targets']['stop_loss']:.2f}.\n\n"
                    f"**Recent News Context:**\n{news_context}\n\n"
                    f"**General Market Context:**\n{market_context}\n\n"
                    "Based on all this information, synthesize a final decision. Should this trade be executed? "
                    "Respond with 'GO' or 'NO GO' on the first line, followed by a brief 2-sentence justification."
                )

                payload = {"contents": [{"parts": [{"text": prompt}]}]}
                url = f"{gemini_details['url']}?key={gemini_details['key']}"

                response = requests.post(url, json=payload)
                response.raise_for_status()

                gemini_response_text = response.json()['candidates'][0]['content']['parts'][0]['text']

                print(f"   - Décision de Gemini: {gemini_response_text.splitlines()[0]}")

                if gemini_response_text.strip().upper().startswith('GO'):
                    print(f"✅ VALIDATION IA RÉUSSIE pour {symbol}. Le signal est confirmé.")
                    # Le signal est validé, on peut maintenant l'enregistrer et alerter.
                    self.alert_manager.save_alert(analysis['symbol'], analysis['signal'], analysis['confidence'], analysis['price'])
                    self.logger.log_signal(analysis)

                    # On stocke le signal pour l'évaluation future
                    self.past_signals.append({
                        'symbol': symbol,
                        'entry_price': analysis['price'],
                        'action': analysis['targets']['action'],
                        'stop_loss': analysis['targets']['stop_loss'],
                        'take_profit': analysis['targets']['target_price'],
                        'holding_period': analysis['targets']['holding_period_hours'],
                        'timestamp': datetime.now()
                    })
                else:
                    print(f"❌ VALIDATION IA ÉCHOUÉE pour {symbol}. Le signal est ignoré.")
                    logging.info(f"Signal for {symbol} discarded by AI validation. Reason: {gemini_response_text}")

            except Exception as e:
                logging.error(f"Gemini API failed for {symbol}: {e}")
                print(f"   - ⚠️ Erreur de validation Gemini pour {symbol}. Le signal est ignoré par sécurité.")

        except Exception as e:
            logging.error(f"Erreur dans la chaîne de validation IA pour {symbol}: {e}")
            print(f"   - ⚠️ Erreur dans la chaîne de validation IA pour {symbol}. Le signal est ignoré.")

    def calculate_ultra_short_term_targets(self, df: pd.DataFrame, symbol: str, signal_type: str,
                                          current_price: float, asset_type: str) -> dict:
        """Calcule les objectifs de prix et délais ultra-courts optimisés"""
        params = self.trading_params[asset_type]

        # Utiliser ATR pour le calcul des targets
        atr = df['ATR_14'].iloc[-1] if 'ATR_14' in df else current_price * 0.01

        support_resistance = self.calculate_support_resistance(df)

        # Calcul du délai de trading (en heures)
        base_holding_hours = params['max_hours']
        # Ajustement en fonction de la volatilité
        volatility_factor = min(2.0, max(0.5, atr / current_price * 100))
        holding_hours = int(base_holding_hours * volatility_factor)

        if "ACHAT" in signal_type:
            # Target basée sur ATR et résistance la plus proche
            atr_target = current_price + (2.5 * atr)

            # Trouver la résistance la plus proche
            resistance_levels = [
                support_resistance['resistance1'],
                support_resistance['resistance2'],
                support_resistance['significant_resistance'],
                *support_resistance['psychological_resistance']
            ]
            nearest_resistance = min((r for r in resistance_levels if r > current_price),
                                    default=atr_target, key=lambda x: x - current_price)

            target_price = min(atr_target, nearest_resistance)
            stop_loss = current_price * (1 - params['stop_loss'])

            # Garantir un ratio risque/récompense minimum
            min_reward = (current_price - stop_loss) * 1.5
            target_price = max(target_price, current_price + min_reward)

            potential_gain = ((target_price - current_price) / current_price) * 100
            risk_reward = (target_price - current_price) / (current_price - stop_loss)

            return {
                'action': 'BUY',
                'entry_price': round(current_price, 4),
                'target_price': round(target_price, 4),
                'stop_loss': round(stop_loss, 4),
                'potential_gain': round(potential_gain, 2),
                'holding_period_hours': holding_hours,
                'risk_reward_ratio': round(risk_reward, 2),
                'confidence_level': 'HIGH' if "FORT" in signal_type else 'MEDIUM'
            }

        elif "VENTE" in signal_type:
            # Target basée sur ATR et support le plus proche
            atr_target = current_price - (2.5 * atr)

            # Trouver le support le plus proche
            support_levels = [
                support_resistance['support1'],
                support_resistance['support2'],
                support_resistance['significant_support'],
                *support_resistance['psychological_support']
            ]
            nearest_support = max((s for s in support_levels if s < current_price),
                                 default=atr_target, key=lambda x: current_price - x)

            target_price = max(atr_target, nearest_support)
            stop_loss = current_price * (1 + params['stop_loss'])

            # Garantir un ratio risque/récompense minimum
            min_reward = (stop_loss - current_price) * 1.5
            target_price = min(target_price, current_price - min_reward)

            potential_gain = ((current_price - target_price) / current_price) * 100
            risk_reward = (current_price - target_price) / (stop_loss - current_price)

            return {
                'action': 'SELL',
                'entry_price': round(current_price, 4),
                'target_price': round(target_price, 4),
                'stop_loss': round(stop_loss, 4),
                'potential_gain': round(potential_gain, 2),
                'holding_period_hours': holding_hours,
                'risk_reward_ratio': round(risk_reward, 2),
                'confidence_level': 'HIGH' if "FORT" in signal_type else 'MEDIUM'
            }

        return {}

    def track_performance(self, symbol: str, signal_type: str, targets: dict, success: bool):
        """Track performance of signals for learning"""
        if not targets:
            return

        gain = targets['potential_gain'] if success else -targets['potential_gain']
        self.performance_tracker[symbol].append(gain)

        # Garder seulement les 100 dernières performances
        if len(self.performance_tracker[symbol]) > 100:
            self.performance_tracker[symbol] = self.performance_tracker[symbol][-100:]

    def analyze_instrument(self, symbol: str) -> dict:
        """Analyse complète d'un instrument de trading"""
        try:
            # Récupérer les données en temps réel
            df = self.fetch_market_data(symbol)

            if df is not None and len(df) > 100:
                df = self.calculate_indicators(df)
                signal, confidence, targets = self.generate_ultra_precise_signal(df, symbol)
                current_price = df['Close'].iloc[-1]

                analysis = {
                    'symbol': symbol,
                    'price': current_price,
                    'signal': signal,
                    'confidence': confidence,
                    'targets': targets,
                    'type': self.trading_universe[symbol]['type'],
                    'sector': self.trading_universe[symbol]['sector'],
                    'timestamp': datetime.now().isoformat(),
                    'volume': df['Volume'].iloc[-1]
                }

                self.signals_history.append(analysis)

                # La logique de logging et de suivi a été déplacée dans `validate_signal_with_ai`
                # pour ne s'exécuter qu'après une validation "GO" de Gemini.

                return analysis
            else:
                return {
                    'symbol': symbol,
                    'price': None,
                    'signal': "DONNÉES INSUFFISANTES",
                    'confidence': 0.0,
                    'targets': {},
                    'type': self.trading_universe[symbol]['type'],
                    'sector': self.trading_universe[symbol]['sector'],
                    'timestamp': datetime.now().isoformat()
                }

        except Exception as e:
            logging.error(f"Erreur analyse {symbol}: {str(e)}")
            return {
                'symbol': symbol,
                'price': None,
                'signal': f"ERREUR: {str(e)}",
                'confidence': 0.0,
                'targets': {},
                'type': self.trading_universe[symbol]['type'],
                'sector': self.trading_universe[symbol]['sector'],
                'timestamp': datetime.now().isoformat()
            }

    def auto_evaluate_signals(self):
        """Revisite les anciens signaux et évalue leur performance en utilisant SL/TP."""
        current_time = datetime.now()

        for signal in self.past_signals[:]:  # Copie pour modification safe
            time_elapsed_hours = (current_time - signal['timestamp']).total_seconds() / 3600

            # Pour une évaluation plus réaliste, on aurait besoin des données OHLC sur la période.
            # En l'absence de ça, on fait une simplification : on regarde le prix actuel
            # et on voit s'il a dépassé le SL/TP ou si le temps est écoulé.

            is_expired = time_elapsed_hours >= signal['holding_period']

            try:
                current_price = self.fetch_current_price(signal['symbol'])
                if not current_price or current_price == 0.0:  # Ne peut pas récupérer le prix
                    continue

                pnl = 0
                trade_closed = False
                exit_price = current_price

                if signal['action'] == 'BUY':
                    if current_price <= signal['stop_loss']:
                        pnl = (signal['stop_loss'] - signal['entry_price']) / signal['entry_price']
                        exit_price = signal['stop_loss']
                        trade_closed = True
                    elif current_price >= signal['take_profit']:
                        pnl = (signal['take_profit'] - signal['entry_price']) / signal['entry_price']
                        exit_price = signal['take_profit']
                        trade_closed = True

                elif signal['action'] == 'SELL':
                    if current_price >= signal['stop_loss']:
                        pnl = (signal['entry_price'] - signal['stop_loss']) / signal['entry_price']
                        exit_price = signal['stop_loss']
                        trade_closed = True
                    elif current_price <= signal['take_profit']:
                        pnl = (signal['entry_price'] - signal['take_profit']) / signal['entry_price']
                        exit_price = signal['take_profit']
                        trade_closed = True

                # Si le trade n'a pas touché SL/TP mais que le temps est écoulé, on le ferme au prix actuel
                if not trade_closed and is_expired:
                    if signal['action'] == 'BUY':
                        pnl = (current_price - signal['entry_price']) / signal['entry_price']
                    else: # SELL
                        pnl = (signal['entry_price'] - current_price) / signal['entry_price']
                    trade_closed = True

                if trade_closed:
                    # Log automatique
                    self.logger.log_performance(
                        signal['symbol'],
                        signal['entry_price'],
                        exit_price,
                        pnl
                    )

                    # Apprentissage auto
                    if pnl > 0:
                        self.performance_tracker[signal['symbol']].append(1.0)
                    else:
                        self.performance_tracker[signal['symbol']].append(-1.0)

                    # Retire le signal traité
                    self.past_signals.remove(signal)

            except Exception as e:
                print(f"Erreur évaluation {signal['symbol']}: {str(e)}")

    def fetch_current_price(self, symbol: str) -> float:
        """Récupère le prix actuel rapidement"""
        try:
            df = self.fetch_market_data(symbol)
            if df is not None and len(df) > 0:
                return df['Close'].iloc[-1]
        except:
            pass
        return 0.0

    def generate_ultra_precise_recommendations(self, analyses: list):
        """Génère des recommandations de trading ultra-précises"""
        # Filtrage des signaux de haute qualité uniquement
        high_quality_signals = [a for a in analyses
                               if ("FORT" in a['signal'] or "MODÉRÉ" in a['signal'])
                               and a['confidence'] >= self.min_confidence
                               and a['targets']]

        # Séparation achats/ventes
        buys = [a for a in high_quality_signals if "ACHAT" in a['signal']]
        sells = [a for a in high_quality_signals if "VENTE" in a['signal']]

        # Tri par ratio risque/récompense et gain potentiel
        buys.sort(key=lambda x: (x['targets'].get('risk_reward_ratio', 0),
                               x['targets'].get('potential_gain', 0)), reverse=True)
        sells.sort(key=lambda x: (x['targets'].get('risk_reward_ratio', 0),
                                x['targets'].get('potential_gain', 0)), reverse=True)

        # Top recommandations seulement
        top_buys = buys[:5]
        top_sells = sells[:3]

        return {
            'top_buys': top_buys,
            'top_sells': top_sells,
            'timestamp': datetime.now().isoformat()
        }

    def display_ultra_precise_results(self, analyses: list, recommendations: dict):
        """Affiche SEULEMENT les alertes importantes"""
        significant_signals = [a for a in analyses
                              if a['price'] is not None
                              and a['targets']
                              and a['confidence'] >= self.min_confidence
                              and ("FORT" in a['signal'] or "MODÉRÉ" in a['signal'])]

        # Affiche seulement s'il y a des signaux
        if significant_signals:
            print(f"\n🚨 ALERTES TRADING {datetime.now().strftime('%H:%M:%S')}")
            print("=" * 100)

            for analysis in significant_signals:
                targets = analysis['targets']
                gain_str = f"+{targets['potential_gain']}%" if targets['action'] == 'BUY' else f"+{targets['potential_gain']}%"

                print(f"{analysis['symbol']} - {analysis['signal']} ({analysis['confidence']:.0%})")
                print(f"💰 Prix: ${analysis['price']:.2f} | 🎯 Cible: ${targets['target_price']:.2f}")
                print(f"⚡ Gain: {gain_str} | ⏱ Délai: {targets['holding_period_hours']}h")
                print(f"🛡 Stop: ${targets['stop_loss']:.2f} | 📊 R/R: {targets['risk_reward_ratio']:.1f}")
                print("-" * 50)

        # Affiche aussi les recommandations top
        if recommendations['top_buys'] or recommendations['top_sells']:
            print("\n⭐️ TOP RECOMMANDATIONS:")
            for rec in recommendations['top_buys'][:3] + recommendations['top_sells'][:2]:
                targets = rec['targets']
                emoji = "🚀" if "FORT" in rec['signal'] else "📈"
                if "VENTE" in rec['signal']:
                    emoji = "🔻" if "FORT" in rec['signal'] else "📉"

                print(f"{emoji} {rec['symbol']}: {rec['signal']} ({rec['confidence']:.0%})")

    def run_analysis(self):
        """Exécute l'analyse complète avec gestion des quotas"""
        print(f"\n🔍 Scan {datetime.now().strftime('%H:%M:%S')}")  # Plus court !

        analyses = []
        for symbol in self.symbols:
            analysis = self.analyze_instrument(symbol)
            analyses.append(analysis)
            time.sleep(1)  # Respect des quotas API

        # Générer les recommandations
        recommendations = self.generate_ultra_precise_recommendations(analyses)

        # Afficher les résultats
        self.display_ultra_precise_results(analyses, recommendations)

        return recommendations

    def continuous_monitoring(self):
        """Surveillance continue avec gestion optimisée des quotas"""
        print("🚀 Démarrage surveillance...")
        cycle_count = 0

        try:
            while True:
                cycle_count += 1
                print(f"\n📈 CYCLE D'ANALYSE ULTRA-PRÉCISE #{cycle_count}")
                print("=" * 100)

                start_time = time.time()
                recommendations = self.run_analysis()

                self.auto_evaluate_signals()  # Évalue les anciens signaux

                # Temps de traitement
                processing_time = time.time() - start_time
                sleep_time = max(5, self.update_interval - processing_time)

                print(f"⏳ Prochaine analyse dans {sleep_time:.0f} secondes...")
                time.sleep(sleep_time)

        except KeyboardInterrupt:
            print("\n🛑 Arrêt du système.")
        except Exception as e:
            logging.error(f"Erreur monitoring: {str(e)}")
            print(f"❌ Erreur système: {str(e)}")

# Exécution
if __name__ == "__main__":
    system = ProfessionalTradingSystem()
    system.continuous_monitoring()
