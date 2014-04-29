import Data.Bits

count_one :: Integer -> IO ()
count_one = print . popCount

main :: IO ()
main = count_one 5
