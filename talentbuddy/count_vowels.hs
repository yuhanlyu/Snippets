count_vowels :: String -> IO ()
count_vowels = print . length . filter (`elem` "aeiouAEIOU")

main :: IO ()
main = count_vowels "Get some"
