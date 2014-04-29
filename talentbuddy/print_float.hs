import Data.List

print_float :: String -> IO ()
print_float s = putStrLn((bin2dec num) ++ "." ++ (bin2decf frac)) where
    sep = ((\(Just i) -> i) . findIndex (== '.')) s
    num = take sep s
    frac = drop (sep+1) s

bin2dec :: String -> String
bin2dec = show . (foldr (\c s -> s * 2 + c) (0::Integer) . reverse . (map c2i))
    where c2i c = if c == '0' then 0 else 1

bin2decf :: String -> String
bin2decf = (drop 2).show . (foldr (\c s -> s * 0.5 + c) (0::Double) . (map c2f))
    where c2f c = if c == '0' then 0.0 else 0.5

main :: IO ()
main = print_float "100.0011"
