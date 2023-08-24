data Thing = Shoe
           | Ship
           | SealingWax
           | Cabbage
           | King
    deriving Show

shoe :: Thing
shoe = Shoe

listO'Things :: [Thing]
listO'Things = [Shoe, SealingWax, King, Cabbage, King]

data FailableDouble = Failure
                    | OK Double
    deriving Show

ex01 :: FailableDouble
ex01 = Failure

ex02 :: FailableDouble
ex02 = OK 3.24

safeDiv :: Double -> Double -> FailableDouble
safeDiv _ 0 = Failure
safeDiv x y = OK (x/y)