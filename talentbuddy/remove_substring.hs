remove_substring :: String -> Int -> Int -> IO ()
remove_substring s p n = putStrLn $ take (p-1) s ++ drop (p + n - 1) s

main :: IO ()
main = remove_substring "abcdefghi" 4 3
