copy_string :: String -> String -> Int -> IO ()
copy_string s1 s2 p = putStrLn $ take p s1 ++ s2 ++ drop p s1

main :: IO ()
main = copy_string "abcdefghi" "xyz" 3
