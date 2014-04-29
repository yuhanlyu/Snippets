compute_sqrt :: Integer -> IO ()
compute_sqrt n = 
    let sqrt l mid h
            | mid * mid <= n && (mid + 1) * (mid + 1) > n = mid
            | mid * mid >= n = sqrt l ((l + mid) `div` 2) mid
            | (mid + 1) * (mid + 1) < n = sqrt l ((l + mid) `div` 2) mid
    in print $ sqrt 1 (n `div` 2) n

main :: IO ()
main = compute_sqrt 17
