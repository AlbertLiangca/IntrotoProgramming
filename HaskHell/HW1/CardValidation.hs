{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use foldr" #-}
numDigits :: Integer -> Integer
numDigits 0 = 0
numDigits n = 1 + numDigits (div n 10)

intListLength :: [Integer] -> Integer
intListLength = foldr (\ x -> (+) 1) 0

toDigitsRev :: Integer -> [Integer]
toDigitsRev n
    |   n <= 0           = []
    |   numDigits n == 1 = [n]
    |   otherwise        = n `mod` 10 : toDigitsRev (n `div` 10)

toDigits :: Integer -> [Integer]
toDigits n
    |   n <= 0           = []
    |   numDigits n == 1 = [n]
    |   otherwise        = toDigits (n `div` 10) ++ [n `mod` 10]

doubleEveryOther :: [Integer] -> [Integer]
doubleEveryOther [] = []
doubleEveryOther [n] = [n]
doubleEveryOther (n:ns)
    |   even (intListLength (n:ns)) = 2*n : doubleEveryOther ns
    |   otherwise                   = n : doubleEveryOther ns

sumDigits :: [Integer] -> Integer
sumDigits [] = 0
sumDigits [n] = n
sumDigits (n:ns) = sumDigits (toDigits n) + sumDigits ns

validate :: Integer -> Bool
validate n
    |   sumDigits (doubleEveryOther (toDigits n)) `mod` 10 == 0 = True
    |   otherwise                                               = False