max_grade :: [Integer] -> IO ()
max_grade = print . maximum

main :: IO ()
main = max_grade [1, 2, 8, 4, 5, 8, 3]
