import Data.List


longest_palind :: String -> IO ()
longest_palind s = putStrLn (maximumBy comp (map pal [0..((length s) - 1)]))
    where comp s1 s2 = compare (length s1) (length s2)
          pal i = if (length e) > (length o) then e else o
            where e = (reverse x) ++ x
                  o = (reverse y) ++ [(s !! i)] ++ y
                  x = longest_prefix (reverse (take (i) s)) (drop i s)
                  y = longest_prefix (reverse (take (i) s)) (drop (i+1) s)
                  longest_prefix _  [] = []
                  longest_prefix [] _  = []
                  longest_prefix (a:ax) (b:bx) =
                      if a == b then a:(longest_prefix ax bx) else []

main = print (concatMap tails $ inits "12345")
