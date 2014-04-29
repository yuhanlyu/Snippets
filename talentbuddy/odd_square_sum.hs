odd_square_sum :: Integer -> Integer -> IO ()
odd_square_sum x y = print $ foldl (+) 0 [k * k | k <- [x..y], odd k]

main :: IO ()
main = odd_square_sum 1 5
