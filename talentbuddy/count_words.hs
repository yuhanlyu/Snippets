
count_words :: String -> IO ()
count_words = print . length . words . map replace where
    replace c = if c == ',' then ' ' else c

main = count_words " one, ,two three,4,"
