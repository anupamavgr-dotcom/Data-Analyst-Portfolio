SELECT SUM(Sales) AS TotalSales
FROM sales_data;
SELECT SUM(Profit) AS TotalProfit
FROM sales_data;
SELECT COUNT(OrderID) AS TotalOrders
FROM sales_data;
SELECT SUM(Quantity) AS TotalQuantity
FROM sales_data;
SELECT AVG(Sales) AS AverageSales
FROM sales_data;
SELECT MAX(Sales) AS HighestSale
FROM sales_data;
SELECT MIN(Sales) AS LowestSale
FROM sales_data;
SELECT
Region,
SUM(Sales) AS TotalSales
FROM sales_data
GROUP BY Region
ORDER BY TotalSales DESC;
SELECT
Region,
SUM(Profit) AS TotalProfit
FROM sales_data
GROUP BY Region
ORDER BY TotalProfit DESC;
SELECT
Category,
SUM(Sales) AS TotalSales
FROM sales_data
GROUP BY Category
ORDER BY TotalSales DESC;
SELECT
Category,
SUM(Profit) AS TotalProfit
FROM sales_data
GROUP BY Category;
SELECT
State,
SUM(Sales) AS TotalSales
FROM sales_data
GROUP BY State
ORDER BY TotalSales DESC;
SELECT
Customer,
SUM(Sales) AS TotalSales
FROM sales_data
GROUP BY Customer
ORDER BY TotalSales DESC
LIMIT 10;
SELECT
Product,
SUM(Sales) AS TotalSales
FROM sales_data
GROUP BY Product
ORDER BY TotalSales DESC
LIMIT 10;
SELECT
MONTH(STR_TO_DATE(`Order Date`, '%d-%m-%Y')) AS Month,
SUM(Sales) AS TotalSales
FROM sales_data
GROUP BY Month
ORDER BY Month;
SELECT
ROUND((SUM(Profit)/SUM(Sales))*100,2) AS ProfitMargin
FROM sales_data;
SELECT
Product,
SUM(Profit) AS TotalProfit
FROM sales_data
GROUP BY Product
ORDER BY TotalProfit DESC
LIMIT 5;
SELECT
Category,
SUM(Quantity) AS QuantitySold
FROM sales_data
GROUP BY Category;
SELECT
State,
COUNT(OrderID) AS Orders
FROM sales_data
GROUP BY State;
SELECT
Region,
AVG(Sales) AS AverageSales
FROM sales_data
GROUP BY Region;
