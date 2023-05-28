import unittest
import random
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      # compute expected outcomes
      expected_stock = quote['stock']
      expected_bid_price = float(quote['top_bid']['price'])
      expected_ask_price = float(quote['top_ask']['price'])
      expected_price = (expected_bid_price + expected_ask_price)/2
      expected_return_value = (expected_stock, expected_bid_price, expected_ask_price, expected_price)

      # assert returned value matches expected value
      self.assertEqual(getDataPoint(quote), expected_return_value)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 117.87, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121.68, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      # compute expected outcomes
      expected_stock = quote['stock']
      expected_bid_price = float(quote['top_bid']['price'])
      expected_ask_price = float(quote['top_ask']['price'])
      expected_price = (expected_bid_price + expected_ask_price)/2
      expected_return_value = (expected_stock, expected_bid_price, expected_ask_price, expected_price)

      # assert returned value matches expected value
      self.assertEqual(getDataPoint(quote), expected_return_value)


  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_calculatePriceAskGreaterThanBid(self):
    quotes = [
      {'top_ask': {'price': 120.48, 'size': 109}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 119.2, 'size': 36}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 81}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 4}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      # compute expected outcomes
      expected_stock = quote['stock']
      expected_bid_price = float(quote['top_bid']['price'])
      expected_ask_price = float(quote['top_ask']['price'])
      expected_price = (expected_bid_price + expected_ask_price)/2
      expected_return_value = (expected_stock, expected_bid_price, expected_ask_price, expected_price)

      # assert returned value matches expected value
      self.assertEqual(getDataPoint(quote), expected_return_value)
  

  def test_getDataPoint_calculatePriceAskEqualToBid(self):
    quotes = [
      {'top_ask': {'price': 120.48, 'size': 109}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 36}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 81}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121.68, 'size': 4}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      # compute expected outcomes
      expected_stock = quote['stock']
      expected_bid_price = float(quote['top_bid']['price'])
      expected_ask_price = float(quote['top_ask']['price'])
      expected_price = (expected_bid_price + expected_ask_price)/2
      expected_return_value = (expected_stock, expected_bid_price, expected_ask_price, expected_price)

      # assert returned value matches expected value
      self.assertEqual(getDataPoint(quote), expected_return_value)


  def test_getRatio_calculateRatioPriceAGreaterThanPriceB(self):
    price_a = random.uniform(100, 105)
    price_b = random.uniform(95, 99)
    expected_return_value = price_a / price_b
    self.assertEqual(getRatio(price_a, price_b), expected_return_value)
  

  def test_getRatio_calculateRatioPriceBGreaterThanPriceA(self):
    price_a = random.uniform(95, 99)
    price_b = random.uniform(100, 105)
    expected_return_value = price_a / price_b
    self.assertEqual(getRatio(price_a, price_b), expected_return_value)
  

  def test_getRatio_calculateRatioPriceAEqualsZeroAndPriceBGreaterThanZero(self):
    price_a = 0.0
    price_b = random.uniform(100, 105)
    self.assertEqual(getRatio(price_a, price_b), 0.0)
  

  def test_getRatio_calculateRatioPriceBEqualsZeroAndPriceAGreaterThanZero(self):
    price_a = random.uniform(100, 105)
    price_b = 0.0
    self.assertIsNone(getRatio(price_a, price_b))

if __name__ == '__main__':
    unittest.main()
