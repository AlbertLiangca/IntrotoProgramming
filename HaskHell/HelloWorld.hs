x :: Int
x = 5

y :: Int
y = y + 1

sumtorial :: Integer -> Integer
sumtorial 0 = 0
sumtorial n = n * sumtorial (n-1)

hailstone :: Integer -> Integer
hailstone n
    |   even n    = n `div` 2
    |   otherwise = n * 3 + 1

foo :: Integer -> Integer
foo 0 = 16
foo 1 
  | "Haskell" > "C++" = 3
  | otherwise         = 4
foo n
  | n < 0            = 0
  | n `mod` 17 == 2  = -43
  | otherwise        = n + 3

f :: Int -> Int -> Int -> Int
f x y z = x + y + z
