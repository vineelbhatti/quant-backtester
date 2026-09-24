from dataclasses import dataclass

@dataclass
class Trade:
    entry_price: float
    entry_date: str
    exit_price: float
    exit_date: str

    @property
    def pnl(self):
        return (self.exit_price - self.entry_price) / self.entry_price