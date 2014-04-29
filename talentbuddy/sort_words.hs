import Data.List

sort_words :: String -> IO ()
sort_words = (mapM_ putStrLn) . sort . words . map replace where
    replace c = if c == ',' then ' ' else c

main :: IO ()
main = sort_words " one, ,two three,4,"
