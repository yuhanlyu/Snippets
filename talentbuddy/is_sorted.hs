is_sorted :: [Integer] -> IO ()
is_sorted grades = print $ if and $ zipWith (<=) grades (tail grades) 
                           then (1 :: Integer) else (0 :: Integer)

main :: IO ()
main = is_sorted [1, 3, 3, 7]
