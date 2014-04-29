import Text.Parsec

expr    = term   `chainl1` addop
term    = parens expr <|> integer
parens  = between (char '(') (char ')')
integer = do { x <- many1 digit; return $ read x }

addop   =   do{ char '+'; return (+) }
        <|> do{ char '-'; return (-) }

compute_expression :: String -> IO ()
compute_expression e = case (parse expr "" e) of
                       Left x -> print x
                       Right x -> print x

main :: IO ()
main = compute_expression "(2-2)-0+7+2-(3)-(3-(6-5))-4"
