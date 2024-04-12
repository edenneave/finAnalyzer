import unittest
from io import StringIO

#FinancialTransaction class allows for the program to read FinancialTransaction data found in test setUp and main below.
#This class does not need to be edited
class FinancialTransaction:
    def __init__(self, date, type, amount):
        self.date = date
        self.type = type
        self.amount = amount

    @staticmethod
    def from_line(line):
        parts = line.strip().split(',')
        date, type, amount = parts[0], parts[1], float(parts[2])
        return FinancialTransaction(date, type, amount)

class FinancialHealthAnalyzer:
    def __init__(self, transactions):
        self.transactions = transactions

    #Adds together all transactions labeled "Income"
    #Change each value from dollars to rands by multiplying each amount by 20
    def total_revenue(self):
        #round revenue off to 2 decimal places as we are working with currency
        return round(sum(transaction.amount*20 for transaction in self.transactions if transaction.type == "Income"), 2)

    #Adds together all transactions labeled "Expense"
    #Expenses are given in rands so no need to multiply by 20
    def total_expenses(self):
        #round expenses off to 2 decimal places as we are working with currency
        return round(sum(transaction.amount for transaction in self.transactions if transaction.type == "Expense"), 2)

    #Finds the difference between the total revenue and total expenses to return profit
    def profit(self):
        #round profit off to 2 decimal places as we are working with currency
        return round(self.total_revenue() - self.total_expenses(), 2)

    #Divides the profit with the total revenue to return profit margin
    def profit_margin(self):
        #Check if total revenue is 0 before trying to calculate profit margin to ensure the fraction is not undefined
        if self.total_revenue() == 0:
            return 0
        #round profit margin off to 4 decimal places as we are working with a margin (margins are usually expressed as percentages, therefore 4 decimal places is better)
        return round(self.profit()/self.total_revenue(), 4)

    #Divides the profit by the number of transactions to return the average transaction amount
    def average_transaction_amount(self):
       #Check if the numbeer of transactions is 0 before trying to calculate the average transaction amount to ensure the fraction is not undefined 
        if len(self.transactions) == 0:
            return 0
        #round average transaction amount off to 2 decimal places as we are working with currency
        return round(self.profit()/len(self.transactions), 2)


    #Determines finalncial health and returns the corresponding string
    def financial_health(self):
        profit = self.profit()
        if profit >= 0:
            return "Healthy"
        #corrected the line below by changing the direction of the sign
        elif -1000 <= profit  < 0:
            return "Warning"
        else:
            return "Critical"

class TestFinancialHealthAnalyzer(unittest.TestCase):
    #Setup data allows for code to be tested without manually writing test transaction code for every test function. 
    #setUp transaction data and structure may be changed to include more test functions.
    def setUp(self):
        transactions_data = [
            FinancialTransaction("2024-01-01", "Income", 17),
            FinancialTransaction("2024-01-02", "Expense", 1100),
            FinancialTransaction("2024-01-03", "Expense", 300.99),
            FinancialTransaction("2024-01-04", "Expense", 600),
            FinancialTransaction("2024-01-05", "Income", 23),

        ]
        self.transactions = transactions_data

    #Test case example that returns total revenue. Inluded as a tutorial for basis of other test cases.
    def test_total_revenue(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.total_revenue(), 800)
    
    #This test case checks if the total expenses is being calculated correctly 
    def test_total_expenses(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.total_expenses(), 2000.99)

    #This test case checks if the profit is being calculated correctly 
    def test_profit(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.profit(), -1200.99)

    #This test case checks if the profit margin is being calculated correctly 
    def test_profit_margin(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.profit_margin(), -1.5012)

    #This test case checks if the average transaction amount is being calculated correctly 
    def test_average_transaction_amount(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.average_transaction_amount(), -240.20)


    #This test case checks if the financial health is being calculated correctly 
    def test_financial_health_Critical(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.financial_health(), "Critical")


    #Additional testing methods might be required. test_total_revenue can be changed/expanded

#Main function is where your code starts to run. Methods need to be compiled correctly before they can be called from main    
if __name__ == '__main__':
    #Do not change the transaction data, this data needs to produce the correct output stated in the lab brief
    transactions_data = [
            FinancialTransaction("2024-01-01", "Income", 50),
            FinancialTransaction("2024-01-02", "Expense", 500),
            FinancialTransaction("2024-01-03", "Expense", 300),
            FinancialTransaction("2024-01-04", "Income", 75)
        ]
    FinancialHealthAnalyzer.transactions = transactions_data
    analyzer = FinancialHealthAnalyzer(FinancialHealthAnalyzer.transactions)
    #called each function so that the values are printed next to their corresponding heading
    print("Profit: R", analyzer.profit())
    print("Profit margin: ", analyzer.profit_margin())
    print("Average transaction amount: R", analyzer.average_transaction_amount())
    print("Financial health: ", analyzer.financial_health())
    unittest.main()
    