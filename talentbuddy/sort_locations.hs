sort_locations :: Integer -> Integer -> Integer -> IO ()
sort_locations a b c =
    putStrLn (show(min) ++ " " ++ show(a+b+c-max-min) ++ " " ++show(max))
    where
        min =
            (if a > b then (if b > c then c else b) else (if a > c then c else a))
        max = 
            (if a > b then (if a > c then a else c) else (if b > c then b else c))

main :: IO ()
main = sort_locations 15 10 5
