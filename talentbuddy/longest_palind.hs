
import Data.List (tails, inits, maximumBy)
import Data.Ord (comparing)

longest_palind :: String -> IO ()
longest_palind = 
    putStrLn . (maximumBy (comparing length)) . 
    (filter (\x -> (x /= []) && (x == reverse x))) .  (concatMap tails) . inits

main = longest_palind "abcdxyzyxabcdaaa"
