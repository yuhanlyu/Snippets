import Data.Char

caesar_shift :: String -> IO ()
caesar_shift = putStrLn . (map f) where
    f c | c >= 'A' && c < 'Z' = succ c
        | c == 'Z'            = 'A'
        | otherwise           = c
main :: IO ()
main = caesar_shift "CAT"
