compute_prediction :: Integer -> Integer -> IO ()
compute_prediction n w =
    (print :: Integer -> IO ()). floor $ fromIntegral n * (1.07 :: Double)^w

main :: IO ()
main = do
    compute_prediction 10 3
    compute_prediction 40 1
