from ..responses import ResponseComponent, Root, CodeValuePair


class StockExchange(ResponseComponent):
    foreign_etf_stock_exchange: Root[CodeValuePair]
