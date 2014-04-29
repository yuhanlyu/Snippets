fizzbuzz :: Integer -> IO ()
fizzbuzz n = mapM_ putStrLn . map f $ [1..n]
    where f x 
            | x `mod` 15 == 0 = "FizzBuzz"
            | x `mod` 5 == 0  = "Buzz"
            | x `mod` 3 == 0  = "Fizz"
            | otherwise       = show x 

main :: IO ()
main = fizzbuzz 15
