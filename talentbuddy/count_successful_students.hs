count_successful_students :: [Integer] -> Integer -> IO ()
count_successful_students grades min_grade =
    (print . length . filter (>= min_grade)) grades

main :: IO ()
main = count_successful_students [1, 2, 8, 4, 5, 8, 3] 5
