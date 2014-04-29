get_sum :: Integer -> Integer -> IO ()
get_sum = (print .) . (+)

main :: IO ()
main = get_sum 3 5
