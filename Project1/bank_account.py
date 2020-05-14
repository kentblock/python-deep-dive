import datetime


class TimeZone:

    def __init__(self, name, hours, minutes):
        self.name = name
        self.offset_minutes = minutes
        self.offset_hours = hours

    @property
    def name(self):
        return self._name

    @property
    def offset_hours(self):
        return self._offset_hours

    @property
    def offset_minutes(self):
        return self._offset_minutes

    @name.setter
    def name(self, name):
        if name is None:
            raise TypeError("name attribute must not be none.")
        if len(name.strip()) == 0:
            raise TypeError("name attribute must not be empty.")
        self._name = str(name).strip()

    @offset_hours.setter
    def offset_hours(self, hours):
        if not isinstance(hours, int):
           raise TypeError("hours must be an integer.") 
        if hours < 0 or hours > 23:
            raise ValueError("hours must be a value between 0 and 23")
        self._offset_hours = hours

    @offset_minutes.setter
    def offset_minutes(self, minutes):
        if not isinstance(minutes, int):
           raise TypeError("minutes must be an integer.") 
        if minutes < 0 or minutes > 59 :
            raise ValueError("minutes must be a value between 0 and 59")
        self._offset_minutes = minutes


class BankAccount:

    WITHDRAW_SYMBOL = 'W'
    DEPOSIT_SYMBOL = 'D'
    INTEREST_SYMBOL = 'I'
    DENIED_SYMBOL = 'X'
    _monthly_int_rate = 2.5

    @classmethod
    def set_int_rate(cls, int_rate):
        if not isinstance(int_rate, float):
            raise TypeError("Interest rate value must be a float.")
        if int_rate < 0:
            raise ValueError("Interest rate must be non-negative.")
        cls._monthly_int_rate = int_rate

    @classmethod
    def get_int_rate(cls):
        return cls._monthly_int_rate

    def __init__(self, account_num, first_name, last_name, initial_balance=0, tz=None):
        self._balance = float(initial_balance)
        self.account_num = account_num
        self.first_name = first_name
        self.last_name = last_name
        self.transaction_codes = []
        self.last_trans_id = -1

        if tz is None:
            self.tz = TimeZone('UTC', 0, 0)
        else:
            self.tz = tz

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def tz(self):
        return self._tz

    @tz.setter
    def tz(self, tz):
        if not isinstance(tz, TimeZone):
            raise TypeError("tz attribute must be of type timezone.")
        self._tz = tz

    @first_name.setter
    def first_name(self, name):
        if name is None or len(name.strip()) == 0:
            raise ValueError("first name attribute must be non-empty")
        self._first_name = str(name).strip()
    
    @last_name.setter
    def last_name(self, name):
        if name is None or len(name.strip()) == 0:
            raise ValueError("last name attribute must be non-empty")
        self._last_name = str(name).strip()

    @property
    def balance(self):
        return self._balance

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def deposit(self, amount):
        if not isinstance(amount, float):
            raise TypeError("deposit amount must be of type float")
        if amount < 0:
            return self.generate_confirmation_code(self.DENIED_SYMBOL)
            raise ValueError("Deposit amount must be greater than 0.")
        self._balance += amount
        return self.generate_confirmation_code(self.DEPOSIT_SYMBOL)

    def withdrawal(self, amount):
        if not isinstance(amount, float):
            raise TypeError("withdrawal amount must be of type float")
        if amount > self.balance:
            raise ValueError("Insufficient Balance.")
            return self.generate_confirmation_code(self.DENIED_SYMBOL)
        else:
            self._balance -= amount
            return self.generate_confirmation_code(self.WITHDRAW_SYMBOL)

    def pay_interest(self):
        interest = self.balance * self._monthly_int_rate
        self._balance -= interest
        return self.generate_confirmation_code(self.INTEREST_SYMBOL)

    def generate_confirmation_code(self, sym):
        self.last_trans_id += 1
        return f"{sym}-{self.account_num}-{self.get_time()}-{self.last_trans_id}"

    def get_time(self):
        now = datetime.datetime.now()
        adjusted_time = now + datetime.timedelta(hours=self.tz.offset_hours, minutes=self.tz.offset_minutes)
        return adjusted_time.strftime("%Y%m%d%H%M%S")
    
    @staticmethod
    def parse_confirmation_code(conf_code, tz=None):
        """parse a confirmation code and return a transaction object instance"""
        code_symbols = conf_code.split('-')
        if len(code_symbols) != 4:
            raise ValueError("Invalid confirmation code.")
        transaction_obj = Transaction()
        Transaction.account_number = code_symbols[1]
        Transaction.transaction_code = code_symbols[0]
        Transaction.transaction_id = code_symbols[3]

        code_time = datetime.strptime("%Y%m%d%H%M%S")
        tz_name = 'UTC'
        utc_time = code_time
        if tz:
            tz_name = tz.name
            utc_time = code_time - datetime.timedelta(hours=tz.offset_hours, minutes=tz.offset_minutes)
        Transaction.time = code_time.strftime(f"%Y-%m-%d %H:%M:%S {tz_name}")
        Transaction.time = utc_time.strftime(f"%Y-%m-%dT%H:%M:%S")

class Transaction:

    @property
    def account_number(self):
        return self._account_number

    @property
    def transaction_code(self):
        return self._transaction_code

    @property
    def transaction_id(self):
        return self._transaction_id

    @property
    def time(self):
        return self._time

    @property
    def time_utc(self):
        return self._time_utc

    @account_number.setter
    def account_number(self, acc_num):
        self._acc_num = acc_num

    @transaction_code.setter
    def transaction_code(self, transaction_code):
        self._transaction_code = tc

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        self._transaction_id = transaction_id

    @time.setter
    def time(self, time):
        self._time = time

    @time_utc.setter
    def time_utc(self, time_utc):
        self._time_utc = time_utc