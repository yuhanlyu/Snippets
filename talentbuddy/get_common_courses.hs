import Data.List

get_common_courses :: [Integer] -> [Integer] -> IO ()
get_common_courses = (((mapM_ print) . nub . sort) .) . intersect

main :: IO ()
main = get_common_courses [1, 2, 8, 4, 5, 8, 3] [8, 2, 2, 7, 10]
