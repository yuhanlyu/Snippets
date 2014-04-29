get_max :: Integer -> Integer -> IO ()
get_max = (print .) . max

main :: IO ()
main = get_max 3 5
