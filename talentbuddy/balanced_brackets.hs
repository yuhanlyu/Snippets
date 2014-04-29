
balanced_brackets :: String -> IO ()
balanced_brackets s = putStrLn (if is_balanced s then "Balanced" else "Unbalanced")
    where is_balanced x = null $ (foldl f [] x)
          f ('(':xs) ')' = xs
          f xs x = x:xs

main :: IO ()
main = do 
    balanced_brackets "(())())"
    balanced_brackets "(()())"
