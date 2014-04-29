sort_students :: [Integer] -> IO ()
sort_students = putStr . unwords . (map show) . sort

sort :: [Integer] -> [Integer]
sort numbers =
    let t = _sort numbers
    in (if t == numbers then t else sort t) where
    _sort (x:x2:xs) = (min x x2):(_sort((max x x2):xs))
    _sort x         = x

main :: IO ()
main = sort_students [1, 9, 4, 5, 7]
