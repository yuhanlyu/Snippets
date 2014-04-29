longest_improvement :: [Integer] -> IO ()
longest_improvement = 
    print . maximum . (map fst) . (scanl f (1 :: Integer, 0 :: Integer)) where
        f (chain, previous) x = (if previous <= x then chain + 1 else 1, x)

main :: IO ()
main = longest_improvement [9, 7, 8, 2, 5, 5, 8, 7]
