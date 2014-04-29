precision :: Double -> Double -> Integer -> IO ()
precision p1 _ v = putStrLn $ show(x) ++ " " ++ show(v - x) where
    x = let (n,r) = properFraction (p1 * (fromIntegral v))
                    in if r < 0.5 then n else n + 1

main :: IO ()
main = do 
    precision 0.95 0.05 100
    precision 0.5 0.5 1
