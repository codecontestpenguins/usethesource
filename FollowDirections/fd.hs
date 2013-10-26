import Control.Monad.State
import Data.List
import Data.Char

main = do
    contents <- getContents
    let instructions = map (delete '\r') $ lines contents
    runStateT (runInstructions instructions) initialState

runInstructions :: [String] -> Robo ()
runInstructions (x:xs) =
    case ins of 
        "Turn" -> turn c >> runInstructions xs
        "Move" -> move (read c) >> runInstructions xs
  where
    (ins : c : _) = words x
runInstructions [] = do
    p <- gets pos 
    liftIO (putStrLn $ show p)

type Position = (Int, Int)

data Direction = North | East | South | West
    deriving (Show, Eq, Enum)

data RoboState = RS { dir :: Direction, pos :: Position }

type Robo = StateT RoboState IO

initialState = RS { dir = North, pos = (0,0) }

turn :: String -> Robo ()
turn "left" = do
    d <- gets dir
    let i = fromEnum d
        d' = toEnum $ (i - 1) `mod` 4 
    modify (\s -> s { dir = d' })

turn "right" = do
    d <- gets dir
    let i = fromEnum d
        d' = toEnum $ (i + 1) `mod` 4 
    modify (\s -> s { dir = d' })


move :: Int -> Robo ()
move n = do
    d <- gets dir
    p <- gets pos
    modify (\s -> s { pos = addP (vec d n) p })


liftP2 f (ax, ay) (bx, by) = (f ax bx, f ay by)

addP = liftP2 (+)

vec :: Direction -> Int -> Position
vec North n = (0,n)
vec South n = (0,-n)
vec East  n= (n,0)
vec West  n= (-n,0)
