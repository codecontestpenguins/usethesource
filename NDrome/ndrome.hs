-- cat SampleInput.txt | runghc ndrome.hs
import Data.List (splitAt, delete)
import Data.List.Split (splitOn)
import Control.Monad (forM_)

main = do
    contents <- getContents
    let cases = map (delete '\r') $ lines contents
    forM_ cases $ \c -> do
        let r = if uncurry ndrome (parse c) then "1" else "0"
        putStr $ c ++ "|" ++ r ++ "\n"

parse :: String -> (Int, String)
parse s = let (x:n:_) = splitOn "|" s in (read n,x)

ndrome :: Int -> String -> Bool
ndrome n s = s == r
  where r = concat $ reverse (splits n s)

splits :: Int -> String -> [String]
splits n s 
    | length s < n  = error "not splittable"
    | length s == n = [s]
    | otherwise     = let (a,b) = splitAt n s
                      in a : splits n b
