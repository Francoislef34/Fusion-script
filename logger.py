import csv
import os
from datetime import datetime

class AdvancedLogger:
    def __init__(self, signal_file='signals_log.csv', performance_file='performance_log.csv'):
        self.signal_file = signal_file
        self.performance_file = performance_file
        self._initialize_files()

    def _initialize_files(self):
        """Crée les fichiers CSV avec les en-têtes s'ils n'existent pas."""
        if not os.path.exists(self.signal_file):
            with open(self.signal_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    'timestamp', 'symbol', 'signal_type', 'confidence',
                    'entry_price', 'target_price', 'stop_loss',
                    'risk_reward_ratio', 'holding_period_hours'
                ])

        if not os.path.exists(self.performance_file):
            with open(self.performance_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    'timestamp', 'symbol', 'entry_price', 'exit_price', 'pnl_percent'
                ])

    def log_signal(self, analysis: dict):
        """Enregistre un signal de trading validé dans le fichier CSV."""
        try:
            with open(self.signal_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    datetime.now().isoformat(),
                    analysis['symbol'],
                    analysis['signal'],
                    f"{analysis['confidence']:.2%}",
                    analysis['targets']['entry_price'],
                    analysis['targets']['target_price'],
                    analysis['targets']['stop_loss'],
                    analysis['targets']['risk_reward_ratio'],
                    analysis['targets']['holding_period_hours']
                ])
        except Exception as e:
            print(f"Erreur lors de l'écriture du log de signal : {e}")

    def log_performance(self, symbol: str, entry_price: float, exit_price: float, pnl: float):
        """Enregistre la performance d'un trade fermé dans le fichier CSV."""
        try:
            with open(self.performance_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    datetime.now().isoformat(),
                    symbol,
                    entry_price,
                    exit_price,
                    f"{pnl:.2%}"
                ])
        except Exception as e:
            print(f"Erreur lors de l'écriture du log de performance : {e}")
