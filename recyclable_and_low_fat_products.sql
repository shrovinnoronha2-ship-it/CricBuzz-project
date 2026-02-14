-- Solution to find products that are both low fat and recyclable
-- Problem: Find the ids of products that are both low fat and recyclable
-- 
-- Table: Products
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | product_id  | int     |
-- | low_fats    | enum    |
-- | recyclable  | enum    |
-- +-------------+---------+
--
-- low_fats is an ENUM of type ('Y', 'N') where 'Y' means low fat
-- recyclable is an ENUM of type ('Y', 'N') where 'Y' means recyclable

SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
