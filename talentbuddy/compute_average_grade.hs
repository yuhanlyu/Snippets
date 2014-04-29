compute_average_grade :: [Integer] -> IO ()
compute_average_grade grades =
    print $ (sum grades) `div` (toInteger $ length grades)

main :: IO ()
main = compute_average_grade [1, 2, 8, 4, 5, 8, 3]
