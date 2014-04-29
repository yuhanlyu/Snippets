import Numeric (readFloat)
import Data.Ratio (numerator, denominator)
import Text.Printf (printf)

compute_fraction :: String -> IO ()
compute_fraction s = 
    let r::Rational
        [(r, _)] = readFloat s in
    printf "%d/%d\n" (numerator r) (denominator r)

main :: IO ()
main = compute_fraction "1.6"
