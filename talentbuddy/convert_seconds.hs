import Text.Printf

convert_seconds :: Integer -> IO ()
convert_seconds seconds = printf "%02d:%02d:%02d" h m s where
    (minutes, s) = seconds `divMod` 60
    (h, m)       = minutes `divMod` 60

main :: IO ()
main = convert_seconds 34565
