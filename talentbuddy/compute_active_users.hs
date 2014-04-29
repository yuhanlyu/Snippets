compute_active_users :: Integer -> Integer -> IO ()
compute_active_users n b =
    print ((n * (100 - b)) `div` 100)

main :: IO ()
main = do
    compute_active_users 1000 25
