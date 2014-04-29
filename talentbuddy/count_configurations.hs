count_configurations :: Integer -> Integer -> Integer -> Integer -> IO ()
count_configurations a b c n =
    print $ length [0 :: Integer | x <- [0..a], y <- [0..b], z <- [0..c], 
                                   x + y + z == n]

main :: IO ()
main = do
    count_configurations 1 1 1 2
    count_configurations 2 2 2 2
