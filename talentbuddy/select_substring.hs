select_substring :: String -> Integer -> Integer -> IO ()
select_substring s p1 p2 = putStrLn $ drop (fromInteger p1-1) $ take (fromInteger p2) s

main :: IO ()
main = select_substring "abcdefghi" 2 4
