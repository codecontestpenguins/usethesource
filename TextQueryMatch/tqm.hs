-- usage: cat SampleInput.txt | runghc tqm.hs | nl

import Data.List (delete, isInfixOf)
import Data.Char (toLower)

main = do
    contents <- getContents
    let (n:xs) = lines contents
    putStrLn n
    mapM_ putStrLn $ map show $ matches (map (delete '\r') xs)

matches :: [String] -> [Bool]
matches [] = []
matches (m:s:xs) = match m s : matches xs
matches (_:xs) = []

match :: String -> String -> Bool
match m s = if head s' /= m0 then
                        mx m' $ unwords $ tail $ words s'
                    else 
                        mx m' s'
  where
    m'@(m0:_) = map toLower m
    s' = map toLower s




-- all input assumed to be lowercase
mx :: String -> String -> Bool
mx (m:ms) (x:xs) 
    | x == m    = mx ms xs     -- match
    | x == ' '  = mx (m:ms) xs -- whitespace
    | otherwise = False
mx [] _ = True                 -- if match string is used up, it is true
mx _  _ = False                -- all other cases: false
