count_digits :: String -> IO ()
count_digits = print . length . filter (`elem` ['0'..'9']) 

main :: IO ()
main = count_digits "abc123"
