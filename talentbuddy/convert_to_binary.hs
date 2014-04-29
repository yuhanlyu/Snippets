convert_to_binary :: Integer -> IO ()
convert_to_binary = (putStrLn . binary) where
    binary 0 = ""
    binary n = (binary $ n `div` 2) ++ (show $ n `mod` 2)
                     
main :: IO ()
main = convert_to_binary 156
