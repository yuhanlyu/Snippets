import Debug.Trace
import Data.Char

compute_expression :: String -> IO ()
compute_expression = print . (eval ([], ['('], []))

eval :: ([Integer], [Char], [Char]) -> String -> Integer
eval (v, o, []) [] = if (top_op o) then (eval (reduce (v, o, []) ')') [])
                                   else (head v)
eval (v, o, n) [] = eval ((nToI n):v, o, []) []
eval (v, o, []) (c:xs) = case c of
    '+' -> eval (reduce (v, o, []) c) xs
    '-' -> eval (reduce (v, o, []) c) xs
    ')' -> eval (reduce (v, o, []) c) xs
    '(' -> eval (v, '(':o, []) xs
    _   -> eval (v, o, [c]) xs
eval (v, o, n) (c:xs) = if isDigit c then (eval (v, o, c:n) xs)
                                     else (eval ((nToI n):v, o, []) (c:xs))

reduce :: ([Integer], [Char], [Char]) -> Char -> ([Integer], [Char], [Char])
reduce (v, o, []) c 
    | c == ')' && top_op o = (v', (drop 2 o), [])
    | c == ')'             = (v, (drop 1 o), [])
    | top_op o             = (v', o', [])
    | otherwise            = (v, c:o, [])
    where v' = (evalbinary (head o) (v !! 1) (head v)):(drop 2 v)
          o' = c:(drop 1 o)

nToI :: [Char] -> Integer
nToI n = read (reverse n)

top_op :: [Char] -> Bool
top_op [] = False
top_op (c:_) = if c `elem` "+-" then True else False

evalbinary :: Char -> Integer -> Integer -> Integer
evalbinary op a b
    | op == '+' = a + b
    | op == '-' = a - b

main :: IO ()
main = compute_expression "(2-2)-0+7+2-(3)-(3-(6-5))-4"
