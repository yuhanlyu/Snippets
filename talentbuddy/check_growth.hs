check_growth :: Integer -> Integer -> IO ()
check_growth d1 d2 =
    putStrLn (if d1 > d2 then "Decrease" else "Increase")

main :: IO ()
main = do
    check_growth 400 1000
